
"""
Módulo de Gestión de Préstamos
Persistencia en JSON usando modulos.persistencia
"""
from datetime import date
from utilidades import limpiar_pantalla, pausar
from modulos.persistencia import leer, escribir, generar_id


def mostrar_menu_prestamos():
    limpiar_pantalla()
    print("--- GESTIÓN DE PRÉSTAMOS ---")
    print("1) Registrar préstamo")
    print("2) Listar préstamos")
    print("3) Volver")


def realizar_prestamo():
    limpiar_pantalla()
    print("--- REGISTRAR PRÉSTAMO ---")
    try:
        usuario_dni = input("DNI del usuario: ").strip()
        libro_id = input("ID del libro (p.ej. LIB001): ").strip().upper()
    except KeyboardInterrupt:
        print("\nOperación cancelada.")
        pausar()
        return

    usuarios = leer("usuarios")
    libros = leer("libros")

    if not any(u.get("dni") == usuario_dni for u in usuarios):
        print("\nNo existe un usuario con ese DNI.")
        pausar()
        return

    if not any(l.get("id") == libro_id for l in libros):
        print("\nNo existe un libro con ese ID.")
        pausar()
        return

    prestamos = leer("prestamos")
    nuevo_id = generar_id("PREST", prestamos, "id", ancho=3)
    hoy = date.today().isoformat()
    prestamos.append({
        "id": nuevo_id,
        "usuario_dni": usuario_dni,
        "libro_id": libro_id,
        "fecha": hoy
    })
    escribir("prestamos", prestamos)
    print(f"\nPréstamo registrado con ID {nuevo_id} ({hoy}).")
    pausar()


def listar_prestamos():
    limpiar_pantalla()
    print("--- LISTA DE PRÉSTAMOS ---")
    prestamos = leer("prestamos")
    libros = {l.get("id"): l for l in leer("libros")}
    usuarios = {u.get("dni"): u for u in leer("usuarios")}

    if not prestamos:
        print("No hay préstamos registrados.")
    else:
        for p in prestamos:
            user = usuarios.get(p.get("usuario_dni"), {})
            libro = libros.get(p.get("libro_id"), {})
            print(f"ID: {p.get('id','')} - Fecha: {p.get('fecha','')} - Usuario: {user.get('nombre','?')} (DNI {p.get('usuario_dni','')}) - Libro: {libro.get('titulo','?')} [{p.get('libro_id','')}]")
    pausar()


def menu_prestamos():
    while True:
        try:
            mostrar_menu_prestamos()
            opcion = input("Seleccione una opción [1-3]: ").strip()
            if opcion == "1":
                realizar_prestamo()
            elif opcion == "2":
                listar_prestamos()
            elif opcion == "3":
                return
            else:
                print("Opción inválida")
                pausar()
        except KeyboardInterrupt:
            print("\nVolviendo al menú principal...")
            pausar()
            return
