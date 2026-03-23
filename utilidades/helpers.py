"""Funciones utilitarias para entrada/salida y manejo simple de fechas."""

from datetime import datetime


FORMATO_FECHA = "%Y-%m-%d"


def convertir_fecha(fecha_texto: str):
    """Convierte texto YYYY-MM-DD a objeto date."""
    return datetime.strptime(fecha_texto, FORMATO_FECHA).date()


def fecha_actual_texto() -> str:
    """Obtiene la fecha actual como texto en formato YYYY-MM-DD."""
    return datetime.now().strftime(FORMATO_FECHA)


def leer_entero(mensaje: str):
    """Solicita un entero al usuario con validación básica."""
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")


def leer_flotante(mensaje: str):
    """Solicita un número decimal al usuario con validación básica."""
    while True:
        try:
            return float(input(mensaje).strip())
        except ValueError:
            print("Entrada inválida. Debe ingresar un valor numérico.")


def leer_fecha(mensaje: str):
    """Solicita una fecha válida en formato YYYY-MM-DD."""
    while True:
        valor = input(mensaje).strip()
        try:
            convertir_fecha(valor)
            return valor
        except ValueError:
            print("Fecha inválida. Use el formato YYYY-MM-DD.")


def pausar():
    """Pausa la consola para lectura de resultados."""
    input("\nPresione Enter para continuar...")
