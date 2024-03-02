Class Employee:
    def __init__(self,emp_id,name)
      self.emp_id=emp_id
      self.name=name
    
        
class SalaryEmployee(Employee):
    def __init__(self,emp_id,name,weekly_salary) 
       super().__init__(emp_id,name)
       self.weekly_salary=weekly_salary
    def calculate_payroll(self):
        return self.weekly_salary 
        
class HourlyEmployee(Employee):
    def __init__(self,emp_id,name, hours_worked,hourly_rate) 
       super().__init__(emp_id,name)
       self.hours_worked=hours_worked
       self.hourly_rate=hourly_rate
    def calculate_payroll(hours_worked,hourly_rate)
       payroll=hours_worked*hourly_rate
       return payroll
       
class commissionEmployee(SalaryEmployee):
    def __init__(self,weekly_salary, commission_value,sales,fixed_salary)
        super().__init__(weekly_salary)
        self.commission_value=commission_value
        self.sales=sales
        self.fixed_salary=fixed_salary
    def calculate_payroll(fixed_salary, commission_value,sales)
        payroll=fixed_salary+((commission*sales)/100)
        return payroll
