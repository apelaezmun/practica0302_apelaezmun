'''
Añadir una clase Pedido que tiene como atributos:
    - lista de productos
    - lista de cantidades
Añade las siguiente funcionalidad:
    - total_pedido: muestra el precio final del pedido
    - mostrar_productos: muestra los productos del pedido
'''
class Producto:

    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, valor):
        self.__precio = valor

    def calcular_total(self, unidades):
        return self.__precio * unidades

    def __str__(self):
        return 'codigo: ' + str(self.__codigo) + ', nombre: ' + self.__nombre + ' precio: ' + str(self.__precio)
    
class Pedido:

    def __init__(self, productos, cantidades):
        self.__productos = productos
        self.__cantidades = cantidades

    def total_pedido(self):
        total = 0

        for (p, c) in zip(self.__productos, self.__cantidades):
            total = total + p.calcular_total(c)
            return total

    def mostrar_pedido(self):
        for (p, c) in zip(self.__productos, self.__cantidades):
            print('Producro ->', p.nombre, 'cantidad: ' + str(c))

p1 = Producto(1, 'producto 1', 5)
p2 = Producto(2, 'producto 2', 10)
p3 = Producto(3, 'producto 3', 15)

productos = [p1, p2, p3]
cantidades = [5, 10, 15]
pedido = Pedido(productos, cantidades)
print('Total pedido: ' + str(pedido.total_pedido()))

pedido.mostrar_pedido()