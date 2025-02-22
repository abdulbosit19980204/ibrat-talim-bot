from django.urls import path
from rest_framework.routers import SimpleRouter
from api.views import BotUserViewSet, FeedbackViewSet

router = SimpleRouter()

urlpatterns = [

]
router.register(r'users', BotUserViewSet)
router.register(r'feedbacks', FeedbackViewSet)
urlpatterns += router.urls
