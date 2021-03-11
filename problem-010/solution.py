from time import time
import threading

class Scheduler:
    def __init__(self):
        self.jobs = [] # tuple of (function, time in miliseconds)

        # prevent race condition when 2 thread access self.jobs at the same time
        self.lock = threading.RLock()

        # condition to make one thread wait, and the other can wakes it up
        self.condition = threading.Condition(self.lock)

        thread = threading.Thread(target=self.poll)
        thread.start()

    def poll(self):
        while True:
            now = time() * 1000

            # take jobs with due time out of the list
            jobs_to_run = []
            with self.lock:
                jobs_to_run = [job for job, due in self.jobs if due <= now]
                self.jobs = [(job, due) for (job, due) in self.jobs if due > now]

            # run jobs from previous list
            for job in jobs_to_run:
                job()

            with self.lock:
                # wait forever if no more jobs
                if not self.jobs:
                    self.condition.wait()
                # wait only until the soonest (smallest) next job's due time
                wait_duration = min(due for job, due in self.jobs) - time()*1000
                self.condition.wait(wait_duration / 1000)

            for job, due in self.jobs:
                if now >= due:
                    job()
            self.jobs = [(job, due) for (job, due) in self.jobs if due > now]

    def delay(self, job, duration):
        now = time() * 1000
        with self.lock:
            self.jobs.append((job, now + duration))
            self.condition.notify_all()

scheduler = Scheduler()
scheduler.delay(lambda: print("5 seconds passed"), 5 * 1000)
scheduler.delay(lambda: print("2 seconds passed"), 2 * 1000)
