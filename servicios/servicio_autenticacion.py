"""Servicio para autenticación básica de usuarios internos."""


class ServicioAutenticacion:
    """Encapsula la lógica de validación de credenciales."""

    @staticmethod
    def autenticar(username: str, password: str, usuarios: list):
        """Retorna el usuario autenticado o None si falla."""
        for usuario in usuarios:
            if usuario.username == username and usuario.password == password:
                return usuario
        return None
