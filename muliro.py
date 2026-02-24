import time
import os
import random

caminho_imagem = r"muliro.jpeg"

# Aqui você define os limites
min_tempo_fechada = 10   # Mínimo de espera
max_tempo_fechada = 720   # Máximo de espera (1 minuto)
tempo_aberta = 5         # Quanto tempo a imagem fica na tela
# ---------------------

def abrir_e_fechar_aleatorio():
    print("Script iniciado (CTRL+C para parar)")
    
    while True:
        espera = random.randint(min_tempo_fechada, max_tempo_fechada)
        print(f"A imagem vai abrir em {espera} segundos")
        
        time.sleep(espera)
        
        print("Abrindo imagem...")
        os.startfile(caminho_imagem)
        
        time.sleep(tempo_aberta)
        
        nome_arquivo = os.path.basename(caminho_imagem)
        print(f"Limpando a tela (Fechando janela: {nome_arquivo})...")
        
        os.system(f'taskkill /FI "WINDOWTITLE eq {nome_arquivo}*" /F >nul 2>&1')
        
        print("--- Ciclo finalizado, sorteando novo tempo ---")

if __name__ == "__main__":
    abrir_e_fechar_aleatorio()