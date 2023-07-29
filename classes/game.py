import pygame
from dataclasses import dataclass

from classes import helpers
from classes.track_controller import TrackController, connect_tracks
from classes.train_controller import TrainController
from enums.train_type import TrainType


@dataclass
class Game:
    size: tuple[int, int]
    fps: int
    run: bool = True
    pos: tuple[int, int] = (0, 0)
    grid_size: int = 32
    grid_mode: bool = True
    node_editor: bool = True

    def __post_init__(self):
        self.width = self.size[0]
        self.height = self.size[1]
        self.win = pygame.display.set_mode(self.get_size())
        self.clock = pygame.time.Clock()

        tracks, trains = helpers.create_tracks_and_trains()
        self.track_controller = TrackController()
        self.track_controller.tracks.extend(tracks)
        self.train_controller = TrainController(trains)
        self.hold = []

    def events(self) -> None:
        if self.grid_mode:
            x, y = pygame.mouse.get_pos()
            self.pos = x // self.grid_size * self.grid_size, y // self.grid_size * self.grid_size
        else:
            self.pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_down_events(event)

            elif event.type == pygame.MOUSEMOTION:
                self.mouse_motion_events()

            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_up_events(event)


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

    def quit(self) -> None:
        self.run = False

    def keydown_events(self, event) -> None:
        if event.key == pygame.K_SPACE:
            self.track_controller.create_track()
        if event.key == pygame.K_q:
            self.train_controller.remove_train(self.pos)
        if event.key == pygame.K_g:
            self.grid_mode = not self.grid_mode
        if event.key == pygame.K_e:
            if (selected_track := self.track_controller.get_first_track_in_position(self.pos)) is not None:
                self.train_controller.add_train(TrainType.CLASSIC, selected_track, self.pos)

    def mouse_button_down_events(self, event) -> None:
        if event.button == 1:
            self.hold = self.track_controller.get_nodes_in_position(self.pos, all_must_by_unlock=True)
            for hold_item in self.hold:
                hold_item.set_block(True)

    def mouse_motion_events(self) -> None:
        if self.hold:
            for hold_item in self.hold:
                hold_item.move(self.pos)

    def mouse_button_up_events(self, event) -> None:
        if self.hold:
            pos = self.track_controller.snap_pos_to_node(self.pos)
            tracks_to_connect = (track for track in self.track_controller.get_tracks_in_position(pos, with_blocked=True) if track.start_node not in self.hold or track.end_node not in self.hold)
            for hold_item in self.hold:
                hold_item.move(pos)
                hold_item.set_block(False)
                for track_to_connect in tracks_to_connect:
                    connect_tracks(hold_item.track, track_to_connect)
            self.hold.clear()

        if event.button == 1:
            self.track_controller.add_node(self.pos)
        elif event.button == 3:
            self.track_controller.remove_node(self.pos)


