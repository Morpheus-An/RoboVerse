"""The draw triangle task from ManiSkill."""

# from metasim.cfg.checkers import PositionShiftChecker
from metasim.cfg.objects import PrimitiveCubeCfg
from metasim.constants import PhysicStateType
from metasim.utils import configclass

from .maniskill_task_cfg import ManiskillTaskCfg


@configclass
class DrawTriangleCfg(ManiskillTaskCfg):
    """The DrawTriangle task from ManiSkill.

    .. Description:

    ### 📦 Source Metadata (from ManiSkill)

    ### title:
    DrawTriangle
    ### group:
    Maniskill
    ### description:
    Draw a goal triangle above the table
    ### randomizations:
    -
    ### success:
    - The drawn points by the robot are within a euclidean distance of 0.05m with points on the goal triangle
    ### badges:
    -
    ### official_url:
    https://maniskill.readthedocs.io/en/latest/tasks/drawing/index.html#drawtriangle-v1
    ### platforms:

    ### notes:
    """

    episode_length = 250
    objects = []
    traj_filepath = "roboverse_data/trajs/maniskill/draw_triangle/v2"
