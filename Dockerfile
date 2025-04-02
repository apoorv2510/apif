FROM python:3.12

# Set working directory
WORKDIR /app

# Copy all files to container
COPY . /app

# ✅ Ensure players_large.json is copied (this is redundant only if already in the project root)
COPY players_large.json /app/players_large.json

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Start the Flask app using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "application:application"]
