from metasim.cfg.checkers import DetectedChecker, RelativeBboxDetector
from metasim.cfg.objects import PrimitiveSphereCfg, RigidObjCfg
from metasim.constants import PhysicStateType
from metasim.utils import configclass

from .maniskill_task_cfg import ManiskillTaskCfg


@configclass
class PlaceSphereCfg(ManiskillTaskCfg):
    """The place-sphere task from ManiSkill.

    .. Description:

    ### 📦 Source Metadata (from ManiSkill)

    ### title:
    PlaceSphere
    ### group:
    Maniskill
    ### description:
    Place the sphere into the shallow bin.
    ### randomizations:
    - The position of the bin and the sphere are randomized: The bin is initialized in [0, 0.1] x [-0.1, 0.1], and the sphere is initialized in [-0.1, -0.05] x [-0.1, 0.1]
    ### success:
    - The sphere is placed on the top of the bin. The robot remains static and the gripper is not closed at the end state.
    ### badges:
    - dense
    - sparse
    ### official_url:
    https://maniskill.readthedocs.io/en/latest/tasks/table_top_gripper/index.html#placesphere-v1
    ### platforms:

    ### notes:
    """

    objects = [
        RigidObjCfg(
            name="bin",
            usd_path="roboverse_data/assets/maniskill/PlaceSphere/bin/usd/PlaceSphere_bin.usd",
            mjcf_path="roboverse_data/assets/maniskill/PlaceSphere/bin/mjcf/PlaceSphere_bin.xml",
            physics=PhysicStateType.RIGIDBODY,
        ),
        PrimitiveSphereCfg(
            name="sphere",
            radius=0.03,
            mass=0.001,
            physics=PhysicStateType.RIGIDBODY,
            color=[1.0, 0.0, 0.0],
        ),
    ]
    episode_length = 250
    checker = DetectedChecker(
        obj_name="sphere",
        detector=RelativeBboxDetector(
            base_obj_name="bin",
            relative_pos=(0.0, 0.0, 0.04),
            relative_quat=(1.0, 0.0, 0.0, 0.0),
            checker_lower=(-0.02, -0.02, -0.02),
            checker_upper=(0.02, 0.02, 0.02),
            ignore_base_ori=True,
        ),
    )
    traj_filepath = "roboverse_data/trajs/maniskill/place_sphere/v2"
