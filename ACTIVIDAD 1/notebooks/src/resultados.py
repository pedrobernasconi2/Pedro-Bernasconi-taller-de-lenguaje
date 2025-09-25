"""
Funciones para ordenar y mostrar los resultados en forma de tabla.
"""

def ordenar_por_puntos(acum: dict) -> list[tuple[str, dict]]:
    """
    Recibe un diccionario acum donde las claves son nombres de equipos y
    los valores son diccionarios con los puntajes.
    Devuelve una lista de tuplas (nombre_equipo, datos_equipo) ordenada 
    por el puntaje total ("total") de mayor a menor.
    """
    # Usamos sorted() con una función lambda que extrae el valor "total" de cada equipo.
    #Ordenamos en reversa (reverse=True) para que el mayor puntaje esté primero.
    return sorted(acum.items(), key=lambda item: item[1].get("total", 0), reverse=True)

def mostrar_tabla(acum: dict, ronda_nro: int, mejor: tuple[str, int]) -> None:
    """
    Imprime los datos de cada equipo en líneas simples, resaltando el mejor equipo.
    """
    equipos_ordenados = ordenar_por_puntos(acum)
    print(f"\n--- Ronda {ronda_nro} ---")
    for nombre, datos in equipos_ordenados:
        if nombre == mejor[0]:
            print(f"*{nombre.upper()}* (Mejor equipo)")
        else:
            print(nombre)
        print(f"  Innovación: {datos.get('innovacion',0)}")
        print(f"  Presentación: {datos.get('presentacion',0)}")
        print(f"  Errores: {datos.get('errores',0)}")
        print(f"  Mejores: {datos.get('mejores',0)}")
        print(f"  Total: {datos.get('total',0)}\n")