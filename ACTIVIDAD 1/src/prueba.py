import pprint
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


def resetear_valores():
    return {"innovacion": 0, "presentacion": 0, "errores": 0, "mejores": 0, "total": 0}


def inicializar_acumulados(evaluaciones):   
    equipos = evaluaciones[0].keys()
    acumulados = dict(map(lambda equipo: (equipo, resetear_valores()), equipos))
    return acumulados

acum = inicializar_acumulados(evaluaciones)
pprint.pprint(acum)


print('-----------------')

print(evaluaciones)

def actualizar_acumulados(acum: dict, ronda: dict, mejor: str) -> dict: 
    print("hola")

actualizar_acumulados(acum,{
 'EquipoA': {'innovacion': 2, 'presentacion': 1, 'errores': True},
 'EquipoB': {'innovacion': 1, 'presentacion': 0, 'errores': False},
 'EquipoC': {'innovacion': 1, 'presentacion': 2, 'errores': True},
 'EquipoD': {'innovacion': 0, 'presentacion': 1, 'errores': False},
 'EquipoE': {'innovacion': 1, 'presentacion': 1, 'errores': False}
 }, "EquipoA")

pprint.pprint(acum)