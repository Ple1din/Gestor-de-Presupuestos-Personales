# Función para agregar un ingreso
def agregar_ingreso(transacciones, balance):
    """
    Esta función agrega un ingreso a la lista de transacciones, 
    actualiza el balance y retorna el nuevo balance.
    """
    ingreso = float(input("Ingresa la cantidad de ingreso: "))
    categoria = input("Ingresa la categoría del ingreso: ")
    if ingreso > 0:
        transacciones.append(('Ingreso', ingreso, categoria))
        balance += ingreso
        print(f"Ingreso agregado. Nuevo balance: {balance}")
    else:
        print("El ingreso debe ser positivo.")
    return balance

# Función para agregar un gasto
def agregar_gasto(transacciones, balance):
    """
    Esta función agrega un gasto a la lista de transacciones,
    actualiza el balance y retorna el nuevo balance.
    """
    gasto = float(input("Ingresa la cantidad de gasto: "))
    categoria = input("Ingresa la categoría del gasto: ")
    if gasto > 0 and gasto <= balance:
        transacciones.append(('Gasto', gasto, categoria))
        balance -= gasto
        print(f"Gasto agregado. Nuevo balance: {balance}")
    else:
        print("El gasto no puede exceder el balance disponible o ser negativo.")
    return balance

# Función para ver el balance actual
def ver_balance(transacciones):
    """
    Calcula el balance actual sumando los ingresos y restando los gastos.
    """
    balance = sum(t[1] if t[0] == 'Ingreso' else -t[1] for t in transacciones)
    print(f"El balance actual es: {balance}")
    return balance

# Función para generar un reporte mensual
def generar_reporte(transacciones):
    """
    Clasifica las transacciones por categoría y muestra el total por categoría.
    """
    categorias = {}
    for tipo, monto, categoria in transacciones:
        if categoria not in categorias:
            categorias[categoria] = 0
        categorias[categoria] += monto if tipo == 'Ingreso' else -monto
    for categoria, total en categorias.items():
        print(f"Categoría: {categoria}, Total: {total}")

# Función para ejecutar pruebas de cada función
def pruebas():
    """
    Esta función ejecuta pruebas sobre las funciones clave del programa
    para verificar su correcto funcionamiento.
    """
    print("Ejecutando pruebas...")
    
    # Caso de prueba 1: Agregar ingreso
    transacciones = []
    balance = agregar_ingreso(transacciones, 0)  # Ingresando un valor positivo
    assert balance > 0, "Error en la prueba de ingreso positivo"
    
    # Caso de prueba 2: Agregar gasto válido
    balance = agregar_gasto(transacciones, balance)
    assert balance >= 0, "Error en la prueba de gasto válido"
    
    # Caso de prueba 3: Balance actualizado correctamente
    balance_calculado = ver_balance(transacciones)
    assert balance == balance_calculado, "Error en la prueba de balance"
    
    # Caso de prueba 4: Generar reporte
    generar_reporte(transacciones)  # Se debe mostrar un reporte categorizado
    
    print("Todas las pruebas pasaron correctamente.")

# Función principal que muestra el menú y gestiona el flujo del programa
def main():
    """
    Función principal del programa que despliega un menú con las opciones para 
    agregar ingresos, gastos, ver el balance, generar un reporte y salir.
    """
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

# Ejecutar pruebas
pruebas()

# Ejecutar programa principal
main()
