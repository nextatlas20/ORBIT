def queue_snapshot(queue):
    pending=len(queue)
    oldest=queue[0] if queue else None
    return {"pending":pending,"oldest":oldest}
    # TODO: expose queue wait duration
