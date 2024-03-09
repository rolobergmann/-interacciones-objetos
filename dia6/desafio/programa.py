import json
from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

def main():
    # Crear una tienda
    tipo_tienda = input("Ingrese el tipo de tienda (Restaurante, Supermercado, Farmacia): ").lower()
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))

    if tipo_tienda == "restaurante":
        tienda = Restaurante(nombre_tienda, costo_delivery)
    elif tipo_tienda == "supermercado":
        tienda = Supermercado(nombre_tienda, costo_delivery)
    elif tipo_tienda == "farmacia":
        tienda = Farmacia(nombre_tienda, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return

    # Ingresar productos
    continuar_agregando = True
    while continuar_agregando:
        nombre_producto = input("Ingrese el nombre del producto (o ingrese 'salir' para finalizar): ")
        if nombre_producto.lower() == "salir":
            break
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        producto = Producto(nombre_producto, precio, stock)
        tienda.agregar_producto(producto)

    # Mostrar opciones al usuario
    while True:
        print("\n**Opciones:**")
        print("1. Listar productos")
        print("2. Realizar venta")
        print("3. Salir del programa")

        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 1:
            print(tienda.listar_productos())
        elif opcion == 2:
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            tienda.realizar_venta(nombre_producto, cantidad)
        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
