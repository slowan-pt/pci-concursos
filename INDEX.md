# 📚 Índice da Documentação

Bem-vindo! Escolha por onde começar:

## 🚀 Quer Começar JÁ?

→ **[QUICKSTART.md](QUICKSTART.md)** (5 minutos)
   - Rodar localmente
   - Hospedar gratuitamente

## 📖 Quer Entender Tudo?

→ **[README.md](README.md)** (20-30 minutos)
   - Descrição completa
   - Todas as features
   - FAQ e troubleshooting

## 🛠️ Quer Fazer Deploy Passo a Passo?

→ **[DEPLOY_GUIDE.md](DEPLOY_GUIDE.md)** (15-20 minutos)
   - GitHub (configurar código)
   - Supabase (banco de dados)
   - Render (servidor)
   - Instruções detalhadas

## 🔀 Quer Entender Git/GitHub?

→ **[GIT_GITHUB_GUIDE.md](GIT_GITHUB_GUIDE.md)** (10 minutos)
   - Instalação
   - Comandos básicos
   - Troubleshooting Git
   - Workflow com Render

## 📂 Quer Ver a Estrutura do Projeto?

→ **[ESTRUTURA.md](ESTRUTURA.md)** (15 minutos)
   - Árvore de arquivos
   - Descrição de cada arquivo
   - Fluxo de dados
   - Database schema
   - Tecnologias usadas

## 🔧 Quer Ajustar o Scraper?

→ **[SCRAPER_GUIDE.md](SCRAPER_GUIDE.md)** (15 minutos)
   - Como o scraper funciona
   - Como diagnosticar problemas
   - Como atualizar para nova estrutura do PCI
   - Testes e debugging

---

## 📋 Arquivos do Projeto

### Backend (Python)
- **app.py** - Aplicação Flask (rotas e lógica)
- **config.py** - Configurações (dev/prod/test)
- **models.py** - Modelo SQLAlchemy (banco de dados)
- **scraper.py** - Web scraper do PCI
- **wsgi.py** - Entry point para produção

### Configuração
- **requirements.txt** - Dependências Python
- **Procfile** - Comando para Render
- **render.yaml** - Configuração avançada (opcional)
- **.env.example** - Exemplo de variáveis
- **.gitignore** - Arquivos ignorados pelo Git

### Frontend (HTML/CSS/JS)
- **templates/base.html** - Template base
- **templates/index.html** - Página principal
- **static/css/style.css** - Estilos CSS
- **static/js/script.js** - JavaScript extra

---

## 🎯 Ordem Recomendada de Leitura

### Para Iniciante (30 min)
1. [QUICKSTART.md](QUICKSTART.md) - Teste localmente
2. [GIT_GITHUB_GUIDE.md](GIT_GITHUB_GUIDE.md) - Prepare GitHub
3. [DEPLOY_GUIDE.md](DEPLOY_GUIDE.md) - Deploy no Render

### Para Desenvolvedor (1h)
1. [README.md](README.md) - Entenda a app
2. [ESTRUTURA.md](ESTRUTURA.md) - Veja a arquitetura
3. [SCRAPER_GUIDE.md](SCRAPER_GUIDE.md) - Saiba como manter

### Para Manutenção (ongoing)
1. [SCRAPER_GUIDE.md](SCRAPER_GUIDE.md) - Se PCI mudar
2. [README.md](README.md) - Troubleshooting
3. Logs do Render - Ver o que está acontecendo

---

## 🚦 Guia Rápido: O que fazer

### "Quero rodar no meu PC agora"
```bash
# 1. Instale Python
# 2. Abra PowerShell na pasta
# 3. python -m venv venv
# 4. venv\Scripts\activate
# 5. pip install -r requirements.txt
# 6. python app.py
# 7. Abra http://localhost:5000
# Veja QUICKSTART.md para detalhes
```

### "Quero colocar online gratuitamente"
```
1. Leia DEPLOY_GUIDE.md (passo 1-3)
2. Crie conta Supabase
3. Crie conta Render
4. Faça deploy
5. Pronto! Seu site está online
```

### "O scraper parou de funcionar"
```
1. Leia SCRAPER_GUIDE.md
2. Inspecione o HTML do PCI (F12)
3. Atualize os seletores em scraper.py
4. Teste localmente
5. Commit e push
6. Render faz redeploy automaticamente
```

### "Quero adicionar uma feature"
```
1. Edite o código (app.py, templates, etc)
2. Teste localmente (python app.py)
3. git add . && git commit -m "descrição"
4. git push origin main
5. Render faz redeploy em 2-3 min
```

---

## 🔗 Links Importantes

| O quê | Onde |
|------|------|
| **Python** | https://www.python.org |
| **Flask Docs** | https://flask.palletsprojects.com |
| **SQLAlchemy** | https://www.sqlalchemy.org |
| **BeautifulSoup** | https://www.crummy.com/software/BeautifulSoup |
| **GitHub** | https://github.com |
| **Render** | https://render.com |
| **Supabase** | https://supabase.com |
| **PCI Concursos** | https://www.pciconcursos.com.br |

---

## ❓ FAQ Rápido

**P: Qual Python preciso?**
R: 3.9+, mas 3.11+ recomendado

**P: Preciso de banco PostgreSQL localmente?**
R: Não! SQLite funciona perfeitamente local. PostgreSQL é só para produção.

**P: Quanto custa hospedar?**
R: **R$ 0,00** no free tier (Render + Supabase)

**P: Quanto tempo leva deploy?**
R: ~2-3 minutos automático após push

**P: Posso editar o CSS/design?**
R: Sim! Edite `static/css/style.css`

**P: Posso adicionar mais campos ao banco?**
R: Sim! Edite `models.py` e o Render recria tabelas

**P: O site fica fora quando durmo?**
R: Pode ficar lento ("cold start") se não acessar por 15+ min, mas não desligava

**P: Preciso de login?**
R: Não nesta v1, mas o código está pronto para adicionar depois

**P: Posso ter múltiplos usuários?**
R: Sim! Adicione autenticação em v2 (veja [README.md](README.md))

---

## 📞 Precisa de Ajuda?

1. **Erro técnico?** → Veja o arquivo de documentação relevante
2. **Dúvida sobre deploy?** → [DEPLOY_GUIDE.md](DEPLOY_GUIDE.md)
3. **Dúvida sobre código?** → [ESTRUTURA.md](ESTRUTURA.md)
4. **Dúvida sobre scraper?** → [SCRAPER_GUIDE.md](SCRAPER_GUIDE.md)
5. **Dúvida sobre Git?** → [GIT_GITHUB_GUIDE.md](GIT_GITHUB_GUIDE.md)

---

**Pronto para começar?** Vá para [QUICKSTART.md](QUICKSTART.md)! 🚀
