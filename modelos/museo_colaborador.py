"""Modelo para museos colaboradores con los que se hacen cesiones."""


class MuseoColaborador:
    """Entidad con los datos básicos de un museo externo."""

    def __init__(self, nombre: str, ciudad: str, pais: str):
        self.nombre = nombre
        self.ciudad = ciudad
        self.pais = pais

    def __str__(self) -> str:
        return f"{self.nombre} - {self.ciudad}, {self.pais}"
