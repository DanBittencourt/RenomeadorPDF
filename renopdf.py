import os
import glob
import re
import PyPDF2
import time

# Define a pasta onde estão os arquivos PDF
pasta_pdf = r'C:\Users\Zito\Desktop\autorizacao_arquivo'

# Define a expressão regular para a palavra que deve ser procurada
padrao_procurado = r'protocolado sob o nº \d{10}'

# Loop pelos arquivos PDF
for arquivo_pdf in glob.glob(os.path.join(pasta_pdf, '*.pdf')):

    # Abre o arquivo PDF
    with open(arquivo_pdf, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)

        # Procura o padrão na primeira página
        page = pdf_reader.pages[0]
        texto = page.extract_text()
        match = re.search(padrao_procurado, texto)
        if match:

            # Obtém a palavra encontrada e renomeia o arquivo
            palavra_encontrada = match.group(0)
            # Extrai apenas os número e remove os 3 primeiros dígitos(sempre zero)
            numeros = re.search(r'\d{10}', palavra_encontrada).group(0)[3:]
            novo_nome = os.path.join(pasta_pdf, f"{numeros}.pdf")

            # Verifica se o novo nome já existe antes de renomear o arquivo
            if not os.path.exists(novo_nome):

                # Fecha o arquivo PDF
                f.close()

                # Verifica se o arquivo está sendo usado por outro processo
                tentativas = 0
                while True:
                    tentativas += 1
                    try:
                        os.rename(arquivo_pdf, novo_nome)
                        break
                    except OSError:
                        if tentativas < 10:  # limite de tentativas
                            print(
                                f"O arquivo {arquivo_pdf} está sendo usado por outro processo. Tentando novamente em 1 segundo...")
                            time.sleep(1)
                        else:
                            print(
                                f"Não foi possível renomear o arquivo {arquivo_pdf} após {tentativas} tentativas. Motivo: O Arquivo está sendo usado por outro processo.")
                            break
            else:
                print(f"O arquivo {novo_nome} já existe.")
        else:
            # Fecha o arquivo PDF
            f.close()
            print(
                f"Não foi possível encontrar o padrão no arquivo{arquivo_pdf}.")

print("Finalizado com sucesso.")
input("Pressione enter para sair")