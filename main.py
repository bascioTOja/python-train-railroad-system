import pygame

from classes.game import Game
from classes.node import Node
from classes.track import Track
from classes.train import Train
from classes.track_controller import TrackController

def main():
    game = Game(size=(800, 600), fps=60)
    image = pygame.image.load("images/train.png")

    track_controller = TrackController()

    track = Track((100, 255, 100), Node(400, 400), Node(200, 400))

    train = Train(track.start_node.get(), track, image)

    track2 = Track((255, 100, 100), Node(200, 200), Node(200, 100))
    train2 = Train(track2.start_node.get(), track2, image)

    track3 = Track((255, 100, 255), Node(100, 400), Node(200, 500))
    train3 = Train(track3.start_node.get(), track3, image)


    track4 = Track((150, 150, 150), Node(500, 100), Node(600, 200))
    track5 = Track((150, 150, 150), Node(600, 200), Node(500, 300))

    track4.connected_with_end.append(track5)
    track5.connected_with_start.append(track4)

    track6 = Track((150, 150, 150), Node(500, 300), Node(400, 200))

    track5.connected_with_end.append(track6)
    track6.connected_with_start.append(track5)

    track7 = Track((150, 150, 150), Node(400, 200), Node(500, 100))

    track6.connected_with_end.append(track7)
    track7.connected_with_start.append(track6)

    track7.connected_with_end.append(track4)
    track4.connected_with_start.append(track7)

    train4 = Train(track4.start_node.get(), track4, image)

    track_controller.tracks.extend([track, track2, track3, track4, track5, track6, track7])
    trains = [train, train2, train3, train4]

    while game.run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    track_controller.add_node(pos)
                elif event.button == 3:
                    pos = pygame.mouse.get_pos()
                    track_controller.remove_node(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    track_controller.create_track()
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

        game.update(*trains)
        game.draw(track_controller, *trains)
        game.clock.tick(game.fps)

pygame.quit()

if __name__ == "__main__":
    main()
