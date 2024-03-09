class Producto:
    def __init__(self, nombre: str, precio: float, stock: int = 0) -> None:
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def precio(self) -> float:
        return self._precio

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, nuevo_stock: int) -> None:
        self._stock = max(nuevo_stock, 0)

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Precio: ${self.precio} - Stock: {self.stock}"

    def __eq__(self, otro_producto) -> bool:
        return self.nombre == otro_producto.nombre
    
    def to_json(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }
    
'''producto1 = Producto("Leche", 1000, 5)
print(producto1)  # Output: Nombre: Leche - Precio: $1000 - Stock: 5

# Intentemos asignar stock negativo
producto1.stock = -3
print(producto1.stock)  # Output: 0 (El setter se encarga de prevenir esto)
'''