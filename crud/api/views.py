from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def studentView(req):
    if req.method=='GET':
     # to catch data afrom client
     json_data=req.body
     # convert into stream
     stream=io.BytesIO(json_data)

     pythondata=JSONParser().parse(stream)
     stuid=pythondata.get('id',None)
     if stuid is not None:
        stu=Student.objects.get(id=stuid)
        stuSei=StudentSerializer(stu)
        json_data=JSONRenderer().render(stuSei.data)
        return HttpResponse(json_data,content_type='application/json')
     
     stu=Student.objects.all()
     stuSei=StudentSerializer(stu, many=True)
     json_data=JSONRenderer().render(stuSei.data)
     return HttpResponse(json_data,content_type='application/json')

    if req.method=="POST":
       json_data=req.body
       stream=io.BytesIO(json_data)
       pythondata=JSONParser().parse(stream)
       stuSei=StudentSerializer(data=pythondata)
       if stuSei.is_valid():
          stuSei.save()
          res={'msg':"Data Added Successfully"}
          json_data=JSONRenderer().render(res)
          return HttpResponse(json_data,content_type='application/json')
       json_data=JSONRenderer().render(stuSei.errors)
       return HttpResponse(json_data,content_type='application/text')
   
    if req.method=="PUT":
       json_data=req.body
       stream=io.BytesIO(json_data)
       pythondata=JSONParser().parse(stream)
       stuid=pythondata.get('id')
       stu=Student.objects.get(id=stuid)
       stuSei=StudentSerializer(stu,data=pythondata,partial=True)
       if stuSei.is_valid():
          stuSei.save()
          res={'msg':"Data Updated Successfully"}
          json_data=JSONRenderer().render(res)
          return HttpResponse(json_data,content_type='application/json')
       json_data=JSONRenderer().render(stuSei.errors)
       return HttpResponse(json_data,content_type='application/text')
    #   For Full data Update
    if req.method=="PUT":
       json_data=req.body
       stream=io.BytesIO(json_data)
       pythondata=JSONParser().parse(stream)
       stuid=pythondata.get('id')
       stu=Student.objects.get(id=stuid)
       stuSei=StudentSerializer(stu,data=pythondata)
       if stuSei.is_valid():
          stuSei.save()
          res={'msg':"Data Updated Successfully"}
          json_data=JSONRenderer().render(res)
          return HttpResponse(json_data,content_type='application/json')
       json_data=JSONRenderer().render(stuSei.errors)
       return HttpResponse(json_data,content_type='application/text')
    
  
    if req.method=="DELETE":
       json_data=req.body
       stream=io.BytesIO(json_data)
       pythondata=JSONParser().parse(stream)
       stuid=pythondata.get('id')
       stu=Student.objects.get(id=stuid)
       stuSei=StudentSerializer()
       stu.delete()
       res={"msg":"Deleted SucessFully"}
       return JsonResponse(res,safe=False)
    res={"msg":"ID dont exist"}
    return JsonResponse(res,safe=False)
   
    
  