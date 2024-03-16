from PIL import Image

def diminuir_tamanho_imagem(entrada, saida, qualidade=85):
    # Abre a imagem
    imagem = Image.open(entrada)

    # Salva a imagem com qualidade ajustada
    imagem.save(saida, optimize=True, quality=qualidade)

# Caminho da i
# Diretório de entrada e saída
diretorio_entrada = r'C:\Users\gusta\OneDrive\Documentos\GitHub\gocode\api\static\betolanches'
diretorio_saida = r'C:\Users\gusta\OneDrive\Documentos\GitHub\gocode\api\static\betolanches\novo'

# Qualidade da compactação (de 0 a 100)
qualidade = 15

# Compactar imagens
diminuir_tamanho_imagem(diretorio_entrada, diretorio_saida, qualidade)
