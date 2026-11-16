from random import shuffle
from time   import sleep
from os     import system

SEEK_TIME = 30
COLUMNS = 5
STRINGS = 5

def generate_table(stroki, stolbci: int) -> None:
    size = stroki * stolbci
    spisok = []

    for i in range(1, size+1):
        spisok.append(i)

    shuffle(spisok)

    num = 0
    for i in range(stolbci):
        for i in range(stroki):
            print(f"{spisok[num]}\t", end="")
            num+=1

        print("\n")

print(f"""
\t\tДобро пожаловать в программу генерации таблицы Шульте!
\tУ вас будет {SEEK_TIME} секунд, чтобы найти на экране {COLUMNS*STRINGS} чисел и сосчитать их.
\t\t\tПо окочанию времени, программа закроется.
""")
system('pause')
system('cls')

generate_table(COLUMNS, STRINGS)
for i in range(1, SEEK_TIME+1):
    print(f"\rОставшееся время: {30-i:>2}", end="")
    sleep(1)

print("\nВремя вышло! Перезапускайте программу, если потребуется")