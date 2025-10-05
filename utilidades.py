"""
Utilidades del Sistema
Funciones auxiliares para el sistema de gestión de biblioteca
"""

import os

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter"""
    input("\nPresione Enter para continuar...")

def mostrar_mensaje(mensaje, tipo="INFO"):
    """Muestra un mensaje con formato"""
    print(f"\n{mensaje}")