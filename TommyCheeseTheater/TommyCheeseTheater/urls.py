from django.conf.urls import patterns, include, url
from django.contrib import admin
from movieshow.views import Orders, CheckOut,ShoppingCar,Shop,MovieDetail,MovieShow,UserLogup,show,Movies,Check
from rest_framework.authtoken import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CheeseTheater.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^cheesetheater/admin/', include(admin.site.urls)),
    url(r'^cheesetheater/movies/$',Movies.as_view()),
    url(r'^cheesetheater/movie/(?P<pk>\d+)/$',MovieDetail.as_view()),
    url(r'^cheesetheater/moviesearch/$',MovieShow.as_view()),
    url(r'^cheesetheater/logup/$',UserLogup.as_view()),
     url(r'^cheesetheater/show/$',show), 
    url(r'^cheesetheater/check/$',Check.as_view()),
    url(r'^cheesetheater/shop/$',Shop.as_view()),
    url(r'^cheesetheater/shoppingcar/$',ShoppingCar.as_view()),
    url(r'^cheesetheater/api-token-auth/', views.obtain_auth_token),
    url(r'^cheesetheater/checkout',CheckOut.as_view()),
    url(r'^cheesetheater/orders',Orders.as_view()),
)
