# Use Python slim base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput || true

# Expose the port (Railway/Django default is 8000)
EXPOSE 8000

# Run migrations and start server with Gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn MelodyHaven.wsgi:application --bind 0.0.0.0:8000"]
