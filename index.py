import os
import shutil
from datetime import datetime
from PIL import Image

# Função para obter a data de criação a partir dos metadados da imagem
def obter_data_de_criacao_de_metadados(caminho_arquivo):
    try:
        with Image.open(caminho_arquivo) as img:
            dados_exif = img._getexif()
            if dados_exif:
                data_str = dados_exif.get(36867)  # 36867 corresponde a DateTimeOriginal
                if data_str:
                    return datetime.strptime(data_str, '%Y:%m:%d %H:%M:%S')
    except Exception as e:
        print(f"Erro ao extrair metadados de {caminho_arquivo}: {e}")
    return None

# Função para obter o nome do mês a partir do número do mês
def nome_do_mes(numero_mes):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    return meses[numero_mes - 1]

# Pasta de origem
pasta_origem = 'C:\\Users\\jonatas.santos.GRUPOMEMORIAL\\Downloads\\PESSOAS'

# Iterar sobre os arquivos na pasta de origem
for nome_arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)

    # Verificar se o nome do arquivo contém uma data no formato YYYY/MM/DD
    formato_data = '%Y%m%d'
    try:
        data_a_partir_do_nome = datetime.strptime(nome_arquivo[:8], formato_data)
    except ValueError:
        data_a_partir_do_nome = None

    # Obter a data de criação a partir dos metadados, se disponível
    data_a_partir_de_metadados = obter_data_de_criacao_de_metadados(caminho_arquivo)

    # Escolher a data de criação com base nas preferências
    if data_a_partir_do_nome:
        data_a_utilizar = data_a_partir_do_nome
    elif data_a_partir_de_metadados:
        data_a_utilizar = data_a_partir_de_metadados
    else:
        # Se não for possível determinar a data de criação, usar a data de modificação do arquivo
        data_a_utilizar = datetime.fromtimestamp(os.path.getmtime(caminho_arquivo))

    # Criar a estrutura de pastas com base na data de criação com o nome do mês
    pasta_destino = os.path.join(
        pasta_origem,
        data_a_utilizar.strftime('%Y',) + '/' + nome_do_mes(data_a_utilizar.month) + '/' + data_a_utilizar.strftime('%d')
    )

    # Criar a pasta de destino, se ainda não existir
    os.makedirs(pasta_destino, exist_ok=True)

    # Mover o arquivo para a pasta de destino
    shutil.move(caminho_arquivo, os.path.join(pasta_destino, nome_arquivo))

print("Organização concluída.")
