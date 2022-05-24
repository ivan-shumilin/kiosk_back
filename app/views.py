from django.http import HttpResponse
from django.shortcuts import render
from requests import Response
from rest_framework import generics
from rest_framework.views import APIView


class GetSAppView(APIView):

    def get(self, request):
        print('ClICK')
        return HttpResponse('Hi!')
