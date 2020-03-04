import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import gym

# 超参数
BATCH_SIZE = 32
LR = 0.01                   # learning rate
EPSILON = 0.9               # 最优选择动作百分比
GAMMA = 0.9                 # 奖励递减参数
TARGET_REPLACE_ITER = 100   # Q 现实网络的更新频率
MEMORY_CAPACITY = 2000      # 记忆库大小
env = gym.make('CartPole-v0')   # 立杆子游戏
env = env.unwrapped
N_ACTIONS = env.action_space.n  # 杆子能做的动作
N_STATES = env.observation_space.shape[0]   # 杆子能获取的环境信息数