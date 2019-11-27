from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from wiki.models import Page
from api.serializers import PageSerializer


class PageList(APIView):
    def get(self, request):
        questions = Page.objects.all()[:20]
        data = PageSerializer(questions, many=True).data
        return Response(data)


class PageDetail(APIView):
    def get(self, request, slug):
        question = get_object_or_404(Page, slug=slug)
        data = PageSerializer(question).data
        return Response(data)
