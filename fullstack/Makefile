run-api-dev:
	cd backend && uv run fastapi dev app/main.py

run-web-dev:
	cd web && npm run dev

run-db-migrations:
	cd backend && uv run alembic upgrade head

# Make sure that the database is running before running this command
setup-dev:
	cd backend && uv sync && make run-db-migrations
	cd web && npm install