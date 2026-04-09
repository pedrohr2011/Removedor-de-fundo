from rembg import remove
from PIL import Image
import os

def remover_fundo(caminho_entrada, caminho_saida):
    try:
        # Verifica se a imagem de entrada existe
        if not os.path.exists(caminho_entrada):
            print(f"Erro: O arquivo '{caminho_entrada}' não foi encontrado.")
            return

        print("Processando a imagem... (Isso pode levar alguns segundos)")
        
        # Abre a imagem original
        imagem_original = Image.open(caminho_entrada)
        
        # Remove o fundo usando a IA
        imagem_sem_fundo = remove(imagem_original)
        
        # Salva a nova imagem
        imagem_sem_fundo.save(caminho_saida)
        
        print(f"Sucesso! Imagem salva em: {caminho_saida}")
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# ==========================================
# USO DO SCRIPT
# ==========================================

# Nome da imagem que você quer remover o fundo (pode ser jpg, png, etc)
imagem_entrada = "" 

# Nome do arquivo de saída (DEVE ser .png para manter o fundo transparente)
imagem_saida = "foto_sem_fundo.png" 

# Chama a função
remover_fundo(imagem_entrada, imagem_saida)