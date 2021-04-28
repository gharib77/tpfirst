from django.urls import path
app_name = 'accounts'
from django.contrib.auth import views
urlpatterns = [
    path('login/',views.LoginView.as_view(template_name='accounts/login.html',redirect_authenticated_user=True),name='login'),
    path('logout/',views.LogoutView.as_view(template_name='accounts/logout.html',next_page='accounts:login'),name='logout')
]
