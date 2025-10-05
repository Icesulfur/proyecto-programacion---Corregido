
# -*- coding: utf-8 -*-
from modulos.gestion_libros import menu_libros
from modulos.gestion_usuarios import menu_usuarios
from modulos.gestion_prestamos import menu_prestamos
from utilidades import limpiar_pantalla, pausar
from modulos.persistencia import inicializar_datos


def mostrar_menu_principal():
    """Muestra el menú principal del sistema"""
    limpiar_pantalla()
    print("="*50)
    print("    SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("="*50)
    print("    Versión 1.0 - Grupo 5")
    print("    UADE - Programación I")
    print("="*50)
    print("1) Libros")
    print("2) Usuarios")
    print("3) Préstamos")
    print("4) Salir")
    print("="*50)


def main():
    inicializar_datos()
    while True:
        try:
            mostrar_menu_principal()
            opcion = input("Seleccione una opción [1-4]: ").strip()
            if opcion == "1":
                menu_libros()
            elif opcion == "2":
                menu_usuarios()
            elif opcion == "3":
                menu_prestamos()
            elif opcion == "4":
                print("\n¡Hasta luego!")
                break
            else:
                print("\nOpción inválida. Por favor ingrese 1, 2, 3 o 4.")
                pausar()
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            pausar()


if __name__ == "__main__":
    main()
