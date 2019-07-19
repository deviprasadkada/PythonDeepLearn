class Employee():
    empCount = 0 #initialization of the data member
    empSal = [];
    def __init__(self,name,family,salary,department): #default constructor
        self.empname = name
        self.empfamily = family
        self.empsalary = salary
        self.empdepartment = department
        Employee.empCount +=1  #counts the number of employees
        Employee.empSal.append(salary)  #appends salaray attribute

    def avg_salary(self):
        print('the average salary is')
        sumSal = 0;
        for sal in Employee.empSal:
            sumSal = sumSal+ int(sal);
        return sumSal/len(Employee.empSal)

class FulltimeEmployee(Employee):
    def _init_(self,name,family,salary,department):
        Employee._init_(self,name,family,salary,department)


emp1 = FulltimeEmployee('prasad','kada','75000','Sales');
emp2 = FulltimeEmployee('elijah','micheal','80000','FInance');
emp3 = FulltimeEmployee('taylor','summers','65000','Marketing');
emp4 = FulltimeEmployee('alex','jones','78000','sales');
print(FulltimeEmployee.empCount)
print(FulltimeEmployee.empSal)
avgSal = FulltimeEmployee.avg_salary(Employee);
print(avgSal)