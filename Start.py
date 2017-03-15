import os
import psutil
import sys
import russian_rullet

print("Привет программист")
name=input("Введите имя: ")

print(name,", добро пожаловать в Питон!")
answer = ''

while answer != 'q':
    answer = input("будем работать?(y/n/q): ")
    if answer=='y':
        print("Я могу выболнить следующие задачи!")
        print("[1] проказать директорию нахождения программы")
        print("[2] Информацию о компе")
        print("[3] рабочие процесы")
        print("[4] Могу удалить ненужные файлы в папке")
        print("[5] СЫГРАТЬ В ИГРУ!!!")
        do = int(input("Введите действие: "))
        if do == 1:
            print("текущая директория: ", os.getcwd())
        elif do == 2:
            print("Система: ", sys.platform)
            print("Кодировка системы: ", sys.getfilesystemencoding())
            print("Имя пользователя: ", os.getlogin())
            print("Кол-во ядер: ", os.cpu_count())
        elif do == 3:
            print("Рабочие процессы: ", psutil.pids())
        elif do == 4:
            i = 0
            dir = input("Введите директорию для удаления файлов: ")
            mylist = os.listdir(dir)
            while i < len(mylist):
                print(i, ")", mylist[i])
                i += 1
            number = int(input("Какой фаил удалить?"))
            os.remove(os.path.join(dir, mylist[number]))
        elif do == 5:
            russian_rullet.main()
        else:	
            pass
    elif answer == 'n':
        print("Лентяй!")
    else:
        print("Попробуй снова")
