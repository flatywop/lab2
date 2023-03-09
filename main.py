"nmj';l"
def zad1():
    mesto = int(input())
    if 37 <= mesto <= 54:
        print("Боковое место")
    elif mesto // 2 == 0 :
        print("Верхнее место")
    elif mesto // 2 != 0 :
        print("Нижнее место")


def zad2():
    god = int(input("Введите год"))
    if (god % 4 == 0 and god % 100 != 0) or god % 400 == 0:
        print("Год високосный")
    else :
        print("Не високосный")



def zad3():
    cvet1 = input("Какой первый цвет")
    cvet2 = input("Какой второй цвет")
    if (cvet1 == "красный" and cvet2 == "синий") or (cvet1 == "синий" and cvet2 == "красный"):
        print("фиолетовый")
    elif (cvet1 == "красный" and cvet2 == "желтый") or (cvet1 == "желтый" and cvet2 == "красный"):
        print("оранжевый")
    elif (cvet1 == "синий" and cvet2 == "желтый") or (cvet1 == "желтый" and cvet2 == "синий"):
        print("зеленый")
    else:
        print("ошибка")
zad3()
