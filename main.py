class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores:
            self.color = color

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        c = 0
        for e in self.asientos:
            if type(e) == Asiento:
                c += 1
        return c

    def verificarIntegridad(self):
        if self.motor.registro != self.registro:
            return "Las piezas no son originales"
        for e in self.asientos:
            if type(e) == Asiento:
                if e.registro != self.registro:
                    return "Las piezas no son originales"
        return "Auto original"
    
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        tipos = ["electrico", "gasolina"]
        if tipo in tipos:
            self.tipo = tipo