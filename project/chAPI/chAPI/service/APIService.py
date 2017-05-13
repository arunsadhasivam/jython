from chAPI.dao import EmployeeDAO as dao

class APIService():
    
    def search(self):
        print('constructor')
       
    def searchEmployee(self,employee):
        employees = dao.search(employee);
        return employees
 
    def __str__(self):
       return self;
