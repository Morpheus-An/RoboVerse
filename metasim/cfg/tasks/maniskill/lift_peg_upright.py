from metasim.cfg.checkers import RotationAxisAngleChecker, PositionShiftRangeChecker
from metasim.cfg.checkers import AndOp, RotationShiftChecker
from metasim.cfg.checkers.detectors import RelativeBboxDetector
from metasim.cfg.objects import PrimitiveCubeCfg
from metasim.constants import PhysicStateType
from metasim.utils import configclass

from .maniskill_task_cfg import ManiskillTaskCfg

peg_length = 0.24
peg_widdth = 0.05


@configclass
class LiftPegUpRightCfg(ManiskillTaskCfg):
    """The lift peg upright from Maniskill

    The robot is tasked to lift a peg upright
    checker: Check if the angle between the x axis of the peg and the y of world coordinate is within a 0.08 radians
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
        target_vector=[0,0,1],
        radian_range = 0.08,
        axis="x",
    )

    lift_checker = PositionShiftRangeChecker(
        obj_name="franka",
        distance_lower=peg_length - 0.05,
        distance_upper=peg_length + 0.05,
        axis="z",
    )

    checker = AndOp([upright_checker,lift_checker])
