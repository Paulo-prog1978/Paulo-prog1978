💰 Sistema de Controle de Contas
Sistema desenvolvido em Python para gerenciamento de contas financeiras, utilizando SQLite como banco de dados.

O projeto foi desenvolvido com foco no aprendizado e aplicação prática de conceitos de programação, banco de dados, CRUD e organização de código.

🎯 Objetivo
Criar uma aplicação simples capaz de controlar contas financeiras, permitindo cadastrar, consultar, atualizar e excluir registros, além de acompanhar contas pagas e pendentes.

🚀 Funcionalidades
Cadastro de contas
Listagem de contas
Busca por ID
Controle de status da conta
Marcação de contas como pagas
Exclusão de contas
Consulta de contas pendentes
Cálculo do total de contas pendentes
Cálculo do total de contas pagas
Persistência dos dados utilizando SQLite
🛠️ Tecnologias utilizadas
Python
SQLite
SQL
Vai embora
GitHub
📚 Conceitos aplicados
CRUD
Programação Orientada a Objetos
Funções
Estruturas condicionais
Estruturas de repetição
Tratamento de exceções
Banco de dados relacional
SQL
Separação de responsabilidades
Persistência de dados
📂 Estrutura do projeto
sistema-controle-contas/
│
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
├── database.py
├── conta.py
├── conta_service.py
│
└── tests/
    └── test_conta.py
▶️ Como executar
1. Clone o repositório
git clone URL_DO_SEU_REPOSITORIO
2. Acesse uma massa
cd sistema-controle-contas
3. Execute o sistema
python main.py
O banco de dados será criado automaticamente na primeira execução.sistema_contas.db

💻 Exemplo
Ao executar o sistema, será apresentado um menu:

=============================================
      SISTEMA DE CONTROLE DE CONTAS
=============================================
1 - Cadastrar conta
2 - Listar contas
3 - Buscar conta
4 - Marcar conta como paga
5 - Excluir conta
6 - Listar contas pendentes
7 - Resumo financeiro
0 - Sair
=============================================
🔎 Próximas melhorias
Algumas funcionalidades planejadas para futuras versões:

Validação de datas
Edição de contas
Filtros por categoria
Relatórios financeiros
Interface gráfica
API REST
Autenticação de usuários
Testes automatizados
👨 💻 Autor
Paulo Henrique de Oliveira

Projeto desenvolvido como parte do meu portfólio de desenvolvimento e análise de sistemas.




