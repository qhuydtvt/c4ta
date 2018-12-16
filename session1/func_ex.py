def triangle_area(a, h):
  area = a * h * 0.5
  return area

def caculate(x, y, op):
  if op == "+":
    r = x + y
    return r
  elif op == "-":
    r = x - y
    return r

# Unit tests
a = triangle_area(5, 2)
assert(a == 5.0)

a = triangle_area(5, 6)
assert(a == 15)

a = triangle_area(10, 7)
assert(a == 35)

s = caculate(4, 5, "+")
assert(s == 9)

s = caculate(8, 10, "-")
assert(s == -2)