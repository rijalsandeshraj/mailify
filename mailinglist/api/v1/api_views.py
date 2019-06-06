from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from mailinglist.permissions import CanUseMailingList
from mailinglist.serializers import MailingListSerializer, SubscriberSerializer
from mailinglist.models import MailingList, Subscriber


class MailingListCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, CanUseMailingList)
    serializer_class = MailingListSerializer

    def get_queryset(self):
        return self.request.user.mailinglist_set.all()

    def get_serializer(self, *args, **kwargs):
        if kwargs.get('data', None):
            data = kwargs.get('data', None)
            owner = {
                'owner': self.request.user.id,
            }
            data.update(owner)
        return super().get_serializer(*args, **kwargs)


class MailingListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, CanUseMailingList)
    serializer_class = MailingListSerializer
    queryset = MailingList.objects.all()


class SubscriberListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, CanUseMailingList)
    serializer_class = SubscriberSerializer

    def get_queryset(self):
        mailing_list_pk = self.kwargs('mailing_list_pk')
        mailing_list = get_object_or_404(MailingList, id=mailing_list_pk)
        return mailing_list.subscriber_set.all()

    def get_serializer(self, *args, **kwargs):
        if kwargs.get('data'):
            mailing_list = {
                'mailing_list': reverse(
                    'mailinglist:api_mailing_list_detail',
                    kwargs={'pk': self.kwargs(mailing_list_pk)}
                )
            }
            data.update(mailing_list)
        return super().get_serializer(*args, **kwargs)
