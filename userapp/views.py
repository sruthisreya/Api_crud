
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from rest_framework import status
from userapp.serializer import PersonSerializer,RegisterSerializer,LoginSerializer,UserSerializer
from userapp.models import Person,Peoples
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication  
from rest_framework.permissions import AllowAny,IsAuthenticated
from .decorators import check_employee
from rest_framework.decorators import action

#jwt based authentication

class Reg(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProtectedView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        return Response({"message":"you are authenticated"})



#token based authentication first reg and login
class RegisterAPI(APIView):
    def post(self,request):
        data1=request.data
        serializer=RegisterSerializer(data=data1)
        if not serializer.is_valid():
            return Response({'message':serializer.errors},status=status.HTTP_404_NOT_FOUND)
        serializer.save()
        return Response({'message':'user created'},status=status.HTTP_201_CREATED)


class LoginAPI(APIView):
    def post(self,request):
        data2=request.data
        serializer=LoginSerializer(data=data2)
        if not serializer.is_valid():
            return Response({'message':serializer.errors},status=status.HTTP_404_NOT_FOUND)
        # print(serializer.data)
        user=authenticate(username=serializer.data['username'],password=serializer.data['password'])

        print(user)
        if not user:
            return Response({'message':'invalid user'},status=status.HTTP_401_UNAUTHORIZED)
        token, _ =Token.objects.get_or_create(user=user)
        return Response({'message':'login successfull','token':str(token)},status=status.HTTP_201_CREATED)


#crud operation for users
class ClassPerson(APIView):

    def get(self,request):
        obj=Person.objects.all()
        serializer=PersonSerializer(obj,many=True)
        return Response(serializer.data)
        

    def post(self,request):
        data=request.data
        serializer=PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class updatePerson(APIView):
    def get(self,request,id):
        obj=Person.objects.get(id=id)
        serializer=PersonSerializer(obj)
        return Response(serializer.data)

    def put(self,request,id):
        data=request.data
        obj=Person.objects.get(id=id)
        serializer=PersonSerializer(obj,data=data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def patch(self,request,id):
        data=request.data
        obj=Person.objects.get(id=id)
        serializer=PersonSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def delete(self,request,id):
        data=request.data
        obj=Person.objects.get(id=id)
        obj.delete()
        return Response({'mesage':'person deleted'})




@api_view(['GET'])
def index(request):
    userdetails={
        'name':'arunima',
        'age':22,
        'place':'kochi',
        'job':'clerk'
    }
    return Response(userdetails)



#signals used
class Personviewset(ModelViewSet):
    queryset=Peoples.objects.all()
    serializer_class=PersonSerializer
    lookup_field='user_id'

# decorators used 
    @action(detail=True,methods=['get'],url_path='details')
    @check_employee
    def get_employee(self,request,user_id=None):
        try:

            obj=Peoples.objects.get(user_id=user_id)
            return Response({
                "name":obj.name,
                "age":obj.age,
                "place":obj.place,
                "job":obj.job,
                "role":obj.role

            })
        except Peoples.DoesNotExist:
            return Response({"error":"does not exist"},status=404)

