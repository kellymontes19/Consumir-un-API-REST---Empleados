#Grupo 5
#Apolinario Nathaly
#Barcia Karol
#Basurto Laura
#Bellolio Karla
#Montes Kelly
#Pilozo Noelia
#Pincay Mell
import requests
ruta= 'https://dummy.restapiexample.com/api/v1/employees'
response = requests.get(ruta, headers= {'User-Agent':'insomnia/2022.1.1'})
datos = response.json()
ids=datos['data']

def listar_empleados(ruta):
    empleados = requests.get(ruta, headers= {'User-Agent':'insomnia/2022.1.1'})
    empleados = empleados.json()
    #print(empleados)
    #print(empleados['data'])
    #print(empleados['data'] [2] ['employee_age'])
    #esta son las edades de los empleado minima y maxima
    edad_mayor=empleados['data'] [2] ['employee_age']
    edad_menor=empleados['data'] [14] ['employee_age']
    #salario maximo y minimo
    salario_minimo=empleados['data'] [23]['employee_salary']
    salario_maximo=empleados['data'] [16] ['employee_salary']
    #promedio de salario
    salarios_promedio=sum((empleados['data'][0]['employee_salary'], empleados['data'][1]['employee_salary'],empleados['data'][2]['employee_salary'],
                        empleados['data'][3]['employee_salary'], empleados['data'][4]['employee_salary'],empleados['data'][5]['employee_salary'],
                        empleados['data'][6]['employee_salary'], empleados['data'][7]['employee_salary'],empleados['data'][8]['employee_salary'],
                        empleados['data'][9]['employee_salary'], empleados['data'][10]['employee_salary'],empleados['data'][11]['employee_salary'],
                        empleados['data'][12]['employee_salary'], empleados['data'][13]['employee_salary'],empleados['data'][14]['employee_salary'],
                        empleados['data'][15]['employee_salary'], empleados['data'][16]['employee_salary'],empleados['data'][17]['employee_salary'],
                        empleados['data'][18]['employee_salary'], empleados['data'][19]['employee_salary'],empleados['data'][20]['employee_salary'],
                        empleados['data'][21]['employee_salary'], empleados['data'][22]['employee_salary'],empleados['data'][23]['employee_salary']))/24
    #promedio de edad
    edad_promedio=sum((empleados['data'][0]['employee_age'],empleados['data'][1]['employee_age'],empleados['data'][2]['employee_age'],
                empleados['data'][3]['employee_age'],empleados['data'][4]['employee_age'],empleados['data'][5]['employee_age'],
                empleados['data'][6]['employee_age'],empleados['data'][7]['employee_age'],empleados['data'][8]['employee_age'],
                empleados['data'][9]['employee_age'],empleados['data'][10]['employee_age'],empleados['data'][11]['employee_age'],
                empleados['data'][12]['employee_age'],empleados['data'][13]['employee_age'],empleados['data'][14]['employee_age'],
                empleados['data'][15]['employee_age'],empleados['data'][16]['employee_age'],empleados['data'][17]['employee_age'],
                empleados['data'][18]['employee_age'],empleados['data'][19]['employee_age'],empleados['data'][20]['employee_age'],
                empleados['data'][21]['employee_age'],empleados['data'][22]['employee_age'],empleados['data'][23]['employee_age'],))/24

    print('cual es la edad mayor de los trabajadores de la empresa:', edad_mayor)
    print('cual es la edad menor de los trabajadores de la empresa:', edad_menor)
    print('Cual es el salario minimo de los trabajadores de la empresa:',salario_minimo)
    print('Cual es el salario maximo de los trabajadores de la empresa:', salario_maximo)
    print('cual es el promedio del salario de los trabajadores de la empresa:', salarios_promedio)
    print('cual es el promedio de la edad de los trabajadores de la empresa:', edad_promedio)

if __name__=='__main__':
    ruta = 'https://dummy.restapiexample.com/api/v1/employees'
    listar_empleados(ruta)

    #detalle_empleados(ruta)
for id in ids:
    ids=id['id']
    #print (ids)
print('Cuantos empleado tiene la empresa:', ids)

