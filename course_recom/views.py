
from django.http.response import JsonResponse
from django.shortcuts import render , get_object_or_404, redirect
from django.core import serializers

from rest_framework.response import Response
import requests
# from chatbot import chatbot
import json
from .models import *
from .serializers import librarySerializer
from rest_framework.views import APIView


# Create your views here.
# class ChatbotApi(APIView):
#     def get(self,request):
#             res = ''
#             query_list = []
#             responses = []
#             quer = request.data.get('query')
#             res=chatbot.chat(quer)

#             print(res)

#             responses.append(res)


#             return JsonResponse(json.dumps(responses), safe=False)

class Library(APIView):
    def get(self, request):
        obj = librarymodel.objects.all()
        print(obj)
        qs_json =librarySerializer( obj, many=True)
        return Response(qs_json.data)


def Tclasses(request):
    req = requests.get('https://trackfinity2022.herokuapp.com/classeslistbyteacher')
    mydata = json.loads(req.content.decode('utf-8'))
    tclass =True
    data = mydata['data']
    id_lis=[]
    for i in range(len(data)):
        id_lis.append(data[i]['_id'])
    mylist = zip(data, id_lis)
    return render(request,'index.html',{'mylist':mylist,'tclass':tclass})

def cstudent(request,slug):
    tclass= None
    print(slug)
    return render(request,'index1.html',{'tclass':tclass})

def profile(request):
    return render(request,'profile.html')
