"""Modelo para representar cesiones de obras entre museos."""

from modelos.estados import EstadoCesion
from modelos.museo_colaborador import MuseoColaborador


class Cesion:
    """Registra la cesión de una obra a un museo colaborador."""

    def __init__(
        self,
        museo_destino: MuseoColaborador,
        fecha_inicio: str,
        fecha_fin: str,
        importe_pagado: float,
        estado: EstadoCesion = EstadoCesion.PENDIENTE,
    ):
        self.museo_destino = museo_destino
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.importe_pagado = importe_pagado
        self.estado = estado

    def activar(self) -> None:
        """Cambia el estado de la cesión a activa."""
        self.estado = EstadoCesion.ACTIVA

    def finalizar(self) -> None:
        """Cambia el estado de la cesión a finalizada."""
        self.estado = EstadoCesion.FINALIZADA

    def __str__(self) -> str:
        return (
            f"Museo: {self.museo_destino.nombre} | "
            f"Periodo: {self.fecha_inicio} - {self.fecha_fin} | "
            f"Importe: {self.importe_pagado:.2f} | Estado: {self.estado.value}"
        )
