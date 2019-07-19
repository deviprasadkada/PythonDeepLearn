class Employee:

    employeeCount=0

    def __init__(self, employeedt):
        self.emp_details = employeedt
        self.employeeCount =len(employeedt)
        self.display_employee_details()

    def display_employee_details(self):
        print("Total number of employees: ", self.employeeCount)

        employeeSalary= 0

        for count in range(len(self.emp_details)):
            employeeSalary=employeeSalary+float(self.emp_details.get(count)[2])
            print("Employee %s Details :" % str(count+1))
            print("Employee Name : %s, Employee Family : %s, Employee Salary : %f, Employee Department : %s "
                  % (str(self.emp_details.get(count)[0]), str(self.emp_details.get(count)[1]),
                    float(self.emp_details.get(count)[2]), str(self.emp_details.get(count)[3])))
            print("Employees Average Salary: %f " % (employeeSalary / self.employeeCount))
