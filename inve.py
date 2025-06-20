# ------------------------------
# Gestión de Inventario para una Pequeña Tienda Local
# Primera versión con persistencia en JSON
# ------------------------------
import json
import os

# Clase Producto (simulada con diccionario)
def crear_producto(codigo, nombre, precio, stock):
    return {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

# ------------------------------
# Funciones principales
# ------------------------------
def agregar_producto(inventario):
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    try:
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock inicial: "))
        inventario.append(crear_producto(codigo, nombre, precio, stock))
        print("\n✅ Producto agregado con éxito!\n")
    except ValueError:
        print("❌ Precio o stock inválido.\n")

def listar_productos(inventario):
    if not inventario:
        print("\n📦 Inventario vacío.\n")
        return
    print("\n📋 Listado de productos:")
    print("Código\tNombre\t\tPrecio\tStock")
    print("-"*40)
    for p in inventario:
        print(f"{p['codigo']}\t{p['nombre']:<10}\t{p['precio']}\t{p['stock']}")
    print()

def buscar_producto(inventario):
    criterio = input("Ingrese el código o nombre del producto a buscar: ").lower()
    encontrados = [p for p in inventario if criterio in p['codigo'].lower() or criterio in p['nombre'].lower()]
    if encontrados:
        print("\n🔎 Productos encontrados:")
        for p in encontrados:
            print(p)
    else:
        print("\n❌ No se encontró el producto.\n")

def actualizar_stock(inventario):
    codigo = input("Ingrese el código del producto a actualizar: ")
    for p in inventario:
        if p['codigo'] == codigo:
            try:
                nuevo_stock = int(input(f"Stock actual: {p['stock']}. Ingrese el nuevo stock: "))
                p['stock'] = nuevo_stock
                print("\n✅ Stock actualizado exitosamente.\n")
            except ValueError:
                print("❌ Stock inválido.")
            return
    print("\n❌ Producto no encontrado.\n")

# ------------------------------
# Persistencia de datos
# ------------------------------
def cargar_inventario(nombre_archivo="inventario.json"):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)
    return []

def guardar_inventario(inventario, nombre_archivo="inventario.json"):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(inventario, archivo, indent=4)

# ------------------------------
# Menú interactivo
# ------------------------------
def menu():
    inventario = cargar_inventario()
    while True:
        print("""
        ==============================
        📦 GESTIÓN DE INVENTARIO
        ------------------------------
        1. Agregar producto
        2. Listar productos
        3. Buscar producto
        4. Actualizar stock
        5. Guardar y Salir
        ==============================
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            listar_productos(inventario)
        elif opcion == '3':
            buscar_producto(inventario)
        elif opcion == '4':
            actualizar_stock(inventario)
        elif opcion == '5':
            guardar_inventario(inventario)
            print("\n✅ Inventario guardado. ¡Hasta luego!\n")
            break
        else:
            print("\n❌ Opción no válida. Intente de nuevo.\n")

# ------------------------------
# Ejecutar programa
# ------------------------------
if __name__ == "__main__":
    menu()
