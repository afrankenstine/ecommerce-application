from django.urls import path, re_path
from .views import (
    AllNotificationsList,
    MarkAllAsRead,
    MarkAsRead,
    MarkAsUnRead,
    UnreadNotificationCount,
    UnreadNotificationsList,
)


urlpatterns =[
    path("", AllNotificationsList.as_view()),
    path("unread/", UnreadNotificationsList.as_view()),
    path("mark-all-as-read/", MarkAllAsRead.as_view(),),
    path('^unread_count/', UnreadNotificationCount.as_view(),
    re_path(r"^mark-as-read/(?P<id>\d+)/$", MarkAsRead.as_view(),
    re_path(r"^mark-as-unread/(?P<id>\d+)/$", MarkAsUnRead.as_view()),
]
