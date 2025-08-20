"""The pick up cube task from ManiSkill."""

from metasim.cfg.checkers import DetectedChecker, Relative2DSphereDetector
from metasim.cfg.objects import PrimitiveCylinderCfg, PrimitiveSphereCfg
from metasim.constants import PhysicStateType
from metasim.utils import configclass

from .maniskill_task_cfg import ManiskillTaskCfg

goal_region_size = 0.1  # The size of the goal region in meters
goal_region_visible_size = 0.05  # The visible size of the goal region in meters


@configclass
class RollBallCfg(ManiskillTaskCfg):
    """The RollBall task from ManiSkill.

    .. Description:

    ### 📦 Source Metadata (from ManiSkill)

    ### title:
    RollBall
    ### group:
    Maniskill
    ### description:
    A simple task where the objective is to push and roll a ball to a goal region at the other end of the table
    ### randomizations:
    - The ball's xy position is randomized on top of a table in the region [0.2, 0.5] x [-0.4, 0.7]. It is placed flat on the table
    - The target goal region is marked by a red/white circular target. The position of the target is randomized on top of a table in the region [-0.4, -0.7] x [0.2, -0.9]
    ### success:
    - The ball's xy position is within goal_radius (default 0.1) of the target's xy position by euclidean distance.
    ### badges:
    - dense
    - sparse
    - demo
    ### official_url:
    https://maniskill.readthedocs.io/en/latest/tasks/table_top_gripper/index.html#rollball-v1
    ### platforms:
    - mujoco
    - isaaclab
    ### video_url:
    roll_ball.mp4
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
        PrimitiveSphereCfg(
            name="ball",
            radius=0.05,
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
        obj_name="ball",
    )

    traj_filepath = "roboverse_data/trajs/maniskill/roll_ball/v2"
