import requests
from bs4 import BeautifulSoup

url = 'https://www.pciconcursos.com.br/concursos/nacional/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'}
r = requests.get(url, headers=headers, timeout=15)
soup = BeautifulSoup(r.content, 'html.parser')

# Achar o primeiro link de concurso e mostrar o HTML do elemento pai
concurso_links = [a for a in soup.find_all('a', href=True) if '/noticias/' in a['href']]
print(f"Total links de noticias: {len(concurso_links)}")

if concurso_links:
    first = concurso_links[0]
    print("\n=== PRIMEIRO LINK ===")
    print(f"TEXT: {first.get_text(strip=True)}")
    print(f"HREF: {first['href']}")

    # Subir até 5 níveis de pai e mostrar o HTML
    parent = first.parent
    for i in range(5):
        classes = ' '.join(parent.get('class', []))
        print(f"\n=== PAI NÍVEL {i+1}: <{parent.name} class='{classes}'> ===")
        print(parent.prettify()[:1000])
        print("...")
        parent = parent.parent
        if parent is None:
            break
