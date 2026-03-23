"""Punto de entrada de la aplicación de consola del museo."""

from modelos.cuadro import Cuadro
from modelos.escultura import Escultura
from modelos.museo_colaborador import MuseoColaborador
from modelos.objeto_museo import ObjetoMuseo
from servicios.servicio_autenticacion import ServicioAutenticacion
from servicios.servicio_cesion import ServicioCesion
from servicios.servicio_consulta import ServicioConsulta
from servicios.servicio_restauracion import ServicioRestauracion
from utilidades.datos_iniciales import cargar_datos_iniciales
from utilidades.helpers import leer_entero, leer_fecha, leer_flotante, pausar


class AplicacionMuseo:
    """Orquesta menús y llamadas a los servicios del sistema."""

    def __init__(self):
        datos = cargar_datos_iniciales()

        self.autores = datos["autores"]
        self.periodos = datos["periodos"]
        self.salas = datos["salas"]
        self.usuarios = datos["usuarios"]
        self.catalogo = datos["catalogo"]
        self.museos_colaboradores = datos["museos_colaboradores"]

        self.servicio_autenticacion = ServicioAutenticacion()
        self.servicio_restauracion = ServicioRestauracion()
        self.servicio_cesion = ServicioCesion()
        self.servicio_consulta = ServicioConsulta()

        self.permisos = {
            "1": ["encargado_catalogo"],
            "5": ["restaurador_jefe"],
            "6": ["restaurador_jefe"],
            "7": ["restaurador_jefe"],
            "8": ["restaurador_jefe"],
            "9": ["encargado_catalogo"],
            "10": ["encargado_catalogo"],
            "12": ["director_museo"],
        }

    def ejecutar(self):
        """Inicia el ciclo principal de la aplicación."""
        while True:
            print("\n=== SISTEMA DE GESTION DEL MUSEO ===")
            print("1. Ingresar como usuario interno")
            print("2. Modo visitante (consultar por sala)")
            print("3. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                usuario = self._login()
                if usuario:
                    self._menu_principal(usuario)
            elif opcion == "2":
                self._menu_visitante()
            elif opcion == "3":
                print("Hasta pronto.")
                break
            else:
                print("Opción inválida.")

    def _login(self):
        """Realiza autenticación simple para usuarios internos."""
        print("\n--- Autenticación interna ---")
        username = input("Usuario: ").strip()
        password = input("Contraseña: ").strip()

        usuario = self.servicio_autenticacion.autenticar(
            username,
            password,
            self.usuarios,
        )

        if usuario is None:
            print("Credenciales inválidas.")
            return None

        print(f"Bienvenido {usuario.username}. Rol: {usuario.rol.nombre}")
        return usuario

    def _menu_principal(self, usuario):
        """Muestra menú principal para usuarios internos autenticados."""
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1. Registrar obra")
            print("2. Listar todas las obras")
            print("3. Buscar obra por ID")
            print("4. Consultar obras por sala")
            print("5. Iniciar restauración")
            print("6. Finalizar restauración")
            print("7. Ver historial de restauraciones de una obra")
            print("8. Ver obras pendientes por restauración")
            print("9. Registrar museo colaborador")
            print("10. Registrar cesión de obra")
            print("11. Ver cesiones de una obra")
            print("12. Consultar valor total del museo")
            print("13. Cambiar de usuario")
            print("14. Salir")
            print("15. Modo visitante")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "14":
                print("Cierre de sesión y salida del sistema.")
                raise SystemExit

            if opcion == "13":
                print("Cierre de sesión realizado.")
                break

            if opcion == "15":
                self._menu_visitante()
                continue

            if not self._tiene_permiso(usuario, opcion):
                print("No tiene permisos para esta opción con su rol actual.")
                pausar()
                continue

            self._ejecutar_opcion(opcion)

    def _menu_visitante(self):
        """Muestra menú reducido para visitantes."""
        while True:
            print("\n=== MODO VISITANTE ===")
            print("1. Consultar obras por sala")
            print("2. Volver")

            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                numero_sala = leer_entero("Número de sala: ")
                obras = self.servicio_consulta.listar_obras_por_sala(
                    self.catalogo,
                    numero_sala,
                )
                if not obras:
                    print("No hay obras registradas en esa sala.")
                else:
                    print("\nObras encontradas:")
                    for obra in obras:
                        print(obra.obtener_informacion())
                pausar()
            elif opcion == "2":
                break
            else:
                print("Opción inválida.")

    def _ejecutar_opcion(self, opcion: str):
        """Despacha la opción seleccionada del menú principal."""
        if opcion == "1":
            self._registrar_obra()
        elif opcion == "2":
            self._listar_obras()
        elif opcion == "3":
            self._buscar_obra_por_id()
        elif opcion == "4":
            self._consultar_obras_por_sala()
        elif opcion == "5":
            self._iniciar_restauracion()
        elif opcion == "6":
            self._finalizar_restauracion()
        elif opcion == "7":
            self._ver_historial_restauraciones()
        elif opcion == "8":
            self._ver_obras_pendientes_restauracion()
        elif opcion == "9":
            self._registrar_museo_colaborador()
        elif opcion == "10":
            self._registrar_cesion()
        elif opcion == "11":
            self._ver_cesiones()
        elif opcion == "12":
            self._consultar_valor_total()
        else:
            print("Opción inválida.")
        pausar()

    def _tiene_permiso(self, usuario, opcion: str) -> bool:
        """Valida permisos por rol para opciones específicas."""
        roles_permitidos = self.permisos.get(opcion)
        if not roles_permitidos:
            return True
        return usuario.rol.nombre in roles_permitidos

    def _obtener_nuevo_id_obra(self) -> int:
        """Genera un ID incremental para nueva obra."""
        obras = self.catalogo.listar_obras()
        if not obras:
            return 1
        return max(obra.id for obra in obras) + 1

    def _seleccionar_autor(self):
        """Solicita al usuario seleccionar un autor existente."""
        print("\nAutores disponibles:")
        for indice, autor in enumerate(self.autores, start=1):
            print(f"{indice}. {autor}")

        while True:
            opcion = leer_entero("Seleccione autor: ")
            if 1 <= opcion <= len(self.autores):
                return self.autores[opcion - 1]
            print("Opción inválida.")

    def _seleccionar_periodo(self):
        """Solicita seleccionar un periodo artístico existente."""
        print("\nPeriodos disponibles:")
        for indice, periodo in enumerate(self.periodos, start=1):
            print(f"{indice}. {periodo}")

        while True:
            opcion = leer_entero("Seleccione periodo: ")
            if 1 <= opcion <= len(self.periodos):
                return self.periodos[opcion - 1]
            print("Opción inválida.")

    def _seleccionar_sala(self):
        """Solicita seleccionar una sala existente."""
        print("\nSalas disponibles:")
        for indice, sala in enumerate(self.salas, start=1):
            print(f"{indice}. {sala}")

        while True:
            opcion = leer_entero("Seleccione sala: ")
            if 1 <= opcion <= len(self.salas):
                return self.salas[opcion - 1]
            print("Opción inválida.")

    def _seleccionar_museo_colaborador(self):
        """Solicita seleccionar un museo colaborador existente."""
        if not self.museos_colaboradores:
            print("No hay museos colaboradores registrados.")
            return None

        print("\nMuseos colaboradores:")
        for indice, museo in enumerate(self.museos_colaboradores, start=1):
            print(f"{indice}. {museo}")

        while True:
            opcion = leer_entero("Seleccione museo destino: ")
            if 1 <= opcion <= len(self.museos_colaboradores):
                return self.museos_colaboradores[opcion - 1]
            print("Opción inválida.")

    def _seleccionar_obra(self):
        """Busca una obra por ID y la retorna."""
        id_obra = leer_entero("Ingrese ID de la obra: ")
        obra = self.catalogo.buscar_obra_por_id(id_obra)
        if obra is None:
            print("No existe una obra con ese ID.")
            return None
        return obra

    def _registrar_obra(self):
        """Registra una nueva obra según el tipo seleccionado."""
        print("\n--- Registro de obra ---")
        print("1. Cuadro")
        print("2. Escultura")
        print("3. Objeto de museo")
        tipo = input("Seleccione tipo de obra: ").strip()

        if tipo not in {"1", "2", "3"}:
            print("Tipo de obra inválido.")
            return

        titulo = input("Título: ").strip()
        autor = self._seleccionar_autor()
        periodo = self._seleccionar_periodo()
        valor = leer_flotante("Valor económico: ")
        fecha_creacion = leer_fecha("Fecha de creación (YYYY-MM-DD): ")
        fecha_ingreso = leer_fecha("Fecha de ingreso al museo (YYYY-MM-DD): ")
        sala = self._seleccionar_sala()
        id_obra = self._obtener_nuevo_id_obra()

        if tipo == "1":
            estilo = input("Estilo del cuadro: ").strip()
            tecnica = input("Técnica del cuadro: ").strip()
            obra = Cuadro(
                id_obra,
                titulo,
                autor,
                periodo,
                valor,
                fecha_creacion,
                fecha_ingreso,
                sala,
                estilo,
                tecnica,
            )
        elif tipo == "2":
            estilo = input("Estilo de la escultura: ").strip()
            material = input("Material de la escultura: ").strip()
            obra = Escultura(
                id_obra,
                titulo,
                autor,
                periodo,
                valor,
                fecha_creacion,
                fecha_ingreso,
                sala,
                estilo,
                material,
            )
        else:
            tipo_objeto = input("Tipo de objeto: ").strip()
            obra = ObjetoMuseo(
                id_obra,
                titulo,
                autor,
                periodo,
                valor,
                fecha_creacion,
                fecha_ingreso,
                sala,
                tipo_objeto,
            )

        self.catalogo.agregar_obra(obra)
        print(f"Obra registrada con éxito. ID asignado: {id_obra}")

    def _listar_obras(self):
        """Lista todas las obras del catálogo."""
        obras = self.catalogo.listar_obras()
        if not obras:
            print("No hay obras registradas.")
            return

        print("\n--- Catálogo de obras ---")
        for obra in obras:
            print(obra.obtener_informacion())

    def _buscar_obra_por_id(self):
        """Muestra el detalle de una obra buscada por ID."""
        obra = self._seleccionar_obra()
        if obra:
            print(obra.obtener_informacion())

    def _consultar_obras_por_sala(self):
        """Permite consultar obras filtradas por número de sala."""
        numero_sala = leer_entero("Número de sala: ")
        obras = self.servicio_consulta.listar_obras_por_sala(self.catalogo, numero_sala)

        if not obras:
            print("No hay obras en la sala indicada.")
            return

        print(f"\nObras en sala {numero_sala}:")
        for obra in obras:
            print(obra.obtener_informacion())

    def _iniciar_restauracion(self):
        """Inicia restauración de una obra, si aplica."""
        obra = self._seleccionar_obra()
        if not obra:
            return

        tipo = input("Tipo de restauración: ").strip()
        observaciones = input("Observaciones: ").strip()
        ok, mensaje = self.servicio_restauracion.iniciar_restauracion(
            obra,
            tipo,
            observaciones,
        )
        print(mensaje)
        if ok:
            print(f"Estado actual de la obra: {obra.estado.value}")

    def _finalizar_restauracion(self):
        """Finaliza restauración de una obra, si está en curso."""
        obra = self._seleccionar_obra()
        if not obra:
            return

        ok, mensaje = self.servicio_restauracion.finalizar_restauracion(obra)
        print(mensaje)
        if ok:
            print(f"Estado actual de la obra: {obra.estado.value}")

    def _ver_historial_restauraciones(self):
        """Muestra historial de restauraciones de una obra."""
        obra = self._seleccionar_obra()
        if not obra:
            return

        historial = self.servicio_restauracion.obtener_historial(obra)
        if not historial:
            print("La obra no tiene restauraciones registradas.")
            return

        print("\n--- Historial de restauraciones ---")
        for restauracion in historial:
            print(restauracion)

    def _ver_obras_pendientes_restauracion(self):
        """Lista obras que deberían pasar por restauración (cada 5 años)."""
        pendientes = self.servicio_restauracion.obras_pendientes_por_restauracion(
            self.catalogo
        )
        if not pendientes:
            print("No hay obras pendientes por restauración.")
            return

        print("\n--- Obras pendientes por restauración ---")
        for obra in pendientes:
            print(obra.obtener_informacion())

    def _registrar_museo_colaborador(self):
        """Registra un nuevo museo colaborador."""
        print("\n--- Registro de museo colaborador ---")
        nombre = input("Nombre: ").strip()
        ciudad = input("Ciudad: ").strip()
        pais = input("País: ").strip()

        museo = MuseoColaborador(nombre, ciudad, pais)
        self.museos_colaboradores.append(museo)
        print("Museo colaborador registrado correctamente.")

    def _registrar_cesion(self):
        """Registra una cesión de obra a un museo colaborador."""
        obra = self._seleccionar_obra()
        if not obra:
            return

        museo = self._seleccionar_museo_colaborador()
        if museo is None:
            return

        fecha_inicio = leer_fecha("Fecha inicio cesión (YYYY-MM-DD): ")
        fecha_fin = leer_fecha("Fecha fin cesión (YYYY-MM-DD): ")
        importe = leer_flotante("Importe pagado: ")

        ok, mensaje = self.servicio_cesion.registrar_cesion(
            obra,
            museo,
            fecha_inicio,
            fecha_fin,
            importe,
        )
        print(mensaje)
        if ok:
            print(f"Estado actual de la obra: {obra.estado.value}")

    def _ver_cesiones(self):
        """Muestra historial de cesiones de una obra."""
        obra = self._seleccionar_obra()
        if not obra:
            return

        cesiones = self.servicio_cesion.obtener_cesiones(obra)
        if not cesiones:
            print("La obra no tiene cesiones registradas.")
            return

        print("\n--- Historial de cesiones ---")
        for cesion in cesiones:
            print(cesion)

    def _consultar_valor_total(self):
        """Calcula y muestra la valoración total del catálogo."""
        valor_total = self.servicio_consulta.calcular_valor_total(self.catalogo)
        print(f"Valor total del museo: {valor_total:.2f}")


if __name__ == "__main__":
    app = AplicacionMuseo()
    app.ejecutar()
