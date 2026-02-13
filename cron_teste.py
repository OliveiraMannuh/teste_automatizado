#Arquivo para testar o cron, verificando se o script é executado no horário configurado.

#Código para configurar CRON no linux para rodar o script diariamente às 14:20
#Utilize o comando para configurar o horário e arquivo: crontab -e
#Adicione a linha no arquivo, abre às 14:20: 20 14 * * * /home/manuela_oliveira/report.sh
## Formato Correto do Crontab:
#minuto (0-59) hora (0-23) dia (1-31) mês (1-12) dia_da_semana (0-7) (0 ou 7 = domingo) comando
#Salve (Ctrl+O, Enter, Ctrl+X)
#Configurar o arquivo report.sh para rodar o script Python, comando: nano /home/manuela_oliveira/report.sh
#Colar o comando para rodar o script Python
'''
#!/bin/bash

{
    echo "========================================="
    echo "INÍCIO: $(date)"
    echo "========================================="
    
    export DISPLAY=:0
    export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    
    # Executar com CAMINHO COMPLETO
    /usr/bin/python3 /opt/lampp/htdocs/automacaowork1/loginproducao/selenium/Report.py
    
    echo "========================================="
    echo "FIM: $(date)"
    echo "========================================="
    echo ""
    
} >> /home/manuela_oliveira/log_report.txt 2>&1
'''
#Salvar o arquivo (Ctrl+O, Enter, Ctrl+X)
#Verificar arquivo cron: crontab -l
#Testar a execução: /home/manuela_oliveira/report.sh
#Verificar o log para confirmar a execução: cat /home/manuela_oliveira/log_report.txt 
#Fim configuração CRON

import subprocess
import pyautogui 
import time
import datetime
# -*- coding: utf-8 -*-
coding='UTF-8'

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

pyautogui.PAUSE = 1  # Pausa de 1 segundo entre as ações do PyAutoGUI

# Configurar o driver do Selenium (neste exemplo, usando o ChromeDriver)
driver = webdriver.Chrome(service=servico, options=options)

#maximizar navegador
driver.maximize_window()

# Abrir Google
driver.get('https://google.com.nr')