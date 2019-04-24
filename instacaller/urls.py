from django.conf.urls import url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from instacaller.views import RegisterUserView,SpamUser,SearchByName,SearchByPhone

urlpatterns = [
    url(r'^register/',csrf_exempt(RegisterUserView.as_view()),name='register_user'),
    url(r'^mark-spam/',csrf_exempt(SpamUser.as_view()),name='spam'),
    url(r'^search-by-name/(?P<search_query>\D+)',SearchByName.as_view(),name='by_name'),
    url(r'^search-by-phone/',SearchByPhone.as_view(),name='by_name'),
]