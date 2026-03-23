"""Modelo que representa un periodo artístico."""


class Periodo:
    """Entidad para agrupar obras por periodo histórico."""

    def __init__(self, nombre: str, fecha_inicio: str, fecha_fin: str):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def __str__(self) -> str:
        return f"{self.nombre} ({self.fecha_inicio} - {self.fecha_fin})"
