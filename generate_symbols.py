import csv
import requests
from exceptions import *
from bs4 import BeautifulSoup
from datetime import datetime


def get_brazilian_symbols() -> list:
    url="https://www.dadosdemercado.com.br/bolsa/acoes"
    
    try:
        if (response := requests.get(url)).status_code != 200:
            raise ContentRetrievalError(f"Falha ao obter o conteúdo da página. Código de status: {response.status_code}")

        soup = BeautifulSoup(response.text, 'html.parser')
        if not (table := soup.find('table', {'id': 'stocks'})):
            raise TableNotFoundError("Tabela com id 'stocks' não encontrada.")

        if not (strong_tags := table.find_all('strong')):
            raise StrongTagsNotFoundError("Tags 'strong' não foram encontradas.")

        if not (a_texts := [strong.get_text()+".SA" for strong in strong_tags]):
            raise TextTagsNotFoundError("Texto das tags 'a' não encontrado.")

        return a_texts

    except requests.exceptions.RequestException as e:
        print("Erro de conexão:", e)
        return []
    except ContentRetrievalError as e:
        print("Erro de obtenção de conteúdo:", e)
        return []
    except TableNotFoundError as e:
        print("Erro de tabela não encontrada:", e)
        return []
    except StrongTagsNotFoundError as e:
        print("Erro de tags 'strong' não encontradas:", e)
        return []
    except TextTagsNotFoundError as e:
        print("Erro de texto das tags 'a' não encontrado:", e)
        return []
    except Exception as ex:
        print("Erro inesperado:", ex)
        return []


def save_brazilian_symbols_in_file():
    symbols = get_brazilian_symbols()
    try:
        with open(str(datetime.now().strftime('%d-%m-%Y'))+"_symbols.txt", 'w') as file:
            for item in symbols:
                file.write(str(item) + '\n')
        print(f"Salvo com sucesso.")
    except Exception as e:
        print("Erro ao salvar a lista:", e)
        