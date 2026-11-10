def is_valid_card(card_number):
    clean_number = card_number.replace(" ", "").replace("-", "")
    
    if not clean_number.isdigit() or not (13 <= len(clean_number) <= 19):
        return False

    total_sum = 0
    
    reversed_digits = clean_number[::-1]

    for i, char in enumerate(reversed_digits):
        digit = int(char)
        
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
                
        total_sum += digit

    return total_sum % 10 == 0

card = input("Введите номер карты: ")
if is_valid_card(card):
    print("Номер карты действителен")
else:
    print("Ошибка: неверный номер карты")
