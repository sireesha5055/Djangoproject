from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
import myapp.models import Product 
def wel(request):
    return HttpResponse("<h1 style ='text-align :center ; border:1px solid green ; background-color:gold'> Welocme to my application")
def Home(request):
    return HttpResponse("<h2>welcome</h2>")
def hai(request):
    return render(request,"hai.html",{ })
def hai_vars(request):
    eid = 101 
    ename = 'siri'
    esal = 17000000
    return render(request,"vform.html",{'eid': eid,'ename': ename,'esal': esal})

def emp(request):
    template= loader.get_template("empform.html")
    context={
    'ename':'k.sireesha',
    'dname':'mlc',
    'sub':'politics',
    }
    return HttpResponse(template.render(context,request))
def dept(request, dname,dno,dlocation):
    return render(request,"dform.html",{'dname':dname,'dno':dno ,'dlocation':dlocation})
def test1(request):
    template=loader.get_template("hform.html")
    return HttpResponse(template.render())
def test2(request):
    template=loader.get_template("home.html")
    context={
        'uname':'sireesha',
        'pass':'sireesha123', }
    return HttpResponse(template.render(context,request))

def test3(request):
    template=loader.get_template("susform.html")
    return HttpResponse(template.render())

def test4(request):
    template=loader.get_template("fform.html")
    return HttpResponse(template.render())

def login(request):
    return render(request,"login.html",{})


def form_submit(request):
    if request.method=='POST':
         uname=request.POST.get('uname')
         pwd=request.POST.get('pwd')
         if uname == 'admin' and pwd == 'admin':
                return render(request,"sus.html",{'uname':uname ,'pwd':pwd})
         else:
                return render(request,"fail.html",{})



def test_for(request):
    template=loader.get_template("fform2.html") 
    context={
        'emps':[
            {'eid':'101','ename':'ravi','esal':'1900000','deptno':'1'},
            {'eid':'102','ename':'rani','esal':'130000','deptno':'2'},
            {'eid':'103','ename':'rajesh','esal':'450000','deptno':'3'},
            {'eid':'104','ename':'rama','esal':'600000','deptno':'4'},
        ],
    }
    return HttpResponse(template.render(context,request))

def test_for_secondex(request):
     template=loader.get_template("rform.html")
     context={
          "arr":[10,20,30,40,40,50,60],
    }
     return HttpResponse(template.render(context,request))

def emp_Details(request):
     template=loader.get_template("emp_report.html")
     context ={
          'emp':[ {'eid':'101','ename':'suma','esal':'180000' },
               {'eid': '102','ename':'siri','esal':'180100'},
               {'eid':'103','ename':'suri','esal':'180400'},
               {'eid': '104','ename':'chinna','esal':'183000'},
           ],
     }
     return HttpResponse(template.render(context,request))

def product_Details(request):
     template=loader.get_template("product_report.html")
     context ={
          'product':[
               {'pNo':'1','pname':"Bike",'pprice':'30000000'},
               {'pNo':'3','pname':"Bike",'pprice':'30000000'},
               {'pNo':'2','pname':"Bike",'pprice':'30000000'},
          ],
        
     }
     return HttpResponse(template.render(context,request))

def dept_Details(request):
     template=loader.get_template("dept_report.html")
     context ={
          'dept':[
               {'DeptNo':'1','Deptname':"Motor"},
               {'DeptNo':'2','Deptname':"Engine"},
          ],
        
     }
     return HttpResponse(template.render(context,request))

def test_for_empty(request):
     template = loader.get_template("fempty.html")
     context={
          'arr':[10,20,30,40,50,60],
     }
     return HttpResponse(template.render(context,request ))

def test_two_same_objs(request):
      template = loader.get_template("isform.html")
      context={
           "a": [1,2,3,4,5],
           "b": [1,2,3,4,5],
      }
      return HttpResponse(template.render(context,request))
           
def Big(request):
     template=loader.get_template("bform.html")    
     context={
          'a':10,
          'b':20,
          'c':30,
          'd':40,
     }
     return HttpResponse(template.render(context,request))

def iform(request):
     return render(request,"iform.html",{ })
     0
def form_submit2(request):
     if request.method == 'GET':
          a = request.GET.get('a')
          b = request.GET.get('b')
          c = request.GET.get('c')
          d = request.GET.get('d')
          if a > b and a > c and a > d :
               
             txt="<html><body><h1 style=text-align:center;background-color:blue> A is big <a href='/iform'  style='color:green;'>Home</a> </h1></body></html>"
             return HttpResponse(txt)  
          elif b > a and b > c and b > d :
               
            txt="<html><body><h1 style=text-align:center;background-color:blue> B is big <a href='/iform' style='color:green;'>Home</a> </h1></body></html>"
            return HttpResponse(txt)  

          elif c > a and c > b and c > d :
               
            txt="<html><body><h1 style=text-align:center;background-color:blue> C is big <a href='/iform'  style='color:green;'>Home</a> </h1></body></html>"
            return HttpResponse(txt)  
          else:
            txt="<html><body><h1 style=text-align:center;background-color:blue>D  is big <a href='/iform'  style='color:green;'>Home</a></h1></body></html>"

            return HttpResponse(txt)  


def Product_insert(request):
    x1=Product(pid=101,pname='Lux',price=1500)
    x1.save()
    template=loader.get_template("insform.html")
    return HttpResponse(template,render())            
     
     

       


   