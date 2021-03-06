from multiprocessing import cpu_count


def max_workers():
    return cpu_count() * 2 + 2


max_requests = 1000
workers = max_workers()
