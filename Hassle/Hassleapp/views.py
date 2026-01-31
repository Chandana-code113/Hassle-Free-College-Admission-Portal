from django.shortcuts import render
import pymysql
# Create your views here.
def home(request):
    return render(request,"home.html")
def Hasslestudent(request):
    return render(request,"Hasslestudent.html")
def Hasslestudentregistration (request):
    return render(request,"Hasslestudentregistration.html")
def Hasslestudentregistrartionaction(request):
    n=request.POST["name"]
    g=request.POST["gender"]
    l=request.POST["lang"] 
    y=request.POST["year"]
    u=request.POST["username"]
    p=request.POST["password"] 

    con=pymysql.connect(host="localhost",user="root",password="root",database="HassleCollege",charset="utf8")
    cur=con.cursor()
    i=cur.execute("insert into student values('"+n+"','"+g+"','"+l+"','"+y+"','"+u+"','"+p+"')")
    con.commit()
    if i>0:   
        context={'data':'Registration Successfull'}
        return render(request,"Hasslestudentregistration.html",context)
    else:
        context={'data':'Registration Failed'}
        return render(request,"Hasslestudentregistration.html",context)

def Hasslestudentlgaction(request):
    u=request.POST["username"]
    p=request.POST["password"]
    con=pymysql.connect(host="localhost",user="root",password="root",database="HassleCollege",charset="utf8")
    cur=con.cursor()
    i=cur.execute("select *from student where username='"+u+"' and password='"+p+"' ")
    con.commit()
    
    if i>0:   
        context={'data':'Login Successfull'}
        return render(request,"home.html",context)
    else:
        context={'data':'Login Failed'}
        return render(request,"home.html",context)
