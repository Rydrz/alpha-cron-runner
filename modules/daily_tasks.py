# modules/daily_tasks.py
import os, json
from datetime import datetime

STATUS_FILE = "logs/daily_status.json"

def already_done_today(task: str) -> bool:
    today = datetime.utcnow().strftime("%Y-%m-%d")
    if not os.path.exists(STATUS_FILE):
        return False
    with open(STATUS_FILE, "r", encoding="utf-8") as f:
        status = json.load(f)
    return status.get(task) == today

def mark_done(task: str):
    today = datetime.utcnow().strftime("%Y-%m-%d")
    status = {}
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r", encoding="utf-8") as f:
            try: status = json.load(f)
            except: status = {}
    status[task] = today
    os.makedirs("logs", exist_ok=True)
    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(status, f, indent=2)

def run_daily_tasks():
    now = datetime.utcnow()
    if now.hour != 0:
        return
    print("📊 Revue quotidienne simulée (fonction score_review() à intégrer ici)")
    mark_done("score_review")

if __name__ == "__main__":
    run_daily_tasks()
