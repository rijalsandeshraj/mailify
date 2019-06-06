from django.urls import path
from mailinglist.api.v1 import api_views
from . import views

app_name = 'mailinglist'

urlpatterns = [
    path('', views.MailingListListView.as_view(), name='mailinglist_list'),
    path('new', views.CreateMailingListView.as_view(), name='create_mailinglist'),
    path('<uuid:pk/delete', views.DeleteMailingListView.as_view(),
         name='delete_mailinglist'),
    path('<uuid:pk>/manage', views.MailingListDetailView.as_view(),
         name='manage_mailinglist'),

    path('<uuid:mailinglist_id>/subscribe', views.SubscribeToMailingListView.as_view(),
         name='subscribe'),
    path('<uuid:pk>/thankyou', views.ThankYouForSubscribingView.as_view(),
         name='subscriber_thankyou'),
    path('subscribe/confirmation/<uuid:pk>', views.ConfirmSubscriptionView.as_view(),
         name='confirm_subscription'),
    path('unsubscribe/<uuid:pk>', views.UnsubscribeView.as_view(),
         name='unsubscribe'),

    path('<uuid:mailinglist_pk>/message/new', views.CreateMessageView.as_view(),
         name='create_message'),
    path('message/<uuid:pk>', views.MessageDetailView.as_view(),
         name='view_message'),

    # for API
    path('api/v1/mailing_list', api_views.MailingListCreateListView.as_view(),
         name='api_mailing_list_list'),
    path('api/v1/mailinglist/<uuid:pk>', api_views.MailingListRetrieveUpdateDestroyView.as_view(),
         name='api_mailing_list_detail'),
     path('api/v1/mailinglist/')
]
