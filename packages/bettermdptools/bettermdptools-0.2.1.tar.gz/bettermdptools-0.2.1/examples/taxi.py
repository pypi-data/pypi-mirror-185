# -*- coding: utf-8 -*-

import gym
import pygame
from algorithms.rl import QLearner as QL
from algorithms.planning import ValueIteration as VI
from algorithms.planning import PolicyIteration as PI
from examples.test_env import TestEnv


class Taxi:
    def __init__(self):
        self.env = gym.make('Taxi-v3', render_mode=None)


if __name__ == "__main__":

    taxi = Taxi()

    # VI/PI
    # V, V_track, pi = VI(taxi.env.P).value_iteration()
    # V, V_track, pi = PI(taxi.env.P).policy_iteration()

    # Q-learning
    QL = QL(taxi.env)
    Q, V, pi, Q_track, pi_track = QL.q_learning()

    test_scores = TestEnv.test_env(env=taxi.env, render=True, user_input=False, pi=pi)
