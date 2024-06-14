"""
Tyler Johnson
Last edit: June 14, 2024

Name: Snake Chaser

Description: A miner goes to try to find treasure in a castle. When the miner reaches the bottom of the castle,
a snake appears and chases after him. The miner ahs to jump form floor ot floor to try to escape the snake. If
the snake touches the miner the fails.

As of now it is more of an escape from the snake instead of a platformer. 

"""

import pygame, simpleGE, random


""" class Intro(simpleGE.Scene):
    def __init__(self):
        super().__init__()
    
    #Intro screen and input to start the game
        self.setImage("black.png")
        self.setSize = (640, 480)
        self.position = (320,240) """

        



class Miner(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
    
    #Miner size, position, speed, and gravity
        self.setImage("miner.png")
        self.setSize(75, 75)
        self.position = ( 320, 380)
        self.moveSpeed = 10
        self.jumpSpeed = 12
        self.addForce(5, 270)

    #Collision between the miner and the platforms
    def process(self):
        self.correction = (0, 0)
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
            self.correction = (10, 0)
        elif self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            self.correciton = (-10, 0)
        elif self.isKeyPressed(pygame.K_UP):
            self.y -= self.jumpSpeed
            self.correction = (0, 10)

        if self.collidesWith(self.scene.leftPlatform):
            self.x += self.correction[0]
            self.y += self.correction[1]
        if self.collidesWith(self.scene.rightPlatform):
            self.x += self.correction[0]
            self.y += self.correction[1]

        if self.y < 0:
            self.y = 0


class Snake(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)

    #Snake size, position, and speed
        self.setImage("snake.png")
        self.setSize(65, 65)
        self.position = (175, 450)
        self.chaseSpeed = 2

    #Snake chases the miner
    def process(self):
        miner = self.scene.miner 
        if self.x < miner.x:
            self.x += self.chaseSpeed
        elif self.x > miner.x:
            self.x -= self.chaseSpeed
        
        if self.y < miner.y:
            self.y += self.chaseSpeed
        elif self.y > miner.y:
            self.y -= self.chaseSpeed

    #If snake touches the miner the game ends
        if self.collidesWith(miner):
            self.scene.endGame()

class Platform(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
    #Platform size, position, and speed
        self.colorRect("black", (275, 50))
        self.position = (335, 0)
        self.dy = 7

    # If the platform gets to low it resets it and sets a new gap and position
    def checkBounds(self):
        if self.y >= 450:
            self.scene.reset()

    def update(self):
        self.checkBounds()
        super().update()

        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("background.jpg")
        self.dy = 2
        self.miner = Miner(self)
        self.snake = Snake(self)
        self.leftPlatform = Platform(self)
        self.rightPlatform = Platform(self)
        self.gap = 400
       

        self.sprites = [self.leftPlatform,
                        self.rightPlatform,
                        self.snake, 
                        self.miner ]
        self.reset()

    #Resets the position and gap size of the platforms
    def reset(self):
        self.leftPosition = random.randint(0, 400)
        self.rightPosition = self.leftPosition + self.gap
        self.leftPlatform.position = (self.leftPosition, 0)  
        self.rightPlatform.position = (self.rightPosition, 0)  

    #End the game if the snake touches the miner
    def endGame(self):
        quit()

    #Run order of the game
def main():
    """ game = Intro() """
    game = Game()
    game.start()


if __name__ == "__main__":
    main()