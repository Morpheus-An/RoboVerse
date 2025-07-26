"""The pick up cube task from ManiSkill."""

from metasim.cfg.checkers import DetectedChecker, Relative2DSphereDetector
from metasim.cfg.objects import PrimitiveCubeCfg, PrimitiveCylinderCfg, RigidObjCfg
from metasim.constants import PhysicStateType
from metasim.utils import configclass

from .maniskill_task_cfg import ManiskillTaskCfg

reach_distance = 0.6  # The distance the robot can reach


@configclass
class PullCubeToolCfg(ManiskillTaskCfg):
    """The PullCubeTool task from ManiSkill.

    .. Description:

    ### 📦 Source Metadata (from ManiSkill)

    ### title:
    PullCubeTool
    ### group:
    Maniskill
    ### description:
    Given an L-shaped tool that is within the reach of the robot, leverage the tool to pull a cube that is out of it's reach
    ### randomizations:
    - The cube's position (x,y) is randomized on top of a table in the region “<out of manipulator reach, but within reach of tool>”. It is placed flat on the table
    ### success:
    - The cube's xy position is within the goal region of the arm's base (marked by reachability)
    ### badges:
    - dense
    - sparse
    - demo
    ### official_url:
    https://maniskill.readthedocs.io/en/latest/tasks/table_top_gripper/index.html#pullcubetool-v1
    ### platforms:

    ### notes:
    - note that the checker is not the same as the one in the original task. Current chekcer checks if the cube is within a sphere of radius reach_distance around the base of the robot.
    """

    episode_length = 250
    objects = [
        PrimitiveCylinderCfg(
            name="franka_base",
            radius=0.02,
            height=0.0001,
            color=[0.0, 0.0, 0.0],
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
        RigidObjCfg(
            name="tool",
            mjcf_path="roboverse_data/assets/maniskill/PullCubeTool/tool/mjcf/PullCubeTool_tool.xml",
            usd_path="roboverse_data/assets/maniskill/PullCubeTool/tool/usd/PullCubeTool_tool.usd",
            physics=PhysicStateType.RIGIDBODY,
        ),
    ]

    detector = Relative2DSphereDetector(
        base_obj_name="franka_base",
        relative_pos=(0.0, 0.0, 0.0),
        radius=reach_distance,
        axis=(0, 1),
    )
    checker = DetectedChecker(
        detector=detector,
        obj_name="cube",
    )

    traj_filepath = "roboverse_data/trajs/maniskill/pull_cube_tool/v2"
