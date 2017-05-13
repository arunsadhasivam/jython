from django.shortcuts import render
from chAPI.service.APIService import APIService
from chAPI.model.employeeForm import employee





def  registration(request):
    return render(request,  'registration.html');

def  search(request):
    #if request.method == 'GET':
    #    qd = request.GET
    #elif request.method == 'POST':
    # qd = request.POST */
     
    empId = request.GET['username']
   
    employee.empid =empId;
    employees =  APIService.searchEmployee('',employee);
    return render(request,  'home.html',{'employees': employees})
    


