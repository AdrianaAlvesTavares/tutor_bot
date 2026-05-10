# 🤖 Tutor Bot — Banco de Dados

## Sobre o projeto

Este projeto foi desenvolvido como trabalho acadêmico.
O objetivo é criar um bot educacional no Telegram capaz de ensinar conceitos de BD de forma interativa,
com módulos de conteúdo, quizzes e um assistente de inteligência artificial para tirar dúvidas.

## Equipe

| Nome | GitHub |
|---|---|
| Adriana Alves | [@adrianatavares](https://github.com/adrianatavares) |
| Arlana Braga | — |
| Bianca Peres | — |
| Fernanda Hipólito | — |
| Italo Feitosa | — |
| Patricia Ferreira | — |
| Sabrina Frazão | — |

---

## 🤖 Tutor Bot — Banco de Dados

Bot do Telegram para ensino de Banco de Dados com módulos de conteúdo, quizzes e assistente de IA (Gemini).

**Funcionalidades:**
- 📚 Módulos de conteúdo — Introdução a BD, SQL Básico, Modelagem e Relacionamentos
- 🎯 Quiz por módulo — 3 questões com feedback e explicação
- 💬 Assistente de IA — Dúvidas respondidas via Gemini 2.5 Flash
- 🛡️ Moderação automática — Aviso progressivo para mensagens fora do contexto

---

## 👤 Para usuários (alunos do grupo)

Você **não precisa instalar nada**. O bot já está rodando num servidor.

1. Abra o Telegram
2. Pesquise pelo nome do bot ou acesse o link compartilhado
3. Envie `/start` e use o menu

---

## 🚀 Para quem vai fazer o deploy (colocar o bot no ar)

> Faça isso **uma vez**. Depois o bot fica rodando 24h sem precisar deixar o computador ligado.

### Pré-requisitos

- Conta no [GitHub](https://github.com) com este repositório
- Conta no [Railway](https://railway.app) (gratuito — entrar com o GitHub)
- Token do bot Telegram → crie via [@BotFather](https://t.me/BotFather) no Telegram (`/newbot`)
- Chave da IA → crie em [aistudio.google.com](https://aistudio.google.com) → **Get API key**

### Passo a passo

**1. Suba o projeto no GitHub**

Se ainda não fez, crie um repositório no GitHub e suba o projeto.

**2. Acesse o Railway e crie um novo projeto**

- Acesse [railway.app](https://railway.app) e faça login com sua conta GitHub
- Clique em **New Project → Deploy from GitHub repo**
- Selecione este repositório

**3. Configure as variáveis de ambiente**

No painel do Railway, vá em **Variables** e adicione:

| Variável | Valor |
|---|---|
| `TELEGRAM_TOKEN` | Token gerado pelo BotFather |
| `GEMINI_KEY` | Chave gerada no Google AI Studio |
| `BOT_TOPIC` | `Banco de Dados` (ou o tema que preferir) |

> Nunca coloque essas chaves no código ou no GitHub. Apenas no painel do Railway.

**4. Faça o deploy**

- Railway detecta o `Procfile` automaticamente e executa `python3 main.py`
- Acompanhe os logs — você verá `✅ Banco de dados inicializado` quando estiver no ar
- Pronto. O bot fica rodando 24h, mesmo com o computador desligado

**5. Compartilhe o link do bot com o grupo**

No Telegram, o link do bot é sempre `t.me/nome_do_seu_bot`.

---

## 🛠️ Para desenvolvedores (rodar localmente e contribuir)

### Pré-requisitos

- Python **3.8**
- Token do Telegram e chave do Gemini (veja seção acima)

### Instalação

**1. Clone o repositório**

```bash
git clone https://github.com/seu-usuario/tutor_bot.git
cd tutor_bot
```

**2. Crie e ative o ambiente virtual**

```bash
python3.8 -m venv .venv
source .venv/bin/activate       # Linux / macOS
.venv\Scripts\activate          # Windows
```

**3. Instale as dependências**

```bash
pip install python-telegram-bot==21.6 python-dotenv requests
```

**4. Configure as variáveis de ambiente**

```bash
cp .env.example .env
```

Edite o `.env` com suas chaves:

```
TELEGRAM_TOKEN=seu_token_aqui
GEMINI_KEY=sua_chave_aqui
BOT_TOPIC=Banco de Dados
```

> O `.env` está no `.gitignore` e nunca deve ser commitado.

**5. Execute**

```bash
python3 main.py
```

Na primeira execução você verá `✅ Banco de dados inicializado`. O bot estará disponível no Telegram.

### Estrutura do projeto

```
tutor_bot/
├── .env.example                # template de variáveis de ambiente
├── config.py                   # carrega .env e exporta constantes
├── main.py                     # ponto de entrada — registra handlers e inicia polling
├── Procfile                    # instrução de execução para o Railway
│
├── database/
│   ├── schema.sql              # DDL das tabelas users e quiz_sessions
│   └── db.py                   # funções de acesso ao SQLite
│
├── data/
│   ├── content.py              # conteúdo dos 3 módulos
│   └── quizzes.py              # 9 questões (3 por módulo)
│
├── services/
│   ├── user_service.py         # lógica de usuário: status, infrações, bloqueio
│   ├── moderation_service.py   # detecção de mensagens inapropriadas / off-topic
│   └── ai_service.py           # integração com Gemini via HTTP
│
└── handlers/
    ├── menu_handler.py         # /start e callbacks do menu principal
    ├── content_handler.py      # exibição dos módulos de conteúdo
    ├── quiz_handler.py         # fluxo completo de quiz
    └── moderation_handler.py   # mensagens livres + pipeline de moderação
```

### Banco de dados

O arquivo `tutor.db` (SQLite) é criado automaticamente ao iniciar. Está no `.gitignore`.

**Tabela `users`**

| Coluna | Tipo | Descrição |
|---|---|---|
| `user_id` | INTEGER PK | ID do usuário no Telegram |
| `username` | TEXT | Username do Telegram |
| `warn_count` | INTEGER | Número de infrações (0–3) |
| `status` | TEXT | `active` / `warned` / `blocked_partial` / `blocked` |
| `created_at` | DATETIME | Data do primeiro acesso |

**Tabela `quiz_sessions`**

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER PK | Auto-incremento |
| `user_id` | INTEGER FK | Referência ao usuário |
| `module_id` | TEXT | ID do módulo (`introducao`, `sql_basico`, `modelagem`) |
| `total_q` | INTEGER | Total de questões |
| `correct_q` | INTEGER | Questões corretas |
| `completed_at` | DATETIME | Data de conclusão |

### Sistema de moderação

| Situação | Resultado |
|---|---|
| `warn_count = 1` → `status = warned` | Aviso 1/2 — IA ainda disponível |
| `warn_count = 2` → `status = blocked_partial` | Aviso 2/2 — IA bloqueada |
| `warn_count = 3` → `status = blocked` | Bloqueio total |

Palavras proibidas: `config.py` → `BLACKLIST_WORDS`
Padrões off-topic: `services/moderation_service.py` → `OFF_TOPIC_PATTERNS`

### Observações técnicas

- Python **3.8** — sem `X | Y` em type hints, sem `asyncio.to_thread`
- Integração com IA via HTTP direto (`requests` + `loop.run_in_executor`)
- Banco SQLite local — não requer servidor de banco de dados
