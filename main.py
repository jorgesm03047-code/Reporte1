from models import *

print("Inventario de prodcutos")

p1 = Producto(1, "Crepa Dulce", 65.0, "Postres")
p2 = Producto(2, "Icee de Cereza", 55.0, "Bebidas")
p3 = Producto(3, "Pizza Individual", 90.0, "Comida")
p4 = Producto(4, "Nachos", 85.0, "Snacks")
p5 = Producto(5, "Gomitas de Gusano", 40.0, "Dulces")
p6 = Producto(6, "Agua Mineral 600ml", 35.0, "Bebidas")
p7 = Producto(7, "Combo Amigos", 250.0, "Combos")
p8 = Producto(8, "Boleto VIP Adulto", 120.0, "Boletos")
p9 = Producto(9, "Boleto 3D Niño", 75.0, "Boletos")
p10 = Producto(10, "Vaso Coleccionable", 180.0, "Promos")

print(p1.mostrar_detalle())
print(p2.mostrar_detalle())
print(p3.mostrar_detalle())
print(p4.mostrar_detalle())
print(p5.mostrar_detalle())
print(p6.mostrar_detalle())
print(p7.mostrar_detalle())
print(p8.mostrar_detalle())
print(p9.mostrar_detalle())
print(p10.mostrar_detalle())


print("\nInventario de Películas")
pel1 = Pelicula("pel1", "Cars", 100, "A", "Animación")
pel2 = Pelicula("pel2", "Rush", 150, "B15", "Acción")
pel3 = Pelicula("pel3", "Senna", 100, "A", "Documental")
pel4 = Pelicula("pel4", "Ford v Ferrari", 150, "B", "Drama")
pel5 = Pelicula("pel5", "Grand Prix", 150, "A", "Deportes")
pel6 = Pelicula("pel6", "Days of Thunder", 100, "B", "Acción")
pel7 = Pelicula("pel7", "Shrek", 100, "A", "Animación")
pel8 = Pelicula("pel8", "Toy Story", 100, "A", "Animación")
pel9 = Pelicula("pel9", "Interstellar", 150, "B", "Ciencia Ficción")
pel10 = Pelicula("pel10", "The Batman", 150, "B15", "Acción")

for pelicula in [pel1, pel2, pel3, pel4, pel5, pel6, pel7, pel8, pel9, pel10]:
    print(f"Película: {pelicula.titulo} - Género: {pelicula.genero} ({pelicula.duracion} min)")

print("\nRegistro de Usuarios")
u1 = Usuario("u1", "Lalolopes21", "lalolopes21@gmail.com", "74795537", 200)
u2 = Usuario("u2", "Checo11", "checo@gmail.com", "5551234", 150)
u3 = Usuario("u3", "Kurt94", "kurt@gmail.com", "5559876", 300)
u4 = Usuario("u4", "SaulH", "saul@gmail.com", "5551111", 50)
u5 = Usuario("u5", "AikoG", "aiko@gmail.com", "5552222", 10)
u6 = Usuario("u6", "ReneXico", "rene@gmail.com", "5553333", 80)
u7 = Usuario("u7", "DiploCafe", "diplo@gmail.com", "5554444", 120)
u8 = Usuario("u8", "MaxV", "max@gmail.com", "5555555", 400)
u9 = Usuario("u9", "LewisH", "lewis@gmail.com", "5556666", 250)
u10 = Usuario("u10", "KirbyFan", "kirby@gmail.com", "5557777", 90)

for usr in [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10]:
    print(f"Usuario: {usr.nombre} - Correo: {usr.correo} - Puntos: {usr.puntos}")


sala_5 = Sala("s2", "05", "Planta Alta", "3D", 80, False)

funcion_cars = Funcion("f102", pel1, sala_5, "19:06 hrs", 90.0)

funcion_cars.asientos_ocupados.append("A2")

print("\nComenzando venta")
print(f"Usuario: {u1.nombre} (Puntos: {u1.puntos})")
print(f"Película: '{funcion_cars.pelicula.titulo}' Sala: {funcion_cars.sala.nombre} ({funcion_cars.sala.tipo})")

asientos_intento_1 = ["A1", "A2", "B9"]
print(f"Seleccione sus asientos (separados por coma): {asientos_intento_1[0]}, {asientos_intento_1[1]}, {asientos_intento_1[2]}")
print("Verificando la disponibilidad...")

reserva_1 = Reserva("843", u1, funcion_cars, asientos_intento_1)
resultado_1 = reserva_1.confirmar_pago()
print(resultado_1)

if "ocupado" in resultado_1:
    print("Por favor, seleccione asientos si disponibles.")
    
    asientos_intento_2 = ["A7", " M7", "B5"]
    print(f"Seleccione sus asientos: {asientos_intento_2[0]}, {asientos_intento_2[1]}, {asientos_intento_2[2]}")
    

    reserva_final = Reserva("843", u1, funcion_cars, asientos_intento_2)
    print(reserva_final.confirmar_pago())
    print(f"Monto base: ${reserva_final.monto_total:.2f}")
    
    promo = Promocion("PROMO_MARTES", "Descuento", 15.0, "Martes solo")
    
    print("¿Cuenta con código de descuento?: SI")
    print(reserva_final.aplicar_promocion(promo))
    print("\n" + reserva_final.generar_ticket())