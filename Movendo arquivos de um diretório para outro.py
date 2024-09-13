# Começar o Projeto Importando o "Shutil" onde ele que faz mover arquivos de um lugar para o outro.

import shutil

# Caminho de origem e destino
origem = r'C:\Users\gamorais\OneDrive - Brasilseg Companhia de Seguros\Área de Trabalho\TESTE PYT'
destino = r'C:\Users\gamorais\Downloads\JOGA AQUI'

# Mover o arquivo
shutil.move(origem, destino)

print(f"Arquivo movido de {origem} para {destino}")
