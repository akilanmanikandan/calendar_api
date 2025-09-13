from fastapi import FastAPI
from datetime import datetime, timedelta
import uvicorn

app = FastAPI()

@app.get("/calendar-options")
def get_calendar_options():
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    day_after = today + timedelta(days=2)

    return {
        "today": today.strftime("%A, %d %b %Y"),
        "tomorrow": tomorrow.strftime("%A, %d %b %Y"),
        "day_after": day_after.strftime("%A, %d %b %Y")
    }

# Run directly with Python (no need to type uvicorn manually)
if __name__ == "__main__":
    uvicorn.run("calendar_api:app", host="0.0.0.0", port=8000, reload=True)
