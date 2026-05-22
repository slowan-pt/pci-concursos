# 📂 Estrutura Completa do Projeto

```
pci-concursos/
│
├── 🐍 ARQUIVOS PYTHON (Backend)
│   ├── app.py                      # Aplicação Flask principal
│   │   ├── Importações e setup
│   │   ├── Rotas HTTP (GET/PUT/POST)
│   │   ├── Endpoints da API
│   │   └── Inicialização
│   │
│   ├── config.py                   # Configurações por ambiente
│   │   ├── Config base
│   │   ├── DevelopmentConfig (SQLite local)
│   │   ├── ProductionConfig (PostgreSQL)
│   │   └── TestingConfig (em memória)
│   │
│   ├── models.py                   # Modelos SQLAlchemy
│   │   ├── db = SQLAlchemy()
│   │   ├── Classe Concurso
│   │   │   ├── id, titulo, orgao, uf...
│   │   │   ├── regiao, link, status...
│   │   │   ├── notas, data_encontrado...
│   │   │   ├── data_atualizacao
│   │   │   └── Método encontrar_por_link()
│   │   └── Índices e relacionamentos
│   │
│   ├── scraper.py                  # Web scraper do PCI
│   │   ├── PAGES (7 URLs do PCI)
│   │   ├── HEADERS (User-Agent)
│   │   ├── extrair_concurso()
│   │   │   ├── Extrai title, orgao, uf...
│   │   │   ├── Tenta múltiplos seletores CSS
│   │   │   └── Retorna dict com dados
│   │   ├── scrape_pci_concursos()
│   │   │   ├── Loop em cada página
│   │   │   ├── Faz requests com timeout
│   │   │   ├── Parse com BeautifulSoup
│   │   │   ├── Busca duplicatas por link
│   │   │   ├── Insere novos ou atualiza
│   │   │   └── Retorna estatísticas
│   │   └── Tratamento de erros
│   │
│   └── wsgi.py                     # Entry point para produção
│       └── Cria tabelas e inicia app
│
├── 📄 ARQUIVOS DE CONFIGURAÇÃO
│   ├── requirements.txt             # Dependências Python
│   │   ├── Flask==3.0.0
│   │   ├── Flask-SQLAlchemy==3.1.1
│   │   ├── Requests==2.31.0
│   │   ├── beautifulsoup4==4.12.2
│   │   ├── gunicorn==21.2.0
│   │   ├── python-dotenv==1.0.0
│   │   └── psycopg2-binary==2.9.9
│   │
│   ├── Procfile                     # Comando para Render
│   │   └── web: gunicorn app:app...
│   │
│   ├── render.yaml                  # Config avançada (opcional)
│   │   ├── Web service settings
│   │   └── Database settings
│   │
│   ├── .env.example                 # Variáveis de exemplo
│   │   ├── FLASK_ENV=development
│   │   ├── DATABASE_URL= (vazio = SQLite)
│   │   └── FLASK_DEBUG=False
│   │
│   └── .gitignore                   # Arquivos ignorados
│       ├── __pycache__/
│       ├── *.pyc, *.db
│       ├── venv/, env/
│       ├── .env
│       └── .DS_Store
│
├── 📖 DOCUMENTAÇÃO
│   ├── README.md                    # Documentação completa (5000+ palavras)
│   │   ├── Características
│   │   ├── Pré-requisitos
│   │   ├── Instalação local
│   │   ├── Uso (filtros, ações)
│   │   ├── PostgreSQL localmente
│   │   ├── Deploy no Render (passo a passo)
│   │   ├── Acessar pelo celular
│   │   ├── Estrutura do projeto
│   │   ├── Como funciona o scraper
│   │   ├── Segurança
│   │   ├── Customizações
│   │   ├── Troubleshooting
│   │   └── Próximas melhorias
│   │
│   ├── QUICKSTART.md                # Guia rápido (2-5 minutos)
│   │   ├── Rodar localmente
│   │   ├── Hospedar gratuitamente
│   │   ├── Estrutura de pastas
│   │   ├── Troubleshooting rápido
│   │   └── URLs importantes
│   │
│   ├── DEPLOY_GUIDE.md              # Guia passo a passo (15-20 minutos)
│   │   ├── Preparar código para GitHub
│   │   ├── Criar banco no Supabase
│   │   ├── Deploy no Render
│   │   ├── Usar a aplicação
│   │   ├── Manutenção e atualizações
│   │   ├── Resolver problemas
│   │   ├── Monitoramento
│   │   └── Checklist final
│   │
│   ├── ESTRUTURA.md                 # Este arquivo
│   │   └── Descrição de cada arquivo
│   │
│   └── SCRAPER_GUIDE.md             # Como ajustar o scraper
│       ├── Entender a estrutura atual
│       ├── Inspecionar novo HTML
│       ├── Encontrar seletores
│       ├── Atualizar scraper.py
│       └── Testar e fazer commit
│
├── 🌐 TEMPLATES HTML (Frontend)
│   ├── templates/
│   │   ├── base.html                # Template base
│   │   │   ├── <!DOCTYPE html>
│   │   │   ├── <head> (meta, CSS)
│   │   │   ├── <header> navbar
│   │   │   │   ├── Título "Controle PCI Concursos"
│   │   │   │   ├── Data última atualização
│   │   │   │   └── Botão "Atualizar do PCI"
│   │   │   ├── <main> {% block content %}
│   │   │   ├── <footer>
│   │   │   └── {% block scripts %}
│   │   │
│   │   └── index.html               # Página principal
│   │       ├── {% extends "base.html" %}
│   │       ├── Seção de filtros
│   │       │   ├── Status dropdown
│   │       │   ├── Região dropdown
│   │       │   ├── UF dropdown
│   │       │   ├── Busca textual
│   │       │   └── Checkbox ocultar removidos
│   │       │
│   │       ├── Seção de estatísticas
│   │       │   ├── Total de concursos
│   │       │   ├── Não classificados
│   │       │   ├── Vou ver de novo (highlight)
│   │       │   └── Removidos
│   │       │
│   │       ├── Container de concursos
│   │       │   └── Renderizado dinamicamente via JS
│   │       │
│   │       ├── Template de card de concurso
│   │       │   ├── Header (título, órgão, badges)
│   │       │   ├── Body (dados do concurso)
│   │       │   ├── Notas pessoais
│   │       │   ├── Botões de status
│   │       │   └── Link para PCI
│   │       │
│   │       ├── Modal de notas
│   │       │   ├── Textarea para edição
│   │       │   ├── Botão Salvar
│   │       │   └── Botão Cancelar
│   │       │
│   │       ├── Toast de notificações
│   │       │   └── Mensagens de sucesso/erro
│   │       │
│   │       └── <script> com toda a lógica JavaScript
│   │           ├── DOM manipulation
│   │           ├── Fetch API calls
│   │           ├── Event listeners
│   │           ├── Formatação de dados
│   │           └── Interação com backend
│   │
│   └── (base.html não renderiza conteúdo direto)
│
└── 🎨 ARQUIVOS ESTÁTICOS
    └── static/
        ├── css/
        │   └── style.css             # Todo o CSS da aplicação
        │       ├── Reset (*{})
        │       ├── Variáveis CSS (:root)
        │       ├── body e html
        │       ├── .navbar (header sticky)
        │       ├── .navbar-container, .navbar-title
        │       ├── .container (main content)
        │       ├── .filters-section
        │       ├── .filters-grid, .filter-group
        │       ├── .filter-select, .filter-input
        │       ├── .stats-section, .stat-item
        │       ├── .concursos-container
        │       ├── .concurso-card
        │       │   ├── .concurso-header
        │       │   ├── .concurso-body
        │       │   ├── .concurso-notes
        │       │   ├── .concurso-footer
        │       │   ├── .status-btn (3 variações)
        │       │   ├── Cores por status (.status-1, .status-2, .status-3)
        │       │   └── Hover effects
        │       │
        │       ├── .modal (edit notas)
        │       │   ├── .modal-header
        │       │   ├── .modal-body
        │       │   └── .modal-footer
        │       │
        │       ├── .toast (notificações)
        │       ├── .btn-primary, .btn-secondary
        │       ├── .badge-*, .badge-uf
        │       ├── @media queries (responsivo)
        │       │   ├── tablet (768px)
        │       │   └── mobile (480px)
        │       │
        │       └── Dark/Light mode ready
        │
        └── js/
            └── script.js             # JavaScript extra (reservado)
                └── (Todo JS está em index.html <script>)
```

