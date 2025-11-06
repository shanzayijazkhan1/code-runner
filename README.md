# Code Runner Sandbox (FastAPI + Docker-ready)

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Tests](https://img.shields.io/badge/tests-pytest-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)


Runs small **Python** snippets with time + memory limits. (Local subprocess demo; swap for Docker in production.)

## Run
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
