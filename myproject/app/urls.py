from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('',views.QuotesList.fetch_data, name='home'),
    path('user_data/',views.userData.get,name='get_data'),
    path('signup/',views.Forms.signUp, name='signupform'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login' ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('response/',views.Forms.reponseView,name='responseView')

]
urlpatterns += staticfiles_urlpatterns()
