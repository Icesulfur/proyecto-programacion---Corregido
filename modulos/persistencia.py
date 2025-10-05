
# -*- coding: utf-8 -*-
"""
Módulo de Persistencia de Datos
- Escritura atómica y recuperación de archivos temporales
- API simple: inicializar_datos, leer, escribir, generar_id, agregar/actualizar/eliminar_registro
"""
from __future__ import annotations

from pathlib import Path
from typing import List, Dict, Any

# Compatibilidad con Python 3.7 (Literal no está en typing)
try:
    from typing import Literal
except Exception:  # pragma: no cover
    from typing_extensions import Literal  # type: ignore

import json
import os

Tabla = Literal["libros", "usuarios", "prestamos"]

# Directorio de datos anclado a la raíz del proyecto (un nivel arriba de /modulos)
DATOS_DIR = Path(__file__).resolve().parents[1] / "datos"
RUTAS: Dict[str, Path] = {
    "libros": DATOS_DIR / "libros.json",
    "usuarios": DATOS_DIR / "usuarios.json",
    "prestamos": DATOS_DIR / "prestamos.json",
}

# Claves mínimas esperadas (para validación ligera)
CLAVES_ESPERADAS = {
    "libros": {"id", "titulo", "autor"},
    "usuarios": {"dni", "nombre"},
    "prestamos": {"id", "usuario_dni", "libro_id", "fecha"},
}


# ------------------------------
# Utilidades internas
# ------------------------------
def _atomic_dump(path: Path, data: Any) -> None:
    """
    Escribe JSON de forma atómica: primero un .tmp y luego reemplaza el final.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.flush()
        os.fsync(f.fileno())
    tmp.replace(path)
    # fsync del directorio (POSIX) para asegurar persistencia del rename
    if os.name == "posix":
        try:
            dir_fd = os.open(str(path.parent), os.O_RDONLY)
            try:
                os.fsync(dir_fd)
            finally:
                os.close(dir_fd)
        except OSError:
            pass


# ------------------------------
# API pública
# ------------------------------
def inicializar_datos(seed: bool = False) -> bool:
    """
    Crea el directorio /datos y los archivos JSON si no existen.
    Si encuentra .tmp y falta el final, recupera el .tmp como archivo definitivo.
    """
    DATOS_DIR.mkdir(parents=True, exist_ok=True)

    # Recuperación de .tmp si es necesario
    for nombre, ruta in RUTAS.items():
        tmp = ruta.with_suffix(ruta.suffix + ".tmp")
        if tmp.exists():
            if not ruta.exists():
                tmp.replace(ruta)  # recupero
            else:
                # Si el final existe, descarto el temporal
                try:
                    tmp.unlink()
                except OSError:
                    pass

    # Crear archivos si no existen
    for ruta in RUTAS.values():
        if not ruta.exists():
            _atomic_dump(ruta, [])
    return True


def leer(tabla: Tabla) -> List[Dict[str, Any]]:
    """Lee y devuelve la lista de registros de una tabla JSON."""
    ruta = RUTAS[str(tabla)]
    if not ruta.exists():
        inicializar_datos(seed=True)
    with ruta.open("r", encoding="utf-8") as f:
        try:
            datos = json.load(f)
        except json.JSONDecodeError:
            # Si está corrupto, lo reparamos a []
            datos = []
            _atomic_dump(ruta, datos)
    if not isinstance(datos, list):
        raise ValueError(f"El archivo {ruta.name} no contiene una lista JSON.")
    return datos


def escribir(tabla: Tabla, registros: List[Dict[str, Any]]) -> None:
    """Sobrescribe la tabla con la lista proporcionada (escritura atómica)."""
    ruta = RUTAS[str(tabla)]
    if not isinstance(registros, list):
        raise TypeError("registros debe ser una lista de diccionarios.")
    _atomic_dump(ruta, registros)


def agregar_registro(tabla: Tabla, registro: Dict[str, Any]) -> None:
    registros = leer(tabla)
    registros.append(registro)
    escribir(tabla, registros)


def actualizar_registro(tabla: Tabla, predicado, transform):
    """
    Actualiza in-place los registros que cumplan el predicado.
    Devuelve la cantidad de registros modificados.
    """
    registros = leer(tabla)
    count = 0
    for i, r in enumerate(registros):
        if predicado(r):
            registros[i] = transform(r)
            count += 1
    if count:
        escribir(tabla, registros)
    return count


def eliminar_registro(tabla: Tabla, predicado) -> int:
    """Elimina los registros que cumplan el predicado y devuelve cuántos borró."""
    registros = leer(tabla)
    nuevos = [r for r in registros if not predicado(r)]
    borrados = len(registros) - len(nuevos)
    if borrados:
        escribir(tabla, nuevos)
    return borrados


def generar_id(prefijo: str, existentes: List[Dict[str, Any]], campo: str, ancho: int = 3) -> str:
    """
    Genera IDs secuenciales del tipo 'LIB001', 'PREST007', etc.
    - prefijo: 'LIB', 'PREST', ...
    - campo: nombre del campo con el ID ('id' o 'codigo')
    """
    mayor = 0
    for r in existentes:
        v = str(r.get(campo, ""))
        if v.startswith(prefijo):
            sufijo = v[len(prefijo):]
            if sufijo.isdigit():
                mayor = max(mayor, int(sufijo))
    return f"{prefijo}{str(mayor + 1).zfill(ancho)}"


def validar_tabla(tabla: Tabla, registros: List[Dict[str, Any]]) -> List[str]:
    """Valida presencia de claves mínimas. Devuelve lista de errores (vacía si OK)."""
    errores = []
    claves = CLAVES_ESPERADAS.get(str(tabla), set())
    for idx, r in enumerate(registros, start=1):
        faltantes = claves - set(r.keys())
        if faltantes:
            errores.append(f"{tabla}[{idx}]: faltan claves {sorted(faltantes)}")
    return errores


def cargar_todo() -> Dict[str, List[Dict[str, Any]]]:
    """Devuelve un dict con las tres tablas cargadas."""
    return {t: leer(t) for t in RUTAS.keys()}
