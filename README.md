## Repositório para demonstrar uso de action para Deploys Automáticos no Heroku

Expliquei com mais detalhes o processo realizado [aqui](https://www.linkedin.com/posts/victor-augusto-oliveira_heroku-github-python-activity-6930705110108901377-DwBF?utm_source=linkedin_share&utm_medium=member_desktop_web).

Link da aplicação [aqui](https://action-heroku-deploy.herokuapp.com/).

### <strong>Instruções para instalação</strong>:

#### Criar e ativar ambiente virtual Python (venv):

```python -m venv .venv```

```source .venv/bin/activate```

#### <strong>Instalar dependências</strong>:

```pip install -r requirements.txt```

#### <strong>Instalar dependências, inclusive de desenvolvimento</strong>:

```pip install -r requirements-dev.txt```

#### Copiar variáveis de ambiente:
```cp contrib/env-sample .env```

#### Rodar Django:
```python manage.py runserver```