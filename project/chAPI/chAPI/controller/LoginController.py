from django.shortcuts import render
from chAPI.service.APIService import APIService
from chAPI.model.employeeForm import employee


def  registration(request):
    return render(request,  'registration.html');

def  search(request):
    employees =  APIService.searchEmployee('',employee);
    return render(request,  'home.html',{'employees': employees})
    
