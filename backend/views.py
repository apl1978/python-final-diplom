from rest_framework.generics import ListAPIView

from backend.serializers import ShopSerializer

from backend.models import Shop


class ShopView(ListAPIView):
    """
    Класс для просмотра списка магазинов
    """
    queryset = Shop.objects.filter(state=True)
    serializer_class = ShopSerializer
