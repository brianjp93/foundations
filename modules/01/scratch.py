from sympy import symbols, simplify

x, y, z = symbols('x, y, z')

stmt1 = ~x & ~y & ~z
stmt2 = ~x & y & ~z
stmt3 = x & ~y & ~z


expr = stmt1 | stmt2 | stmt3
expr = simplify(expr)
print(expr)
