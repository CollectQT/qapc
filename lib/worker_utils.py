############################################################
# worker data transforms
############################################################

def make_worker_total_earnings(workers, table):
    for video in table.values():
        for worker, earnings in video['earnings'].items():
            workers[worker]['earnings'] += earnings

    return workers