---

## Fluxo de Dados

### 1. Carregamento Inicial
```
User abre browser
    ↓
GET / (app.py:index())
    ↓
Renderiza index.html (com <script>)
    ↓
document.addEventListener('DOMContentLoaded')
    ↓
carregarConcursos() → fetch /api/concursos
    ↓
app.py:get_concursos() → query database
    ↓
JSON response
    ↓
renderizarConcursos() → cria cards dinâmicos
```

### 2. Mudar Status de Concurso
```
User clica botão "Vou ver de novo"
    ↓
mudarStatus(btn, status)
    ↓
fetch PUT /api/concursos/{id}/status
    ↓
app.py:update_status() → db.session.commit()
    ↓
Atualiza UI localmente
    ↓
Toast "Status atualizado!"
    ↓
carregarStats() → atualiza widget stats
```

### 3. Scraper Manual
```
User clica botão "🔄 Atualizar do PCI"
    ↓
scrapeNow() → fetch POST /api/scrape
    ↓
app.py:scrape()
    ↓
scraper.scrape_pci_concursos(db, Concurso)
    ↓
Para cada URL em PAGES:
    - requests.get() com timeout
    - BeautifulSoup parse
    - extrair_concurso() para cada item
    - Verifica duplicata por link
    - Insert ou Update
    ↓
Retorna JSON {novos, atualizados, total}
    ↓
mostrarToast("✅ 5 novos, 12 atualizados")
    ↓
carregarConcursos() → refresh view
```

