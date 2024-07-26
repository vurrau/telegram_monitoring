#!/bin/sh

# Run the database initialization script
python app/db.py

# Start cron in the background
cron

# Tail cron logs
tail -f /var/log/cron.log &

# Run the main application
exec "$@"