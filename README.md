# Course Web App Backend

This is a small Django REST API providing basic course management and a simple OpenAI assistant endpoint.

## Setup

1. **Install dependencies**

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. **Configure environment variables**

Copy `.env.example` to `.env` and update the values:

```bash
cp .env.example .env
```

`DJANGO_SECRET_KEY` is required. `OPENAI_API_KEY` is optional and used by the agent endpoint.

3. **Start Redis** (required for caching)

```bash
redis-server
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Run the development server**

```bash
python manage.py runserver
```

6. **Run tests**

```bash
python manage.py test
```

