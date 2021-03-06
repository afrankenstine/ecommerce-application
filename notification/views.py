from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import NotificationSerializer
from .models import Notification


class BaseNotificationViewList(ListAPIView):
    serializer_class = NotificationSerializer
    model = Notification
    paginate_by = 50


class AllNotificationsList(BaseNotificationViewList):
    def get_queryset(self):
        # qset = self.request.user.notifications.active()
        qset = self.request.user.notifications.all()
        return qset


class UnreadNotificationsList(BaseNotificationViewList):
    def get_queryset(self):
        return self.request.user.notifications.unread()


class MarkAllAsRead(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        request.user.notifications.mark_all_as_read()
        content = {"success": "True"}
        return Response(content, status=status.HTTP_200_OK)


class MarkAsRead(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=None):
        notification = get_object_or_404(Notification, recipient=request.user, id=id)
        notification.mark_as_read()
        content = {"success": "True"}
        return Response(content, status=status.HTTP_200_OK)


class MarkAsUnRead(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=None):
        notification = get_object_or_404(Notification, recipient=request.user, id=id)
        notification.mark_as_unread()
        content = {"success": "True"}
        return Response(content, status=status.HTTP_200_OK)


class UnreadNotificationCount(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=None):
        data = {
            "unread_count": request.user.notifications.unread().count(),
        }
        return Response(data, status=status.HTTP_200_OK)
