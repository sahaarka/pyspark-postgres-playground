#!/usr/bin/env bash
set -euo pipefail

echo "Stopping and removing containers (keeps volumes by default)."
docker compose down

echo "If you want to remove volumes as well (delete DB data), run:"
echo "  docker compose down -v"