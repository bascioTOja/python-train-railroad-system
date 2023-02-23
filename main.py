import pygame

from classes.game import Game

from enums.train_type import TrainType


def main():
    game = Game(size=(800, 600), fps=60)

    while game.run:
        game.pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    game.track_controller.add_node(game.pos)
                elif event.button == 3:
                    game.track_controller.remove_node(game.pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.track_controller.create_track()
                if event.key == pygame.K_q:
                    game.train_controller.remove_train(game.pos)
                if event.key == pygame.K_e:
                    if (selected_track := game.track_controller.get_first_track_in_position(game.pos)) is not None:
                        game.train_controller.add_train(TrainType.CLASSIC, selected_track, game.pos)
            # elif event.type == pygame.MOUSEBUTTONUP:
            #     if event.button == 1:
            #         selected_point = None
            #         spline.positions = spline.evaluate_spline(spline.t)
            #
            # elif event.type == pygame.MOUSEMOTION:
            #     cursor_position = pygame.mouse.get_pos()
            #     if selected_point:
            #         pos = pygame.mouse.get_pos()
            #         spline.positions = spline.evaluate_spline(spline.t)
            #         selected_point.x, selected_point.y = pos
            #         selected_point.rect.x, selected_point.rect.y = selected_point.x - selected_point.size // 2, selected_point.y - selected_point.size // 2

        game.update(game.train_controller)
        game.hover(game.train_controller, game.track_controller)
        game.draw(game.track_controller, game.train_controller)
        game.clock.tick(game.fps)

pygame.quit()

if __name__ == "__main__":
    main()
