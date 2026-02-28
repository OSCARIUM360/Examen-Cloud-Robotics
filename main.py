from datetime import datetime
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/telemetry")
async def telemetry(req: Request):
    data = await req.json()
    ts = datetime.utcnow().isoformat()
    print(f"{ts} telemetry={data}")
    return {"received": True, "ts": ts}