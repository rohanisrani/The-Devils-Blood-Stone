# The Nobles
# The Devils Blood Cell 
# Rohan Israni , Vincent He
# After a long and hard day at work, you couldn’t
# wait to go home to see your cousin, Nina. When you
# get to her home you see that see is infected with
# something called Demon Freeze, a dangerous infection
# that’ll freeze them from inside out. You must go to
# the Noblesse Mansion to get the Devil’s Blood Stone
# which is the only cure to the disease.
# You have to get through the multiple levels of
# guardians protecting it, you have kill them to reach the Devil’s Blood Stone.

from gamelib import *

#---------------------------------- Game Startup ----------------------------

game = Game(1200,800,"The Devils Blood Cell")
bk = Image("Title_Screen.jpg",game)
bk.resizeTo(1200,800)

#----------------------------------- Story Variables ------------------------

story_1 = Image("Storyline_1.png",game)
story_2 = Image("Storyline_2.png",game)
story_3 = Image("Storyline_3.png",game)
story_4 = Image("Storyline_4.png",game)
story_5 = Image("Storyline_5.png",game)
story_7 = Image("Storyline_7.png",game)
story_7.resizeTo(game.width,game.height)
story_8 = Image("Storyline_8.png",game)
story_9 = Image("hell_story.png",game)
story_8.resizeTo(game.width,game.height)
story_9.resizeTo(game.width,game.height)
play = Animation("Play_Button.png",8,game,470/2,308/4,2)
title = Animation("title.png",8,game,878,624/8,2)
instruction = Image("instruction.png",game)
instruction.resizeTo(1200,800)
skill1 = Image("first_skill.png",game)
skill2 = Image("second_skill.png",game)
skill2.resizeTo(game.width,game.height)
click = Image("click.png",game)
click.resizeTo(700,100)
hero = Animation("hero.png",12,game,1920/3,1920/4,2)
wolf = Animation("wolf.png",8,game,1200/2,1536/4,2)
robot = Animation("robot.png",4,game,500/2,630/2,2)
zombie = Animation("zombie.png",12,game,2000/4,1752/3,2)
mansion = Image("bk.jpg",game)
mansion.resizeTo(1200,800) 
play.moveTo(620,375)
skill1.resizeTo(1200,800)
story_1.resizeTo(1200,800)
story_2.resizeTo(1200,800)
story_3.resizeTo(1200,800)
story_4.resizeTo(1200,800)
story_5.resizeTo(1200,800)
fireball1 = Animation("bosslv.png",90,game,2500/10,2250/9)
fireball1.resizeTo(60,60)
title.moveTo(600,285)
fireball1.visible = False
boom = Animation("boom.png",20,game,1000/5,1128/4)
boom.visible = False
hero.moveTo(1000,650)
hero.resizeBy(-70)
hero.kills = 0
hell = Animation("hell.png",8,game,1656/2,1432/4)
hell.resizeTo(1200,800)
game.setBackground(hell)
death = Image("dead.jpg",game)
death.resizeTo(game.width,game.height)


wolf = []
for index in range(45):
    wolf.append(Animation("wolf.png",8,game,1200/2,1536/4,2))
for index in range(45):
    speed = randint(4,8)
    wolf[index].setSpeed(speed,270)
    x = randint(-10000,50)
    y = randint(50,750)
    wolf[index].moveTo(x,y)
    wolf[index].resizeTo(150,150)
sword = []
for index in range(37):
    sword.append(Image("sword.png",game))
for index in range(37):
    speed = randint(4,8)
    sword[index].setSpeed(speed,270)
    x = randint(-10000,50)
    y = randint(50,750)
    sword[index].moveTo(x,y)
    sword[index].resizeTo(75,75)
robot = []
for index in range(45):
    robot.append(Animation("robot.png",4,game,500/2,630/2,2))
for index in range(45):
    speed = randint(4,8)
    robot[index].setSpeed(speed,270)
    x = randint(-10000,50)
    y = randint(50,750)
    robot[index].moveTo(x,y)
    robot[index].resizeTo(150,150)
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

#----------------------------------- Game Screen ----------------------------

#(Splash Screen)
while not game.over:
    game.processInput()

    bk.draw()
    title.draw()
    play.draw()
    if play.collidedWith(mouse)and mouse.LeftClick:
        game.over = True

    game.update(60)
