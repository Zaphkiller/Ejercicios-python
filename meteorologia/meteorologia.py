import random
from datetime import date, datetime

ALFABETO = [chr(ord("A") + i) for i in range(26)]

def generar_codigo_meteo():
    return f"{random.choice(ALFABETO)}{random.randint(0,100):02d}"

def obtener_temp():
    return float(f"{random.randint(27, 38) + random.random():.1f}")

def obter_sss(temp : float):
    delta = 3
    return float(f"{random.randint(int(temp) - delta, int(temp) + delta) + random.random():.1f}")

def obtener_fecha():
    return datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

def obtener_promedio(temperaturas : list):
    #temp index 0
    # ST index 1
    promedio_temp = sum([t[0] for t in temperaturas])/len(temperaturas)
    promedio_st = sum([t[1] for t in temperaturas])/len(temperaturas)
    return (promedio_temp, promedio_st)

def obtener_mayor_y_menor_temp(temperaturas : list):
    temp_max = 0
    temp_min = 10000
    # temp_max_indice
    # temp_min_indice
    for i in range(len(temperaturas)):
        if temperaturas[i][0] < temp_min:
            temp_min = temperaturas[i][0]
            temp_min_index = i

        if temperaturas[i][0] > temp_max:
            temp_max = temperaturas[i][0]
            temp_max_index = i

    return temp_max_index,temp_min_index

if __name__ == '__main__':
    N = int(input("Numero de mediciones: "))

    codigos = []
    fecha = []
    temperatura = []

    for i in range(N):
        codigos.append(generar_codigo_meteo())
        fecha.append(obtener_fecha())
        temp = obtener_temp()
        temperatura.append( (temp, obter_sss(temp)) )
    
    temperatura_promedio, sensacion_promedio = obtener_promedio(temperatura)
    temp_max_index, temp_min_index = obtener_mayor_y_menor_temp(temperatura)

    print("Estaciones: ")
    print(codigos)
    print("Fechas: ")
    print(fecha)
    print("Temperatura, Sensacion Termica: ")
    print(temperatura)

    print(f"Temperatura promedio: {temperatura_promedio:.1f}, Sensacion promedio: {sensacion_promedio:.1f}")
    print(f"Temperatura Mayor: {temperatura[temp_max_index][0]}, Estacion : {codigos[temp_max_index]}, Fecha : {fecha[temp_max_index]}")
    print(f"Temperatura Menor: {temperatura[temp_min_index][0]}, Estacion : {codigos[temp_min_index]}, Fecha : {fecha[temp_min_index]}")

