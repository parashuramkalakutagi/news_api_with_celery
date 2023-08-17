from django.shortcuts import render
from .NewsApiData import News_data,jaurnal
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import *
from .models import NewsBusiness,journal
from .serializer import BusinessNewsSerializer,journalSerializer
from rest_framework.pagination import LimitOffsetPagination

class FeatchNewsBusiness(viewsets.ModelViewSet):
    queryset = NewsBusiness.objects.all().order_by('?')[:10]
    serializer_class = BusinessNewsSerializer
    pagination_class = LimitOffsetPagination



class journaldata(viewsets.ModelViewSet):
    queryset = journal.objects.all().order_by('?')[:5]
    serializer_class = journalSerializer
    pagination_class = LimitOffsetPagination



