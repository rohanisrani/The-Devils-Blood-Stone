from gamelib import *
game = Game(1200,800,"The Devils Blood Cell")

hero = Animation("hero.png",12,game,1920/3,1920/4,2)
hero.moveTo(1000,650)
hero.resizeBy(-70)
fireball1 = Animation("bosslv.png",90,game,2500/10,2250/9)
fireball1.resizeTo(60,60)
fireball1.visible = True

demon = []
for index in range(150):
    demon.append(Animation("demon.png",16,game,1172/4,1116/4))
for index in range(150):
    speed = randint(4,8)
    demon[index].setSpeed(speed,270)
    x = randint(-10000,50)
    y = randint(50,750)
    demon[index].moveTo(x,y)
    demon[index].resizeTo(75,75)
demon[index].resizeTo(200,200)
    
hell = Animation("hell.png",8,game,1656/2,1432/4)
hell.resizeTo(1200,800)
game.setBackground(hell)




while not game.over:
    game.processInput()
    
    game.scrollBackground("right",3)
    for index in range(150):
        demon[index].move()
    
    
    hero.draw()
            
    for index in range(150):    
        if demon[index].collidedWith(hero):
            game.over = True
        
    if keys.Pressed[K_SPACE]:
        fireball1.moveTo(hero.x,hero.y)
        fireball1.setSpeed(45,90)
        fireball1.visible = True

    if keys.Pressed[K_w]:
        hero.y -=15
    if keys.Pressed[K_s]:
        hero.y +=15
    if keys.Pressed[K_a]:
        hero.x -=15
    if keys.Pressed[K_d]:
        hero.x +=15
    
        
    
    for index in range(150):  
        if fireball1.collidedWith(demon[index]):
            game.score +=1
            demon[index].visible = False
            fireball1.visible = False
            

    if game.score>=30:
        game.over = True
        
    
   
    game.displayScore()
    fireball1.move()
        


    game.update(30)
