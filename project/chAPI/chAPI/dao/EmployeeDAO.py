import sqlite3

from django.shortcuts import render

from chAPI.model.employeeForm import employee as employee



def search(request):
    print('dao')
    db = sqlite3.connect( database='C:\softwares\sqllite\db\emp.db')
    #db = sqlite3.connect( database='emp')
    cursor = db.cursor()
    employees=[];
    cursor.execute('SELECT * FROM employee')
    employees= cursor.fetchall();
    print (employees);
    
   
    #employees = employee.from_db(db, name_map, employees);
    print('----------')
    print(employees[0][0])
    
   
    #
    #employee.objects.raw('SELECT * FROM employee',name_map)
    #print ('employees1');
    #print (employee.objects.values_list());
    

    
   #names = ['arun','kumar','teja']
    
   #names = ['arun','kumar','teja']
    #employees = [{'Name':'Arun','Empid':'101', 'employee':'wipro'}, 
    #             {'Name':'Teja','Empid':'105', 'employee':'hcl'},
    #             {'Name':'Test','Empid':'103', 'employee':'symantec'}]

    #db.close() 
   # employee.objects.raw(cursor.fetchall())
    #for p in employee.objects.raw('SELECT id, first_name FROM myapp_person'):
    #print(employee.employee.values_list());
        

    return render(request,  'home.html',{'employees': employees})
