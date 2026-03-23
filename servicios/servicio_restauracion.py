"""Servicio de reglas para gestionar restauraciones."""

from modelos.estados import EstadoObra
from modelos.restauracion import Restauracion
from utilidades.helpers import fecha_actual_texto, convertir_fecha


class ServicioRestauracion:
    """Aplica reglas de negocio relacionadas con restauraciones."""

    def iniciar_restauracion(self, obra, tipo: str, observaciones: str = ""):
        """Inicia una restauración si la obra no está en restauración."""
        if obra.estado == EstadoObra.EN_RESTAURACION:
            return False, "La obra ya se encuentra en restauración."

        restauracion = Restauracion(tipo, fecha_actual_texto(), observaciones)
        obra.agregar_restauracion(restauracion)
        obra.cambiar_estado(EstadoObra.EN_RESTAURACION)
        return True, "Restauración iniciada correctamente."

    def finalizar_restauracion(self, obra):
        """Finaliza la restauración activa de la obra."""
        if obra.estado != EstadoObra.EN_RESTAURACION:
            return False, "La obra no está en restauración."

        restauracion_activa = None
        for restauracion in obra.restauraciones:
            if restauracion.esta_activa():
                restauracion_activa = restauracion

        if restauracion_activa is None:
            return False, "No existe una restauración activa para finalizar."

        restauracion_activa.finalizar(fecha_actual_texto())
        obra.cambiar_estado(EstadoObra.EXPUESTA)
        return True, "Restauración finalizada correctamente."

    def obtener_historial(self, obra) -> list:
        """Retorna historial ordenado por antigüedad (inicio más antiguo)."""
        return sorted(
            obra.restauraciones,
            key=lambda item: convertir_fecha(item.fecha_inicio),
        )

    def obras_pendientes_por_restauracion(self, catalogo) -> list:
        """Obtiene obras que superan 5 años desde su última restauración."""
        pendientes = []
        hoy = convertir_fecha(fecha_actual_texto())

        for obra in catalogo.listar_obras():
            if obra.estado == EstadoObra.EN_RESTAURACION:
                continue

            fecha_referencia = convertir_fecha(obra.fecha_ingreso_museo)
            historial = self.obtener_historial(obra)

            if historial:
                ultima = historial[-1]
                if ultima.fecha_fin:
                    fecha_referencia = convertir_fecha(ultima.fecha_fin)
                else:
                    # Si hay restauración abierta no debería entrar por estado,
                    # pero se deja la validación por seguridad.
                    continue

            dias = (hoy - fecha_referencia).days
            if dias >= 365 * 5:
                pendientes.append(obra)

        return pendientes
