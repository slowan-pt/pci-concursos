# 🔀 Guia: Git e GitHub para Iniciantes

Este guia ajuda você a colocar o código no GitHub para depois fazer deploy no Render.

## 📚 O que é Git?

**Git** = Sistema para rastrear mudanças no código (tipo "histórico" do Word, mas para programação)

**GitHub** = Site para armazenar repositórios Git online (como Google Drive do código)

## ⚙️ Instalação

### Windows

1. Acesse https://git-scm.com/download/win
2. Baixe o instalador
3. Execute e clique **Next** em tudo
4. Reinicie o PC

### macOS

```bash
# Instale via Homebrew
brew install git
```

### Linux

```bash
sudo apt-get install git
```

## 🎯 Configuração Inicial

Abra **PowerShell** (Windows) ou **Terminal** (Mac/Linux) e execute:

```bash
# Configure seu nome
git config --global user.name "Seu Nome Completo"

# Configure seu email (use o mesmo do GitHub!)
git config --global user.email "seu@email.com"

# Verifique
git config --global user.name
git config --global user.email
```

---

## 📖 Workflow Básico

### 1. Criar Repositório no GitHub

1. Vá para https://github.com/new
2. Faça login (ou crie conta em https://github.com)
3. Preencha:
   - **Repository name**: `pci-concursos`
   - **Description**: `Sistema para controlar concursos públicos do PCI`
   - **Public** (selecionado)
   - NÃO marque "Add .gitignore" ou "Add LICENSE" (vamos fazer manual)
4. Clique **Create repository**
5. Copie a URL HTTPS (ex: `https://github.com/seu-usuario/pci-concursos.git`)

### 2. Inicializar Git Localmente

```bash
# Navegue até a pasta do projeto
cd C:\Users\Sloan\Downloads\PCI

# Inicie git
git init

# Adicione todos os arquivos
git add .

# Faça o primeiro commit
git commit -m "Initial commit: Controle PCI Concursos v1.0"

# Configure repositório remoto (cole sua URL)
git remote add origin https://github.com/seu-usuario/pci-concursos.git

# Renomeie branch para 'main' (padrão novo do GitHub)
git branch -M main

# Envie para GitHub
git push -u origin main
```

Se funcionar, seu código está no GitHub! ✅

---

## 📝 Comandos Diários

### Ver Status

```bash
git status
# Mostra quais arquivos foram alterados
```

### Adicionar Mudanças

```bash
# Adicionar arquivo específico
git add app.py

# Adicionar todos os arquivos alterados
git add .
```

### Fazer Commit (salvar mudança)

```bash
git commit -m "Descrição clara da mudança"

# Exemplos bons:
# "Adicionar filtro por UF"
# "Corrigir bug do status"
# "Atualizar scraper para nova estrutura do PCI"
```

### Enviar para GitHub

```bash
git push origin main
```

### Ver Histórico

```bash
git log

# Mostra últimas mudanças
# Aperte 'q' para sair
```

---

## 🔄 Fluxo Completo: Fazendo Uma Mudança

### Situação: Você quer adicionar uma nova feature

```bash
# 1. Verifique status
git status

# 2. Faça as mudanças nos arquivos

# 3. Veja o que mudou
git status
git diff

# 4. Adicione os arquivos
git add .

# 5. Commit
git commit -m "Adicionar nova feature XYZ"

# 6. Push
git push origin main

# Feito! A mudança está no GitHub e Render faz redeploy
```

---

## 🌳 Entender Branches

**Branch** = "ramo" do código (como versões alternativas)

### Branch Principal

```bash
# 'main' é o branch principal (produção)
# Tudo que você faz aqui é enviado ao Render
```

### Criar Branch Para Feature

(Opcional, para quem quer mais controle)

```bash
# Criar novo branch
git checkout -b feature/novo-filtro

# Fazer mudanças...

# Adicionar e commit
git add .
git commit -m "Adicionar novo filtro"

# Push do branch
git push origin feature/novo-filtro

# No GitHub, fazer um Pull Request
# Depois fazer merge com main
```

Para simplificar, **sempre trabalhe em 'main'** enquanto for um desenvolvedor só.

---

## ⚠️ Problemas Comuns

### Erro: "fatal: not a git repository"

```bash
# Você não está numa pasta com git inicializado
# Solução: rode 'git init' na pasta certa
cd C:\Users\Sloan\Downloads\PCI
git init
```

### Erro: "fatal: pathspec 'file.txt' did not match any files"

```bash
# Você tentou adicionar arquivo que não existe
# Solução: verifique o caminho
ls  # Lista arquivos

# Ou adicione tudo
git add .
```

### Erro: "Please tell me who you are"

```bash
# Você não configurou user.name e user.email
# Solução:
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

### Erro ao fazer Push: "fatal: Authentication failed"

```bash
# Seu token de autenticação expirou
# Solução (Windows): Delete credenciais salvas
# Control Panel → Credential Manager → Windows Credentials
# Procure por 'git:https://github.com'
# Delete
# Próximo push vai pedir para logar novamente

# Ou use token de acesso (melhor)
# https://github.com/settings/tokens
# Gere novo token com 'repo' completo
# Use token no lugar da senha ao fazer push
```

---

## 🔐 Usar Token de Acesso (Recomendado)

GitHub não recomenda mais senhas. Use tokens:

### Passo 1: Gerar Token

1. Vá para https://github.com/settings/tokens
2. Clique **Generate new token (classic)**
3. Preencha:
   - **Note**: `git-cli`
   - **Expiration**: `90 days`
   - **Scopes**: Marque **repo** (completo)
4. Clique **Generate token**
5. **COPIE O TOKEN** (não consegue ver depois!)

### Passo 2: Usar Token no Git

```bash
# Próximo push vai pedir autenticação
git push origin main

# Coloque seu usuário do GitHub como user
# Coloque o TOKEN como password
```

---

## 🚀 Workflow com Render

### Automaticamente:

1. Você faz `git push origin main`
2. GitHub notifica Render
3. Render detecta mudança
4. Render faz rebuild automático (~2 min)
5. Seu site é atualizado!

**Não precisa fazer nada além de push.**

---

## 📊 Ver Mudanças no GitHub

1. Vá para https://github.com/seu-usuario/pci-concursos
2. Veja histórico em **Commits**
3. Veja branches em **Branches**
4. Veja código em **Code**

---

## 🔍 Útil: .gitignore

Este arquivo já está criado. Ele faz Git ignorar:

- Pasta `venv/` (ambiente virtual)
- Arquivo `.env` (variáveis sensíveis)
- `__pycache__/` (cache Python)
- `*.db` (banco de dados local)

**Nunca commite:**
- Senhas
- Tokens
- Arquivos muito grandes
- `.env` com dados reais

---

## 📝 Boas Práticas de Commit

### ✅ Mensagens Boas

```
"Adicionar botão de atualizar scraper"
"Corrigir bug no filtro por UF"
"Melhorar responsividade mobile"
"Atualizar scraper para nova estrutura do PCI"
```

### ❌ Mensagens Ruins

```
"abc"
"fix"
"mudanças"
"wtf"
```

**Regra**: Descreva **O QUÊ** foi feito, não **COMO**.

---

## 🎓 Recursos Extras

- **GitHub Learning**: https://github.github.io/training-kit/
- **Atlassian Git Tutorial**: https://www.atlassian.com/git
- **Pro Git Book**: https://git-scm.com/book/en/v2

---

## ✅ Checklist: Primeiro Push

- [ ] Git instalado?
- [ ] User e email configurados?
- [ ] Repositório criado no GitHub?
- [ ] Pasta inicializada com `git init`?
- [ ] Arquivos adicionados com `git add .`?
- [ ] Primeiro commit feito com `git commit -m "..."`?
- [ ] Remote adicionado com `git remote add origin`?
- [ ] Branch renomeado para main?
- [ ] Push feito com `git push -u origin main`?
- [ ] Código aparece no GitHub?

✅ Se tudo OK, você está pronto para o deploy no Render!

---

**Dúvida?** Procure por "Git tutorial português" ou veja https://rogerdudler.github.io/git-guide/index.pt_BR.html
