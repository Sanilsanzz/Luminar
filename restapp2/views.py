from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime

class HelloWorld(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Helloworld.."})

class HiWorld(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Hiworld.."})


class Greetings(APIView):
    def get(self,request):
        cdate=datetime.datetime.now()
        chour=cdate.hour
        msg=""
        if chour<12:
            msg="Good Morning"
        elif chour<18:
            msg="Good Afternoon"
        else:
            msg="Good Nyt"
        return Response({"Hello":msg})

class Add(APIView):
    def post(self,request):
        print(request.data)
        n1=request.data.get("num1")
        n2 = request.data.get("num2")
        total=n1+n2
        return Response({"Hello":total})

class factorial(APIView):
    def post(self,request):
        fact=0
        print(request.data)
        f1=request.data.get("factorial1")
        if f1<0:
            print("No factorial")
        elif f1==0:
            fact=1
        else:
            for i in range(1,fact+1):
                fact=fact*1
        return Response({"Factorial:":fact})




        total=n1+n2
        return Response({"Hello":total})