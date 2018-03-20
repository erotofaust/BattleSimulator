# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 18:39:29 2018

@author: hoyong.kim
"""

class Skill:
    def __init__(self, attack_rate, attack_range, waiting_time, follow_through, stamina_consume, moving_range):
        self.attack_rate = attack_rate
        self.attack_range = attack_range
        self.waiting_time = waiting_time
        self.follow_through = follow_through
        self.stamina_consume = stamina_consume
        self.moving_range = moving_range
    
    