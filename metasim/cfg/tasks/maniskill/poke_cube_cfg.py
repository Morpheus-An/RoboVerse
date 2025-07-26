"""The pick up cube task from ManiSkill."""

from metasim.cfg.checkers import DetectedChecker, Relative2DSphereDetector
from metasim.cfg.objects import PrimitiveCubeCfg, PrimitiveCylinderCfg, RigidObjCfg
from metasim.constants import PhysicStateType
from metasim.utils import configclass

from .maniskill_task_cfg import ManiskillTaskCfg

goal_region_size = 0.05  # The size of the goal region in meters
goal_region_visible_size = 0.05  # The visible size of the goal region in meters


@configclass
class PokeCubeCfg(ManiskillTaskCfg):
    """The PokeCube task from ManiSkill.

    .. Description:

    ### 📦 Source Metadata (from ManiSkill)

    ### title:
    PokeCube
    ### group:
    Maniskill
    ### description:
    A simple task where the objective is to poke a red cube with a peg and push it to a target goal position.
    ### randomizations:
    - the peg's xy position is randomized on top of a table in the region [0.1, 0.1] x [-0.1, -0.1]. It is placed flat along it's length on the table
    - the cube's x-coordinate is fixed to peg's x-coordinate + peg half-length (0.12) + 0.1 and y-coordinate is randomized in range [-0.1, 0.1]. It is placed flat on the table
    - the cube's z-axis rotation is randomized in range [- pi/6, pi/6]
    - the target goal region is marked by a red/white circular target. The position of the target is fixed to be the cube xy position + [0.05 + goal_radius, 0]
    ### success:
    - the cube's xy position is within goal_radius (default 0.05) of the target's xy position by euclidean distance
    - the robot is static
    ### badges:
    - dense
    - sparse
    - demo
    ### official_url:
    https://maniskill.readthedocs.io/en/latest/tasks/table_top_gripper/index.html#pokecube-v1
    ### platforms:

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
        RigidObjCfg(
            name="peg",
            usd_path="roboverse_data/assets/maniskill/PokeCube/peg/usd/stick.usd",
            mjcf_path="roboverse_data/assets/maniskill/PokeCube/peg/mjcf/stick.xml",
            physics=PhysicStateType.RIGIDBODY,
            fix_base_link=False,
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
    traj_filepath = "roboverse_data/trajs/maniskill/poke_cube/v2/"
