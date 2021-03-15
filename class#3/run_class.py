# module/class/run_class.py
import classPerson

name = "sudawan ngaosri"
age = 21
address = "London"

Person = classPerson(name, age, address)

print(Person.get_name())
print(Person.get_age())
print(Person.get_address())
print(Person.get_info())