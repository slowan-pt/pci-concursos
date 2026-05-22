# 🔧 Guia: Ajustar o Scraper se o PCI Mudar

Se o PCI Concursos alterar a estrutura do site, o scraper pode parar de funcionar. Este guia ajuda a diagnosticar e corrigir.

## ⚡ Quick Fix (Teste Primeiro)

O scraper **já tenta múltiplos seletores CSS**. Se não funcionar:

1. Acesse https://www.pciconcursos.com.br/concursos/nacional/
2. Abra DevTools (F12)
3. Veja se consegue visualizar concursos

Se sim → o scraper deveria pegar. Se não → o PCI pode estar fora.

---

## 📊 Entender o Scraper Atual

### Estrutura do scraper.py

```python
PAGES = {
    'nacional': 'https://www.pciconcursos.com.br/concursos/nacional/',
    # ... mais 6 URLs
}

def extrair_concurso(item, regiao, url_page):
    # Tenta encontrar: titulo, orgao, uf, cargos, escolaridade, vagas, prazo
    # Tenta múltiplos seletores (class, id, tag)
    # Retorna dict com dados extraídos

def scrape_pci_concursos(db, Concurso):
    # Para cada página
    # Faz request com timeout
    # Parse com BeautifulSoup
    # Extrai concursos
    # Insert ou Update no banco
```

### Seletores Atuais

O scraper tenta encontrar concursos com:

```python
items = soup.find_all(class_='resultado-item')  # Primeiro try
if not items:
    items = soup.find_all(class_='concurso')     # Segundo try
if not items:
    items = soup.find_all('article')             # Terceiro try
if not items:
    items = soup.find_all('div', class_='item')  # Quarto try
```

E dentro de cada item, tenta extrair com:

```python
titulo_elem = item.find('a', class_='result')
orgao_elem = item.find(class_='orgao')
uf_elem = item.find(class_='uf')
# ... etc
```

---

## 🔍 Diagnosticar o Problema

### Passo 1: Inspecionar o HTML Atual

1. Abra https://www.pciconcursos.com.br/concursos/nacional/
2. Pressione **F12** (ou Ctrl+Shift+I)
3. Vá para **Inspector** / **Elements**
4. Procure por um **card de concurso**

Exemplo de estrutura esperada:

```html
<div class="resultado-item">
    <a class="result" href="...">Nome do Concurso</a>
    <span class="orgao">Nome do Órgão</span>
    <span class="uf">SP</span>
    <td>Cargo</td>
    <td>Escolaridade</td>
    ...
</div>
```

### Passo 2: Anotar a Nova Estrutura

Se for diferente, anote:

- ❓ Qual é a **classe/id** do container do concurso?
- ❓ Qual é a **classe/id** do título?
- ❓ Qual é a **classe/id** do órgão?
- ❓ Qual é a **classe/id** do UF?
- ❓ Onde estão cargo, escolaridade, vagas, prazo?

---

## ✏️ Atualizar o Scraper

### Cenário 1: Mudou o seletor do container

**Antes:**
```python
items = soup.find_all(class_='resultado-item')
```

**Novo seletor:** `class='card-concurso'`

**Depois:**
```python
items = soup.find_all(class_='resultado-item')
if not items:
    items = soup.find_all(class_='card-concurso')  # ← Adicione esta linha
if not items:
    items = soup.find_all(class_='concurso')
# ... resto do código
```

### Cenário 2: Mudou o seletor do título

**Antes:**
```python
titulo_elem = item.find('a', class_='result')
```

**Novo HTML:**
```html
<h2 class="titulo-concurso">
    <a href="...">Nome</a>
</h2>
```

**Depois:**
```python
titulo_elem = item.find('a', class_='result')
if not titulo_elem:
    titulo_h2 = item.find('h2', class_='titulo-concurso')
    if titulo_h2:
        titulo_elem = titulo_h2.find('a')  # ← Adicione esta lógica
```

### Cenário 3: Reorganizou as informações

**Antes:**
```html
<td>Escolaridade</td>
<td>Ensino Médio</td>
```

**Novo HTML:**
```html
<div data-field="education">Ensino Médio</div>
```

**Depois:**
```python
escolaridade_elem = item.find(data_field='education')
if escolaridade_elem:
    escolaridade = escolaridade_elem.get_text(strip=True)
```

---

## 🧪 Testar as Mudanças

### Teste 1: Localmente

```bash
# Edite scraper.py

# Abra Python interativo
python

# Teste o scraper
from scraper import scrape_pci_concursos
from models import db, Concurso
result = scrape_pci_concursos(db, Concurso)
print(result)
# Deve retornar: {'novos': X, 'atualizados': Y, 'total': Z}
```

### Teste 2: Rodar a app

