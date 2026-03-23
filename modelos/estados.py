"""Enumeraciones de estados del dominio del museo."""

from enum import Enum


class EstadoObra(Enum):
    """Representa los estados posibles de una obra de arte."""

    EXPUESTA = "Expuesta"
    EN_RESTAURACION = "En restauración"
    CEDIDA = "Cedida"


class EstadoCesion(Enum):
    """Representa los estados posibles de una cesión."""

    PENDIENTE = "Pendiente"
    ACTIVA = "Activa"
    FINALIZADA = "Finalizada"
