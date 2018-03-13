from django.conf.urls import patterns, include, url
 
urlpatterns = patterns('photomanage.views',
    url(r'^$', 'index', name='home'),
    # for our home/index page
 
    # url(r'^(?P&lt;short_id&gt;\w{6})$', 'redirect_original', name='redirectoriginal'),
    # # when short URL is requested it redirects to original URL
 
    url(r'^get_all_photos/$', 'get_all_photos', name='getallphotos'),
    )