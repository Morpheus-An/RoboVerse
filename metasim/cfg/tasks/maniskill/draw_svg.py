"""The draw triangle task from ManiSkill."""

# from metasim.cfg.checkers import PositionShiftChecker
from metasim.cfg.objects import PrimitiveCubeCfg
from metasim.constants import PhysicStateType
from metasim.utils import configclass

from .maniskill_task_cfg import ManiskillTaskCfg


@configclass
class DrawSVGCfg(ManiskillTaskCfg):
    """The draw SVG task from ManiSkill.
    """

    episode_length = 500
    objects = []
    traj_filepath = "roboverse_data/trajs/maniskill/draw_svg/v2"
