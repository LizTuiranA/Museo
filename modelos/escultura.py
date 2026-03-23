"""Subtipo de obra de arte: escultura."""

from modelos.obra_arte import ObraArte


class Escultura(ObraArte):
    """Representa esculturas dentro del catálogo."""

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
        estilo: str,
        material: str,
    ):
        super().__init__(
            id_obra,
            titulo,
            autor,
            periodo,
            valor,
            fecha_creacion,
            fecha_ingreso_museo,
            sala,
        )
        self.estilo = estilo
        self.material = material

    def obtener_informacion(self) -> str:
        return (
            f"[Escultura] ID: {self.id} | Título: {self.titulo} | "
            f"Autor: {self.autor.nombre} | Periodo: {self.periodo.nombre} | "
            f"Estilo: {self.estilo} | Material: {self.material} | "
            f"Estado: {self.estado.value} | Sala: {self.sala.numero} | "
            f"Valor: {self.valor:.2f}"
        )
