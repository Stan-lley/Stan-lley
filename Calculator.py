class Employee:
  """
  Base class for all employee types.
  """
  def __init__(self, emp_id, name):
    self.emp_id = emp_id
    self.name = name

  def calculate_payroll(self):
    """
    Abstract method to calculate the employee's weekly payroll.

    This method should be implemented by subclasses.
    """
    raise NotImplementedError("Subclass must implement calculate_payroll()")

class SalaryEmployee(Employee):
  """
  Employee class for salaried employees.
  """
  def __init__(self, emp_id, name, weekly_salary):
    super().__init__(emp_id, name)
    self.weekly_salary = weekly_salary

  def calculate_payroll(self):
    """
    Calculates the weekly payroll for a salaried employee.

    Returns:
      The weekly salary of the employee.
    """
    return self.weekly_salary

class HourlyEmployee(Employee):
  """
  Employee class for hourly employees.
  """
  def __init__(self, emp_id, name, hours_worked, hourly_rate):
    super().__init__(emp_id, name)
    self.hours_worked = hours_worked
    self.hourly_rate = hourly_rate

  def calculate_payroll(self):
    """
    Calculates the weekly payroll for an hourly employee.

    Returns:
      The total earnings for the hours worked by the employee.
    """
    return self.hours_worked * self.hourly_rate

class CommissionEmployee(SalaryEmployee):
  """
  Employee class for commission-based employees.
  """
  def __init__(self, emp_id, name, weekly_salary, commission):
    super().__init__(emp_id, name, weekly_salary)
    self.commission = commission

  def calculate_payroll(self):
    """
    Calculates the weekly payroll for a commission-based employee.

    Returns:
      The total earnings (salary + commission) for the employee.
    """
    return super().calculate_payroll() + self.commission

# Example usage
emp1 = SalaryEmployee(1, "John Doe", 1000)
emp2 = HourlyEmployee(2, "Jane Smith", 40, 20)
emp3 = CommissionEmployee(3, "Michael Lee", 800, 100)

employees = [emp1, emp2, emp3]

for emp in employees:
  print(f"{emp.name} - Weekly Payroll: ${emp.calculate_payroll():.2f}")
