from django.urls import path

from backend.views import ShopView, CategoryView, PartnerUpdate

app_name = 'backend'
urlpatterns = [
    path('shops', ShopView.as_view(), name='shops'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
]