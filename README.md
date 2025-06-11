```markdown
# FastAPI + Redis Counter App

Este proyecto es una demostración de orquestación de múltiples servicios con Docker Compose, que incluye:

- **FastAPI** como framework web.
- **Redis** para persistencia de un contador de visitas.
- **Docker Compose** para definir y levantar todo el stack con un solo comando.

---

## 📁 Estructura del proyecto

```

fastapi-redis-basic/
├── app.py
├── requirements.txt
│── Dockerfile
├── .env
└── docker-compose.yml

````

- **api/**: código fuente de la aplicación FastAPI.  
- **.env**: variables de entorno para Redis.  
- **docker-compose.yml**: definición de los servicios `api` y `cache`.  

---

## 🚀 Requisitos

- Docker ≥ 20.10  
- Docker Compose v2 (CLI integrada en Docker)  
- (Opcional) Python 3.12+ para desarrollo local sin contenedores  

---

## ⚙️ Variables de Entorno

Define en `.env` (no debe subirse a Git):

```dotenv
REDIS_HOST=cache
REDIS_PORT=6379
````

Puedes usar un `.env.example` para documentar los valores requeridos:

```dotenv
# .env.example
REDIS_HOST=cache
REDIS_PORT=6379
```

---

## 📦 Construcción y Arranque

1. Clona este repositorio:

   ```bash
   git clone <tu-repo-url>
   cd day2-demo-fastapi
   ```

2. Levanta el stack (reconstruyendo siempre la imagen API):

   ```bash
   docker compose up --build --force-recreate -d
   ```

3. Comprueba el estado:

   ```bash
   docker compose ps
   ```

4. Consulta los logs en tiempo real:

   ```bash
   docker compose logs -f api
   ```

---

## 🔗 Endpoints

| Método | Ruta      | Descripción                                      |
| ------ | --------- | ------------------------------------------------ |
| GET    | `/`       | Incrementa el contador y devuelve `{ visits }`.  |
| GET    | `/visits` | Devuelve `{ total_visits }` sin modificar valor. |

Prueba en terminal:

```bash
curl http://localhost:8000
# {"visits": 1}

curl http://localhost:8000/visits
# {"total_visits": 1}
```

---

## 🔄 Escalado

Para probar escalado horizontal de la API:

```bash
docker compose up -d --scale api=3
docker compose ps
```

Verás tres instancias de `api` compartiendo el mismo contador en Redis.

---

## 🧹 Limpieza

Para detener y eliminar todos los contenedores, redes y volúmenes:

```bash
docker compose down --volumes
docker volume prune --force
```

---

## 🔧 Desarrollo Local

Si prefieres desarrollar sin Docker, instala dependencias:

```bash
cd api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export REDIS_HOST=localhost
export REDIS_PORT=6379
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

---

## 📖 Referencias

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Redis Python Client](https://pypi.org/project/redis/)
* [Docker Compose Documentation](https://docs.docker.com/compose/)

---

> **Autor:** Álvaro "Chamo" Linares Cabré

```
```
