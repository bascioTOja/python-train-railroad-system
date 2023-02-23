import pygame
from dataclasses import dataclass

from classes import helpers
from classes.track_controller import TrackController
from classes.train_controller import TrainController
from enums.train_type import TrainType


@dataclass
class Game:
    size: tuple[int, int]
    fps: int
    run: bool = True
    pos: tuple[int, int] = (0, 0)

    def __post_init__(self):
        self.width = self.size[0]
        self.height = self.size[1]
        self.win = pygame.display.set_mode(self.get_size())
        self.clock = pygame.time.Clock()

        tracks, trains = helpers.create_tracks_and_trains()
        self.track_controller = TrackController()
        self.track_controller.tracks.extend(tracks)
        self.train_controller = TrainController(trains)

    def events(self):
        self.pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_up_events(event)

            if event.type == pygame.KEYDOWN:
                self.keydown_events(event)

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

    def draw(self, *args) -> None:
        self.win.fill((0, 0, 0))
        for item in args:
            item.draw(self.win)
        pygame.display.update()

    def update(self, *args) -> None:
        for item in args:
            item.update(self)

    def hover(self, *args) -> None:
        for item in args:
            item.hover(self.pos)

    def get_size(self) -> tuple[int, int]:
        return self.width, self.height

    def quit(self):
        self.run = False

    def mouse_button_up_events(self, event):
        if event.button == 1:
            self.track_controller.add_node(self.pos)
        elif event.button == 3:
            self.track_controller.remove_node(self.pos)

    def keydown_events(self, event):
        if event.key == pygame.K_SPACE:
            self.track_controller.create_track()
        if event.key == pygame.K_q:
            self.train_controller.remove_train(self.pos)
        if event.key == pygame.K_e:
            if (selected_track := self.track_controller.get_first_track_in_position(self.pos)) is not None:
                self.train_controller.add_train(TrainType.CLASSIC, selected_track, self.pos)

