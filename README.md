# 📋 Controle PCI Concursos

Uma aplicação web para gerenciar e acompanhar concursos públicos do site PCI Concursos com sistema de classificação pessoal.

## 🎯 Características

- ✅ Scraper automático dos concursos do PCI Concursos
- ✅ Interface responsiva (mobile-first)
- ✅ Classificação de concursos em 3 status
- ✅ Filtros por região, UF, status e busca textual
- ✅ Notas pessoais para cada concurso
- ✅ Dados persistentes (SQLite local ou PostgreSQL)
- ✅ Hospedagem gratuita no Render
- ✅ Código organizado para adicionar login depois

## 📋 Pré-requisitos

- Python 3.9+
- pip (gerenciador de pacotes Python)
- Git

## 🚀 Instalação Local

### 1. Clonar o repositório

```bash
git clone <seu-repositorio>
cd pci-concursos
```

### 2. Criar ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o .env com suas configurações
# Por padrão, usa SQLite local
```

### 5. Executar a aplicação

```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`

### 6. Primeira atualização

Clique no botão "🔄 Atualizar do PCI" para fazer o scraping inicial dos concursos.

## 📱 Uso

### Filtros
- **Status**: Filtra por "Ainda não classificados", "Vou ver de novo" ou "Tire da minha lista"
- **Região**: Filtra por Nacional, Sudeste, Sul, Norte, Nordeste, Centro-Oeste ou Últimas
- **UF**: Filtra por estado
- **Busca**: Procura no título, órgão ou UF
- **Ocultar removidos**: Esconde concursos marcados como "Tire da minha lista"

### Ações por concurso
- **Mudar status**: Use os 3 botões na parte inferior do card
- **Adicionar notas**: Clique em "✏️ Notas" para editar observações pessoais
- **Abrir no PCI**: Clique em "🔗 PCI" para abrir a página original em nova aba
- **Atualizar**: Clique em "🔄 Atualizar do PCI" para fazer scraping dos concursos atualizados

## 🐘 Usando PostgreSQL Localmente

Se quiser testar com PostgreSQL localmente:

1. Instale PostgreSQL
2. Crie um banco de dados:
```sql
CREATE DATABASE pci_concursos;
```

3. Configure o `.env`:
```
DATABASE_URL=postgresql://usuario:senha@localhost:5432/pci_concursos
```

4. Execute a aplicação normalmente

## 🌐 Hospedagem no Render (Gratuito)

### Pré-requisitos
- Conta no Render (https://render.com) - gratuita
- Conta no Supabase (https://supabase.com) - gratuita com limite generoso
- Código no GitHub

### Passo 1: Preparar GitHub

```bash
# Inicializar git (se não estiver)
git init
git add .
git commit -m "Initial commit: Controle PCI Concursos"

# Criar repositório no GitHub e fazer push
git remote add origin https://github.com/seu-usuario/pci-concursos.git
git branch -M main
git push -u origin main
```

### Passo 2: Criar banco de dados no Supabase

1. Acesse https://supabase.com
2. Clique em "New Project"
3. Preencha os dados:
   - Nome do projeto: `pci-concursos`
   - Database Password: Escolha uma senha forte (salve!)
   - Region: Escolha uma próxima a você
4. Espere o banco ser criado (leva alguns minutos)
5. Vá para **Settings → Database** e copie a **Connection string** (modo URI)

### Passo 3: Deploy no Render

1. Acesse https://render.com e faça login
2. Clique em **+ New** → **Web Service**
3. Conecte seu repositório GitHub
4. Configure:
   - **Name**: `controle-pci-concursos`
   - **Runtime**: `Python 3.11`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - **Plan**: Free (gratuito)

5. Adicione as variáveis de ambiente:
   - **FLASK_ENV**: `production`
   - **DATABASE_URL**: Cola a string do Supabase aqui

6. Clique em **Deploy**

Seu site estará pronto em alguns minutos!

## 📱 Acessar pelo Celular

Após fazer deploy no Render, você terá um URL como:
```
https://controle-pci-concursos.onrender.com
```

Abra este URL no navegador do seu celular e adicione à tela inicial:
- **iOS**: Safari → Compartilhar → Adicionar à Tela Inicial
- **Android**: Chrome → Menu → Instalar app

## 🔧 Estrutura do Projeto

```
pci-concursos/
├── app.py                 # Aplicação Flask principal
├── config.py              # Configurações (dev/prod)
├── models.py              # Modelos SQLAlchemy
├── scraper.py             # Web scraper do PCI
├── requirements.txt       # Dependências Python
├── Procfile              # Para Render
├── render.yaml           # Config avançada do Render
├── .env.example          # Exemplo de variáveis
├── .gitignore            # Arquivos ignorados pelo Git
├── README.md             # Este arquivo
├── static/
│   ├── css/
│   │   └── style.css     # Estilos CSS
│   └── js/
│       └── script.js     # JavaScript (reservado)
└── templates/
    ├── base.html         # Template base
    └── index.html        # Página principal
