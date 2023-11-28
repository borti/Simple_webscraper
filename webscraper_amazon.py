import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_amazon_price(product_url):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    # Effettua la richiesta HTTP
    response = requests.get(product_url, headers=headers)

    if response.status_code == 200:
        # Analizza il codice HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Trova l'elemento che contiene il prezzo
        price_element = soup.find('span', {'class': 'a-offscreen'})
        if price_element:
            price = price_element.text.strip()
            return price
        else:
            return 'Prezzo non trovato'

    else:
        return f'Errore nella richiesta HTTP: {response.status_code}'

# Esempio di utilizzo
amazon_product_url = 'https://www.amazon.it/gp/product/B09MKFNMNN?ref=ppx_pt2_dt_b_prod_image'  # URL del prodotto su Amazon
price = get_amazon_price(amazon_product_url)
print(f'Il prezzo del prodotto elevatore di tensione su Amazon è: {price}')
