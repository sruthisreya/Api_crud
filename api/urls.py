from django.urls import path
from userapp.views import index,ClassPerson,updatePerson

urlpatterns = [
    path('index/',index,name='index'),
    path('ClassPerson/',ClassPerson.as_view(),name='ClassPerson'),
    path('updatePerson/<int:id>/',updatePerson.as_view(),name='updatePerson'),
]
