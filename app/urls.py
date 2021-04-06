from django.urls import path
from app.views import index, indexhtml, login_user, do_logout, recipehtml, new_register, show_form, gallary_page, ajax_path, ajax_path2
from app.views import api_1, get_csv, shop_page, our_beer_page, our_contacts_page
urlpatterns = [
    path('just_page', index),
    path('page', indexhtml),
    path('index_2', login_user),
    path('page_2', do_logout),
    path('page_3', recipehtml),
    path('register', new_register),
    path('registration_user', show_form),
    path('gallary', gallary_page),
    path('page_unknown', ajax_path),
    path('check_login', ajax_path2),
    path('api_test1', api_1),
    path('get_csv', get_csv),
    path('shop', shop_page),
    path('our_beer', our_beer_page),
    path('contacts', our_contacts_page),

]