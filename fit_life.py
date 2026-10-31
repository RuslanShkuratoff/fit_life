user_name = input("Введите ваше имя - ")
user_age = int(input("Укажите ваш возраст - "))
user_weight = float(input("Укажите свой вес в килограммах, например: 68.5 - "))
user_height = float(input("Укажите свой рост в метрах, например: 1.68 - "))
bmi = round(user_weight / (user_height ** 2),1)
water_ml = user_weight * 30
water_l = water_ml / 1000
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l} л. в день")
