from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . models import Employee,Role,Department
from .form import EmployeeForm
from django.db.models import Q




# Create your views here.

#home page
def index(request):
    return render(request, 'index.html')


def view_all_employees(request):
    emp = Employee.objects.all()
    context = {
        'emp': emp
    }
        
    
    return render(request, 'view_all_employees.html',context)

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_all_employees')  
    else:
        form = EmployeeForm()
    
    return render(request, 'add_employees.html', {'form': form})





def remove_employee(request, emp_id = 0):
    if emp_id:
     try:
        emp_to_remove = Employee.objects.get(id=emp_id)
        emp_to_remove.delete()
        return HttpResponse("Employee  has been removed!!!")
     except:
        return HttpResponse("Employee does not exist.")


    emp = Employee.objects.all()
    context = {
        'emp': emp
    }
    return render(request, 'remove_employee.html', context)



def filter_employee_details(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')  # Use get() method to handle the absence of the key
        dept = request.POST.get('dept', '')  
        role = request.POST.get('role', '')  
        
        emp = Employee.objects.all()

        if name:
            emp = emp.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        
        if dept:
            emp = emp.filter(dept__name__icontains=dept)
        
        if role:
            emp = emp.filter(role__name__icontains=role)
            
        context = {
            'emp': emp
        }
        
        return render(request, 'view_all_employees.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_employee_details.html')

    else:
        return HttpResponse('An exception occurred')