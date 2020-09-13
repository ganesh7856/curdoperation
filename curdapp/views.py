from django.shortcuts import render,redirect
from curdapp.models import Employee
from curdapp.form import EmployeeForm
# Create your views here.

def Employee_views(request):
    employees=Employee.objects.all()
    return render(request,'curdapp/info.html',{'employees':employees})

def Employee_info(request):
    form=EmployeeForm()
    if request.method=='POST':
         form=EmployeeForm(request.POST)
         if form.is_valid:
          form.save()
          return redirect('/info')
    return render(request,'curdapp/create.html',{'form':form})

def Employee_Delet(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/info')

def Employee_update(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
         form=EmployeeForm(request.POST,instance=employee)
         if form.is_valid:
          form.save()
          return redirect('/info')
    return render(request,'curdapp/update.html',{'employee':employee})
