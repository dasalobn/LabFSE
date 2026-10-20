n = int(input("введите количество секунд: "))

hours = n // 3600 % 24
minutes = (n % 3600) // 60
seconds = n % 60

print("время:", "{}:{:02}:{:02}".format(hours, minutes, seconds))