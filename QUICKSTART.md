# ⚡ Guia Rápido - Controle PCI Concursos

## Rodar Localmente (2 minutos)

```bash
# 1. Clone ou baixe os arquivos
cd pci-concursos

# 2. Crie ambiente virtual
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

# 3. Instale dependências
pip install -r requirements.txt

# 4. Execute
python app.py

# 5. Abra no navegador
# http://localhost:5000
```

## Hospedar Gratuitamente (5 minutos)

### 1️⃣ Banco de Dados (Supabase)
1. Vá para https://supabase.com
2. Crie novo projeto
3. Copie a **Connection String** (Settings → Database)

### 2️⃣ Servidor (Render)
1. Vá para https://render.com
2. **New Web Service** → conecte GitHub
3. Configure:
   ```
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app --bind 0.0.0.0:$PORT
   ```
4. Adicione variável de ambiente:
   ```
   DATABASE_URL = (cole aqui a string do Supabase)
   FLASK_ENV = production
   ```
5. Deploy!

Seu site estará pronto em ~3 minutos em um URL como:
```
https://seu-app.onrender.com
```

## Arquivo de Estrutura

```
pci-concursos/
│
├── 📄 app.py                    # App principal (rotas e lógica)
├── 📄 config.py                 # Configurações (dev/prod/test)
├── 📄 models.py                 # Modelo da base de dados
├── 📄 scraper.py                # Web scraper do PCI
├── 📄 wsgi.py                   # Entry point para produção
│
├── 📋 requirements.txt           # Dependências Python
├── 📋 Procfile                   # Comando para Render
├── 📋 render.yaml                # Config avançada (opcional)
├── 📋 .env.example               # Exemplo de variáveis
├── 📋 .gitignore                 # Arquivos ignorados
│
├── 📖 README.md                  # Documentação completa
├── 📖 QUICKSTART.md              # Este arquivo
├── 📖 DEPLOY_GUIDE.md            # Guia passo a passo
│
├── 📁 templates/
│   ├── base.html                 # Template base
│   └── index.html                # Página principal
│
└── 📁 static/
    ├── css/
    │   └── style.css             # Estilos
    └── js/
        └── script.js             # JavaScript extra
```

## Troubleshooting Rápido

| Problema | Solução |
|----------|---------|
| `ModuleNotFoundError: No module named 'flask'` | Ative venv e rode `pip install -r requirements.txt` |
| `SQLite database is locked` | Feche todas as instâncias da app e delete `pci_concursos.db` |
| Site lento no Render | Normal! Free tier faz "cold start". Recarregue após 30s |
| Scraper não retorna dados | Verifique internet. PCI pode estar fora do ar |
| `DATABASE_URL` não funciona | Copie EXATAMENTE a string. Não adicione `postgresql+psycopg2://` |

## URLs Importantes

- **Supabase**: https://supabase.com
- **Render**: https://render.com
- **GitHub**: https://github.com
- **PCI Concursos**: https://www.pciconcursos.com.br

## Próximos Passos

1. ✅ Rode localmente
2. ✅ Teste o scraper (botão "Atualizar do PCI")
3. ✅ Crie conta no Supabase e Render
4. ✅ Faça upload para GitHub
5. ✅ Deploy no Render
6. ✅ Compartilhe o link!

---

**Dúvida?** Leia o README.md completo.
