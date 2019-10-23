from django.contrib.auth.models import Group
from groupDM.models import *
from groupDM.serializers import *

from rest_framework import generics, permissions, viewsets
from snippets.permissions import IsOwnerOrReadOnly

class AdminGroupList(generics.ListAPIView):
    queryset = AdminGroup.objects.all().order_by("lastName")
    serializer_class = GroupSerializer

class StaffGroupDetail(generics.RetrieveAPIView):
    queryset = StaffGroup.objects.all()
    serializer_class = GroupSerializer
    
class UserGroupDetail(generics.RetrieveAPIView):
    queryset = UserGroup.objects.all().order_by("lastName")
    serializer_class = GroupSerializer
