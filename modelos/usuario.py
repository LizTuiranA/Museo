"""Modelo de usuario del sistema interno del museo."""

from modelos.rol import Rol


class Usuario:
    """Entidad para autenticación simple en memoria."""

    def __init__(self, username: str, password: str, rol: Rol):
        self.username = username
        self.password = password
        self.rol = rol

    def __str__(self) -> str:
        return f"{self.username} ({self.rol.nombre})"
