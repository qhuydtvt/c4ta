# Khai bao (1)
def say_hello(name, is_female):
  print("Hello", name)
  if is_female:
    print("You're so pretty")
  else:
    print("You're so handsome")
  print("Byebye")

def add(a, b):
  s = a + b
  return s

# Goi ham (n)
say_hello("Nguyen", False)
say_hello("Nhi", True)
say_hello("Trung", False)

a = 7
u = add(a, 8) # u = 15
t = add(5, 6) # t = 11
result = add(u, t)
print(result)