
# Dothraki Translator

Uma aplicação web simples para tradução de texto para a língua Dothraki, inspirada no universo de Game of Thrones.

## Tecnologias:
- Flask (framework web em Python)
- HTML, CSS, Bootstrap (front-end)
- API Funtranslations para tradução para Dothraki


## Instalação

### Clone o repositório do projeto:

```bash
  git clone git@github.com:kritgarb/dothraki-translation.git

```
### Instale as dependências:

```bash
  pip install -r requirements.txt

```
### Uso:
1. Inicie o servidor Flask:
```bash
  python app.py

```
2. Acesse a aplicação no navegador: http://127.0.0.1:5000/

3. Insira um texto em inglês no campo e clique no botão "Traduzir".

## Recursos Técnicos:
- app.py: Lógica principal do servidor Flask.
- index.html: Página principal da aplicação.
- dothraki_translator.py: Módulo para interagir com a API Funtranslations.

## Segurança:

- Uso de exceções para lidar com erros.
- Validação básica dos dados de entrada do usuário.

## Melhorias Futuras:
- Implementar cache para reduzir chamadas à API.
- Adicionar suporte a mais idiomas.
- Aprimorar a interface do usuário.

## Notas Adicionais:

- Este projeto foi criado como parte de um exercício prático.
- Quaisquer problemas ou sugestões podem ser relatados no repositório.

    
## Autores

- [@kritgarb](https://www.github.com/kritgarb)


## Referência
- [Dothraki translator API](https://funtranslations.com/api/dothraki)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)



