import sys
from datetime import datetime
from os.path import abspath, dirname

sys.path.append(dirname(dirname(dirname(abspath(__file__)))))

from dispatcher.app import *


@app.scheduled_job(trigger='interval', minutes=1)
def pprint_jobs():
    schedule_jobs = 0
    other_jobs = 0

    for job in app.get_jobs():
        if job.name.endswith('schedule'):
            schedule_jobs += 1
        else:
            other_jobs += 1
    print 'Schedule jobs:', schedule_jobs,
    print 'Other jobs:   ', other_jobs,
    print 'Total jobs:   ', len(app.get_jobs())
    print 'Now:', datetime.now(), '\n', '_' * 50, '\n'

# start all jobs
app.start()
