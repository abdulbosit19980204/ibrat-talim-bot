from django.urls import path
from rest_framework.routers import SimpleRouter
from api.views import BotUserViewSet, FeedbackViewSet, FilialViewSet, FilialDetailViewSet, YonalishlarViewSet, \
    PriceViewSet, ChegirmaViewSet

router = SimpleRouter()

urlpatterns = [

]
router.register(r'users', BotUserViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'filiallar', FilialViewSet)
router.register(r'filialdetails', FilialDetailViewSet)
router.register(r'yonalishlar', YonalishlarViewSet)
router.register(r'prices', PriceViewSet)
router.register(r'chegirmalar', ChegirmaViewSet)
urlpatterns += router.urls
