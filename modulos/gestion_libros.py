
"""
Módulo de Gestión de Libros
Desarrollado por: Equipo

Persistencia en JSON usando modulos.persistencia
"""
from utilidades import limpiar_pantalla, pausar
from modulos.persistencia import leer, escribir, generar_id


def mostrar_menu_libros():
    """Muestra el menú de gestión de libros"""
    limpiar_pantalla()
    print("--- GESTIÓN DE LIBROS ---")
    print("1) Agregar libro")
    print("2) Listar libros")
    print("3) Volver")

def agregar_libro():
    """Agrega un libro y lo persiste en datos/libros.json"""
    limpiar_pantalla()
    print("--- AGREGAR LIBRO ---")
    try:
        titulo = input("Título: ").strip()
        autor  = input("Autor: ").strip()
    except KeyboardInterrupt:
        print("\nOperación cancelada.")
        pausar()
        return

    if not titulo or not autor:
        print("\nTítulo y Autor son obligatorios.")
        pausar()
        return

    libros = leer("libros")
    nuevo_id = generar_id("LIB", libros, "id")
    libros.append({"id": nuevo_id, "titulo": titulo, "autor": autor})
    escribir("libros", libros)

    print(f"\nLibro '{titulo}' agregado exitosamente (ID {nuevo_id}).")
    pausar()

def listar_libros():
    """Lista siempre lo que está guardado en el JSON"""
    limpiar_pantalla()
    print("--- LISTA DE LIBROS ---")

    libros = leer("libros")
    if not libros:
        print("No hay libros registrados.")
    else:
        for libro in libros:
            print(f"ID: {libro.get('id','')} - {libro.get('titulo','')} - {libro.get('autor','')}")
    pausar()


def menu_libros():
    """Menú principal de gestión de libros"""
    while True:
        try:
            mostrar_menu_libros()
            opcion = input("Seleccione una opción [1-3]: ").strip()
            if opcion == "1":
                agregar_libro()
            elif opcion == "2":
                listar_libros()
            elif opcion == "3":
                return
            else:
                print("Opción inválida")
                pausar()
        except KeyboardInterrupt:
            # Volver al menú principal ante Ctrl+C en este submenú
            print("\nVolviendo al menú principal...")
            pausar()
            return
