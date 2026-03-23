"""Modelo para registrar restauraciones de obras."""


class Restauracion:
    """Registra el ciclo de una restauración realizada a una obra."""

    def __init__(self, tipo: str, fecha_inicio: str, observaciones: str = ""):
        self.tipo = tipo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = None
        self.observaciones = observaciones

    def finalizar(self, fecha_fin: str) -> None:
        """Marca la restauración como finalizada."""
        self.fecha_fin = fecha_fin

    def esta_activa(self) -> bool:
        """Indica si la restauración sigue en curso."""
        return self.fecha_fin is None

    def __str__(self) -> str:
        fin = self.fecha_fin if self.fecha_fin else "En curso"
        return (
            f"Tipo: {self.tipo} | Inicio: {self.fecha_inicio} | "
            f"Fin: {fin} | Obs: {self.observaciones}"
        )
