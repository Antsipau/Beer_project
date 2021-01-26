from django.urls import path
from app.views import index, indexhtml, login_user, do_logout, recipehtml, new_register, show_form, privet, ajax_path, ajax_path2
urlpatterns = [
    path('just_page', index),
    path('page', indexhtml),
    path('index_2', login_user),
    path('page_2', do_logout),
    path('page_3', recipehtml),
    path('register', new_register),
    path('registration_user', show_form),
    path('privet', privet),
    path('page_unknown', ajax_path),
    path('check_login', ajax_path2),

]