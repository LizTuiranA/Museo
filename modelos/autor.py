"""Modelo que representa un autor de obras de arte."""


class Autor:
    """Entidad simple para identificar al creador de una obra."""

    def __init__(self, nombre: str, nacionalidad: str):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self) -> str:
        return f"{self.nombre} ({self.nacionalidad})"
