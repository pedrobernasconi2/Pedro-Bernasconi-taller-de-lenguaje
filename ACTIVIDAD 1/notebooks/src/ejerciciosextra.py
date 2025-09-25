def equipo_mas_constante(evaluaciones):
    """
    Determina el equipo más constante, es decir, el que tuvo la menor variación
    entre sus puntajes de ronda (diferencia entre su puntaje máximo y mínimo).
    Retorna el nombre del equipo y el valor de esa diferencia.
    """
    # Inicializa un diccionario para guardar los puntajes de cada equipo por ronda
    puntajes_por_equipo = {equipo: [] for equipo in evaluaciones[0].keys()}
    
    # Recorre cada ronda y calcula el puntaje de cada equipo en esa ronda
    for ronda in evaluaciones:
        for equipo, datos in ronda.items():
            # Calcula el puntaje según la fórmula usada en el programa principal
            puntaje = datos["innovacion"]*3 + datos["presentacion"]*1
            if datos["errores"]:
                puntaje -= 1
            # Guarda el puntaje en la lista correspondiente al equipo
            puntajes_por_equipo[equipo].append(puntaje)
    
    # Calcula la variación (máximo - mínimo) de puntajes para cada equipo
    variaciones = {equipo: max(puntajes)-min(puntajes) for equipo, puntajes in puntajes_por_equipo.items()}
    
    # Busca el equipo con la menor variación
    equipo_constante = min(variaciones, key=variaciones.get)
    
    # Retorna el nombre del equipo y la diferencia encontrada
    return equipo_constante, variaciones[equipo_constante]

def promedios_innovacion_presentacion(evaluaciones):
    """
    Calcula los promedios generales de innovación y presentación entre todos los equipos,
    al finalizar todas las rondas. Retorna ambos promedios.
    """
    total_innovacion = 0  # Acumulador de innovación
    total_presentacion = 0  # Acumulador de presentación
    total_equipos = 0  # Contador de equipos (en todas las rondas)
    
    # Recorre todas las rondas y suma los valores de innovación y presentación
    for ronda in evaluaciones:
        for datos in ronda.values():
            total_innovacion += datos["innovacion"]
            total_presentacion += datos["presentacion"]
            total_equipos += 1  # Cuenta cada equipo en cada ronda
    
    # Calcula los promedios dividiendo el total por la cantidad de equipos/rondas
    promedio_innovacion = total_innovacion / total_equipos
    promedio_presentacion = total_presentacion / total_equipos
    
    # Retorna ambos promedios
    return promedio_innovacion, promedio_presentacion