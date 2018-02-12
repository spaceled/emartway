from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from .views import ProductDetailView, ProductListView,VariationListView 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	#url(r'^categories/', include(products.url)),
	url(r'^(?P<pk>d+)', ProductDetailView.as_view(), name='product_detail'),
	url(r'^categories/', include('products.urls_categories')),
]
