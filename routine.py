# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from win10toast import ToastNotifier
import numpy as np
import pandas as pd
import datetime
import time

time_old = 255

while(True):
    now = datetime.datetime.now()
    
    if now.hour != time_old:
        #pega dia da semana e converte em texto
        weekday = now.isoweekday()
        if weekday == 1:
            weekday_name = "segunda"
        if weekday == 2:
            weekday_name = "terca"
        if weekday == 3:
            weekday_name = "quarta"
        if weekday == 4:
            weekday_name = "quinta"
        if weekday == 5:
            weekday_name = "sexta"
        if weekday == 6:
            weekday_name = "sabado"
        if weekday == 7:
            weekday_name = "domingo"
        
        
        #Abre planilha, checa dia da semana e horas nela, depois retorna 
        #deve o que fazer
        csv = pd.read_csv('routine.csv')
        action = csv[f'{weekday_name}'][now.hour]
        toaster = ToastNotifier()
        toaster.show_toast(f"{action}".upper(),f"{time.asctime(datetime.datetime.now().timetuple())}",duration=7)
        
        time_old = now.hour
    

