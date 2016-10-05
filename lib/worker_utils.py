############################################################
# worker data transforms
############################################################


def make_worker_video_list(workers, table):

    for video in table.values():
        for worker in video['Workers'].keys():
            workers[worker]['videos'].append( video )

    return workers


def make_worker_total_earnings(workers):
    for worker, values in workers.items():
        for video in values['videos']:
            workers[worker]['earnings'] += video['earnings'][worker]

    for worker, values in workers.items():
        workers[worker]['earnings'] = round(values['earnings'], 2)

    return workers
