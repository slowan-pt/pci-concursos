import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.pciconcursos.com.br/concursos/nacional/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'}
r = requests.get(url, headers=headers, timeout=15)
soup = BeautifulSoup(r.content, 'html.parser')

# Pegar HTML completo do primeiro ca e na
for cls in ['ca', 'na']:
    div = soup.find('div', class_=cls)
    if div:
        print(f"=== DIV CLASS='{cls}' HTML COMPLETO ===")
        print(div.prettify())
        print()

# Ver como os grupos de UF estão organizados dentro de #concursos
concursos_div = soup.find('div', id='concursos')
if concursos_div:
    print("=== ESTRUTURA RAIZ DE #concursos ===")
    # Mostrar filhos diretos
    for child in concursos_div.children:
        if hasattr(child, 'name') and child.name:
            classes = ' '.join(child.get('class', []))
            cid = child.get('id', '')
            print(f"  <{child.name} id='{cid}' class='{classes}'> {child.get_text(strip=True)[:80]}")
