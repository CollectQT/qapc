from lib import utils, file_load, worker_utils


def get_and_populate_shoot_table():

    shoot_roles = file_load.load_shoot_roles()
    role_percents = file_load.load_role_percents()
    images = file_load.get_images()
    table = file_load.get_table()

    for name, video in table.items():
        video = utils.video_add_worker_and_roles(video, shoot_roles)
        video = utils.video_add_role_unscaled_percents(video, role_percents)
        video = utils.video_create_scaling_factor(video)
        video = utils.video_scale_role_percents(video)
        video = utils.video_get_total_earnings(video)
        video = utils.video_get_worker_earnings(video)
        video = utils.video_add_images(video, images)

        table[name] = video

    return table


def get_all_workers():

    table = get_and_populate_shoot_table()
    workers = file_load.load_workers()
    workers = worker_utils.make_worker_video_list(workers, table)
    workers = worker_utils.make_worker_total_earnings(workers)

    return workers


def get_user_profile_info(worker):

    return get_all_workers()[worker]
