# Gestor de Presupuestos Personales 

Contexto del Proyecto: Gestor de Presupuestos Personales
Contexto:
La gestión eficaz de las finanzas personales es una habilidad esencial en la actualidad. Un gestor de presupuesto te proporciona las herramientas necesarias para organizar tus ingresos y gastos, analizar tus hábitos de consumo y, en última instancia, mejorar tu bienestar financiero. En un mundo donde las transacciones son muy frecuentes, mantener un control sobre los gastos es un desafío. Un gestor de presupuesto personal es una solución práctica que ayuda a organizar las finanzas, clasificando los ingresos y gastos para que se puedan tomar decisiones informadas y alcanzar metas financieras.

Justificación del Proyecto:
La gestión de las finanzas personales puede ser abrumadora. El gestor de presupuestos simplifica este proceso al proporcionar una visión clara de los ingresos y gastos. Al automatizar tareas repetitivas, con el proposito de ayudar a tomar decisiones financieras más inteligentes.

Solución propuesta:
1. Estructura de Archivos
Vamos a agregar la funcionalidad para almacenar y recuperar transacciones desde un archivo, lo que permitirá mantener un registro persistente. Utilizaremos archivos de texto para almacenar ingresos y gastos en un formato estructurado.

2. Uso de Listas o Matrices
La lista de transacciones será restaurada al inicio del programa desde el archivo y actualizada cada vez que se agregue una nueva transacción. Esto nos permite mantener un historial de las transacciones sin perder la información entre sesiones.

Algoritmo del Proyecto:
Inicio

Verificar si existe un archivo de transacciones previas.
Si existe, cargar el archivo y restaurar las transacciones.
Si no, inicializar una lista vacía de transacciones.
Menú Principal

Mostrar las opciones:
Agregar ingreso.
Agregar gasto.
Ver balance.
Generar reporte mensual.
Guardar y salir.
Agregar Ingreso

Solicitar la cantidad del ingreso y la categoría.
Agregar el ingreso a la lista de transacciones.
Actualizar el balance sumando el ingreso.
Guardar la transacción en el archivo.
Agregar Gasto

Solicitar la cantidad del gasto y la categoría.
Agregar el gasto a la lista de transacciones.
Actualizar el balance restando el gasto.
Guardar la transacción en el archivo.
Ver Balance

Calcular el balance total sumando todos los ingresos y restando todos los gastos de la lista de transacciones.
Mostrar el balance actual al usuario.
Generar Reporte Mensual

Iterar a través de la lista de transacciones y clasificar las transacciones por categorías.
Calcular el total de ingresos y gastos por categoría.
Mostrar el reporte categorizado al usuario.
Guardar y Salir

Guardar todas las transacciones en el archivo.
Finalizar el programa.
Fin
