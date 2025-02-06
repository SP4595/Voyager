import os.path
import time
import warnings
from typing import SupportsFloat, Any, Tuple, Dict

import requests
import json

import gymnasium as gym
from gymnasium.core import ObsType

import voyager.utils as U

from .minecraft_launcher import MinecraftInstance
from .process_monitor import SubprocessMonitor
from env.voyager_env import StarDojoVoyagerEnv


class VoyagerEnv(gym.Env):
    def __init__(
        self,
        configs : dict,
    ):
        self.env = StarDojoVoyagerEnv(**configs)

    def step(
        self,
        code: str,
        programs: str = "",
    ) -> Tuple[ObsType, SupportsFloat, bool, bool, Dict[str, Any]]:
        data = {
            "code": code,
            "programs": programs
        }
        return self.env.step(data)
    
    def obs(self):
        return self.env.get_obs()
        

    def render(self):
        raise NotImplementedError("render is not implemented")

    def reset(self) -> Tuple[ObsType, Dict[str, Any]]:
        return self.reset()

    def close(self):
        self.env.close()
       

    def pause(self):
        raise NotImplementedError("pause is not implemented")

    def unpause(self):
        raise NotImplementedError("unpause is not implemented")
