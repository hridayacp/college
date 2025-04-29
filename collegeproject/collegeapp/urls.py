from django.urls import path
from collegeapp import views

urlpatterns = [

    path('',views.index,name='index'),
    
    path('logins',views.logins,name='logins'),
    path('logouts',views.logouts,name='logouts'),


    path('adminhome',views.adminhome,name='adminhome'),
    path('teacherhome',views.teacherhome,name='teacherhome'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('',views.mainhome,name='mainhome'),
    
    path('adddep',views.adddep,name='adddep'),
    path('addteacher',views.addteacher,name='addteacher'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('viewstudents',views.viewstudents,name='viewstudents'),
    path('admin_approve_students/<int:aid>',views.admin_approve_students,name='admin_approve_students'),
    path('updateteacher',views.updateteacher,name='updateteacher'),
    path('updateteacher1/<int:uid>',views.updateteacher1,name='updateteacher1'),
    path('viewteachers',views.viewteachers,name='viewteachers'),
    path('viewactivestudents',views.viewactivestudents,name='viewactivestudents'),
    path('staff_register',views.staff_register,name='staff_register'),
    path('stafflist',views.stafflist,name='stafflist'),


]

