"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #
def is_on_list(list, element):
  for i in list:
    if i == element:
      return True
  return False

def get_x(list, num):
  return list[num]

def add_x(list, element):
  return list.append(element)

def remove_x(list, element):
  return list.remove(element)
  
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)


# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #




