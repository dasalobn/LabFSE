import random
import time

n = int(input("Введите количество примеров: "))

correct_answers = 0
total_time = 0.0

for i in range(1, n + 1):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    
    print(f"Вопрос {i}/{n}")
    start_time = time.time()
    
    while True:
        try:
            answer = int(input(f"{a} × {b} = "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")
            
    time_spent = time.time() - start_time
    total_time += time_spent
    
    if answer == a * b:
        print(f"Верно! (Время: {time_spent:.1f} сек)")
        correct_answers += 1
    else:
        print(f"Неверно! Правильно: {a * b} (Время: {time_spent:.1f} сек)")

avg_time = total_time / n if n > 0 else 0
percent_correct = (correct_answers / n) * 100 if n > 0 else 0

print("=" * 30)
print("СТАТИСТИКА:")
print("=" * 30)
print(f"Общее время: {total_time:.1f} секунд")
print(f"Среднее время на вопрос: {avg_time:.1f} сек")
print(f"Правильных ответов: {correct_answers}/{n}")
print(f"Процент правильных: {percent_correct:.1f}%")
