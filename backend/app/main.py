import subprocess, tempfile, os, signal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Code Runner Sandbox")

class RunRequest(BaseModel):
    language: str = "python"
    code: str

@app.post("/run")
def run(req: RunRequest):
    if req.language != "python":
        raise HTTPException(400, "Only Python supported in demo")
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(req.code)
        path = f.name
    try:
        proc = subprocess.run(
            ["python","-S",path],
            capture_output=True, text=True, timeout=2
        )
        return {"stdout": proc.stdout[-4000:], "stderr": proc.stderr[-4000:], "returncode": proc.returncode}
    except subprocess.TimeoutExpired:
        return {"stdout":"","stderr":"Timeout","returncode":124}
    finally:
        try: os.remove(path)
        except Exception: pass
