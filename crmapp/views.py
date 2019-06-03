from rest_framework import generics
from .models import Account, Activity, ActivityStatus, Contact, ContactSource, ContactStatus
from .serializers import AccountSerializer, ActivitySerializer, ActivityStatusSerializer, ContactSerializer, ContactSourceSerializer, ContactStatusSerializer
#from rest_framework.permissions import IsAdminUser

class AccountAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    #permission_classes = (IsAdminUser,)

class ActivityAPIView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    #permission_classes = (IsAdminUser,)

class ActivityStatusAPIView(generics.ListCreateAPIView):
    queryset = ActivityStatus.objects.all()
    serializer_class = ActivitySerializer
    #permission_classes = (IsAdminUser,)

class ContactAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    #permission_classes = (IsAdminUser,)

class ContactStatusAPIView(generics.ListCreateAPIView):
    queryset = ContactStatus.objects.all()
    serializer_class = ContactSerializer
    #permission_classes = (IsAdminUser,)

class ContactSourceAPIView(generics.ListCreateAPIView):
    queryset = ContactSource.objects.all()
    serializer_class = ContactSourceSerializer
    #permission_classes = (IsAdminUser,)
