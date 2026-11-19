deti = int(input("Количество детей: "))
oranges = int(input("Количество мандаринов: "))

if oranges >= deti:
    print(f"Все дети с мандаринами\nOстаток: {oranges % deti}")
else:
    print(f"{deti - oranges} детям не хватает мандаринов")