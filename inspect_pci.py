import requests
from bs4 import BeautifulSoup

url = 'https://www.pciconcursos.com.br/concursos/nacional/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'}
r = requests.get(url, headers=headers, timeout=15)
soup = BeautifulSoup(r.content, 'html.parser')

print("=== STATUS ===")
print(f"HTTP {r.status_code}, {len(r.content)} bytes")

print("\n=== PRIMEIROS ELEMENTOS COM CLASSE ===")
seen = set()
for tag in soup.find_all(True, limit=200):
    classes = ' '.join(tag.get('class', []))
    key = f"{tag.name}.{classes}"
    if classes and key not in seen:
        seen.add(key)
        text = tag.get_text(strip=True)[:60]
        print(f"<{tag.name} class='{classes}'> {text}")

print("\n=== LINKS DE CONCURSOS ===")
for a in soup.find_all('a', href=True):
    href = a['href']
    text = a.get_text(strip=True)[:80]
    if '/concurso/' in href or '/noticias/' in href:
        print(f"HREF: {href}")
        print(f"TEXT: {text}")
        print("---")
