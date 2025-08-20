"""The draw triangle task from ManiSkill."""

# from metasim.cfg.checkers import PositionShiftChecker
from metasim.utils import configclass

from .maniskill_task_cfg import ManiskillTaskCfg


@configclass
class DrawSVGCfg(ManiskillTaskCfg):
    """Draw a SVG path.

    .. Description::

    ### title:
    draw_svg

    ### group:
    maniskill

    ### description:
    Draw a goal SVG path above the table.

    ### randomizations:
    -

    ### success:
    - not yet implemented

    ### badges:
    - demos

    ### official_url:
    https://maniskill.readthedocs.io/en/latest/tasks/drawing/index.html#drawsvg-v1

    ### video_url:
    draw_svg.mp4

    ### platforms:
    - mujoco
    - isaaclab

    ### notes:
    """

    episode_length = 500
    objects = []
    traj_filepath = "roboverse_data/trajs/maniskill/draw_svg/v2"
