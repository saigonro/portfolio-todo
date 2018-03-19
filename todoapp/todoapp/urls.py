from django.conf.urls import url, include
from django.contrib import admin
import home.views as home_views
from todo import urls as todo_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.get_index, name="home"),
    url(r'^todo/', include(todo_urls)),
]
