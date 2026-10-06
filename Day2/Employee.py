Emp = ['101,john,sales,1000','102,ram,prod,2000','103,raju,hr,3000','104,bibu,sales,4000']
total = 0
for var in Emp:
    e_id,emp_name,emp_dept,emp_cost = var.split(',')
    print(f"Emp Name:{emp_name.title()}\t Emp Dept:{emp_dept.upper()}") # display empName in title case and emp department in upper case
    total = total +int(emp_cost)
    
print(f"Total Salary:{total}") # display the total salary