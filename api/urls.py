from django.urls import path

from api.views import PageList, PageDetail

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('wiki/', PageList.as_view(), name='page_list'),
    path('wiki/<str:slug>', PageDetail.as_view(), name='page_detail')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
