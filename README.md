# Processador e Formatador de Pedidos CSV (CLI)

Um script de terminal em Python puro para ler, sanitizar e formatar relatórios de pedidos a partir de um arquivo `.csv`. Este projeto simula o fluxo inicial de **Higienização de Dados (Data Cleaning)** em ambiente comercial, tratando inconsistências como números em formato brasileiro (vírgula), espaços extras e campos ausentes.

## Funcionalidades Atuais

- **Leitura estruturada em dicionário:** utiliza o módulo nativo `csv.DictReader` para ler arquivos delimitados por ponto e vírgula (`;`), mapeando o cabeçalho automaticamente para fácil acesso às colunas.
- **Sanitização de strings:** aplicação de `.strip()` para remover espaços em branco nas extremidades e `.capitalize()` para padronizar os nomes dos clientes.
- **Conversão de tipos (casting):** tratamento do formato numérico brasileiro (`replace(",", ".")`) para conversão segura de texto para `float`.
- **Tratamento de dados ausentes:** verificação condicional inline para identificar campos de peso não preenchidos, exibindo `"Sem peso"` em vez de falhar a execução.
- **Exibição tabular formatada:** organização da saída no terminal em colunas alinhadas usando especificadores de largura em *f-strings* (`:<12`, `:>15`, etc.) e a função `format()`.

## *Feats* Futuras

- [ ] **Cálculo de total do pedido:** multiplicar o peso pelo valor por kg para obter o valor final de cada compra.
- [ ] **Filtragem por status:** Exibir apenas pedidos com determinado status (ex: `"Pendente"`, `"Entregue"`).
- [ ] **Exportação de base limpa:** salvar os registros higienizados em um novo arquivo.

## Pré-requisitos

Para rodar este projeto, você precisa apenas do **Python 3.x** instalado. Não é necessária a instalação de bibliotecas de terceiros.

## Como clonar e executar para uso próprio

1. Abra o seu terminal (ou Git Bash).
2. Clone este repositório:
   ```bash
   git clone https://github.com/nathanmontt/analise_vendas.git
   ```
3. Certifique-se de que o arquivo `pedidos.csv` está na mesma pasta e execute:
   ```bash
   python analise_vendas.py
   ```