from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .permissions import CanUseMailingList
from .serializers import MailingListSerializer


class MailingListCreateListView(generics.ListCreateAPIView):
