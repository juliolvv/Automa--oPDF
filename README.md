📚 PDFAutomation

O PDFAutomation é um script simples em Python desenvolvido para mesclar automaticamente vários arquivos PDF em um único documento final. Ele percorre uma pasta contendo PDFs, organiza-os em ordem alfabética e cria um novo arquivo consolidado.

🚀 Funcionalidades

🔍 Lê automaticamente todos os arquivos PDF dentro da pasta Documents/

🧩 Mescla os arquivos em uma única sequência

📑 Gera um arquivo final nomeado como PDF Final.pdf

⚙️ Ordena os arquivos em ordem alfabética antes da fusão

🧠 Como funciona

O script utiliza a biblioteca PyPDF2 para realizar a fusão dos arquivos.
O processo básico é:

Ler todos os arquivos da pasta Documents/

Filtrar apenas os PDFs

Adicionar cada PDF ao objeto PdfMerger

Gerar o arquivo final na raiz do projeto

📦 Estrutura do Projeto
📂 PDFAutomation/
├── 📂 Documents/
│   ├── arquivo1.pdf
│   ├── arquivo2.pdf
│   └── ...
├── PDFAutomation.py
└── PDF Final.pdf  ← (gerado automaticamente)

🧰 Requisitos

Python 3.x

Biblioteca PyPDF2

Instalação dos pacotes necessários:

pip install PyPDF2

▶️ Como usar

Crie uma pasta chamada Documents no mesmo diretório do script.

Adicione dentro dela todos os arquivos .pdf que deseja unir.

Execute o script:

python PDFAutomation.py


Após a execução, o arquivo PDF Final.pdf será gerado automaticamente na raiz do projeto.

⚠️ Observações

Certifique-se de que os nomes dos arquivos PDF estejam em ordem alfabética se quiser manter a sequência correta na fusão.

A pasta é sensível a maiúsculas/minúsculas no nome (Documents ≠ documents).

🧑‍💻 Autor

Júlio César
