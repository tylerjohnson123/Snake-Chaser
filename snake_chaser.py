"""
Tyler Johnson
Last edit: June 14, 2024

Name: Snake Chaser

Description: A miner goes to try to find treasure in a castle. When the miner reaches the bottom of the castle,
a snake appears and chases after him. The miner ahs to jump form floor ot floor to try to escape the snake. If
the snake touches the miner the fails.

The higher the miner gets the better the score.

"""

import pygame, simpleGE, random

class Miner(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("miner.png")
        self.setSize(45, 45)
        self.position = ( 160, 25)

    def movement(self):
        if self.inAir:
            self.addForce(.5, 100)
            


        if self.y > 450:
            self.inAir = False
            self.y = 450
            self.dy  = 0
        


class Snake(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("snake.png")
        self.setSize(45, 45)
        self.position = (120, 0)




class Platform(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("platform.png")
        self.setSize(75, 25)
        self.position = (200, 200)




class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("background.jpg")

        self.miner = Miner(self)
        self.snake = Snake(self)
        self.platform = Platform(self)

        self.sprites = [self.platform, 
                        self.snake, 
                        self.miner ]


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()