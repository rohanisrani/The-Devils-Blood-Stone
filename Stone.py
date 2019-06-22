from gamelib import *
game = Game(1200,800,"The Devils Blood Cell")
bk = Image("Title_Screen.jpg",game)
bk.resizeTo(1200,800)

mansion = Image("bk.jpg",game)
game.setBackground(mansion)

hero = Animation("hero.png",12,game,1920/3,1920/4,2)
hero.moveTo(1000,650)
hero.resizeBy(-70)
play = Animation("Play_Button.png",8,game,470/2,308/4,2)
gem = Animation("prize.png",63,game,3464/7,2974/9)
mansion.resizeTo(1200,800)
gem.resizeTo(250,250)
gem.moveTo(200,570)
gem.setSpeed(1,270)
while not game.over:
    game.processInput()

    bk.draw()
    play.draw()
    if play.collidedWith(mouse)and mouse.LeftClick:
        game.over = True

    game.update(60)
game.over = False


while not game.over:
    game.processInput()
    mansion.draw()
    game.scrollBackground("right",3)
    
    hero.draw()
    gem.move()
    



    

    if keys.Pressed[K_w]:
        hero.y -=15
    if keys.Pressed[K_s]:
        hero.y +=15
    if keys.Pressed[K_a]:
        hero.x -=15
    if keys.Pressed[K_d]:
        hero.x +=15

    if hero.collidedWith(gem):
        game.over = True
    

    game.update(60)
