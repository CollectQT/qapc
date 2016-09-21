from lib import utils


def get_and_populate_shoot_table():

    shoot_roles = utils.load_shoot_roles()
    role_percents = utils.load_role_percents()
    table = utils.get_table()

    for name, video in table.items():
        video = utils.video_add_worker_and_roles(video, shoot_roles)
        video = utils.video_add_role_unscaled_percents(video, role_percents)
        video = utils.video_create_scaling_factor(video)
        video = utils.video_scale_role_percents(video)
        video = utils.video_get_total_earnings(video)
        video = utils.video_get_worker_earnings(video)

        table[name] = video

    return table
