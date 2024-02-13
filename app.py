from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def translate_to_dothraki(text, api_key=None):
    base_url = "https://api.funtranslations.com/translate/dothraki.json"
    
    headers = {}
    if api_key:
        headers['X-Funtranslations-Api-Secret'] = api_key
    
    payload = {'text': text}
    
    try:
        response = requests.post(base_url, headers=headers, json=payload)
        response.raise_for_status()  # Lança uma exceção para códigos de status diferentes de 2xx
        result = response.json()
        if 'contents' in result and 'translated' in result['contents']:
            translated_text = result['contents']['translated']
            return translated_text
        else:
            return f"Erro: Resposta inesperada da API - {result}"
    except requests.exceptions.RequestException as e:
        return f"Erro na requisição: {e}"

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
