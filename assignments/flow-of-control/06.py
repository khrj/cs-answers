(a := float(input("Enter side 1: "))) and (b := float(input("Enter side 2: "))) and (c := float(input("Enter side 3: "))) and print("equilaterial" if a == b == c else ("isosceles" if a == b or b == c or c == a else "scalene"))