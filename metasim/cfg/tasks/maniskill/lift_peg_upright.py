from metasim.cfg.checkers import AndOp, PositionShiftRangeChecker, RotationAxisAngleChecker
from metasim.cfg.objects import PrimitiveCubeCfg
from metasim.constants import PhysicStateType
from metasim.utils import configclass

from .maniskill_task_cfg import ManiskillTaskCfg

peg_length = 0.24
peg_widdth = 0.05


@configclass
class LiftPegUpRightCfg(ManiskillTaskCfg):
    """The lift peg upright from Maniskill.

    .. Description::

    ### title:
    lift_peg_upright

    ### group:
    maniskill

    ### description:
    Lift a peg upright on a table.

    ### randomizations:
    -

    ### success:
    - the absolute value of the peg's y euler angle is within 0.08 of pi/2 and the z position of the peg is within 0.005 of its half-length (0.12).

    ### badges:
    - demos

    ### official_url:
    https://maniskill.readthedocs.io/en/latest/tasks/table_top_gripper/index.html#liftpegupright-v1

    ### video_url:
    lift_peg_upright.mp4

    ### platforms:

    ### notes:
    """

    episode_length = 200
    objects = [
        PrimitiveCubeCfg(
            name="peg",
            size=[peg_length, peg_widdth, peg_widdth],
            mass=0.04,
            physics=PhysicStateType.RIGIDBODY,
            color=[1.0, 0.0, 0.0],
        ),
    ]

    traj_filepath = "roboverse_data/trajs/maniskill/lift_peg_upright/v2"

    upright_checker = RotationAxisAngleChecker(
        obj_name="peg",
        target_vector=[0, 0, 1],
        radian_range=0.08,
        axis="x",
    )

    lift_checker = PositionShiftRangeChecker(
        obj_name="franka",
        distance_lower=peg_length - 0.005,
        distance_upper=peg_length + 0.005,
        axis="z",
    )

    checker = AndOp([upright_checker, lift_checker])
