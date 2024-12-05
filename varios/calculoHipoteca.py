def calcular_cuota_mensual(prestamo, tasa_interes_anual, anos):
    tasa_interes_mensual = tasa_interes_anual / 12 / 100
    numero_pagos = anos * 12
    cuota_mensual = (prestamo * tasa_interes_mensual) / (1 - (1 + tasa_interes_mensual) ** -numero_pagos)
    return cuota_mensual

def main():
    prestamo = float(input("Introduce el monto del préstamo: "))
    euribor = float(input("Introduce el valor del Euribor (%): "))
    incremento = float(input("Introduce el incremento (%): "))
    anos = int(input("Introduce el número de años: "))

    tasa_interes_anual = euribor + incremento
    cuota_mensual = calcular_cuota_mensual(prestamo, tasa_interes_anual, anos)

    print(f"La cuota mensual es: {cuota_mensual:.2f} euros")

if __name__ == "__main__":
    main()