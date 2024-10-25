# RenomeadorPDF

## Descrição
O **RenomeadorPDF** é um script em Python criado para automatizar a renomeação de arquivos PDF. Esse projeto foi desenvolvido para facilitar a organização de documentos, onde cada PDF é recebido com um nome genérico e precisa ser renomeado com base no número de protocolo contido dentro do próprio arquivo. O script analisa cada PDF em uma pasta especificada, extrai o número de protocolo e renomeia o arquivo automaticamente.

Este script é particularmente útil para quem lida com grandes volumes de documentos PDF e precisa manter uma organização rigorosa baseada em informações internas dos arquivos.

## Funcionalidades
- Analisa uma pasta designada contendo arquivos PDF.
- Busca o número de protocolo dentro de cada PDF.
- Renomeia os arquivos PDF com base no número de protocolo encontrado.
- Permite alterar o caminho da pasta de destino diretamente no script.

## Tecnologias Utilizadas
- `os`: Para manipulação de arquivos e diretórios.
- `glob`: Para busca de padrões de arquivos dentro de pastas.
- `re`: Para trabalhar com expressões regulares e localizar o número do protocolo.
- `PyPDF2`: Para extrair texto dos arquivos PDF.
- `time`: Para pausas e temporizações durante a execução do script.

## Pré-requisitos
- Python 3.x instalado.
- As bibliotecas PyPDF2 precisam estar instaladas. Você pode instalá-la com o comando:
    ```bash
    pip install PyPDF2
    ```

## Instalação
1. Clone este repositório ou faça o download dos arquivos:
    ```bash
    git clone https://github.com/seu-usuario/renomeadorpdf.git
    ```

2. Certifique-se de que o Python 3.x está instalado em seu sistema.

3. Instale as dependências necessárias com:
    ```bash
    pip install -r requirements.txt
    ```

## Como Executar
1. Abra o prompt de comando no diretório onde o script está localizado.

2. Execute o script com o Python:
    ```bash
    python RenomeadorPDF.py
    ```

3. O script irá processar todos os arquivos PDF na pasta especificada, renomeando-os de acordo com o número de protocolo encontrado dentro de cada PDF. Se necessário, altere o caminho da pasta diretamente no script.

## Personalização
- O caminho da pasta onde os PDFs estão armazenados pode ser modificado dentro do código.
- Certifique-se de que os PDFs estão corretamente formatados para que o número de protocolo possa ser identificado via expressões regulares.

## Licença
Este projeto está licenciado sob a [Licença MIT](./LICENSE) - sinta-se à vontade para usá-lo, modificá-lo e distribuí-lo conforme as permissões da licença.

---

**Autor:** Daniel Bittencourt  
- [![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/danielbittenc)
- [![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/danibittenc/)
- [![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://x.com/smashpump)
