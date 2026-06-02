#!/bin/bash
set -e

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL..."
while ! pg_isready -h db -U appuser 2>/dev/null; do
  sleep 1
done
echo "PostgreSQL is ready"

# Check if database is empty and initialize if needed
python -c "
import os
from app import app, db
from models import User

with app.app_context():
    try:
        # Try to query users table
        user_count = User.query.count()
        print(f'Database already initialized ({user_count} users found)')
    except Exception as e:
        print(f'Database not initialized, running setup: {e}')
        exec(open('setup_db.py').read())
"

# Start Gunicorn
exec gunicorn -w 4 -b 0.0.0.0:8000 app:app
