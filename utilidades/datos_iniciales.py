"""Carga de datos iniciales para pruebas del sistema."""

from modelos.autor import Autor
from modelos.catalogo_obras import CatalogoObras
from modelos.cuadro import Cuadro
from modelos.escultura import Escultura
from modelos.museo_colaborador import MuseoColaborador
from modelos.objeto_museo import ObjetoMuseo
from modelos.periodo import Periodo
from modelos.rol import Rol
from modelos.sala import Sala
from modelos.usuario import Usuario


def cargar_datos_iniciales():
    """Construye entidades base para ejecutar el programa en memoria."""

    autores = [
        Autor("Pablo Picasso", "Española"),
        Autor("Auguste Rodin", "Francesa"),
        Autor("Autor desconocido", "Egipcia"),
        Autor("Frida Kahlo", "Mexicana"),
    ]

    periodos = [
        Periodo("Renacimiento", "1400-01-01", "1600-12-31"),
        Periodo("Modernismo", "1850-01-01", "1950-12-31"),
        Periodo("Antiguo Egipto", "-3000-01-01", "-30-12-31"),
        Periodo("Contemporáneo", "1951-01-01", "2026-12-31"),
    ]

    salas = [
        Sala("Sala Principal", 1),
        Sala("Sala de Esculturas", 2),
        Sala("Sala Histórica", 3),
    ]

    rol_encargado = Rol("encargado_catalogo")
    rol_restaurador = Rol("restaurador_jefe")
    rol_director = Rol("director_museo")

    usuarios = [
        Usuario("catalogo", "1234", rol_encargado),
        Usuario("restaurador", "1234", rol_restaurador),
        Usuario("director", "1234", rol_director),
    ]

    museos_colaboradores = [
        MuseoColaborador("Museo del Prado", "Madrid", "España"),
        MuseoColaborador("Louvre", "París", "Francia"),
    ]

    catalogo = CatalogoObras()
    catalogo.agregar_obra(
        Cuadro(
            1,
            "Guernica",
            autores[0],
            periodos[1],
            2000000,
            "1937-06-01",
            "2010-03-15",
            salas[0],
            "Cubismo",
            "Óleo sobre lienzo",
        )
    )
    catalogo.agregar_obra(
        Escultura(
            2,
            "El Pensador",
            autores[1],
            periodos[1],
            1500000,
            "1904-01-01",
            "2012-05-10",
            salas[1],
            "Realismo",
            "Bronce",
        )
    )
    catalogo.agregar_obra(
        ObjetoMuseo(
            3,
            "Máscara funeraria",
            autores[2],
            periodos[2],
            800000,
            "1000-01-01",
            "2015-09-20",
            salas[2],
            "Pieza arqueológica",
        )
    )

    return {
        "autores": autores,
        "periodos": periodos,
        "salas": salas,
        "usuarios": usuarios,
        "catalogo": catalogo,
        "museos_colaboradores": museos_colaboradores,
    }
