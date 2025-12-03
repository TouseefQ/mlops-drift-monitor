# 1. Base Image: Start with a lightweight version of Python
FROM python:3.9-slim

# 2. Work Directory: Create a folder inside the container called /app
WORKDIR /app

# 3. Dependencies: Copy the requirements file first (caching strategy)
COPY requirements.txt .

# 4. Install: Run pip inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy Code: Move your python script into the container
COPY . .

# 6. Command: What to do when the container starts?
CMD ["python", "app.py"]