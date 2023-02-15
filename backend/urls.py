from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backend.views import ShopViewSet, CategoryViewSet, PartnerUpdate, RegisterAccount, ConfirmAccount, AccountDetails, \
    LoginAccount

router = DefaultRouter()
router.register('shops', ShopViewSet, basename='shops')
router.register('categories', CategoryViewSet, basename='categories')

app_name = 'backend'
urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
] + router.urls
