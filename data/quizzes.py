QUIZZES = {
    "introducao": [
        {
            "question": "O que é um SGBD?",
            "options": [
                "Uma linguagem de programação para bancos",
                "Um software que gerencia bancos de dados",
                "Um tipo de banco de dados não-relacional",
                "Uma tabela especial do banco"
            ],
            "answer": 1,
            "explanation": "SGBD é o Sistema Gerenciador de Banco de Dados — o software responsável por criar, manter e controlar o acesso aos dados. Exemplos: MySQL, PostgreSQL, SQLite."
        },
        {
            "question": "Como chamamos uma linha de uma tabela de banco de dados?",
            "options": ["Campo", "Atributo", "Registro", "Índice"],
            "answer": 2,
            "explanation": "Uma linha representa um registro — um conjunto completo de dados de uma entidade. Uma coluna representa um campo (atributo)."
        },
        {
            "question": "Qual é a diferença entre banco relacional e não-relacional?",
            "options": [
                "Relacional usa arquivos de texto; não-relacional usa tabelas",
                "Relacional armazena dados em tabelas com relações; não-relacional usa outros modelos como documentos",
                "Relacional é mais moderno que o não-relacional",
                "Não há diferença prática entre eles"
            ],
            "answer": 1,
            "explanation": "Bancos relacionais organizam dados em tabelas ligadas por relacionamentos e usam SQL. Bancos não-relacionais (NoSQL) usam modelos alternativos como documentos JSON, pares chave-valor ou grafos."
        }
    ],
    "sql_basico": [
        {
            "question": "Qual comando SQL é usado para consultar dados em uma tabela?",
            "options": ["GET", "FETCH", "SELECT", "READ"],
            "answer": 2,
            "explanation": "SELECT é o comando de consulta do SQL. GET, FETCH e READ não são comandos SQL padrão."
        },
        {
            "question": "O que a cláusula WHERE faz em uma query SQL?",
            "options": [
                "Ordena os resultados",
                "Limita a quantidade de resultados",
                "Filtra os registros por uma condição",
                "Agrupa os resultados"
            ],
            "answer": 2,
            "explanation": "WHERE filtra os registros retornados pela query. Apenas os registros que satisfazem a condição são incluídos no resultado."
        },
        {
            "question": "Qual é a query correta para inserir um novo registro?",
            "options": [
                "INSERT alunos VALUES ('Ana', 9.0)",
                "INSERT INTO alunos (nome, nota) VALUES ('Ana', 9.0)",
                "ADD INTO alunos (nome, nota) VALUES ('Ana', 9.0)",
                "INSERT (nome, nota) IN alunos VALUES ('Ana', 9.0)"
            ],
            "answer": 1,
            "explanation": "A sintaxe correta é INSERT INTO tabela (colunas) VALUES (valores). As outras opções têm erros de sintaxe SQL."
        }
    ],
    "modelagem": [
        {
            "question": "O que é uma Chave Primária (PRIMARY KEY)?",
            "options": [
                "A primeira coluna de qualquer tabela",
                "Um campo que referencia outra tabela",
                "Um campo que identifica unicamente cada registro",
                "Uma coluna obrigatória chamada 'id'"
            ],
            "answer": 2,
            "explanation": "A Chave Primária identifica cada registro de forma única. Não pode ter valores repetidos nem nulos. Geralmente é um campo 'id', mas pode ser qualquer campo único."
        },
        {
            "question": "O que é uma Chave Estrangeira (FOREIGN KEY)?",
            "options": [
                "Uma chave primária de tabela internacional",
                "Um campo que referencia a chave primária de outra tabela",
                "Uma chave que criptografa os dados",
                "O segundo identificador único de uma tabela"
            ],
            "answer": 1,
            "explanation": "A Chave Estrangeira (FK) é um campo que aponta para a Chave Primária de outra tabela, criando um relacionamento entre elas."
        },
        {
            "question": "Um professor pode ter várias turmas, e cada turma pertence a um professor. Que tipo de relacionamento é esse?",
            "options": ["1:1", "N:M", "1:N", "0:N"],
            "answer": 2,
            "explanation": "É um relacionamento 1:N — um professor para muitas turmas. Se cada turma pudesse ter vários professores também, seria N:M."
        }
    ]
}