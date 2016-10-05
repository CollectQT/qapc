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
            name        = video['name']
            earnings    = video['earnings'][worker]

            workers[worker]['earnings']            += earnings
            workers[worker]['earnings_map'][name]   = earnings

    for worker, values in workers.items():
        workers[worker]['earnings'] = values['earnings']

    return workers
