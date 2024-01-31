import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
data = pd.read_csv("datos.csv")
data_dict = data.to_dict('list')
celulares = data_dict['celular']
mensajes = data_dict['mensaje']
links = data_dict['link']
combo = zip(celulares,mensajes,links)
first = True
for celular,mensaje,link in combo:
    time.sleep(8)
    web.open_new_tab("https://web.whatsapp.com/send?phone="+str(celular)+"&text="+str(mensaje)+str(link))
    if first:
        time.sleep(8)
        first=False
    width,height = pg.size()
    pg.click(width/3,height/3)
    time.sleep(30)
    pg.press('enter')
    time.sleep(6)
    pg.hotkey('ctrl', 'w')