import zipfile  # для работы с файлами zip
import time  # для создания эффекта печатания текста с задержкой
# для работы с файлами rar необходмио установить (pip install unrar)
from unrar import rarfile
# секундомер. Необходимо установить (pip install stopwatch.py)
from stopwatch import Stopwatch
# для созлания разноцветного текста в программе. Необходимо установить (pip install colorama)
from colorama import init, Fore, Back, Style
init()


def console_picture():
    print(Style.BRIGHT + Fore.CYAN)
    print("   ########   ########  ##      ##   #######   ########    ######## ")
    print("   ########   ########  ##      ##   ##    ##  ##          ######## ")
    print("   ##    ##   ##    ##  ##     ###   ########  ########       ##  ")
    print("   ##    ##   ########  ##  ##  ##   ##    ##  ##             ##  ")
    print("   ##    ##   ##        ## #    ##   ########  ########       ##  ")
    print("   ##    ##   ##        ##      ##   #######   ########       ##  ")
    print()
    print()
    print("   ########      ###    ##      ##   ########   ##      ##  ########     @@ ")
    print("   ##           #####   ##      ##   ##    ##   ##      ##  ########     @@ ")
    print("   ######      ##   ##  ##########   ##    ##   ##      ##     ##        @@ ")
    print("   ##    ##   ##     ## ##      ##   ##    ##   ##    ####     ##        @@ ")
    print("   ########   ######### ##      ##   ##    ##   ##  ##  ##     ##        @@ ")
    print("   ######     ##     ## ##      ##  ##########  ## #    ##     ##           ")
    print("                                    ##      ##  ##      ##     ##        @@ ")
    print()
    print()
    print()


console_picture()


wordTitle = '          Программа для взлома запароленных zip и rar архивов '
# создаем эффект печатания текста (текст выводиться с задержкой)
for i in wordTitle:
    print(i.upper(), end="")
    time.sleep(0.03)

stopwatch = Stopwatch(2)  # 2 это десятична точность для секундомера


def crack_password(password_list, file_for_breaking):

    indx = 0
    cnt = len(list(open(password_list, 'rb')))
    # открываем файл (with open() as file: - пишем так, чтобы потом не писать комманду закрытия файла (close()). rb открытие в двоичном режиме )
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                # вычисляем в процентном соотношении количество пребранных паролей
                x = (indx+1)/cnt * 100
                # отсекаем цифры после запятой до 2-х, чтоб не получалось вроде такого: 0.9834539503%
                x = float('{:.2f}'.format(x))
                print(
                    f'Количество перебранных паролей {indx} ----- Процент перебранных паролей {x} ---- Прошло времени {str(stopwatch)}\r', end="")  # подсчитываем количество перебранных паролей. Вывод текста в одну строку с затиранием предыдущего
                try:
                    indx += 1
                    # # pwd: если zip-файл зашифрован, передайте пароль в этом аргументе (по умолчанию: None) .
                    # делаем проверку, имеется ли в имени файла расширения файла zip или rar
                    if (file_for_breaking.filename.endswith('.zip')):
                        file_for_breaking.extractall(pwd=word)
                    elif (file_for_breaking.filename.endswith('.rar')):
                        file_for_breaking.extractall(pwd=word.decode("utf8"))
                    print("\n")
                    print(Style.BRIGHT + Fore.GREEN)
                    print("Пароль найден в строке: ", indx)
                    # Декодирует байтстроку в строку.
                    print("Пароль: ", word.decode())
                    # После нахождения пароля, спрашиваем про желание продолжить взламывать пароли
                    print(Style.BRIGHT + Fore.YELLOW)
                    continue_work = input(
                        "Хотите продолжить? Если да, то нажмите букву 'д'")
                    if (continue_work == 'д'):
                        main_data()
                        # return True
                    else:
                        return True

                except:

                    continue
    return False


def main_data():
    print(Style.BRIGHT + Fore.YELLOW)
    archive_file = input("\nВведите адрес архива ")
    # делаем проверку рассширенния взламываемого файла
    if not archive_file.endswith('.zip') and not archive_file.endswith('.rar'):
        # if not any(map(archive_file.endswith, ('.zip', '.rar'))):
        print(Style.BRIGHT + Fore.RED)
        print(
            "Вы указали неверный файл для взлома. Файл не имеет расширения 'zip' или 'rar' ")
        main_data()

    password_list = input("Введите адресс словаря ")

    # Инициализируем
    if (archive_file.endswith('.zip')):
        file_for_breaking = zipfile.ZipFile(archive_file)
    elif (archive_file.endswith('.rar')):
        file_for_breaking = rarfile.RarFile(archive_file)

    # подсчитываем количесвто слов в словаре
    cnt = len(list(open(password_list, 'rb')))

    print("Количество паролей в данном словаре ", cnt)

    if crack_password(password_list, file_for_breaking) == False:
        print(Style.BRIGHT + Fore.RED)
        print("\nПароль не найден. Попробуйте другой словарь ")
        main_data()


main_data()