```bash
python app.py

# Abra http://localhost:5000
# Clique em "Atualizar do PCI"
# Deve mostrar concursos novos
```

### Teste 3: Verificar Logs

Se der erro, veja os logs:

```bash
# Terminal mostra mensagens do scraper
# Procure por linhas com "Erro ao acessar" ou "Erro ao processar"
```

---

## 🚀 Fazer Commit e Deploy

Após testar localmente:

```bash
# Commitr as mudanças
git add scraper.py
git commit -m "Atualizar scraper para nova estrutura do PCI"
git push origin main

# Render fará deploy automaticamente (2-3 min)

# Teste no site ao vivo
# https://seu-app.onrender.com
```

---

## 📚 Referência: Seletores BeautifulSoup

### Encontrar por classe

```python
# Uma classe
item = soup.find(class_='resultado-item')

# Múltiplas classes
item = soup.find(class_='card resultado')

# Class que contém texto
item = soup.find(class_=lambda x: x and 'resultado' in x)
```

### Encontrar por ID

```python
item = soup.find(id='main-content')
```

### Encontrar por atributo customizado

```python
item = soup.find(attrs={'data-field': 'education'})
item = soup.find('div', {'data-id': '123'})
```

### Encontrar por texto

```python
# Exato
item = soup.find('h3', string='Concurso Público')

# Contém
item = soup.find('h3', string=lambda s: 'Concurso' in s)
```

### Combinar seletores

```python
# E
item = soup.find('div', class_='resultado-item', id='item-1')

# Ou (múltiplas tentativas)
item = soup.find('a', class_='result')
if not item:
    item = soup.find('a', class_='titulo')
```

### CSS Selector (mais avançado)

```python
# Se preferir, use select() com CSS selectors
items = soup.select('div.resultado-item')
items = soup.select('div#main > article.card')
items = soup.select('div[data-field="concurso"]')
```

---

## 🆘 Problemas Comuns

### Erro: "Nenhum concurso encontrado"

**Causa**: Seletor não corresponde

**Solução**:
```bash
# Copie o HTML real da página
# Abra Python e teste:
from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.pciconcursos.com.br/concursos/nacional/')
soup = BeautifulSoup(r.content, 'html.parser')

# Print o HTML raw para inspecionar
print(soup.prettify()[:2000])

# Procure manualmente por divs/articles/classes que parecem concursos
```

### Erro: "Extrai concurso vazio"

**Causa**: Seletor encontra elemento, mas está vazio

**Solução**:
```python
# Adicione prints de debug
def extrair_concurso(item, regiao, url_page):
    titulo = None
    titulo_elem = item.find('a', class_='result')
    if titulo_elem:
        titulo = titulo_elem.get_text(strip=True)
        print(f"Título encontrado: {titulo}")  # ← Debug
    else:
        print(f"Nenhum título encontrado neste item")  # ← Debug
```

### Erro: "Timeout ao acessar PCI"

**Causa**: PCI muito lento ou você sem internet

**Solução**:
```python
# Aumentar timeout (em scraper.py)
response = requests.get(url, headers=HEADERS, timeout=15)  # Era 10, agora 15
```

### Erro: "Nenhuma classe 'resultado-item' encontrada"

**Causa**: PCI mudou o nome da classe

**Solução**:
1. Use DevTools para copiar a classe nova
2. Adicione nova tentativa em `scraper.py`
3. Teste localmente
4. Faça commit

---

## 🔗 Recursos Úteis

- **DevTools Inspector**: F12 no navegador
- **BeautifulSoup Docs**: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- **CSS Selectors**: https://www.w3schools.com/cssref/selectors_attr_contains.php
- **Regex para parsing**: https://docs.python.org/3/library/re.html

---

## 📋 Checklist de Troubleshooting

- [ ] Página do PCI carrega normalmente?
- [ ] F12 mostra HTML do concurso?
- [ ] Você copiou o seletor certo?
- [ ] Testou localmente com `python app.py`?
- [ ] Viu mensagem de sucesso na console?
- [ ] Concursos aparecem na interface?
- [ ] Fez commit e push?
- [ ] Render fez redeploy?
- [ ] Esperou 2-3 minutos?
- [ ] Recarregou a página no Render?

---

## 💡 Dicas Pro

1. **Salve estruturas antigas**: Keep a backup do HTML que funcionava
2. **Use git branches**: `git checkout -b fix/scraper-update` antes de mexer
3. **Logs são seu amigo**: `logger.error()` ajuda a debugar no Render
4. **Teste em dev primeiro**: Nunca commita sem testar localmente
5. **Versionamento**: Increment `__version__` em mudanças significativas

---

**Precisa de ajuda?** Veja os logs no Render (Settings → Logs) ou rode localmente com `python -m pdb app.py`.
