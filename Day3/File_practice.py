read_file = open("C:\\Users\\Anilreddy\\OneDrive\\Desktop\\Python\\Day3\\emp.csv",'r')
s = read_file.read()
read_file.close()

print(type(s),len(s))
print("") # empty line
print("Display file content")
print(s)



print("========================readline()=====================")
read_emp = open("C:\\Users\\Anilreddy\\OneDrive\\Desktop\\Python\\Day3\\emp.csv",'r')
load = read_emp.readlines()
read_emp.close()

print(type(load),len(load))
print("") # empty line
print("Display file content")
print(load)