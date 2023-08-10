from django.shortcuts import render,get_object_or_404, redirect
from testapp.models import vehicle
from django.contrib import messages
from .models import vehicle
from .models import UserRole
from .forms import VehicleForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def test1(request):
    return render(request,"back.html")

def form1(request):
    return render(request,"form.html")

def saver2(request):
    if request.method=="POST":
        num=request.POST.get("number")
        typ = request.POST.get("type")
        mod = request.POST.get("model")
        desc = request.POST.get("description")

        obj=vehicle(number=num,type=typ,model=mod,description=desc)
        obj.save()
        return redirect(form1)

@login_required
def display1(request):
    data=vehicle.objects.all()
    return render(request,"display.html",{"data":data})


@login_required
def edit1(request,dataid):
    data=vehicle.objects.get(id=dataid)
    messages.success(request, "Vehicle Updated Successfully")
    return render(request,"edit.html",{"data":data})

@login_required
def update1(req,dataid):
    if req.method == "POST":
        num = req.POST.get("name")
        typ = req.POST.get("type")
        mod = req.POST.get("model")
        des = req.POST.get("description")
        vehicle.objects.filter(id=dataid).update(number=num,type=typ,model=mod,description=des)
        messages.success(req, "Data Updated")
        return redirect(display1)

@login_required
def delete1(request,dataid):
    data=vehicle.objects.filter(id=dataid)
    data.delete()
    messages.error(request, "Vehicle Deleted")
    return redirect(display1)


# vehicles/views.py

def assign_roles():
    super_admin, created = User.objects.get_or_create(username='superadmin')
    super_admin.set_password('superadmin')
    super_admin.save()

    admin, created = User.objects.get_or_create(username='admin')
    admin.set_password('admin')
    admin.save()

    user, created = User.objects.get_or_create(username='user')
    user.set_password('user')
    user.save()

    if created:
        UserRole.objects.create(user=super_admin, role='SuperAdmin')
        UserRole.objects.create(user=admin, role='Admin')
        UserRole.objects.create(user=user, role='User')