```

## 🔄 Como funciona o Scraper

1. O scraper acessa as 7 páginas do PCI Concursos
2. Extrai informações: título, órgão, UF, cargo, escolaridade, vagas, prazo
3. Verifica se o concurso já existe (por link)
4. Se for novo: adiciona com status "Ainda não classificados"
5. Se existir: atualiza dados, mas **preserva** status e notas pessoais

### Páginas rastreadas
- Nacional
- Sudeste
- Sul
- Norte
- Nordeste
- Centro-Oeste
- Últimas

## 🛡️ Segurança

- ✅ Sem login nesta versão (planejado para v2)
- ✅ Dados pessoais (status, notas) nunca são sobrescritos
- ✅ Estrutura de código pronta para adicionar autenticação
- ✅ Proteção contra duplicatas por URL
- ✅ Tratamento de erros no scraper

## 🚨 Tratamento de Erros do Scraper

Se o PCI mudar a estrutura HTML, o scraper:

1. **Tentará múltiplos seletores CSS** (resultado-item, concurso, article, div.item)
2. **Não quebrará a aplicação** - continua funcionando com dados existentes
3. **Logará os erros** para debug
4. **Preservará dados anteriores**

Para corrigir em caso de mudanças:
1. Abra o navegador e inspecione a página do PCI
2. Identifique os novos seletores CSS
3. Atualize as linhas no `scraper.py` que fazem `find()` e `find_all()`
4. Faça um commit e push para atualizar no Render

## 📊 Estatísticas

O dashboard mostra:
- Total de concursos
- Concursos não classificados
- Concursos para revisar (destacado)
- Concursos removidos

## 🎨 Customizações

### Alterar cores
Edite o `:root` no `static/css/style.css`:
```css
:root {
    --primary: #2563eb;      /* Azul principal */
    --warning: #ea580c;      /* Laranja */
    --danger: #dc2626;       /* Vermelho */
    /* ... mais cores ... */
}
```

### Alterar nome da aplicação
Edite `navbar-title` em `templates/base.html` e o `<title>` no HTML.

## 🤝 Adicionar Login Depois

A estrutura já suporta adicionar autenticação:

1. Instale Flask-Login: `pip install Flask-Login`
2. Crie um modelo `User` em `models.py`
3. Adicione middleware de autenticação em `app.py`
4. Proteja as rotas com `@login_required`
5. Adicione templates de login/registro

## 📞 Troubleshooting

### Erro de conexão ao banco
- ✅ SQLite: Verifique permissões da pasta
- ✅ PostgreSQL: Teste a string de conexão com `psql`
- ✅ Render: Vá a **Settings → Environment** e verifique `DATABASE_URL`

### Scraper não funciona
- ✅ Verifique se consegue acessar pciconcursos.com.br manualmente
- ✅ Verifique logs: `app.py` imprime mensagens de erro
- ✅ Pode ser timeout - execute de novo

### Site carrega lento
- ✅ No Render gratuito, pode ter delay ao acordar (cold start)
- ✅ Clique no link de novo ou espere 30 segundos
- ✅ Primeiro acesso do dia é mais lento (normal)

## 📝 Licença

MIT - Use livremente!

## 🚀 Próximas melhorias

- [ ] Autenticação com login/senha
- [ ] Múltiplos usuários com dados separados
- [ ] Notificações quando novos concursos chegam
- [ ] Agendamento automático do scraper
- [ ] Exportar para Excel/PDF
- [ ] Integração com calendários
- [ ] Sugestões baseadas em histórico

---

**Dúvidas?** Abra uma issue no GitHub ou revise os logs da aplicação.

Boa sorte nos concursos! 🎯
