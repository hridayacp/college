from django.shortcuts import render,redirect
from collegeapp.models import Department,User,Teacher,student,Staff
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def adminhome(request):
    return render(request,'adminhome.html')


def index(request):
    return render(request,'index.html')

# @never_cache
# @login_required
def teacherhome(request):
    return render(request,'teacherhome.html')
# @never_cache
# @login_required
def studenthome(request):
    return render(request,'studenthome.html')

# @never_cache
# @login_required
def adddep(request):
    if request.method=="POST":
        d=request.POST['dep']
        x=Department.objects.create(Dep_Name=d)
        x.save()
        return HttpResponse("<script>alert('added successfully');</script>")
    else:
        return render(request,'adddep.html')
    

# @never_cache
# @login_required    
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

# @never_cache
# @login_required
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
    
# @never_cache
# @login_required
def viewstudents(request):
    x=student.objects.all()
    return render(request,'viewstudents.html',{'data':x})
# @never_cache
# @login_required
def admin_approve_students(request,aid):
    stud=student.objects.get(id=aid)
    stud.stud_id.save()
    return redirect(viewstudents)
# @never_cache
# @login_required
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
    

# @never_cache
# @login_required
def logouts(request):
    logout(request)
    return redirect(mainhome)

# @never_cache
# @login_required
def updateteacher(request):
    teach=request.session.get("teacher_id")
    print(teach,"..............")
    teacher=Teacher.objects.get(teach_id_id=teach)
    user1=User.objects.get(id=teach)
    print(teacher,"okkk")
    print(user1,"hello")
    return render(request,'updateteacher.html',{"teacher":teacher,"user1":user1})

# @never_cache
# @login_required
def updateteacher1(request,uid):
    if request.method=="POST":
        teach=Teacher.objects.get(id=uid)
        tid=teach.teach_id_id
        print(teach,tid)

        user1=User.objects.get(id=tid)
        user1.first_name=request.POST['fname']
        user1.last_name=request.POST['lname']
        user1.email=request.POST['email']
        user1.save()
        teach.phone=request.POST['phone']
        teach.Qualification=request.POST['qual']
        teach.save()
        return HttpResponse("success")

# @never_cache
# @login_required
def viewteachers(request):
    x=Teacher.objects.all()
    return render(request,'viewteachers.html',{'data':x})

def viewactivestudents(request):
    activestudents=student.objects.filter(stud_id__is_active=True)
    return render(request,"activestudents.html",{"activestudents":activestudents})

def staff_register(request):
    if request.method=="POST":
        n=request.POST.get("name")
        p=request.FILES.get("photo")
        Staff.objects.create(name=n,photo=p)
        return HttpResponse("success")
    else:
        return render(request,'staff_register.html')
    

def stafflist(request):
    staff=Staff.objects.all()
    return render(request,'stafflist.html',{'staff':staff})


def viewdepteachers(request):
    departments=Department.objects.all()
    data =[]

    for dept in departments:
        teachers=Teacher.objects.filter(dep_id=dept)
        data.append({
            'department':dept,
            'teacher':teachers
        })
    return render(request, 'departmentteachers.html',{'data':data})


def viewdepteachers_activestudents(request):
    departments=Department.objects.all()
    data =[]

    for dept in departments:
        students=student.objects.filter(dep_id=dept,stud_id__is_active=True)
        data.append({
            'department':dept,
            'students':students
        })
    return render(request,'departmentactivestudents.html',{'data':data})
