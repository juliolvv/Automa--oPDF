<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta charset="utf-8" />
  <meta name="generator" content="pandoc" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  <title>-</title>
</head>
<body>
<h1 id="pdfautomation">PDFAutomation</h1>
<p>O <strong>PDFAutomation</strong> é um script em
<strong>Python</strong> desenvolvido para mesclar automaticamente vários
arquivos PDF em um único documento final.<br />
Ele percorre uma pasta contendo arquivos PDF, organiza-os em ordem
alfabética e cria um novo arquivo consolidado.</p>
<hr />
<h2 id="funcionalidades">Funcionalidades</h2>
<ul>
<li>Lê automaticamente todos os arquivos PDF dentro da pasta
<code>Documents/</code></li>
<li>Mescla os arquivos em uma única sequência</li>
<li>Gera um arquivo final nomeado como <code>PDF Final.pdf</code></li>
<li>Ordena os arquivos em ordem alfabética antes da fusão</li>
</ul>
<hr />
<h2 id="como-funciona">Como funciona</h2>
<p>O script utiliza a biblioteca <strong>PyPDF2</strong> para realizar a
fusão dos arquivos.<br />
O processo básico é o seguinte:</p>
<ol type="1">
<li>Ler todos os arquivos da pasta <code>Documents/</code></li>
<li>Filtrar apenas os PDFs</li>
<li>Adicionar cada PDF ao objeto <code>PdfMerger</code></li>
<li>Gerar o arquivo final na raiz do projeto</li>
</ol>
<hr />
<h2 id="estrutura-do-projeto">Estrutura do Projeto</h2>
<pre><code>PDFAutomation/
│
├── Documents/
│   ├── arquivo1.pdf
│   ├── arquivo2.pdf
│   └── ...
│
├── PDFAutomation.py
└── PDF Final.pdf  (gerado automaticamente)</code></pre>
<hr />
<h2 id="requisitos">Requisitos</h2>
<ul>
<li>Python 3.x<br />
</li>
<li>Biblioteca PyPDF2</li>
</ul>
<p>Instale a dependência com o comando:</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="ex">pip</span> install PyPDF2</span></code></pre></div>
<hr />
<h2 id="como-usar">Como usar</h2>
<ol type="1">
<li><p>Crie uma pasta chamada <code>Documents</code> no mesmo diretório
do script.<br />
</p></li>
<li><p>Adicione dentro dela todos os arquivos <code>.pdf</code> que
deseja unir.<br />
</p></li>
<li><p>Execute o script:</p>
<div class="sourceCode" id="cb3"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="ex">python</span> PDFAutomation.py</span></code></pre></div></li>
<li><p>O arquivo <code>PDF Final.pdf</code> será gerado automaticamente
na pasta principal.</p></li>
</ol>
<hr />
<h2 id="observações">Observações</h2>
<ul>
<li>Certifique-se de que os nomes dos arquivos estejam em ordem
alfabética se quiser controlar a sequência.<br />
</li>
<li>O nome da pasta deve ser exatamente <code>Documents</code>
(respeitando maiúsculas e minúsculas).</li>
</ul>
<hr />
<h2 id="autor">Autor</h2>
<p><strong>Júlio César</strong><br />
Projeto acadêmico e experimental em Python.</p>
</body>
</html>
