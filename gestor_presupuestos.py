def agregar_ingreso(transacciones, balance):
    ingreso = float(input("Ingresa la cantidad de ingreso: "))
    categoria = input("Ingresa la categoría del ingreso: ")
    if ingreso > 0:
        transacciones.append(('Ingreso', ingreso, categoria))
        balance += ingreso
        print(f"Ingreso agregado. Nuevo balance: {balance}")
    else:
        print("El ingreso debe ser positivo.")
    return balance

def agregar_gasto(transacciones, balance):
    gasto = float(input("Ingresa la cantidad de gasto: "))
    categoria = input("Ingresa la categoría del gasto: ")
    if gasto > 0 and gasto <= balance:
        transacciones.append(('Gasto', gasto, categoria))
        balance -= gasto
        print(f"Gasto agregado. Nuevo balance: {balance}")
    else:
        print("El gasto no puede exceder el balance disponible o ser negativo.")
    return balance

def ver_balance(transacciones):
    balance = sum(t[1] if t[0] == 'Ingreso' else -t[1] for t in transacciones)
    print(f"El balance actual es: {balance}")
    return balance

def generar_reporte(transacciones):
    categorias = {}
    for tipo, monto, categoria in transacciones:
        if categoria not in categorias:
            categorias[categoria] = 0
        categorias[categoria] += monto if tipo == 'Ingreso' else -monto
    for categoria, total in categorias.items():
        print(f"Categoría: {categoria}, Total: {total}")

def pruebas():
    # Pruebas para cada función
    print("Ejecutando pruebas...")
    transacciones = []
    balance = agregar_ingreso(transacciones, 0)
    balance = agregar_gasto(transacciones, balance)
    ver_balance(transacciones)
    generar_reporte(transacciones)

def main():
    transacciones = []
    balance = 0
    while True:
        print("\nMenú Principal:")
        print("1. Agregar Ingreso")
        print("2. Agregar Gasto")
        print("3. Ver Balance")
        print("4. Generar Reporte Mensual")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            balance = agregar_ingreso(transacciones, balance)
        elif opcion == '2':
            balance = agregar_gasto(transacciones, balance)
        elif opcion == '3':
            ver_balance(transacciones)
        elif opcion == '4':
            generar_reporte(transacciones)
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")