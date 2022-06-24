from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home' ),
    path('signup/', views.provider, name='provider' ),
    path('login/', views.LoginView.as_view(template_name='ambulanceapp/login.html'), name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout',kwargs={'next_page':'/'}),        
    path('account/list/', views.AccountList.as_view(), name='account_list'),
    
]
