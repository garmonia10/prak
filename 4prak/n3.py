chislo = int(input("Введите любое 4-ёх значное число: "))

def checker(x):
    if len(str(x)) != 4:
        print("Введено неверное число")
        return

checker(chislo)
tisha = chislo // 1000
sotnia = (chislo - tisha*1000) // 100
desiat = (chislo - ((tisha*1000)+(sotnia*100))) // 10
edinica = chislo - (tisha*1000+sotnia*100+desiat*10)

print("Тысячи: ", tisha)
print("Сотни: ", sotnia)
print("Десятки: ", desiat)
print("Единицы: ", edinica)