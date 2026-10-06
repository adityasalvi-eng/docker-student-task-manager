# 1. Start from an official image that already has Python 3.12 installed.
#    "slim" means a smaller version, so the download is faster.
FROM python:3.12-slim

# 2. Make sure Python prints logs immediately (so "docker logs" works well).
ENV PYTHONUNBUFFERED=1

# 3. Create and move into a folder called /app inside the image.
#    All following commands run from this folder.
WORKDIR /app

# 4. Copy ONLY requirements.txt first.
#    (Docker caches each step, so dependencies are not reinstalled
#     every time we change app.py.)
COPY requirements.txt .

# 5. Install the Python libraries listed in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy all remaining project files (app.py, templates, static) into /app.
COPY . .

# 7. Document that the app listens on port 5000 inside the container.
EXPOSE 5000

# 8. The command that runs when the container starts.
CMD ["python", "app.py"]