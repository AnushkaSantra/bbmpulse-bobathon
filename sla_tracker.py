
from datetime import datetime, timedelta
def sla_tracker(ticket):
    sla_hours = 48 if ticket["type"]=="pothole" else 24
    deadline = ticket["created_at"] + timedelta(hours=sla_hours)
    breached = datetime.utcnow() > deadline
    return {"breached": breached, "deadline": deadline.isoformat(), "escalate": breached}
