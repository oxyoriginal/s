from s_app import views
from s_app.views import index, page, static_page, main, about, services, gallery, contact, \
    showcategory, showservice, review, add_item, RegisterFormView, LoginFormView, LogoutView, search, update_item, \
    get_item_one, delete_item

from django.urls import path, include


urlpatterns = [
    path('', main, name='main'),
    path('page/', page),
    path('page1/', static_page, name='static_page'),

    path('main/', main, name='main'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),

    path('showservice/<int:id>', showservice, name='showservice'),
    path('showcategory/<int:id>', showcategory, name='showcategory'),


    path('review/', review, name='review'),
    path('add_item/', add_item, name='add_item'),
    path('registration/', RegisterFormView.as_view(), name='registration'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('search/', search, name='search'),
    path('editreview/<int:id>', update_item, name='update_item'),
    path('review/<int:id>/', get_item_one, name='get_item_one'),
    path('deletereview/<int:id>/', delete_item, name='delete_item'),
]
