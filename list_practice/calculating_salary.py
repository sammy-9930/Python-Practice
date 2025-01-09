def calculate_salary(work_hours, salary):
    weekly_wage = 0
    for hour in work_hours:
        total_wage = hour * salary 
        weekly_wage += total_wage
    return weekly_wage

"""to take input as list, use split(). split converts input into string so to convert back to int type, 
we use list comprehension."""
work_hours = [int(x) for x in input("Enter work hours of the week, separated by space: ").split()]
salary = float(input("Enter salary: "))
print(calculate_salary(work_hours, salary))
