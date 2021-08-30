
def main():
    a = int(input("Da el valor de A: "))
    b = int(input("Da el valor de B: "))
    c = int(input("Da el valor de C: "))

    if a == 0 and b == 0:
        print("No tiene solución")
        
    elif a == 0 and b != 0:
        y = -c / b
        print(y)
        
    elif a != 0 and b != 0:
        c = b * b - 4 * a * c
        
        if c < 0:
            print("Raíces complejas")

        elif c > 0:
            x1 = (-b + c ** (1 / 2) ) / ( 2 * a )
            x2 = (-b - c ** (1 / 2) ) / ( 2 * a )
            print(x1)
            print(x2)

        else:
            x= -b / (2 * a)
            print(x)
main()

