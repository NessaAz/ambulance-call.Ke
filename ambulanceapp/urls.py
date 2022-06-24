from django.urls import path, include
from . import views 


urlpatterns = [
    path('', views.home, name='home' ),
    path('signup/', views.provider, name='provider' ),
    path('login/', views.LoginView.as_view(template_name='ambulanceapp/login.html'), name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout',kwargs={'next_page':'/'}),        
    path('account/list/', views.AccountList.as_view(), name='account_list'),
    # path('account/list/',views.AccountList.as_view(), name='account_list'),
    path('account/(?P<uuid>[\w-]+)/', views.accountdetail,name='account_detail'),
    path('account/new/',views.accountcru, name='account_new'),
    # path('account/list/', views.AccountList.as_view(), name='account_list'),    
    path('account/new/(?P<uuid>[\w-]+)/',views.accountcru, name='account_detail'),    
    path('account/edit/', views.accountcru, name='account_update'),    
    path('contact/(?P<uuid>[\w-]+)/', views.contactdetail, name='contactdetail')

]


