#Logando e exportando relatórios Alunos por turma 2026

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
from selenium.webdriver.chrome.options import Options


# Configurar Chrome em modo headless
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')

# Iniciar o Chrome
#driver = webdriver.Chrome(options=options)

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