---

## Tecnologias Utilizadas

| Camada | Tecnologia | Versão | Função |
|--------|-----------|--------|--------|
| **Backend** | Python | 3.9+ | Linguagem |
| | Flask | 3.0.0 | Framework web |
| | SQLAlchemy | 2.0.23 | ORM |
| | Flask-SQLAlchemy | 3.1.1 | Integração |
| **Scraper** | Requests | 2.31.0 | HTTP requests |
| | BeautifulSoup | 4.12.2 | Parse HTML |
| **Banco** | SQLite | Built-in | Local |
| | PostgreSQL | 13+ | Produção |
| | psycopg2 | 2.9.9 | Driver PG |
| **Hospedagem** | Gunicorn | 21.2.0 | App server |
| | Render | - | PaaS |
| | Supabase | - | DBaaS |
| **Frontend** | HTML5 | - | Markup |
| | CSS3 | - | Estilos |
| | Vanilla JS | ES6 | Interatividade |
| | Bootstrap | - | Não usado (CSS próprio) |

---

## Banco de Dados - Schema

### Tabela: concursos

```sql
CREATE TABLE concursos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    
    -- Dados do concurso (do PCI)
    titulo VARCHAR(255) NOT NULL,
    orgao VARCHAR(255),
    uf VARCHAR(2) INDEX,
    regiao VARCHAR(50) NOT NULL INDEX,
    link VARCHAR(500) UNIQUE,
    cargos TEXT,
    escolaridade VARCHAR(100),
    vagas VARCHAR(100),
    prazo VARCHAR(100),
    
    -- Dados pessoais
    status VARCHAR(50) DEFAULT 'Ainda não classificados' INDEX,
    notas TEXT DEFAULT '',
    
    -- Timestamps
    data_encontrado DATETIME DEFAULT CURRENT_TIMESTAMP INDEX,
    data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### Índices
- `id` (PK)
- `titulo` (busca textual)
- `uf` (filtro)
- `regiao` (filtro)
- `status` (filtro)
- `link` (evitar duplicatas)
- `data_encontrado` (ordenação)

---

## Ambiente

### Development
- SQLite local: `pci_concursos.db`
- Debug: ON
- Host: localhost:5000
- Reloader: ON

### Production (Render)
- PostgreSQL via Supabase
- Debug: OFF
- Host: 0.0.0.0:PORT (Render injeta PORT)
- Workers: 2 (gunicorn)
- Timeout: 60s

---

## Segurança

- ✅ HTTPS (automático no Render)
- ✅ Sem SQL injection (SQLAlchemy ORM)
- ✅ Sem XSS (Jinja2 escapa HTML)
- ✅ CSRF: Desativado (formulário sem sessão)
- ✅ No cookie sensitive info
- ✅ Database não exposto (credenciais via ENV)

---

## Performance

- **Browser cache**: Estáticos (CSS/JS) cacheados
- **Lazy loading**: Cards renderizados sob demanda
- **Paginação**: Não implementada (< 1000 registros é rápido)
- **Índices**: Banco otimizado para buscas
- **Gzip**: Render comprime automaticamente
- **CDN**: Não necessário (assets pequenos)

---

## Escalabilidade Futura

Para crescer além do free tier:
1. **Banco**: Upgrade Supabase (pago)
2. **Servidor**: Upgrade Render (pago) ou Heroku, Railway
3. **Cache**: Redis (session cache)
4. **Auth**: JWT + refresh tokens
5. **API**: Rate limiting
6. **Logs**: CloudWatch, DataDog
7. **Monitoring**: Sentry (error tracking)
