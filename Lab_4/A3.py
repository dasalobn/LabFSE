packets = input()

if len(packets) < 5 or not all(char in '01' for char in packets):
    print("Неверный ввод. Используйте только символы '0' и '1' (длина не менее 5)!")
else:
    total_packets = len(packets)
    lost_packets = packets.count('0')
    
    max_zeros = 0
    current_zeros = 0
    for packet in packets:
        if packet == '0':
            current_zeros += 1
            if current_zeros > max_zeros:
                max_zeros = current_zeros
        else:
            current_zeros = 0
            
    loss_percent = (lost_packets / total_packets) * 100
    
    if loss_percent <= 1:
        quality = "отличное"
    elif loss_percent <= 5:
        quality = "хорошее"
    elif loss_percent <= 10:
        quality = "удовлетворительное"
    elif loss_percent <= 20:
        quality = "плохое"
    else:
        quality = "критическое состояние сети"
        
    print(f"Общее количество пакетов: {total_packets}")
    print(f"Количество потерянных пакетов: {lost_packets}")
    print(f"Длина самой длинной последовательности потерянных пакетов: {max_zeros}")
    print(f"Процент потерь: {loss_percent:.1f}%")
    print(f"Качество связи: {quality}")
