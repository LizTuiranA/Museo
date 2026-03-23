"""Subtipo de obra de arte: cuadro."""

from modelos.obra_arte import ObraArte


class Cuadro(ObraArte):
    """Representa obras pictóricas dentro del catálogo."""

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
        tecnica: str,
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
        self.tecnica = tecnica

    def obtener_informacion(self) -> str:
        return (
            f"[Cuadro] ID: {self.id} | Título: {self.titulo} | "
            f"Autor: {self.autor.nombre} | Periodo: {self.periodo.nombre} | "
            f"Estilo: {self.estilo} | Técnica: {self.tecnica} | "
            f"Estado: {self.estado.value} | Sala: {self.sala.numero} | "
            f"Valor: {self.valor:.2f}"
        )
