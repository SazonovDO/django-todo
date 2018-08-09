from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('toDoList',views.toDoListView)
router.register('company',views.companyView)


urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.login, name='login'),
    path('', views.index, name='index'),
]
