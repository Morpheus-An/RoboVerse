"""Task configurations for ManiSkill tasks."""

# ruff: noqa: F401

import importlib

__CANDIDATE_MODULES = [
    "peg_insertion_side",
    "pick_single_egad",
    "pick_single_ycb",
]


def __getattr__(name):
    from .draw_svg import DrawSVGCfg
    from .draw_triangle import DrawTriangleCfg
    from .lift_peg_upright import LiftPegUpRightCfg
    from .peg_insertion_side import PegInsertionSide0Cfg
    from .pick_cube_cfg import PickCubeCfg
    from .place_sphere_cfg import PlaceSphereCfg
    from .plug_charger_cfg import PlugChargerCfg
    from .poke_cube_cfg import PokeCubeCfg
    from .pull_cube_cfg import PullCubeCfg
    from .pull_cube_tool_cfg import PullCubeToolCfg
    from .push_cube_cfg import PushCubeCfg
    from .roll_ball_cfg import RollBallCfg
    from .stack_cube_cfg import StackCubeCfg
    from .stack_pyramid_cfg import StackPyramidCfg

    if name in locals():
        return locals()[name]

    # Lazy load modules
    for module_name in __CANDIDATE_MODULES:
        module = importlib.import_module(f".{module_name}", __name__)
        if name in module.__dict__:
            return getattr(module, name)

    raise AttributeError(f"module {__name__} has no attribute {name}")
