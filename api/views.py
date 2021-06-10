from json.decoder import JSONDecodeError
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# def home_view(request):
#     obj = Blog.objects.all()
#     # result = []
#     # for rec in obj:
#     #     d = {}
#     #     d['title']= rec.title
#     #     d['descriptions']= rec.descriptions
#     #     d['date']= str(rec.created_date)
#     #     d['created_by']= rec.created_by
#     #     result.append(d)
#     # final_result = json.dumps(result)
#     return HttpResponse(final_result)

class BlogView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        qs = Blog.objects.all()
        serializer_obj = BlogSerializer(qs, many=True)

        return Response(serializer_obj.data)

class SingleBlogView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        blog_id = request.GET.get('id')

        qs = Blog.objects.get(id=blog_id)
        serializer_obj = BlogSerializer(qs)

        return Response(serializer_obj.data) 

class CreateBlog(APIView):

    def post(self, request):
        form_data = request.data    #getting data from gui  from user 
        ser_obj = BlogSerializer(data=form_data)
        if(ser_obj.is_valid()):
            ser_obj.save()
            return Response(ser_obj.data, status=status.HTTP_201_CREATED)
        return Response(ser_obj.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteBlog(APIView):

    def delete(self, request):
        rec_id = request.data["id"]    #getting data from gui  from user 
        rec = Blog.objects.get(id=rec_id)
        rec.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UpdateBlog(APIView):

     def put(self, request):
        rec_id = request.data["id"]
        rec = Blog.objects.get(id=rec_id)
        
        serializer = BlogSerializer(rec, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)