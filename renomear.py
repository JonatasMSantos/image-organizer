import os

# Pasta onde os arquivos estão localizados
pasta_origem = 'C:\\Users\\jonatas.santos.GRUPOMEMORIAL\\Downloads\\PESSOAS\\ARRUMAR'

# Função para renomear os arquivos
def renomear_arquivos(pasta):
    for nome_arquivo in os.listdir(pasta):
        caminho_arquivo_antigo = os.path.join(pasta, nome_arquivo)

        # Verificar se o arquivo começa com um dos prefixos
        if nome_arquivo.startswith(('IMG-', 'VID_', 'VID-')):
            # Remover o prefixo do nome do arquivo
            novo_nome_arquivo = nome_arquivo.lstrip('IMG-').lstrip('VID-')

            # Construir o caminho para o novo nome do arquivo
            caminho_arquivo_novo = os.path.join(pasta, novo_nome_arquivo)

            # Renomear o arquivo
            os.rename(caminho_arquivo_antigo, caminho_arquivo_novo)
            print(f"Arquivo renomeado: {nome_arquivo} -> {novo_nome_arquivo}")

# Chamar a função para renomear arquivos na pasta de origem
renomear_arquivos(pasta_origem)