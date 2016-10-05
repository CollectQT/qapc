############################################################
# worker data transforms
############################################################


def make_worker_total_earnings(workers, table):
    for video in table.values():
        for worker, earnings in video['earnings'].items():
            workers[worker]['earnings'] += earnings

    return workers


def make_worker_video_list(workers, table):

    for video in table.values():
        for worker in video['Workers'].keys():
            workers[worker]['videos'].append( video )

    return workers
