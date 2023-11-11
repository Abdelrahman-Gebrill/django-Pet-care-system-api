from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns =[
    path('employer/create/',views.Registration,name='employercreate'),
    path('employer/list/',views.Registration,name='employerlist'),
    path('employer/edit/<int:pk>',views.Mentainanace,name='employeredit'),
    path('employer/delete/<int:pk>',views.Mentainanace,name='employerdelete'),
    path('employer/<int:pk>',views.Mentainanace,name='employerget'),
    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]