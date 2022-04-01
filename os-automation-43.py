@contextlib.contextmanager
def measure_time():
    start = last  = datetime.datetime.now()
    def click():
        nonlocal last
        current = datetime.datetime.now()
        interval = current - last
        last = current
        print(round(interval.total_seconds()*1000, 3))
    start = last
    try:
        yield click
    finally:
        current = datetime.datetime.now()
        print("total time", round((current - start).total_seconds()*1000, 3))
