############################################################
# worker data transforms
############################################################


def make_worker_video_list(workers, table):

    for video in table.values():
        for worker in video['Workers'].keys():
            try:
                workers[worker]['videos'].append( video )
            except KeyError:
                workers[worker]['videos'] = [video]

    return workers


def make_worker_total_earnings(workers):

    for worker, values in workers.items():
        for video in values['videos']:
            name        = video['name']
            earnings    = video['earnings'][worker]

            try:
                workers[worker]['earnings'] += earnings
            except KeyError:
                workers[worker]['earnings'] = earnings

            try:
                workers[worker]['earnings_map'][name] = earnings
            except KeyError:
                workers[worker]['earnings_map'] = {name: earnings}

    return workers
