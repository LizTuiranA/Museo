"""Modelo agregador del catálogo de obras del museo."""


class CatalogoObras:
    """Administra la colección de obras en memoria."""

    def __init__(self):
        self.obras = []

    def agregar_obra(self, obra) -> None:
        """Registra una nueva obra en el catálogo."""
        self.obras.append(obra)

    def listar_obras(self) -> list:
        """Retorna todas las obras registradas."""
        return self.obras

    def buscar_obra_por_id(self, id_obra: int):
        """Busca una obra por su identificador único."""
        for obra in self.obras:
            if obra.id == id_obra:
                return obra
        return None

    def listar_obras_por_sala(self, numero_sala: int) -> list:
        """Retorna obras ubicadas en una sala específica."""
        return [obra for obra in self.obras if obra.sala.numero == numero_sala]
