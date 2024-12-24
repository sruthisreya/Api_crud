from .models import Peoples
from rest_framework import status
from functools import wraps
from rest_framework.response import Response

def check_employee(func):
    @wraps(func)
    def wrapper(view_instance,request, *args, **kwargs):
            user_id=kwargs.get('user_id')
            obj=Peoples.objects.get(user_id=user_id)
            if obj and obj.role !='EMPLOYEE':
                return Response({"error":"aceess denied:not employee"},status=status.HTTP_403_FORBIDDEN)
            return func(view_instance,request,*args,**kwargs)
    return wrapper

