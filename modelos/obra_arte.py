"""Clase abstracta base para obras de arte del museo."""

from abc import ABC, abstractmethod

from modelos.estados import EstadoObra


class ObraArte(ABC):
    """Abstracción común de toda obra registrada en el catálogo."""

    def __init__(
        self,
        id_obra: int,
        titulo: str,
        autor,
        periodo,
        valor: float,
        fecha_creacion: str,
        fecha_ingreso_museo: str,
        sala,
    ):
        self.id = id_obra
        self.titulo = titulo
        self.autor = autor
        self.periodo = periodo
        self.valor = valor
        self.fecha_creacion = fecha_creacion
        self.fecha_ingreso_museo = fecha_ingreso_museo
        self.estado = EstadoObra.EXPUESTA
        self.sala = sala

        # Historiales asociados a la obra.
        self._restauraciones = []
        self._cesiones = []

    @abstractmethod
    def obtener_informacion(self) -> str:
        """Retorna información detallada de la obra."""

    def cambiar_estado(self, nuevo_estado: EstadoObra) -> None:
        """Permite actualizar el estado de la obra."""
        self.estado = nuevo_estado

    @property
    def restauraciones(self) -> list:
        """Expone la lista de restauraciones asociadas."""
        return self._restauraciones

    @property
    def cesiones(self) -> list:
        """Expone la lista de cesiones asociadas."""
        return self._cesiones

    def agregar_restauracion(self, restauracion) -> None:
        """Agrega una restauración al historial de la obra."""
        self._restauraciones.append(restauracion)

    def agregar_cesion(self, cesion) -> None:
        """Agrega una cesión al historial de la obra."""
        self._cesiones.append(cesion)
