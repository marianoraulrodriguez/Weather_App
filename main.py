from tkinter import *
import requests


# db127015acc3512d1d23651766aaf9c9
# api.openweathermap.org/data/2.5/weather?q={city name}


def show_weather(weather):
    try:
        # tuve que imprmir el json antes, para ver la ubicacion de estos datos print(response.json). Se guardan en weather
        # asignamos a variables los valores obtenidos desde el weather (desde el json)
        name_city = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        # se asignan esos valores a las Labels nomabradas anteriormente
        city['text'] = name_city  # se imprimen en pantalla con la Label mas abajo
        description['text'] = desc
        temperature['text'] = str(int(temp)) + '°C'  # venia como float, lo converti a entero y al str para sumar signo
    except:
        weather['name'] = 'Intenta nuevamente'  # Le damos la opcion de inpuntear sobre la equitera para reintentar


def weather_json(city):
    try:
        api_key = 'db127015acc3512d1d23651766aaf9c9'  # key de API
        url = 'https://api.openweathermap.org/data/2.5/weather'  # URL de API
        parameters = {'APPID': api_key, 'q': city, 'units': 'metric',
                      'lang': 'es'}  # parametros es un dic, con APPID que es la key, y la q es pedida por la API
        response = requests.get(url,
                                params=parameters)  # la respuesta que espero, la pido con request, la guardo con get y le paso parametros con params
        weather = response.json()
        show_weather(weather)  # usamos la funcion y le pasamos el weather encontrado
    except:
        print('Error')


window = Tk()  # Creamos la ventana
window.title('Weather App')  # Titulo a la ventana
window.geometry('350x400')  # Asignando tamano a la ventana 

# Caja de texto
text_city = Entry(window, font=('Courier', 20, 'normal'), justify='center')  # font, tamano, tipo, justificacion
text_city.pack(padx=30, pady=30)  # con pad se da el margen
text_city.focus()

# Boton
get_weather = Button(window, text='Obtener clima', font=('Courier', 20, 'normal'),
                     command=lambda: weather_json(text_city.get()))
# con el comando get() en text_city tomamos la informacion que se alojo en esa variable al usar Entry
get_weather.pack()

# Etiquetas
city = Label(window, font=('Courier', 20, 'normal'))
city.pack(padx=10, pady=10)

temperature = Label(window, font=('Courier', 50, 'normal'))
temperature.pack(padx=10, pady=20)

description = Label(window, font=('Courier', 20, 'normal'))
description.pack(padx=10, pady=10)

window.mainloop()
