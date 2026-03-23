"""Modelo de sala dentro del museo."""


class Sala:
    """Entidad para ubicar físicamente las obras en el museo."""

    def __init__(self, nombre: str, numero: int):
        self.nombre = nombre
        self.numero = numero

    def __str__(self) -> str:
        return f"Sala {self.numero} - {self.nombre}"
