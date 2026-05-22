import os
os.environ['FLASK_ENV'] = 'development'

from app import app, db
from models import Concurso
from scraper import scrape_pci_concursos

print("Iniciando scraping de todas as páginas do PCI...")
with app.app_context():
    db.create_all()
    result = scrape_pci_concursos(db, Concurso)
    print(f"\n✅ CONCLUÍDO!")
    print(f"   Novos:       {result['novos']}")
    print(f"   Atualizados: {result['atualizados']}")
    print(f"   Total:       {result['total']}")

    # Mostrar amostra
    print("\n=== AMOSTRA DOS PRIMEIROS 5 CONCURSOS ===")
    for c in Concurso.query.limit(5).all():
        print(f"  [{c.regiao.upper()}] {c.titulo}")
        print(f"    Vagas: {c.vagas} | Prazo: {c.prazo} | UF: {c.uf}")
        print(f"    Link:  {c.link}")
        print()
