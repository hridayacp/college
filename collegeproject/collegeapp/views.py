from django.shortcuts import render,redirect
from collegeapp.models import Department,User,Teacher,student
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout


def adminhome(request):
    return render(request,'adminhome.html')

def teacherhome(request):
    return render(request,'teacherhome.html')

def studenthome(request):
    return render(request,'studenthome.html')


def adddep(request):
    if request.method=="POST":
        d=request.POST['dep']
        x=Department.objects.create(Dep_Name=d)
        x.save()
        return HttpResponse("<script>alert('added successfully');</script>")
    else:
        return render(request,'adddep.html')
    

    
def addteacher(request):
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        ph=request.POST['phone']
        qu=request.POST['qual']
        d=request.POST['did']
        print(f,l,e,u,p,ph,qu,d)
        x=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l,usertype="teacher")
        x.save()
        y=Teacher.objects.create(teach_id=x,Qualification=qu,phone=ph,dep_id_id=d)
        y.save()
        return HttpResponse("success")
    else:
        x=Department.objects.all()
        return render(request,'addteacher.html',{'data':x})


def mainhome(request):
    return render(request,'mainhome.html')


def addstudent(request):
    if request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        ph=request.POST['phone']
        pl=request.POST['place']
        d=request.POST['did']
        x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,usertype="student",is_active=False)
        x.save()
        y=student.objects.create(dep_id_id=d,phone=ph,place=pl,stud_id=x)
        y.save()
        return HttpResponse("success")
    else:
        x=Department.objects.all()
        return render(request,'addstudent.html',{'data':x})
    

def viewstudents(request):
    x=student.objects.all()
    return render(request,'viewstudents.html',{'data':x})

def admin_approve_students(request,aid):
    stud=student.objects.get(id=aid)
    stud.stud_id.save()
    return redirect(viewstudents)

def logins(request):
    if request.method=="POST":
        un=request.POST['uname']
        ps=request.POST['password']
        print(un,ps)
        user=authenticate(request,username=un,password=ps)
        print(user)
        if user is not None and user.is_superuser==1:
            return redirect(adminhome)
        elif user is not None and user.usertype=="teacher":
            login(request,user)
            request.session['teacher_id']=user.id
            return redirect(teacherhome)
        elif user is not None and user.usertype=="student" and user.is_active==1:
            login(request,user)
            request.session['student_id']=user.id
            return redirect(studenthome)
        else:
            return HttpResponse("invalid")
    else:
        return render(request,'logins.html')
    


def logouts(request):
    logout(request)
    return redirect(mainhome)


# def updateteacher(request):
#     teach=request.session.get("teacher_id")
#     print(teach,"..............")
#     teacher=Teacher.objects.get(teach_id_id=teach)
#     user1=User.objects.get(id=teach)
#     print(teacher,"okkk")
#     print(user1,"hello")
#     return render(request,'updateteacher.html',{"teacher":teacher,"user1":user1})


# def updateteacher1(request,uid):
#     if request.method=="POST":
#         teach=Teacher.objects.get(id=uid)
#         tid=teach.teach_id_id
#         print(teach,tid)

#         user1=User.objects.get(id=tid)
#         user1.first_name=request.POST['fname']
#         user1.last_name=request.POST['lname']
#         user1.email=request.POST['email']
#         user1.save()
#         teach.phone=request.POST['phone']
#         teach.Qualification=request.POST['qual']
#         teach.save()
#         return HttpResponse("success")


# # def viewteachers(request):
# #     x=Teacher.objects.all()
# #     return render(request,'viewteachers.html',{'data':x})
