"""Servicio de reglas para cesiones de obras a museos colaboradores."""

from modelos.cesion import Cesion
from modelos.estados import EstadoCesion, EstadoObra


class ServicioCesion:
    """Gestiona cesiones activas, pendientes e historial por obra."""

    def registrar_cesion(
        self,
        obra,
        museo,
        fecha_inicio: str,
        fecha_fin: str,
        importe: float,
    ):
        """Registra una cesión aplicando reglas de estado."""
        if obra.estado == EstadoObra.EN_RESTAURACION:
            return False, "No se puede ceder una obra en restauración."

        cesion_activa = self._obtener_cesion_activa(obra)
        if cesion_activa:
            cesion = Cesion(
                museo,
                fecha_inicio,
                fecha_fin,
                importe,
                estado=EstadoCesion.PENDIENTE,
            )
            obra.agregar_cesion(cesion)
            return (
                True,
                "La obra ya está cedida. La nueva cesión quedó pendiente.",
            )

        cesion = Cesion(
            museo,
            fecha_inicio,
            fecha_fin,
            importe,
            estado=EstadoCesion.ACTIVA,
        )
        obra.agregar_cesion(cesion)
        obra.cambiar_estado(EstadoObra.CEDIDA)
        return True, "Cesión registrada y activada correctamente."

    def solicitar_cesion(
        self,
        obra,
        museo,
        fecha_inicio: str,
        fecha_fin: str,
        importe: float,
    ):
        """Alias semántico para solicitar una cesión."""
        return self.registrar_cesion(obra, museo, fecha_inicio, fecha_fin, importe)

    def obtener_cesiones(self, obra) -> list:
        """Retorna el historial de cesiones de una obra."""
        return obra.cesiones

    def finalizar_cesion_activa(self, obra):
        """Finaliza la cesión activa y activa la siguiente pendiente, si existe."""
        activa = self._obtener_cesion_activa(obra)
        if not activa:
            return False, "La obra no tiene cesión activa."

        activa.finalizar()
        siguiente = self._obtener_primera_pendiente(obra)

        if siguiente:
            siguiente.activar()
            obra.cambiar_estado(EstadoObra.CEDIDA)
            return True, "Cesión activa finalizada y pendiente activada."

        obra.cambiar_estado(EstadoObra.EXPUESTA)
        return True, "Cesión activa finalizada. La obra vuelve a expuesta."

    @staticmethod
    def _obtener_cesion_activa(obra):
        for cesion in obra.cesiones:
            if cesion.estado == EstadoCesion.ACTIVA:
                return cesion
        return None

    @staticmethod
    def _obtener_primera_pendiente(obra):
        for cesion in obra.cesiones:
            if cesion.estado == EstadoCesion.PENDIENTE:
                return cesion
        return None
