from django.urls import path
from .import views

urlpatterns = [

    path('frontpage', views.frontpage, name='frontpage'),
    path('index', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('emp_login', views.emp_login, name='emp_login'),
    path('emp_home', views.emp_home, name='emp_home'),
    path('profile', views.profile, name='profile'),
    path('Logout', views.Logout, name='Logout'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('my_experience', views.my_experience, name='my_experience'),
    path('edit_experience', views.edit_experience, name='edit_experience'),
    path('my_education', views.my_education, name='my_education'),
    path('edit_myeducation', views.edit_myeducation, name='edit_myeducation'),
    path('change_password', views.change_password, name='change_password'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('all_employee', views.all_employee, name='all_employee'),
    path('adminedit_empprofile/<int:pid>', views.adminedit_empprofile, name='adminedit_empprofile'),
    path('admin_delete/<int:pid>', views.admin_delete, name='admin_delete'),
    path('adminedit_empeducation/<int:pid>', views.adminedit_empeducation, name='adminedit_empeducation'),
    path('adminedit_empexperience/<int:pid>', views.adminedit_empexperience, name='adminedit_empexperience')

]
