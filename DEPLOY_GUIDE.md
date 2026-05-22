# 🚀 Guia Completo de Deploy - Controle PCI Concursos

## Visão Geral

Vamos hospedar tudo **gratuitamente**:
- **Banco de dados**: Supabase PostgreSQL (free tier)
- **Servidor**: Render (free tier)
- **Código**: GitHub (públicas grátis)

Custo total: **R$ 0,00**

## Passo 1: Preparar o Código para GitHub

### 1.1 Inicializar Git

```bash
# Entre na pasta do projeto
cd caminho\para\pci-concursos

# Inicie git
git init

# Adicione todos os arquivos
git add .

# Faça commit
git commit -m "Initial commit: Controle PCI Concursos v1.0"
```

### 1.2 Criar Repositório no GitHub

1. Abra https://github.com/new
2. Preencha:
   - **Repository name**: `pci-concursos`
   - **Description**: "Sistema para controlar concursos públicos do PCI"
   - **Public** (público - necessário para Render gratuito)
3. **Create Repository**
4. Copie o URL HTTPS (ex: `https://github.com/seu-usuario/pci-concursos.git`)

### 1.3 Fazer Push para GitHub

```bash
# Adicione o repositório remoto
git remote add origin https://github.com/seu-usuario/pci-concursos.git

# Configure a branch principal
git branch -M main

# Envie os arquivos
git push -u origin main
```

✅ Seu código está no GitHub!

---

## Passo 2: Criar Banco de Dados no Supabase

### 2.1 Criar Conta

1. Acesse https://supabase.com
2. Clique em **"Sign Up"**
3. Use email ou GitHub (recomendado GitHub)
4. Confirme no email

### 2.2 Criar Novo Projeto

1. No dashboard, clique em **"New Project"**
2. Preencha:
   - **Name**: `pci-concursos`
   - **Database Password**: Escolha algo forte (ex: `Abc#123XyZ$456`)
     - ⚠️ **SALVE ESTA SENHA** - você vai precisar
   - **Region**: Escolha próximo a você (ex: São Paulo → South America - São Paulo)
3. Clique **"Create new project"**
4. Aguarde ~2-3 minutos (mostra animação de carregamento)

### 2.3 Copiar String de Conexão

1. Quando pronto, clique em **"Settings"** (engrenagem, canto inferior esquerdo)
2. Vá para **"Database"** (menu lateral)
3. Na seção **"Connection string"**, copie a string **URI** (parece com isso):
```
postgresql://postgres.abcdefgh:sua_senha@aws-0-us-east-1.pooler.supabase.com:6543/postgres
```

✅ Salve esta string em um local seguro!

---

## Passo 3: Deploy no Render

### 3.1 Criar Conta no Render

1. Acesse https://render.com
2. Clique em **"Sign up"**
3. Use **GitHub** (recomendado)
   - Autorize Render acessar seus repositórios
   - Selecione **apenas** o repositório `pci-concursos`

### 3.2 Criar Web Service

1. No dashboard do Render, clique em **"New +"**
2. Selecione **"Web Service"**
3. Escolha seu repositório `pci-concursos`
4. Configure:

   | Campo | Valor |
   |-------|-------|
   | **Name** | `controle-pci-concursos` |
   | **Region** | `São Paulo` (recomendado) |
   | **Branch** | `main` |
   | **Runtime** | `Python 3.11` |
   | **Build Command** | `pip install -r requirements.txt` |
   | **Start Command** | `gunicorn app:app --bind 0.0.0.0:$PORT` |
   | **Plan** | `Free` |

5. Scroll down e clique em **"Advanced"**

### 3.3 Configurar Variáveis de Ambiente

Na seção **"Environment Variables"**, adicione:

```
FLASK_ENV = production
```

Clique em **"Add Environment Variable"**

```
DATABASE_URL = (cole aqui a string do Supabase - COMPLETA!)
```

⚠️ **IMPORTANTE**: Cole a string COMPLETA do Supabase, incluindo `postgresql://` no início e a senha

### 3.4 Deploy

1. Clique em **"Create Web Service"**
2. Aguarde ~2-3 minutos
3. Quando ficar verde com ✅, seu site está pronto!

