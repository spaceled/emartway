from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from emart import views
from accounts import views as accounts_views
from carts import views as cart_views
from orders import views as order_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', views.home, name='home'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^return/$', views.return_policy, name='return'),
	
	url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	url(r'^signup/$', accounts_views.signup, name='signup'),
	url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
	
	url(r'^reset/$',
		auth_views.PasswordResetView.as_view(
			template_name='password_reset.html',
			email_template_name='password_reset_email.html',
			subject_template_name='password_reset_subject.txt'
		), name='password_reset'),
	url(r'^reset/done/$',
		auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
		name='password_reset_done'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
		name='password_reset_confirm'),
	url(r'^reset/complete/$',
		auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
		name='password_reset_complete'),		
	url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
		name='password_change'),
	url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
		name='password_change_done'),
		
	## Product Views
	#url(r'^product/(?P<id>\d+)/$', views.home, name='home'),
	url(r'^list/$', views.ProductListView.as_view(), name='products'),
	url(r'^product/(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product_detail'),
	url(r'^product/(?P<pk>\d+)/inventory/$', views.VariationListView.as_view(), name='product_inventory'),
	url(r'^product/categories/', views.CategoryListView.as_view(), name='categories'),
    #url(r'^(?P<slug>[\w-]+)/$', views.CategoryDetailView.as_view(), name='category_detail'),
	
	# Cart Views
	url(r'^cart/$', cart_views.CartView.as_view(), name='cart'),
	url(r'^cart/count/$', cart_views.ItemCountView.as_view(), name='item_count'),
	url(r'^checkout/$', cart_views.CheckoutView.as_view(), name='checkout'),
	url(r'^checkout/final/$', cart_views.CheckoutFinalView.as_view(), name='checkout_final'),
	
	## Order Views 
	url(r'^orders/$', order_views.OrderList.as_view(), name='orders'),
	url(r'^orders/(?P<pk>\d+)/$', order_views.OrderDetail.as_view(), name='order_detail'),
	url(r'^checkout/address/$', order_views.AddressSelectFormView.as_view(), name='order_address'),
	url(r'^checkout/address/add/$', order_views.UserAddressCreateView.as_view(), name='user_address_create'),
	
]
if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)