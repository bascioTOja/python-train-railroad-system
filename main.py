import pygame

from classes.factories.track_factory import TrackFactory
from classes.game import Game
from classes.menu import Menu
from enums.track_type import TrackType


def main():
    game = Game(size=(800, 800), fps=60)
    track_factory = TrackFactory(game)
    menu = Menu(game)
    test_track = track_factory.create_track(TrackType.NORMAL, (415, 425), menu.rotate)

    game.track_controller.append_track(test_track)

    while game.run:
        game.hover(game.train_controller, game.track_controller) # TODO: Optimize and get the elements by checking if they are hovering, rather than checking by coordinates each time.
        game.events()
        game.update(game.train_controller)
        game.draw(game.track_controller, game.train_controller)
        game.clock.tick(game.fps)

pygame.quit()

if __name__ == "__main__":
    main()