O URL será algo como:
```
https://controle-pci-concursos.onrender.com
```

✅ **Seu site está online!**

---

## Passo 4: Usar a Aplicação

### 4.1 Primeira Visita

1. Abra o link: `https://controle-pci-concursos.onrender.com`
2. Pode estar lenta na primeira vez (Render acordando) - espere 20 segundos
3. Recarregue a página
4. Clique em **"🔄 Atualizar do PCI"** para fazer scraping inicial

### 4.2 No Celular

1. Abra o link no navegador do celular
2. A interface é responsiva e funciona perfeito
3. Para instalar como app:
   - **iPhone**: Toque em Compartilhar → Adicionar à Tela Inicial
   - **Android**: Menu do Chrome → Instalar App

---

## Passo 5: Manutenção e Atualizações

### 5.1 Fazer Alterações no Código

```bash
# Faça suas mudanças nos arquivos

# Commit
git add .
git commit -m "Descrição da mudança"

# Push
git push origin main
```

Render vai detectar automaticamente e fazer redeploy (~2 minutos).

### 5.2 Ver Logs

No dashboard do Render:
1. Clique em seu serviço
2. Abra a aba **"Logs"**
3. Veja erros ou mensagens da aplicação

### 5.3 Reimiciar o Serviço

No dashboard do Render:
1. Clique em seu serviço
2. Clique em **"Manual Deploy"** → **"Deploy latest commit"**

---

## Passo 6: Resolver Problemas

### Site não carrega

**Possível causa**: Cold start (Render gratuito adormece)
```
✅ Solução: Recarregue a página após 30 segundos
```

### Erro 502 Bad Gateway

**Possível causa**: Erro na aplicação ou banco offline
```
✅ Solução 1: Verifique os Logs no Render
✅ Solução 2: Verifique DATABASE_URL está correto
✅ Solução 3: Faça um manual deploy
```

### Scraper não funciona

**Possível causa**: PCI Concursos fora do ar ou mudança de estrutura
```
✅ Solução 1: Tente novamente em alguns minutos
✅ Solução 2: Verifique se pciconcursos.com.br está acessível
✅ Solução 3: Veja logs no Render para mensagens de erro
```

### Banco de dados cheio

**Possível causa**: Supabase free tem limite de armazenamento
```
✅ Solução: Limpe concursos antigos com SQL (raro acontecer)
```

### Erro ao fazer commit/push

```bash
# Se der erro de autenticação, use token de acesso
# Gere em https://github.com/settings/tokens
# Permissões: repo (completo)

git config --global user.email "seu@email.com"
git config --global user.name "Seu Nome"
git push
```

---

## Monitoramento Contínuo

### Supabase
- Vá em **"Home"** → **"Storage"** para ver uso de disco
- Vá em **"Query Editor"** para executar SQL direto
- Crie backups automáticos em **"Settings"** → **"Backups"**

### Render
- Configure **"Auto-Deploy"** em **"Settings"** (já vem ligado)
- Vá em **"Events"** para ver histórico de deploys
- Configure **"Email Notifications"** para saber quando cai

---

## Próximos Passos (Opcional)

### Adicionar Domínio Próprio

Render permite domínios customizados:
1. Compre um domínio (GoDaddy, Namecheap, etc)
2. No Render, vá em **"Settings"** → **"Custom Domain"**
3. Siga as instruções para apontar DNS

### Escalar para Mais Usuários

Se crescer, migre para:
- **Render Paid** (~$10/mês)
- **Supabase Paid** (~$25/mês)

Ou use Docker + Heroku, Railway, etc.

---

## Checklist Final

- [ ] Código no GitHub
- [ ] Banco no Supabase
- [ ] Web Service no Render
- [ ] DATABASE_URL configurada corretamente
- [ ] FLASK_ENV = production
- [ ] Site acessível via URL do Render
- [ ] Scraper testado (botão Atualizar)
- [ ] Funciona no celular

✅ **PRONTO! Seu app está no ar!**

---

## Suporte

Problemas?
1. Leia os logs (Render → Logs)
2. Verifique o README.md
3. Revise as variáveis de ambiente
4. Tente fazer um manual deploy

**Email Supabase**: support@supabase.com
**Email Render**: support@render.com

Boa sorte! 🚀
