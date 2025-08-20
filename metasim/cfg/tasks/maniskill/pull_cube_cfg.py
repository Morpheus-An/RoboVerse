"""The pick up cube task from ManiSkill."""

from metasim.cfg.checkers import DetectedChecker, Relative2DSphereDetector
from metasim.cfg.objects import PrimitiveCubeCfg, PrimitiveCylinderCfg
from metasim.constants import PhysicStateType
from metasim.utils import configclass

from .maniskill_task_cfg import ManiskillTaskCfg

goal_region_size = 0.1  # The size of the goal region in meters
goal_region_visible_size = 0.05  # The visible size of the goal region in meters


@configclass
class PullCubeCfg(ManiskillTaskCfg):
    """The PullCube task from ManiSkill.

    .. Description:

    ### 📦 Source Metadata (from ManiSkill)

    ### title:
    PullCube
    ### group:
    Maniskill
    ### description:
    A simple task where the objective is to pull a cube onto a target.
    ### randomizations:
    - the cube's xy position is randomized on top of a table in the region [0.1, 0.1] x [-0.1, -0.1].
    - the target goal region is marked by a red and white target. The position of the target is fixed to be the cube's xy position - [0.1 + goal_radius, 0]
    ### success:
    - the cube's xy position is within goal_radius (default 0.1) of the target's xy position by euclidean distance..
    ### badges:
    - dense
    - sparse
    - demo
    ### official_url:
    https://maniskill.readthedocs.io/en/latest/tasks/table_top_gripper/index.html#pullcube-v1
    ### platforms:
    - mujoco
    - isaaclab

    ### video_url:
    pull_cube.mp4
    ### notes:
    """

    episode_length = 250
    objects = [
        PrimitiveCylinderCfg(
            name="goal_region",
            radius=goal_region_visible_size,
            height=0.0001,
            color=[0.0, 0.0, 1.0],
            collision_enabled=False,
            physics=PhysicStateType.XFORM,
            fix_base_link=True,  # Fix the goal region to the ground
        ),
        PrimitiveCubeCfg(
            name="cube",
            size=[0.04, 0.04, 0.04],
            mass=0.02,
            physics=PhysicStateType.RIGIDBODY,
            color=[1.0, 0.0, 0.0],
        ),
    ]

    detector = Relative2DSphereDetector(
        base_obj_name="goal_region",
        relative_pos=(0.0, 0.0, 0.0),
        radius=goal_region_size,
        axis=(0, 1),
    )
    checker = DetectedChecker(
        detector=detector,
        obj_name="cube",
    )

    traj_filepath = "roboverse_data/trajs/maniskill/pull_cube/v2"
