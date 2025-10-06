# PySpark + PostgreSQL Playground

A self-contained, reproducible Data Engineering sandbox built using **Docker Compose** — combining:
- 🧮 **PySpark** for distributed data processing
- 🐘 **PostgreSQL** for SQL practice
- 🧰 **pgAdmin** for database visualization
- 💻 **JupyterLab** for interactive PySpark notebooks

Ideal for:
- Practicing **LeetCode SQL** questions using Spark
- Learning **PySpark JDBC connections**
- Building **data pipelines** locally before deploying to cloud
- Teaching or demoing **Data Engineering fundamentals**

---

## 🚀 Features
- One-command startup using `docker compose up -d`
- Shared environment variables via `.env` file
- Persistent PostgreSQL storage via Docker volumes
- Configured JupyterLab workspace (PySpark pre-installed)
- Integrated pgAdmin for DB management
- Secure defaults — secrets isolated in `.env`

---

## 🧰 Stack Overview
| Component | Purpose |
|------------|----------|
| PySpark (JupyterLab) | Run Spark code interactively |
| PostgreSQL | Backend relational database |
| pgAdmin | Browser-based SQL & DB management |
| Docker Compose | Orchestrates the environment |

## Project Layout

leetcode-pyspark/<br>
├─ docker-compose.yml<br>
├─ .env.example<br>
├─ .gitignore<br>
├─ README.md<br>
├─ libs/                     # optional: place JDBC jar(s) here<br>
├─ workspace/<br>
│  ├─ Dockerfile<br>
│  ├─ requirements.txt<br>
│  ├─ seed_data.py<br>
│  └─ notebooks/             # your Jupyter notebooks<br>
└─ .devcontainer/<br>
   └─ devcontainer.json<br>

## Step-by-step setup (for a new user)

### 1) Clone the repo
```bash
git clone <repo-url>
cd pyspark-postgres-playground   # or your repo folder name
```

### 2) Create .env from the template (do NOT commit .env)
```
cp .env.example .env
# Edit .env if you want custom credentials
```

### 4) Start Docker Desktop and enable WSL2 integration
* Install [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/)
* BIOS virtualization (VT-x) should be enabled.
* Install WSL2 (Ubuntu recommended)
Open PowerShell as Administrator and run:
```
wsl --install -d ubuntu
```
or, if WSL already installed:
```
wsl --update
wsl --set-default-version 2
```
* Install [Visual Studio Code](https://code.visualstudio.com/download) and install [devcontainers](https://code.visualstudio.com/docs/devcontainers/containers) extension.
* Open Docker Desktop → Settings → Resources → WSL Integration → enable for Ubuntu-22.04 (if using WSL).
* When Windows firewall asks, **Allow on Private networks only, not Public networks**.

### 5) Build & run the stack
From the project root:
```
docker compose up -d --build
```

### 6) Check container health
```
docker compose ps
docker compose logs -f
```
Wait until:
* db shows database system is ready to accept connections.
* workspace prints the Jupyter URL (with token).

### 7) Seed the database (run once)
```
docker compose exec workspace python /home/jovyan/work/seed_data.py
```
This creates an **employees** table with sample rows.

### 8) Open the UIs
* JupyterLab: [http://localhost:8888](http://localhost:8888) — get the token via docker compose logs workspace or run docker compose exec workspace jupyter notebook list.
* pgAdmin: [http://localhost:5050](http://localhost:5050) — login with admin@local.com / admin.

### 9) Register Postgres in pgAdmin
If pgAdmin runs as a container (recommended), register server with:

* Host name/address: **db**
* Port: **5432**
* DB: **leetcode** (or postgres)
* User: from *.env* (e.g., postgres)
* Password: from *.env* (e.g., postgrespw)

If you use a desktop DB client (DBeaver/pgAdmin desktop), use **localhost** as host.

### 10) Use VS Code Dev Container
Open VS Code → Command Palette → Remote-Containers: Open Folder in Container... → choose repo folder.
VS Code will attach to the **workspace** service defined in **.devcontainer/devcontainer.json**.

### 11) Reading DB tables in PySpark (example)
Open a notebook in Jupyter and run:
```
from pyspark.sql import SparkSession
import os

spark = SparkSession.builder \
    .appName("ReadFromPostgres") \
    .config("spark.jars", "/usr/local/spark/jars/postgresql-42.6.0.jar") \
    .getOrCreate()

jdbc_url = "jdbc:postgresql://db:5432/leetcode"
props = {"user": os.getenv("POSTGRES_USER"), "password": os.getenv("POSTGRES_PASSWORD"), "driver": "org.postgresql.Driver"}

df = spark.read.jdbc(url=jdbc_url, table="employees", properties=props)
df.show()
```

## Some useful commands:
* ```docker compose down```
* ```docker compose down -v```
* ```docker compose up -d --build```
* ```jupyter notebook list```
* ```docker compose exec workspace bash```
* ```docker compose exec workspace jupyter notebook list```
* The below sql query can be run in PGAdmin to get all the tables in "leetcode" database
```
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_type = 'BASE TABLE'
  AND table_schema NOT IN ('pg_catalog', 'information_schema')
ORDER BY table_schema, table_name;
```
* ```docker compose logs -f db```
* ```docker compose logs -f workspace```