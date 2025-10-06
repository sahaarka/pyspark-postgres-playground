**start.ps1**
```
Write-Host "🚀 Starting Docker stack..." -ForegroundColor Cyan
if (Test-Path ".env") {
  Get-Content .env | ForEach-Object {
    if ($_ -match "^(.*?)=(.*)$") {
      [System.Environment]::SetEnvironmentVariable($matches[1], $matches[2])
    }
  }
}
docker compose up -d --build
Write-Host "Waiting for Postgres..." -ForegroundColor Yellow
$ready = $false
for ($i=0; $i -lt 30; $i++) {
  $status = docker compose exec db pg_isready -U $env:POSTGRES_USER -d $env:POSTGRES_DB 2>$null
  if ($status -match "accepting connections") { $ready = $true; break }
  Start-Sleep -Seconds 2
  Write-Host "." -NoNewline
}
if (-not $ready) { Write-Host "`n❌ DB not ready"; exit 1 }
Write-Host "`n✅ DB ready. Seeding..." -ForegroundColor Green
docker compose exec workspace python /home/jovyan/work/seed_data.py
Write-Host "✅ Environment started!"
Write-Host "🌐 Jupyter: http://localhost:8888"
Write-Host "🌐 pgAdmin: http://localhost:5050 (admin@local.com / admin)"
docker compose ps
```

**stop.ps1**

```
Write-Host "🧹 Stopping containers..." -ForegroundColor Yellow
docker compose down
Write-Host "✅ Containers stopped (data preserved)."
Write-Host "To remove DB data completely: docker compose down -v"
```
