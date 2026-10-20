x1 = int(input("введите x1: "))
y1 = int(input("введите y1: "))
x2 = int(input("введите x2: "))
y2 = int(input("введите y2: "))

color1 = (x1 + y1) % 2  # 0 — белая, 1 — чёрная
color2 = (x2 + y2) % 2

if color1 == color2:
    print("клетки одного цвета: YES")
    print("цвет клеток:", "White" if color1 == 0 else "Black")
else:
    print("клетки разного цвета: NO")