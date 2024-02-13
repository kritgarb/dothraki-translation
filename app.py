from flask import Flask, render_template, request
from requests.exceptions import ConnectionError, RequestException
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
Bootstrap(app)

def translate_to_dothraki(text, api_key=None):
    base_url = "https://api.funtranslations.com/translate/dothraki.json"
    
    headers = {}
    if api_key:
        headers['X-Funtranslations-Api-Secret'] = api_key
    
    payload = {'text': f"{text}"}
    
    try:
        response = requests.post(base_url, headers=headers, json=payload)
        
        if response.status_code == 200:
            try:
                result = response.json()
                if 'contents' in result and 'translated' in result['contents']:
                    translated_text = result['contents']['translated']
                    return translated_text
                else:
                    raise ValueError(f"Erro: Resposta inesperada da API - {result}")
            except ValueError:
                return "Erro: Resposta da API não pôde ser convertida para JSON."
        else:
            return f"Erro na requisição: {response.status_code}, {response.text}"

    except ConnectionError as ce:
        return f"Erro na conexão: {ce}. Verifique sua conexão com a internet e tente novamente."

    except RequestException as re:
        return f"Erro na requisição: {re}. Verifique sua conexão com a internet e tente novamente."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    english_text = request.form['english_text']
    api_key = None  # Substitua pela sua chave de API

    translated_text = translate_to_dothraki(english_text, api_key)
    return render_template('index.html', english_text=english_text, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
