from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import UserSerializer

class UserViewSet(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer