import Character
import DataManager as dm
import random


if __name__ == "__main__":

    character_data = dm.readData('Character')
    skill_data = dm.readData('Skill')
    
    win_1 = 0
    win_2 = 0
    draw = 0

    

    for i in range(0,10):
        b = True
            
    
        char1 = Character.Character(1, character_data, -3)
        char2 = Character.Character(4, character_data, 3)
        
        while(b):
            
            char1.staminaRecov()
            char2.staminaRecov()
    
            char1.statusCheck()
            char1_rand = random.random()
            
            if char1_rand < 0.25:
                char1.moveLeft() 
            elif 0.25 <= char1_rand < 0.5:
                char1.moveRight()
            elif 0.5 <= char1_rand < 0.75:
                char1.useSkill(skill_data, 1, char2)
            elif 0.75 <= char1_rand <= 1:
                char1.useSkill(skill_data, 2, char2)
            
            
            char2.statusCheck()
            char2_rand = random.random()
    
            if char2_rand < 0.25 and char2.position > -10:
                char2.moveLeft()
            elif 0.25 <= char2_rand < 0.5 and char2.position < 10:
                char2.moveRight()
            elif 0.5 <= char2_rand < 0.75:
                char2.useSkill(skill_data, 1, char1)
            elif 0.75 <= char2_rand <= 1:
                char2.useSkill(skill_data, 2, char1)
            
            if char1.hp <= 0 and char2.hp <= 0:
                print("비겼습니다")
                b = False 
                draw += 1
                
            elif char2.hp <= 0:
                print("%s이 이겼습니다" % char1.name)
                b = False
                win_1 += 1
    
            elif char1.hp <= 0:
                print("%s이 이겼습니다" % char2.name)    
                b = False
                win_2 += 1
        

