def draw_rectangle(rows, columns, ch):
    print(f"ПРЯМОУГОЛЬНИК {rows}x{columns}:")
    for i in range(rows):
        for j in range(columns):
            print(ch, end="")
        print()

def draw_triangle(rows, ch):
    print("ПРАВЫЙ ТРЕУГОЛЬНИК:")
    for i in range(1, rows + 1):
        for j in range(i):
            print(ch, end="")
        print()

def draw_frame(rows, columns, ch):
    print(f"РАМКА {rows}*{columns}:")
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print(ch, end="")
            else:
                print(" ", end="")
        print()

n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))

print()
draw_rectangle(n, m, "#")
print()
draw_triangle(n, "#")
print()
draw_frame(n, m, "#")
