from django.urls import path,include
from userapp.views import index,ClassPerson,updatePerson,RegisterAPI,LoginAPI,Reg,ProtectedView,Personviewset,paginationAPI,Apipatchview
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter

# from userapp.views import Personviewset




router=DefaultRouter()
router.register(r'persons',Personviewset)

urlpatterns = [
    path('',include(router.urls)),

    path('index/',index,name='index'),
    path('classperson/',ClassPerson.as_view(),name='classperson'),
    path('updateperson/<int:id>/',updatePerson.as_view(),name='updateperson'),
    path('register',RegisterAPI.as_view(),name='register'),
    path('login/',LoginAPI.as_view(),name='login'),
    path('reg/',Reg.as_view(),name='reg'),
    path('token/',TokenObtainPairView.as_view(),name='token'),
    path('refresh/',TokenRefreshView.as_view(),name='refresh'),
    path('protected/',ProtectedView.as_view(),name='protected'),
    path('paginationAPI/',paginationAPI.as_view(),name='paginationAPI'),
    path('Apipatchview/<int:id>/',Apipatchview.as_view(),name='Apipatchview')
   

] + router.urls
