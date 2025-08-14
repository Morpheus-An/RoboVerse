"""The draw triangle task from ManiSkill."""

# from metasim.cfg.checkers import PositionShiftChecker
from metasim.utils import configclass

from .maniskill_task_cfg import ManiskillTaskCfg


@configclass
class DrawTriangleCfg(ManiskillTaskCfg):
    """The DrawTriangle task from ManiSkill.

    .. Description::

    ### title:
    draw_traingle

    ### group:
    maniskill

    ### description:
    Draw a goal triangle path above the table.

    ### randomizations:
    -

    ### success:
    - not yet implemented

    ### badges:
    - demos

    ### official_url:
    https://maniskill.readthedocs.io/en/latest/tasks/drawing/index.html#drawtriangle-v1

    ### platforms:

    ### notes:
    """

    episode_length = 250
    objects = []
    traj_filepath = "roboverse_data/trajs/maniskill/draw_triangle/v2"
