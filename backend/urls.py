from django.urls import path
from rest_framework.routers import DefaultRouter
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from backend.views import ShopViewSet, CategoryViewSet, PartnerUpdate, RegisterAccount, ConfirmAccount, AccountDetails, \
    LoginAccount, ContactView, ProductInfoView, PartnerState, PartnerOrders, BasketView, OrderView

router = DefaultRouter()
router.register('shops', ShopViewSet, basename='shops')
router.register('categories', CategoryViewSet, basename='categories')
router.register('products', ProductInfoView, basename='products')

app_name = 'backend'
urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),

    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),

    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),

] + router.urls
