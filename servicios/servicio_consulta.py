"""Servicio de consultas de lectura para catálogo y reportes."""


class ServicioConsulta:
    """Contiene operaciones de consulta sin alterar el estado del sistema."""

    @staticmethod
    def listar_obras_por_sala(catalogo, numero_sala: int) -> list:
        """Devuelve obras filtradas por número de sala."""
        return catalogo.listar_obras_por_sala(numero_sala)

    @staticmethod
    def calcular_valor_total(catalogo) -> float:
        """Suma la valoración de todas las obras del catálogo."""
        return sum(obra.valor for obra in catalogo.listar_obras())
