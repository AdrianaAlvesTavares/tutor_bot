MODULES = {
    "introducao": {
        "title": "🗄️ Introdução a Banco de Dados",
        "text": (
            "Um banco de dados é um sistema organizado para armazenar, "
            "gerenciar e recuperar informações de forma eficiente.\n\n"
            "Conceitos fundamentais:\n"
            "• BD (Banco de Dados): coleção organizada de dados relacionados\n"
            "• SGBD: Software que gerencia o banco (MySQL, PostgreSQL, SQLite)\n"
            "• Tabela: estrutura que organiza dados em linhas e colunas\n"
            "• Registro: uma linha da tabela (um dado completo)\n"
            "• Campo: uma coluna da tabela (um atributo)\n\n"
            "Tipos de bancos de dados:\n"
            "• Relacional: dados em tabelas com relacionamentos (SQL)\n"
            "• Não-relacional: documentos, chave-valor, grafos (NoSQL)"
        ),
        "example": (
            "Tabela: alunos\n"
            "+----+----------+-------+\n"
            "| id | nome     | nota  |\n"
            "+----+----------+-------+\n"
            "| 1  | Ana      | 8.5   |\n"
            "| 2  | Bruno    | 7.0   |\n"
            "| 3  | Carla    | 9.2   |\n"
            "+----+----------+-------+\n"
            "Cada linha = 1 registro\n"
            "Cada coluna = 1 campo"
        ),
        "order": 1
    },
    "sql_basico": {
        "title": "📝 SQL Básico",
        "text": (
            "SQL (Structured Query Language) é a linguagem padrão para "
            "interagir com bancos de dados relacionais.\n\n"
            "Os 4 comandos essenciais (CRUD):\n"
            "• SELECT: consulta/lê dados da tabela\n"
            "• INSERT: insere novos registros\n"
            "• UPDATE: atualiza registros existentes\n"
            "• DELETE: remove registros\n\n"
            "Cláusulas importantes:\n"
            "• WHERE: filtra os registros\n"
            "• ORDER BY: ordena o resultado\n"
            "• LIMIT: limita a quantidade de resultados"
        ),
        "example": (
            "-- Consultar todos os alunos\n"
            "SELECT * FROM alunos;\n\n"
            "-- Filtrar por nota\n"
            "SELECT nome, nota FROM alunos\n"
            "WHERE nota >= 7.0\n"
            "ORDER BY nota DESC;\n\n"
            "-- Inserir novo aluno\n"
            "INSERT INTO alunos (nome, nota)\n"
            "VALUES ('Daniel', 8.0);\n\n"
            "-- Atualizar nota\n"
            "UPDATE alunos SET nota = 9.0\n"
            "WHERE nome = 'Bruno';\n\n"
            "-- Remover registro\n"
            "DELETE FROM alunos WHERE id = 3;"
        ),
        "order": 2
    },
    "modelagem": {
        "title": "🔗 Modelagem e Relacionamentos",
        "text": (
            "Modelagem de dados é o processo de definir a estrutura "
            "do banco antes de criá-lo.\n\n"
            "Conceitos de chaves:\n"
            "• Chave Primária (PK): identifica unicamente cada registro\n"
            "• Chave Estrangeira (FK): referencia a PK de outra tabela\n"
            "• Chave única: não permite valores duplicados\n\n"
            "Tipos de relacionamento:\n"
            "• 1:1 — um registro se relaciona com exatamente um outro\n"
            "• 1:N — um registro se relaciona com vários outros\n"
            "• N:M — vários registros se relacionam com vários outros\n\n"
            "Integridade referencial: garante que uma FK sempre "
            "aponte para um registro que existe na tabela pai."
        ),
        "example": (
            "-- Tabela pai\n"
            "CREATE TABLE cursos (\n"
            "    id   INTEGER PRIMARY KEY,\n"
            "    nome TEXT NOT NULL\n"
            ");\n\n"
            "-- Tabela filha com FK\n"
            "CREATE TABLE alunos (\n"
            "    id        INTEGER PRIMARY KEY,\n"
            "    nome      TEXT NOT NULL,\n"
            "    curso_id  INTEGER,\n"
            "    FOREIGN KEY (curso_id) REFERENCES cursos(id)\n"
            ");\n\n"
            "-- Relacionamento 1:N\n"
            "-- 1 curso pode ter N alunos\n"
            "-- 1 aluno pertence a 1 curso"
        ),
        "order": 3
    }
}