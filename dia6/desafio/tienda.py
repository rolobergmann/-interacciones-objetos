from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    def __init__(self, nombre: str, costo_delivery: float) -> None:
        self._nombre = nombre
        self._costo_delivery = costo_delivery
        self._productos = []

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def costo_delivery(self) -> float:
        return self._costo_delivery

    def agregar_producto(self, producto: Producto) -> None:
        producto_existente = self.buscar_producto(producto.nombre)
        if producto_existente:
            producto_existente.stock += producto.stock
        else:
            self._productos.append(producto)

    def buscar_producto(self, nombre_producto: str) -> Producto:
        for producto in self._productos:
            if producto.nombre == nombre_producto:
                return producto
        return None 

    def listar_productos(self) -> str:
        resultado = f"**Productos de {self.nombre}**\n"
        for producto in self._productos:
            if isinstance(self, Restaurante):
                resultado += f"- {producto.nombre}\n"
            elif isinstance(self, Farmacia) and producto.precio > 15000:
                resultado += f"- {producto.nombre} - Precio: ${producto.precio} - Envío gratis\n"
            elif isinstance(self, Supermercado) and producto.stock < 10:
                resultado += f"- {producto.nombre} - Precio: ${producto.precio} - Pocos productos disponibles ({producto.stock})\n"
            else:
                resultado += f"- {producto.nombre} - Precio: ${producto.precio}\n"
        return resultado
    def calcular_total(self, nombre_producto: str, cantidad: int) -> float:
        producto = self.buscar_producto(nombre_producto)
        if producto:
            # Realizar el calculo de total_producto (precio de producto por cantidad)
            total_producto = producto.precio * cantidad

            # Verificar si hay costo de delivery y de ser asi, sumarlo
            if self.costo_delivery > 0:
                total_producto += self.costo_delivery
            # Verificar si aplica free deliver, si es asi restarlo
            if Farmacia and producto.precio > 15000:
                total_producto -= self.costo_delivery

            return total_producto
        else:
            raise ValueError(f"Producto '{nombre_producto}' no encontrado")
    
"""     def to_json(self):
        return {
            "nombre": self.nombre,
            "costo_delivery": self.costo_delivery,
            "productos": [producto.to_json() for producto in self._productos]
        } """

@abstractmethod
def realizar_venta(self, nombre_producto: str, cantidad: int) -> None:
    pass

class Restaurante(Tienda):
    def __init__(self, nombre: str, costo_delivery: float) -> None:
        super().__init__(nombre, costo_delivery)

    def realizar_venta(self, nombre_producto: str, cantidad: int) -> None:
        producto = self.buscar_producto(nombre_producto)
        if producto:
            print(f"\n**Venta realizada en {self.nombre}**")
            print(f"Producto: {nombre_producto}")
            print(f"Cantidad: {cantidad}")
            print(f"Total: ${self.calcular_total(nombre_producto, cantidad)}")
        else:
            print(f"El producto {nombre_producto} no existe.")


class Supermercado(Tienda):
    def __init__(self, nombre: str, costo_delivery: float) -> None:
        super().__init__(nombre, costo_delivery)
        
    def realizar_venta(self, nombre_producto: str, cantidad: int) -> None:
        producto = self.buscar_producto(nombre_producto)
        if producto:
            print(f"\n**Venta realizada en {self.nombre}**")
            print(f"Producto: {nombre_producto}")
            print(f"Cantidad: {cantidad}")
            print(f"Total: ${self.calcular_total(nombre_producto, cantidad)}")
        else:
            print(f"El producto {nombre_producto} no existe.")


class Farmacia(Tienda):
    def __init__(self, nombre: str, costo_delivery: float) -> None:
        super().__init__(nombre, costo_delivery)

    def realizar_venta(self, nombre_producto: str, cantidad: int) -> None:
        producto = self.buscar_producto(nombre_producto)
        if producto and producto.stock >= cantidad and cantidad <= 3:
            producto.stock -= cantidad
            delivery = int(self.costo_delivery)
            print(f"\n**Venta realizada en {self.nombre}**")
            print(f"Producto: {nombre_producto}")
            print(f"Cantidad: {cantidad}")
            print(f"Total: $ {self.calcular_total(nombre_producto, cantidad)}" )
                
        elif not producto:
            print(f"El producto {nombre_producto} no existe.")
        elif cantidad > 3:
            print(f"No se puede vender más de 3 unidades del producto {nombre_producto} por compra.")
        else:
            print(f"No hay stock suficiente del producto {nombre_producto}.")

    def buscar_producto(self, nombre_producto: str) -> Producto:
        for producto in self._productos:
            if producto.nombre == nombre_producto:
                return producto
        return None

