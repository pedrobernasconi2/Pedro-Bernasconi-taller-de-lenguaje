import pprint
from src.evaluacion import mejor_equipo_ronda
from src.acumulados import inicializar_acumulados, actualizar_acumulados
from src.resultados import mostrar_tabla


#----rondas resultados--------:
evaluaciones = [
 # Ronda 1
 {
 'EquipoA': {'innovacion': 2, 'presentacion': 1, 'errores': True},
 'EquipoB': {'innovacion': 1, 'presentacion': 0, 'errores': False},
 'EquipoC': {'innovacion': 1, 'presentacion': 2, 'errores': True},
 'EquipoD': {'innovacion': 0, 'presentacion': 1, 'errores': False},
 'EquipoE': {'innovacion': 1, 'presentacion': 1, 'errores': False}
 },
 # Ronda 2
 {
 'EquipoA': {'innovacion': 0, 'presentacion': 2, 'errores': False},
 'EquipoB': {'innovacion': 2, 'presentacion': 0, 'errores': True},
 'EquipoC': {'innovacion': 1, 'presentacion': 1, 'errores': False},
 'EquipoD': {'innovacion': 2, 'presentacion': 1, 'errores': True},
 'EquipoE': {'innovacion': 0, 'presentacion': 1, 'errores': False}
 },
 # Ronda 3
 {
 'EquipoA': {'innovacion': 3, 'presentacion': 2, 'errores': False},
 'EquipoB': {'innovacion': 1, 'presentacion': 1, 'errores': True},
 'EquipoC': {'innovacion': 2, 'presentacion': 0, 'errores': False},
 'EquipoD': {'innovacion': 1, 'presentacion': 3, 'errores': True},
 'EquipoE': {'innovacion': 2, 'presentacion': 2, 'errores': False}
 },
 # Ronda 4
 {
 'EquipoA': {'innovacion': 1, 'presentacion': 3, 'errores': True},
 'EquipoB': {'innovacion': 2, 'presentacion': 2, 'errores': False},
 'EquipoC': {'innovacion': 3, 'presentacion': 1, 'errores': False},
 'EquipoD': {'innovacion': 0, 'presentacion': 2, 'errores': True},
 'EquipoE': {'innovacion': 2, 'presentacion': 0, 'errores': False}
 },
 # Ronda 5
 {
 'EquipoA': {'innovacion': 2, 'presentacion': 2, 'errores': False},
 'EquipoB': {'innovacion': 1, 'presentacion': 3, 'errores': True},
 'EquipoC': {'innovacion': 0, 'presentacion': 2, 'errores': False},
 'EquipoD': {'innovacion': 3, 'presentacion': 1, 'errores': False},
 'EquipoE': {'innovacion': 2, 'presentacion': 3, 'errores': True}
 }
]

# ----FLUJO PRINCIPAL--------:

## Inicializamos acumulados con los equipos de la primera ronda
acumulados = inicializar_acumulados(list(evaluaciones[0].keys()))

# Procesamos cada ronda
nro_Ronda=1 
for ronda in evaluaciones:
    mejor = mejor_equipo_ronda(ronda)
    acumulados = actualizar_acumulados(acumulados, ronda, mejor[0])
    mostrar_tabla(acumulados, nro_Ronda, mejor)
    nro_Ronda= nro_Ronda + 1

