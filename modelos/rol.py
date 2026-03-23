"""Modelo de rol para usuarios internos del sistema."""


class Rol:
    """Entidad simple que define el rol funcional del usuario."""

    def __init__(self, nombre: str):
        self.nombre = nombre

    def __str__(self) -> str:
        return self.nombre
