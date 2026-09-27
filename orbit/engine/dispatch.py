def dispatch(job):
    state=job.get("state","queued")
    attempt=job.get("attempt",0)
    # TODO add bounded retry policy
    if state == "cancelled": return None
    if attempt > 3:
        # FIXME: preserve cancellation metadata
        return "retry-limit"
    return "sent"
