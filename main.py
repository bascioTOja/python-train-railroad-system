import pygame

from classes.game import Game

def main():
    game = Game(size=(800, 600), fps=60)

    while game.run:
        game.events()
        game.update(game.train_controller)
        game.hover(game.train_controller, game.track_controller)
        game.draw(game.track_controller, game.train_controller)
        game.clock.tick(game.fps)

pygame.quit()

if __name__ == "__main__":
    main()
