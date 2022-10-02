from django.urls import path
from .views import WomenList, WomenAbout, AddPage, ContactFormView, ShowPost, WomenCategory, RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('', WomenList.as_view(), name='home'),
    path('about/', WomenAbout.as_view(), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('category/<slug:category_slug>', WomenCategory.as_view(), name='category'),

]
