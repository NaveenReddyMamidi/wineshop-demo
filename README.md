# WineShop Demo

A small Flask website for a wineshop with owner and worker roles and a PostgreSQL backend.

## Features
- Login page with role-based access
- Owner dashboard with wine creation and price management
- Expense tracking by shop and date, with net sales reflected in reports and dashboard
- Worker dashboard with shop and wine pricing view
- Multiple shops with different prices per wine

## Setup
1. Install Python dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Create a PostgreSQL database and update `DATABASE_URL` if needed.
   Copy the example file to `.env`:
   ```powershell
   copy .env.example .env
   ```
   Then edit `.env` to set your connection and secret:
   ```text
   DATABASE_URL=postgresql+pg8000://postgres:your_password@localhost:5432/wineshop
   SECRET_KEY=your-secret-key
   ```
3. Initialize database and sample data:
   ```bash
   python setup_db.py
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open `http://127.0.0.1:5000` in your browser.

## Docker deployment

### Development / quick launch
1. Copy `.env.example` to `.env` and update values.
2. Start with:
   ```bash
   docker-compose up --build
   ```
3. Visit `http://localhost:8000`.

### Production-ready Docker stack
1. Copy `.env.example` to `.env` and update values.
2. Start the production compose stack:
   ```bash
   docker-compose -f docker-compose.prod.yml up --build -d
   ```
3. Visit `http://localhost`.

This stack uses `Dockerfile.prod` for the app, `postgres:15` for the database, and `nginx:stable-alpine` to route traffic and serve static assets.

### Notes
- Do not commit `.env` with secrets.
- If you want HTTPS in production, put a certificate-terminating proxy in front of `nginx` or add cert management separately.
- The CI workflow is in `.github/workflows/docker-ci.yml`.

## Default accounts
- `owner` / `ownerpass`
- `worker` / `workerpass`

## Notes
- The app uses Flask templates for support pages.
- Owners can update prices, add wines, and add shops.
- Workers can view shops and pricing only.