game.over = False

#-------------------------------- Story Begins ------------------------------

#(Story 1)
while not game.over:
    game.processInput()
    mansion.draw()

    story_1.draw()
    click.draw()
    click.moveTo(800,700)
    if click.collidedWith(mouse)and mouse.LeftClick:
        game.over = True


    game.update(60)
game.over = False

#(Story 2)
while not game.over:
    game.processInput()

    story_2.draw()
    click.draw()
    click.moveTo(600,650)
    if click.collidedWith(mouse)and mouse.LeftClick:
        game.over = True

    game.update(60)
game.over = False

#(Story 3)
while not game.over:
    game.processInput()

    story_3.draw()
    click.draw()
    click.moveTo(800,650)
    if click.collidedWith(mouse)and mouse.LeftClick:
        game.over = True

    game.update(60)
game.over = False

#(Story 4) 
while not game.over:
    game.processInput()

    story_4.draw()
    click.draw()
    click.resizeTo(300,150)
    click.moveTo(200,700)
    if click.collidedWith(mouse)and mouse.LeftClick:
        game.over = True

    game.update(60)
game.over = False

#(Story 5)
while not game.over:
    game.processInput()

    story_5.draw()
    click.draw()
    click.resizeTo(700,100)
    click.moveTo(600,650)
    if click.collidedWith(mouse)and mouse.LeftClick:
        game.over = True

    game.update(60)
game.over = False

#-------------------------------- Story Ends Here --------------------------

while not game.over:
    game.processInput()
    mansion.draw()
    for index in range(37):
        wolf[index].move()
    for index in range(37):
        sword[index].move()
    hero.draw()
    for index in range(37):
        if hero.collidedWith(sword[index]):
            game.over = True
            
    for index in range(45):    
        if wolf[index].collidedWith(hero):
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
    
    for index in range(45):  
        if fireball1.collidedWith(wolf[index]):
            game.score +=1
            wolf[index].visible = False
            fireball1.visible = False
            boom.moveTo(wolf[index].x,wolf[index].y)
            boom.visible = True
    if hero.health <= 0:
        death.draw()

   
    game.displayScore()
    fireball1.move()
        


    game.update(60)
game.over = False

#Level 2
while not game.over:
    game.processInput()
    mansion.draw()
    for index in range(37):
        robot[index].move()
    for index in range(37):
        sword[index].move()
    hero.draw()
    for index in range(37):
        if hero.collidedWith(sword[index]):
            game.over = True
            
    for index in range(45):    
        if robot[index].collidedWith(hero):
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
   
    for index in range(45):  
        if fireball1.collidedWith(robot[index]):
            game.score +=1
            robot[index].visible = False
            fireball1.visible = False
            boom.moveTo(robot[index].x,robot[index].y)
            boom.visible = True
    if hero.health <= 0:
        death.draw()

    game.displayScore()
    fireball1.move()
    game.update(60)
game.over = False

#(boss story )
while not game.over:
    game.processInput()

    story_9.draw()
    click.draw()
    click.resizeTo(700,100)
    click.moveTo(600,650)
    if click.collidedWith(mouse)and mouse.LeftClick:
        game.over = True

    game.update(60)
game.over = False

#Boss LvL
while not game.over:
    game.processInput()
    hell.draw()
    game.scrollBackground("right",3)
    for index in range(50):
        demon[index].move()
    for index in range(37):
        sword[index].move()
    hero.draw()
    for index in range(37):
        if hero.collidedWith(sword[index]):
            hero.health -=25
            sword[index].visible = False

            
    for index in range(50):    
        if demon[index].collidedWith(hero):
            hero.health -=25
            demon[index].visible = False

        
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
    game.drawText("Heath: " + str(hero.health),hero.x,hero.y+20)


    if hero.health<=0:
        game.over = True
        
    
    for index in range(50):  
        if fireball1.collidedWith(demon[index]):
            game.score +=1
            demon[index].visible = False
            fireball1.visible = False
            boom.moveTo(demon[index].x,demon[index].y)
            boom.visible = True
    if hero.health <= 0:
        death.draw()

   
    game.displayScore()
    fireball1.move()
        


    game.update(60)
game.over = False


