import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PAGES = {
    'nacional':    'https://www.pciconcursos.com.br/concursos/nacional/',
    'sudeste':     'https://www.pciconcursos.com.br/concursos/sudeste/',
    'sul':         'https://www.pciconcursos.com.br/concursos/sul/',
    'norte':       'https://www.pciconcursos.com.br/concursos/norte/',
    'nordeste':    'https://www.pciconcursos.com.br/concursos/nordeste/',
    'centrooeste': 'https://www.pciconcursos.com.br/concursos/centrooeste/',
    'ultimas':     'https://www.pciconcursos.com.br/ultimas/',
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  'Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'pt-BR,pt;q=0.9',
}

def extrair_uf_do_titulo(title_attr):
    """Extrai UF de strings como 'Prefeitura de Natal - RN abre...'"""
    match = re.search(r'[-–]\s*([A-Z]{2})\s+', title_attr or '')
    if match:
        return match.group(1)
    return ''

def scrape_page(url, regiao, db, Concurso):
    novos = 0
    atualizados = 0

    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.content, 'html.parser')

        concursos_div = soup.find('div', id='concursos')
        if not concursos_div:
            logger.warning(f"Div#concursos não encontrado em {url}")
            return novos, atualizados

        current_uf = regiao.upper() if regiao != 'ultimas' else 'VÁRIOS'

        for element in concursos_div.children:
            if not hasattr(element, 'name') or not element.name:
                continue

            classes = element.get('class', [])

            # Atualiza o UF corrente quando encontra cabeçalho de grupo
            if 'ua' in classes:
                eid = element.get('id', '').strip()
                if eid:
                    current_uf = eid
                continue

            # Processa cards de concurso (da = destaque, na = normal)
            if 'da' not in classes and 'na' not in classes:
                continue

            ca = element.find('div', class_='ca')
            if not ca:
                ca = element

            link_tag = ca.find('a', href=True)
            if not link_tag:
                continue

            link = link_tag.get('href', '').strip()
            titulo = link_tag.get_text(strip=True)
            title_attr = link_tag.get('title', '')

            if not link or not titulo:
                continue

            # Vagas / cargos / escolaridade — dentro de div.cd
            cd = ca.find('div', class_='cd')
            vagas = cargos = escolaridade = ''
            if cd:
                textos = [t.strip() for t in cd.stripped_strings]
                if textos:
                    vagas = textos[0]
                if len(textos) > 1:
                    cargos = textos[1]
                if len(textos) > 2:
                    escolaridade = textos[2]

            # Prazo — dentro de div.ce
            ce = ca.find('div', class_='ce')
            prazo = ' '.join(ce.stripped_strings) if ce else ''

            # UF: tenta extrair do título do link, senão usa o grupo atual
            uf = extrair_uf_do_titulo(title_attr) or current_uf

            # Salva ou atualiza no banco
            existente = Concurso.encontrar_por_link(link)
            if existente:
                existente.titulo   = titulo
                existente.vagas    = vagas
                existente.cargos   = cargos
                existente.escolaridade = escolaridade
                existente.prazo    = prazo
                existente.uf       = uf
                existente.data_atualizacao = datetime.now()
                db.session.commit()
                atualizados += 1
            else:
                novo = Concurso(
                    titulo=titulo,
                    orgao=titulo,
                    uf=uf,
                    regiao=regiao,
                    link=link,
                    vagas=vagas,
                    cargos=cargos,
                    escolaridade=escolaridade,
                    prazo=prazo,
                    status='Ainda não classificados',
                )
                db.session.add(novo)
                db.session.commit()
                novos += 1

    except requests.RequestException as e:
        logger.error(f"Erro de rede em {url}: {e}")
    except Exception as e:
        logger.error(f"Erro ao processar {regiao}: {e}", exc_info=True)

    return novos, atualizados


def scrape_pci_concursos(db, Concurso):
    total_novos = 0
    total_atualizados = 0
    total = 0

    for regiao, url in PAGES.items():
        logger.info(f"Scraping {regiao}: {url}")
        novos, atualizados = scrape_page(url, regiao, db, Concurso)
        total_novos += novos
        total_atualizados += atualizados
        total += novos + atualizados
        logger.info(f"  {regiao}: {novos} novos, {atualizados} atualizados")

    return {
        'novos': total_novos,
        'atualizados': total_atualizados,
        'total': total,
    }
