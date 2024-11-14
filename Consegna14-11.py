print("quadrato")
print("cerchio")
print("rettangolo")
scelta = input("scegli la figura e calcoliamo: ")

if scelta == "quadrato":
    lato = float(input("Lunghezza del lato del quadrato: "))
    print("Perimetro del quadrato:", lato * 4)

elif scelta == "cerchio":
    raggio = float(input("Raggio del cerchio: "))
    print("Circonferenza del cerchio:", 2 * 3.14 * raggio)

elif scelta == "rettangolo":
    base = float(input("Lunghezza della base del rettangolo: "))
    altezza = float(input("Lunghezza dell'altezza del rettangolo: "))
    print("Perimetro del rettangolo:", 2 * (base + altezza))

else:
    print("Scelta non valida.")
