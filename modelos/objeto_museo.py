"""Subtipo de obra de arte: objeto de museo."""

from modelos.obra_arte import ObraArte


class ObjetoMuseo(ObraArte):
    """Representa objetos históricos o culturales no clasificados."""

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
        tipo_objeto: str,
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
        self.tipo_objeto = tipo_objeto

    def obtener_informacion(self) -> str:
        return (
            f"[Objeto] ID: {self.id} | Título: {self.titulo} | "
            f"Autor: {self.autor.nombre} | Periodo: {self.periodo.nombre} | "
            f"Tipo: {self.tipo_objeto} | Estado: {self.estado.value} | "
            f"Sala: {self.sala.numero} | Valor: {self.valor:.2f}"
        )
