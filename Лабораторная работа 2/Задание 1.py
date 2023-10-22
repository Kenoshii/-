money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
coast = 0
rashod = spend - salary #количество денег которое отнимается от падушки безопасности
while rashod <= money_capital:
    spend = spend + (spend * increase)#увеличение трат следующего мес. с учетом роста цен
    rashod = spend - salary
    money_capital = money_capital - rashod
    coast +=1
print("Количество месяцев, которое можно протянуть без долгов:", coast)
