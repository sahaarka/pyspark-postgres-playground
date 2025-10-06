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






