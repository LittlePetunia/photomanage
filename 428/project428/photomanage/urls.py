from django.conf.urls import patterns, include, url
 
urlpatterns = patterns('photomanage.views',
    url(r'^$', 'index', name='home'),
    # for our home/index page
 
    url(r'^add_category/(?P<photo_id>\d+)/(?P<category_code>\d)$', 'add_category', name='addcategory'),
    url(r'^get_all_photos/$', 'get_all_photos', name='getallphotos'),
    url(r'^get_photos_by_category/(?P<category_code>\d)$', 'get_photos_by_category', name='getphotosbycategory'),
    url(r'^reset_category/$', 'reset_category', name='resetcategory'),
    url(r'^custome_category/(?P<category>.+)$', 'custome_category', name='customecategory'),
    )