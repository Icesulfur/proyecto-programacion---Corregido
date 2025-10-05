"""
Módulo de Gestión de Usuarios
Desarrollado por: MILITELLO, LUCA SANTINO

Usa listas para almacenar información de usuarios
"""

from utilidades import limpiar_pantalla, pausar
from modulos.persistencia import leer, escribir


def mostrar_menu_usuarios():
    limpiar_pantalla()
    print("--- GESTIÓN DE USUARIOS ---")
    print("1) Registrar usuario")
    print("2) Listar usuarios")
    print("3) Volver")


def registrar_usuario():
    limpiar_pantalla()
    print("--- REGISTRAR USUARIO ---")
    try:
        dni = input("DNI: ").strip()
        nombre = input("Nombre completo: ").strip()
    except KeyboardInterrupt:
        print("\nOperación cancelada.")
        pausar()
        return

    if not dni or not nombre:
        print("\nDNI y Nombre son obligatorios.")
        pausar()
        return

    usuarios = leer("usuarios")
    if any(u.get("dni") == dni for u in usuarios):
        print("\nYa existe un usuario con ese DNI.")
        pausar()
        return

    usuarios.append({"dni": dni, "nombre": nombre})
    escribir("usuarios", usuarios)
    print(f"\nUsuario {nombre} (DNI {dni}) registrado.")
    pausar()


def listar_usuarios():
    limpiar_pantalla()
    print("--- LISTA DE USUARIOS ---")
    usuarios = leer("usuarios")
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for u in usuarios:
            print(f"DNI: {u.get('dni','')} - {u.get('nombre','')}")
    pausar()


def menu_usuarios():
    while True:
        try:
            mostrar_menu_usuarios()
            opcion = input("Seleccione una opción [1-3]: ").strip()
            if opcion == "1":
                registrar_usuario()
            elif opcion == "2":
                listar_usuarios()
            elif opcion == "3":
                return
            else:
                print("Opción inválida")
                pausar()
        except KeyboardInterrupt:
            print("\nVolviendo al menú principal...")
            pausar()
            return
