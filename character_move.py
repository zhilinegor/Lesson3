x_coord = 0 # координата x
y_coord = 0 # координата y
def cls(): # очистка терминала
    print("\n"*100)
def inp_command(): # проверка ввода номера команды

    while True:
        
        number_command = (input("\nВведите номер команды: "))
        number_str = str(number_command) # для проверки что цифра
       
        if (number_str.isdigit() == False): # проверка, что введена цифра
            cls()
            print("\nВы должны ввести валидный номер команды, попробуйте снова: \n1 - шаг вверх\n2 - шаг вниз\n3 - шаг вправо\n4 - шаг влево\n5 - выход из скрипта\n")
            continue
        
        if (0 < int(number_command) < 6): # проверка валидных номеров команд
            return number_command
            break
        
        else:
             cls()
             print("\nВы должны ввести валидный номер команды, попробуйте снова: \n1 - шаг вверх\n2 - шаг вниз\n3 - шаг вправо\n4 - шаг влево\n5 - выход из скрипта\n")

while True:
    cls()
    print ("\nКоманды для движения персонажа по координатам:\n1 - шаг вверх\n2 - шаг вниз\n3 - шаг вправо\n4 - шаг влево\n5 - выход из скрипта\n \nТекущее положение: (",x_coord,",",y_coord,")")
    ch_command = inp_command()
    if ch_command == '1': # движение на шаг вверх
        y_coord += 1
        continue
    elif ch_command == '2': # движение на шаг вниз
        y_coord -= 1
        continue
    elif ch_command == '3': # движение на шаг вправо
        x_coord += 1
        continue
    elif ch_command == '4': # движение на шаг влево
        x_coord -= 1
        continue
    else:
        break
