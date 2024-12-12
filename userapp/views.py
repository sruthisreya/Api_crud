from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from userapp.serializer import PersonSerializer
from userapp.models import Person



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