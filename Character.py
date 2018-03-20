# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 12:38:32 2018

@author: hoyong.kim
"""

class Character:
    def __init__(self, name, hp, attack, defence, position, moving_speed, skill_1, skill_2):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.position = position
        self.moving_speed = moving_speed
        self.skill_1 = skill_1
        self.skill_2 = skill_2
        self.canaction = True
        
        
    def attackTo(self, enemy):
        print("%s는 %s를(을) 공격했다!!" % (self.name, enemy.name))
        enemy.defenceFrom(self.attack)


    def defenceFrom(self, attack):
        damage = attack - self.defence
        self.hp = self.hp-damage
        print("%s는 %d의 데미지를 입었다! 남은 체력은 %d!" %(self.name, damage, self.hp))
    
    
    def moveForward(self):
        if self.canaction == True:
            movingRange = self.moving_speed * frame
            self.position = self.position + movingRange
            print("%s는 앞으로 %f 이동했다!! 현재 위치는 %f!" % (self.name, movingRange, self.position))

    
    def moveBackward(self):
        if self.canaction == True:
            movingRange = self.moving_speed * frame
            self.position = self.position - movingRange
            print("%s는 뒤로 %f 이동했다!! 현재 위치는 %f!" % (self.name, movingRange, self.position))
    
    
    def waiting(self):
        print("스킬 사용 대기 중입니다")
        self.canaction = False
        
    
    def followthrough(self):
        print("스킬 사용 후 경직 중입니다")
        self.canaction = False

        