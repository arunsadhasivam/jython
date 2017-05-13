import sqlite3


from chAPI.model.employeeForm import employee as employee





def search(employee):
    print('dao')
    db = sqlite3.connect( database='C:\softwares\sqllite\db\emp.db')
    #db = sqlite3.connect( database='emp')
    cursor = db.cursor()
    employees=[];
    query = "SELECT * FROM employee"
    cursor.execute('SELECT empid,name,employer FROM employee')
   
    employees = dictfetchall(cursor)
    db.close() 
    # employee.objects.raw(cursor.fetchall())
    #for p in employee.objects.raw('SELECT id, first_name FROM myapp_person'):
    #print(p);
        
    return employees

    #return render(request,  'home.html',{'employees': employees})




def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
    dict(zip(columns, row))
    for row in cursor.fetchall()
    ]
