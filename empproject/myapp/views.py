from django.shortcuts import render
from myapp.models import Employee
# Create your views here.
def myview(request):
    res=Employee.objects.all()
    d={'key':res}
    return render(request,'myapp/result.html',d)