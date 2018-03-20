import numpy as np
import pandas as pd
import DataManager as dm

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 12:38:32 2018

@author: hoyong.kim
"""

class Character:
    def __init__(self, id, character_data, position):
        
        self.position = position
        self.can_action = True
        self.freeze_frame = 0
        self.stamina = 100
        self.damage_frame = [-1,-1,-1,-1,-1]

        self.name = character_data.at[int(np.where(character_data["id"] == id)[0]), "name"]
        self.hp = character_data.at[int(np.where(character_data["id"] == id)[0]), "hp"]
        self.attack = character_data.at[int(np.where(character_data["id"] == id)[0]), "attack"]
        self.defence = character_data.at[int(np.where(character_data["id"] == id)[0]), "defence"]
        self.moving_speed = character_data.at[int(np.where(character_data["id"] == id)[0]), "moving_speed"]
        self.skill_1 = character_data.at[int(np.where(character_data["id"] == id)[0]), "skill_1"]
        self.skill_2 = character_data.at[int(np.where(character_data["id"] == id)[0]), "skill_2"]

    def staminaRecov(self):
        if self.stamina < 100:
            self.stamina += 1
                
    def defenceFrom(self, attack, min_range, max_range):
        if min_range < self.position < max_range:
            damage = attack - self.defence
            self.hp = self.hp-damage
            print("%s는 %d의 데미지를 입었다! 남은 체력은 %d!" %(self.name, damage, self.hp))
        else:
            print("하지만 %s는(은) 적의 공격을 피했다" % self.name)
    
    
    def moveRight(self):
        if self.can_action == True:
            movingRange = self.moving_speed
            self.position += movingRange
            if self.position > 5:
                self.position = 5
            print("%s는 오른쪽으로 %f 이동했다!! 현재 위치는 %f!" % (self.name, movingRange, self.position))

    
    def moveLeft(self):
        if self.can_action == True:
            movingRange = self.moving_speed
            self.position -= movingRange
            if self.position < -5:
                self.position = -5
            print("%s는 왼쪽으로 %f 이동했다!! 현재 위치는 %f!" % (self.name, movingRange, self.position))
    
    
    def statusCheck(self):
        if self.freeze_frame == 0:
            self.can_action = True

        else:
            self.freeze_frame -= 1
            
        if self.damage_frame[3] == 0:
            attack = self.damage_frame[1]
            min_range = self.damage_frame[4] - self.damage_frame[2]
            max_range = self.damage_frame[4] + self.damage_frame[2]
            self.damage_frame[0].defenceFrom(attack, min_range, max_range)
            print("%s는 %s를(을) 범위 %f~%f로 공격했다!!" % (self.name, self.damage_frame[0].name, min_range, max_range))
            self.damage_frame[3] = -1
        else:
            self.damage_frame[3] -= 1
            

    
    def useSkill(self, skill_data, skill_index, enemy):
        if self.can_action == True:
            self.can_action = False
            
            if skill_index == 1:
                skill = skill_data.iloc[int(np.where(skill_data["id"] == self.skill_1)[0])]
                
            elif skill_index == 2:
                skill = skill_data.iloc[int(np.where(skill_data["id"] == self.skill_2)[0])]
                
            self.freeze_frame += skill[3] + skill[4]
            self.stamina -= skill[5]
            self.position += skill[6]
            self.damage_frame = [enemy, skill[1] * self.attack, skill[2], skill[3], self.position]               
        
            


