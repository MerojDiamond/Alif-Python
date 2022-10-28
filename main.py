from List import *
while True:
    file=input("Путь к файлу:")
    action=input("Действие:")
    content = List(file)
    if action=='Добавить в список' or action=='Изменить запись в списке':
        content.add_update()
    elif action=='Удалить из списка':
        content.delete()
    elif action=='Вывести общую сумму':
        content.summ()
        print(content.get_summ())
    else:
        print("Нет такой дейтсвии")