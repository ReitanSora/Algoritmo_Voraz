
def planificar(tareas=[{"num": 0, "beneficio": 0, "plazo": 0}], grupo_tareas=3):
    tareas.sort(key=lambda x: x[1], reverse=True)
    plazos = [0]+[t[2] for t in tareas]
    resultado = [0] * len(plazos)
    numTareas = 1
    resultado[1] = 1
    beneficio = int()

    for i in range(2, grupo_tareas):
        tarea = numTareas
        while plazos[resultado[tarea]] > max(plazos[i], tarea):
            tarea -= 1
        if plazos[i] > tarea:
            j = numTareas
            while j >= tarea + 1:
                resultado[j + 1] = resultado[j]
                j -= 1
            resultado[tarea + 1] = i
            
            numTareas += 1
    
    resultado = [v for v in resultado if v > 0]
    for i in resultado:
        beneficio = beneficio + tareas[i-1][1]
    return (resultado, beneficio)
