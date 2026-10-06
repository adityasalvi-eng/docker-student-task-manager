# Docker Student Task Manager

A simple Student Task Manager built with Python Flask and SQLite,
containerised using Docker. Created for the Agile lab experiment:
**"Understand and implement application containerisation using Docker."**

## Features
- View tasks
- Add a task
- Delete a task

## Technologies
Python | Flask | SQLite | HTML/CSS | Docker | GitHub

## Why Docker?

Docker is used to containerize the Student Task Manager application
along with its required dependencies. This ensures that the application
runs consistently across different environments without requiring manual
installation of all dependencies.

Docker provides:
- Consistent application environment
- Easy deployment
- Dependency isolation
- Portable application containers

## Run Without Docker
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open: http://localhost:5000

## Run With Docker
```bash
docker build -t student-task-manager .
docker run -d --name task-manager -p 5000:5000 student-task-manager
```
Open: http://localhost:5000

## Useful Docker Commands
```bash
docker images              # list images
docker ps                  # list running containers
docker logs task-manager   # view app logs
docker stop task-manager   # stop container
docker start task-manager  # start it again
docker rm task-manager     # remove container
```

## Workflow
GitHub repo → Source code → Dockerfile → docker build → Image → docker run → Container → Browser
