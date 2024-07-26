#!/bin/bash
*.sh text eol=lf
while ! pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
  echo "Waiting PostgreSQL..."
  sleep 2
done
# Run the database initialization script
python app/db.py
# Start cron in the background
cron
# Tail cron logs
tail -f /var/log/cron.log &
# Run the main application
exec "$@"