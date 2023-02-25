import pygame

from classes.game import Game

def main():
    game = Game(size=(800, 600), fps=60)

    while game.run:
        game.hover(game.train_controller, game.track_controller)  #TODO: Optimize and get the elements by checking if they are hovering, rather than checking by coordinates each time.
        game.events()
        game.update(game.train_controller)
        game.draw(game.track_controller, game.train_controller)
        game.clock.tick(game.fps)

pygame.quit()

if __name__ == "__main__":
    main()
