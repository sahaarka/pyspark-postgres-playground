#!/usr/bin/env bash
set -euo pipefail

# load .env if present (optional)
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

echo "Building and starting containers..."
docker compose up -d --build

echo "Waiting for Postgres to be ready..."
# loop until pg_isready inside db returns OK
until docker compose exec -T db pg_isready -U "${POSTGRES_USER:-postgres}" -d "${POSTGRES_DB:-leetcode}" >/dev/null 2>&1; do
  printf '.'
  sleep 2
done
echo
echo "Postgres is ready."

echo "Seeding database (seed_data.py)..."
docker compose exec workspace python /home/jovyan/work/seed_data.py || {
  echo "Seeding failed — check logs:"
  docker compose logs --tail 200 workspace
  exit 1
}

echo "All services up. Useful URLs:"
echo " - JupyterLab: http://localhost:8888  (token in 'docker compose logs workspace')"
echo " - pgAdmin:    http://localhost:5050  (admin@local.com / admin)"
echo
docker compose ps