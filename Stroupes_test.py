import colorama, random, time, os
colorama.just_fix_windows_console()

CHANGE_SPEED = 1
QUANTITY = 30 

WORD_LIST = [
    "красный",
    "синий",
    "зелёный",
    "жёлтый",
    "белый",
    "чёрный",
    "фиолетовый",
    "оранжевый",
    "серый",
    "коричневый",
    "розовый"
]

COLOR_LIST = [
    colorama.Fore.RED,
    colorama.Fore.BLUE,
    colorama.Fore.GREEN,
    colorama.Fore.YELLOW,
    colorama.Fore.WHITE,
    colorama.Fore.BLACK,
    colorama.Fore.MAGENTA,
]

print("\t\tДобро пожаловать в программу генерации Теста Стурпа!")
print(f"У вас будет {CHANGE_SPEED} секунды, чтобы сказать, каким цветом написано слово. Всего слов: {QUANTITY}")
print("\t\t\tПо окочанию времени, программа закроется.\n")
os.system("pause")

def generate_word(words: list, colors: list) -> None:
    word = random.choice(words)
    color = random.choice(colors)
    print(color + word)

for i in range(QUANTITY):
    os.system("cls")
    generate_word(WORD_LIST, COLOR_LIST)
    time.sleep(CHANGE_SPEED)

print(colorama.Fore.WHITE + "Количество слов кончилось! Перезапускайте программу, если потребуется")