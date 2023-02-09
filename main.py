import pygame

from classes.game import Game
from classes.track import Track
from classes.node import Node
from classes.train import Train

def main():
    game = Game((800, 600), 60)

    start_node = Node(400, 400)
    end_node = Node(200, 400)
    track = Track((100, 255, 100), start_node, end_node)

    train = Train(start_node.get(), track)

    start_node2 = Node(200, 200)
    end_node2 = Node(200, 100)
    track2 = Track((255, 100, 100), start_node2, end_node2)
    train2 = Train(start_node2.get(), track2)

    start_node3 = Node(100, 400)
    end_node3 = Node(200, 500)
    track3 = Track((255, 100, 255), start_node3, end_node3)
    train3 = Train(start_node3.get(), track3)


    node1 = Node(500, 100)
    node2 = Node(600, 200)
    track4 = Track((150, 150, 150), node1, node2)

    node3 = Node(600, 200)
    node4 = Node(500, 300)
    track5 = Track((150, 150, 150), node3, node4)

    track4.connected_with_end.append(track5)
    track5.connected_with_start.append(track4)

    node5 = Node(500, 300)
    node6 = Node(400, 200)
    track6 = Track((150, 150, 150), node5, node6)

    track5.connected_with_end.append(track6)
    track6.connected_with_start.append(track5)

    node7 = Node(400, 200)
    node8 = Node(500, 100)
    track7 = Track((150, 150, 150), node7, node8)

    track6.connected_with_end.append(track7)
    track7.connected_with_start.append(track6)

    track7.connected_with_end.append(track4)
    track4.connected_with_start.append(track7)

    train4 = Train(track4.start_node.get(), track4)

    tracks = [track, track2, track3, track4, track5, track6, track7]
    trains = [train, train2, train3, train4]

    while game.run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.run = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         pos = pygame.mouse.get_pos()
            #         for point in spline.points:
            #             if point.rect.collidepoint(pos):
            #                 selected_point = point
            #                 break
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
        game.draw(*tracks, *trains)
        game.clock.tick(game.fps)

pygame.quit()

if __name__ == "__main__":
    main()
