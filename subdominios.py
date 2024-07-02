import requests
import argparse

# Definindo a função main()
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--wordlist", help="Adicionar a wordlist (arquivo.txt)")
    parser.add_argument("-u", "--url", help="Adicionar a url alvo")
    args = parser.parse_args()

    wordlist_file = args.wordlist
    target_url = args.url

    try:
        with open(wordlist_file, "r") as wordlist:
            for word in wordlist:
                word = word.strip()
                if not word:
                    continue
                url = f'https://{word}.{target_url}'
                try:
                    r = requests.get(url)
                    if r.status_code == 200:
                        print(f'[+] Encontrado: {url}')
                except requests.exceptions.RequestException as e:
                    print(f'[-] Erro: {e}')

    except FileNotFoundError:
        print(f'[-] Arquivo não encontrado: {wordlist_file}')

# Chamando a função main()
if __name__ == "__main__":
    main()
