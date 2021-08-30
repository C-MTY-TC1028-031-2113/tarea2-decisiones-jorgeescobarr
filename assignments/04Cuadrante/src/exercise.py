def main():
    gr= int(input("Introduce los grados: "))

    if gr < 0 or gr > 360:
        print("excede")

    elif gr == 0 or gr == 90 or gr == 180 or gr == 270 or gr == 360:
        print("eje")
    elif gr > 0 and gr < 90:
        print("cuadrante 1")
    elif gr > 90 and gr < 180:
        print("cuadrante 2")
    elif gr > 180 and gr < 270:
        print("cuadrante 3")
    elif gr > 270 and gr < 360:
        print("cuadrante 4")
main()
