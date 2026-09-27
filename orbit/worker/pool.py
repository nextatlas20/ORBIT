class WorkerPool:
    def __init__(self, workers): self.workers=workers
    def shutdown(self):
        for worker in self.workers: worker.stop()
        return len(self.workers)
    # TODO: close idle workers during shutdown
