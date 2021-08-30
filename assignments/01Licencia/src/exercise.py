def main():
    age = int(input("Ingresa tu edad: "))
    if age < 18 and age > 0:
        print("No cumples requisitos")
    elif age <= 10:
        print("Respuesta incorrecta")
    elif age >= 18:
        id = input("¿Tienes identificación oficial? (s/n): ")
        if id == ("s"):
            print("Trámite de licencia concedido")
        elif id == ("n"):
            print("No cumples con los requisitos")
        elif id != "n" or "s":
            print("Respuesta incorrecta")
main()
