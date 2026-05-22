import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.pciconcursos.com.br/concursos/nacional/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'}
r = requests.get(url, headers=headers, timeout=15)
soup = BeautifulSoup(r.content, 'html.parser')

# Filtrar apenas links de notícias com slug (não o menu)
concurso_links = [
    a for a in soup.find_all('a', href=True)
    if re.search(r'/noticias/[a-z0-9\-]+$', a['href'])
]

print(f"Total concursos encontrados: {len(concurso_links)}")
print()

# Mostrar HTML do pai de cada um dos 3 primeiros
for i, link in enumerate(concurso_links[:3]):
    print(f"=== CONCURSO {i+1} ===")
    print(f"TEXTO: {link.get_text(strip=True)}")
    print(f"HREF: {link['href']}")

    # Subir para encontrar o elemento container
    parent = link.parent
    for level in range(6):
        tag = parent.name
        classes = ' '.join(parent.get('class', []))
        pid = parent.get('id', '')
        all_text = parent.get_text(separator='|', strip=True)[:200]
        print(f"  [Nível {level}] <{tag} id='{pid}' class='{classes}'> TEXT: {all_text}")
        parent = parent.parent
        if parent is None or parent.name == 'body':
            break
    print()
