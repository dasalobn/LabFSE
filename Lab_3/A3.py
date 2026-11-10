prev = int(input())
curr = int(input())

if curr >= prev:
    used = curr - prev
else:
    used = (10000 - prev) + curr

# Расчет стоимости по ступенчатому тариф
if used <= 300:
    cost = 21.0
elif used <= 600:
    cost = 21.0 + (used - 300) * 0.06
elif used <= 800:
    cost = 21.0 + 300 * 0.06 + (used - 600) * 0.04
else:
    cost = 21.0 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025

avg_price = cost / used if used > 0 else 0.0

print(f"{'Предыдущее':<14}{'Текущее':<12}{'Использовано':<16}{'К оплате':<12}{'Ср. цена m^3'}")
print(f"{prev:^10}{curr:^15}{used:^14}{cost:^16.2f}{avg_price:^10.2f}")
