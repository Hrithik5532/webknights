
from django.http.response import JsonResponse
from rest_framework.response import Response

# from chatbot import chatbot
import json
from .models import *
from .serializers import librarySerializer
from rest_framework.views import APIView


# # Create your views here.
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
