# 🚀 Django + Docker

## 🔑 Main Commands
python3 -m venv venv
source venv/bin/activate 
# for Linux/macOS 
venv\Scripts\activate 
# for Windows 
pip install -r requirements.txt
# Build and start containers
docker compose up --build

# Start in detached mode
docker compose up -d --build

# Stop containers
docker compose down

# Run migrations
docker compose run web python manage.py makemigrations
docker compose run web python manage.py migrate

# Create superuser
docker compose run web python manage.py createsuperuser

# Collect static files
docker compose run web python manage.py collectstatic --noinput


# Enter web container
docker compose exec web bash

