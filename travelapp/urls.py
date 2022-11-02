from django.urls import path

from . import views

urlpatterns=[
    path('',views.fun,name='fun'),
    path('add',views.add,name='add')
    # path('add',views.addition,name='add')
]