from gamelib import *

game = Game(640,480,"Flappy Bird")

bk = Image("images\\day.png",game)
bk.resizeTo(game.width, game.height)
game.setBackground(bk)

bird = Animation("images\\bird.png",3,game,44,34,frate=6)

ring = Animation("images\\ring2.png",64,game,64,64)
ring.moveTo(35,430)

scoreFont = Font(black,36)

while not game.over:
    game.processInput()
    game.drawBackground()
    #bird.draw()
    ring.moveTo(mouse.x,mouse.y)

    bird.rotateTowards(ring)

    bird.moveTowards(ring,2)
    
    game.update(30)

game.drawText("Press [Enter] to Exit.",200,400, Font(black,40,green))
game.update()
game.wait(K_RETURN)
game.quit()
