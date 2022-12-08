import math
import cmath

def a_complex_input(): # проверка ввода

    while True:
        
        try:
            numA = complex(input("\na: "))
            return numA
            break
            
        except ValueError:
            print("\nВы должны ввести комплексное число, попробуйте снова.")
def b_complex_input(): # проверка ввода

    while True:
        
        try:
            numB = complex(input("\nb: "))
            return numB
            break
            
        except ValueError:
            print("\nВы должны ввести комплексное число, попробуйте снова.")
def c_complex_input(): # проверка ввода

    while True:
        
        try:
            numC = complex(input("\nc: "))
            return numC
            break
            
        except ValueError:
            print("\nВы должны ввести комплексное число, попробуйте снова.")
def a_digit_input(): # проверка ввода

    while True:
        
        try:
            num_dig_a = float(input("\na: "))
            return num_dig_a
            break
            
        except ValueError:
            print("\nВы должны ввести простое или вещественное число, попробуйте снова.")
def b_digit_input(): # проверка ввода

    while True:
        
        try:
            num_dig_b = float(input("\nb: "))
            return num_dig_b
            break
            
        except ValueError:
            print("\nВы должны ввести простое или вещественное число, попробуйте снова.")
def c_digit_input(): # проверка ввода

    while True:
        
        try:
            num_dig_c = float(input("\nc: "))
            return num_dig_c
            break
            
        except ValueError:
            print("\nВы должны ввести простое или вещественное число, попробуйте снова.")

def q_equ(a, b, c):
    if a == 0 and b == 0 and c == 0:
        print("\nx - принимает любое число")
    else:
        if a == 0 and b == 0:
            print("\nРешений нет")
        else:
            if a == 0 and c == 0:
                print("\nКорни:")
                print("\nx =", 0)
            else:
                if a == 0:
                    x = (-c / b)
                    print("\nКорни:")
                    print("\nx =", x)
                else:
                    d = b * b - 4 * a * c
                    if d > 0:
                        x1 = (-b + math.sqrt(d)) / (2 * a)
                        x2 = (-b - math.sqrt(d)) / (2 * a)
                        if x1 == x2:
                            print("\nКорни:")
                            print("\nx1 =", x1)
                        else:
                            print("\nКорни:")
                            print("x1 =", x1)
                            print("x2 =", x2)
                    else:
                        x1 = (-b + cmath.sqrt(d)) / (2 * a)
                        x2 = (-b - cmath.sqrt(d)) / (2 * a)
                        print("\nКорни:")
                        print("x1 =", x1)
                        print("x2 =", x2)
 
def q_equ_complex(a,b,c):
    if a == 0 and b == 0 and c == 0:
        print("\nx - принимает любое число")
    else:
        if a == 0 and b == 0:
            print("\nРешений нет")
        else:
            if a == 0 and c == 0:
                print("\nКорни:")
                print("\nx =", 0)
            else:
                if a == 0:
                    x = (-c / b)
                    print("\nКорни:")
                    print("\nx =", x)
                else:
                    if b == 0:
                        print("\nКорни:")
                        print("\nx =", math.sqrt(-c / a))
                    else:
                        d = b * b - 4 * a * c
                        x1 = (-b + cmath.sqrt(d)) / (2 * a)
                        x2 = (-b - cmath.sqrt(d)) / (2 * a)
                        print("\nКорни:")
                        print("x1 =", x1)
                        print("x2 =", x2)
 

print("\nБудут ли коэффициенты комплексные?")
answer= input("\nВведите +, если 'да' и -, если 'нет'(+/-): ")
if answer == '+':
        print("\nВведите комплексные коэффициенты квадратного уравнения (вида j, 1+j и т.д.)")
        a = a_complex_input()
        b = b_complex_input()
        c = c_complex_input()
        print("\nУравнение:\n")
        print(a,"* x^2 +",b,"* x +",c,"\n")
        q_equ_complex(a, b, c)
else:
        print("\nВведите коэффициенты квадратного уравнения")
        a = a_digit_input()
        b = b_digit_input()
        c = c_digit_input()
        print("\nУравнение:\n")
        print(a,"* x^2 +",b,"* x +",c,"\n")
        q_equ(a, b, c)
    