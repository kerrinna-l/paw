# Resumo Flask para Prova

## 1. render_template
Envia dados do Python para o HTML.

```python
return render_template('pagina.html', nome="Ana", idade=20)
````

HTML:

```html
{{ nome }}
{{ idade }}
```

Pode enviar variáveis, listas, dicionários e objetos.

---

## 2. Passando dicionário

```python
dados = {"nome": "Ana", "idade": 20}
return render_template('pagina.html', dados=dados)
```

HTML:

```html
{{ dados.nome }}
{{ dados.idade }}
```

---

## 3. Rotas com parâmetros

```python
@app.route('/usuario/<nome>')
def usuario(nome):
    return nome
```

Exemplo:
/usuario/joao

---

## 4. Tipos de parâmetros

```python
<int:idade>
<float:valor>
```

---

## 5. Vários parâmetros

```python
@app.route('/somar/<int:n1>/<int:n2>')
def somar(n1, n2):
    return str(n1 + n2)
```

---

## 6. Valores padrão

Forma 1:

```python
@app.route('/user', defaults={"nome": "visitante"})
@app.route('/user/<nome>')
def user(nome):
    return nome
```

Forma 2:

```python
@app.route('/user')
@app.route('/user/<nome>')
def user(nome="visitante"):
    return nome
```

---

## 7. Arquivos static

Estrutura:

```
/static
/templates
```

HTML:

```html
<img src="{{ url_for('static', filename='imgs/foto.jpg') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

---

## 8. Imagem dinâmica

```python
@app.route('/perfil/<usuario>')
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)
```

HTML:

```html
<img src="{{ url_for('static', filename='imgs/'+usuario+'.jpg') }}">
```

---

## 9. Formulários

### GET

HTML:

```html
<form action="/receber">
  <input name="nome">
</form>
```

Python:

```python
nome = request.args.get('nome')
```

---

### POST

HTML:

```html
<form method="post">
```

Python:

```python
nome = request.form.get('nome')
```

Diferença:

* GET → request.args
* POST → request.form

---

## 10. Múltiplos campos

```python
nome = request.form.get('nome')
email = request.form.get('email')
```

---

## 11. Select

HTML:

```html
<select name="estado">
  <option value="RN">RN</option>
</select>
```

Python:

```python
estado = request.form['estado']
```

---

## 12. Radio

HTML:

```html
<input type="radio" name="sexo" value="F">
```

Python:

```python
sexo = request.form['sexo']
```

---

## 13. Checkbox

```python
itens = request.form.getlist('itens')
```

Retorna lista.

---

## 14. If no Python

```python
if idade >= 18:
```

---

## 15. If no HTML (Jinja)

```html
{% if idade >= 18 %}
  Maior
{% else %}
  Menor
{% endif %}
```

---

## 16. For no HTML

```html
{% for i in lista %}
  {{ i }}
{% endfor %}
```

---

## 17. Range no HTML

```html
{% for i in range(1, n) %}
```

---

## 18. Lista de dicionários

Python:

```python
dados = [
  {"nome": "Ana", "tel": "123"},
  {"nome": "João", "tel": "456"}
]
```

HTML:

```html
{% for d in dados %}
  {{ d.nome }} - {{ d.tel }}
{% endfor %}
```

---

## 19. Rota recebendo POST

```python
@app.route('/receber', methods=['POST'])
def receber():
    nome = request.form.get('nome')
    return nome
```

---
