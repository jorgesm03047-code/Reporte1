class Persona:
    def __init__(self, idPersona, nombre, correo, telefono):
        self.idPersona = idPersona
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

class Usuario(Persona):
    def __init__(self, idPersona, nombre, correo, telefono, puntos):
        super().__init__(idPersona, nombre, correo, telefono)
        self.puntos = puntos
        self.historial_reservas = []

class Empleado(Persona):
    def __init__(self, idPersona, nombre, correo, telefono, idEmpleado, rol, horario):
        super().__init__(idPersona, nombre, correo, telefono)
        self.idEmpleado = idEmpleado
        self.rol = rol
        self.horario = horario
class Espacio:
    def __init__(self, idEspacio, nombre, ubicacion):
        self.idEspacio = idEspacio
        self.nombre = nombre
        self.ubicacion = ubicacion

class Sala(Espacio):
    def __init__(self, idEspacio, nombre, ubicacion, tipo, capacidad_total, es_vip):
        super().__init__(idEspacio, nombre, ubicacion)
        self.tipo = tipo
        self.capacidad_total = capacidad_total
        self.es_vip = es_vip

class ZonaComida(Espacio):
    def __init__(self, idEspacio, nombre, ubicacion, lista_productos, stock_actual):
        super().__init__(idEspacio, nombre, ubicacion)
        self.lista_productos = lista_productos
        self.stock_actual = stock_actual

class Pelicula:
    def __init__(self, idPelicula, titulo, duracion, clasificacion, genero):
        self.idPelicula = idPelicula
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.genero = genero

class Funcion:
    def __init__(self, idFuncion, pelicula, sala, horario_inicio, precio_base):
        self.idFuncion = idFuncion
        self.pelicula = pelicula
        self.sala = sala
        self.horario_inicio = horario_inicio
        self.precio_base = precio_base
        self.asientos_ocupados = []

class Promocion:
    def __init__(self, codigo, descripcion, porcentaje_descuento, fecha_expiracion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.porcentaje_descuento = porcentaje_descuento
        self.fecha_expiracion = fecha_expiracion
    def aplicar_descuento(self, monto):
        return monto - (monto * (self.porcentaje_descuento / 100))

class Reserva:
    def __init__(self, idReserva, usuario, funcion, asientos):
        self.idReserva = idReserva
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.monto_total = len(asientos) * funcion.precio_base
        self.estado = "Pendietne"

    def confirmar_pago(self):
        ocupados = [a for a in self.asientos if a in self.funcion.asientos_ocupados]
        if ocupados:
            return f"El asiento {ocupados[0]} ya está ocupado por otra reservacion."
        
        self.funcion.asientos_ocupados.extend(self.asientos)
        self.estado = "Pagado"
        
        asientos_str = ""
        for i in range(len(self.asientos)):
            asientos_str += self.asientos[i]
            if i < len(self.asientos) - 1:
                asientos_str += ", "
                
        return f" Los asientos {asientos_str} fueron seleccionados con éxito."

    def generar_ticket(self):
        ahorro = (len(self.asientos) * self.funcion.precio_base) - self.monto_total
        
        asientos_str = ""
        for i in range(len(self.asientos)):
            asientos_str += self.asientos[i]
            if i < len(self.asientos) - 1:
                asientos_str += ", "
                
        return (f"Resumen de Reserva #{self.idReserva}:\n"
                f"Usuario: {self.usuario.nombre}\n"
                f"Función: {self.funcion.pelicula.titulo} ({self.funcion.horario_inicio})\n"
                f"Asientos: [{asientos_str}]\n"
                f"Total Final: ${self.monto_total:.2f} (Ahorraste ${ahorro:.2f})\n"
                f"Estado: Pagado. Ticket generado en PDF.")
    def aplicar_promocion(self, promo):
        self.monto_total = promo.aplicar_descuento(self.monto_total)
        return f"Estamos validando tu código... (Descuento del {int(promo.porcentaje_descuento)} % aplicado)."
    

class Producto:
    def __init__(self, id_prod, nombre, precio, categoria):
        self.id_prod = id_prod
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    def mostrar_detalle(self):
        return f"Id: {self.id_prod} {self.nombre} (${self.precio}) - Cat: {self.categoria}"