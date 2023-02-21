from typing import List, Tuple
from dataclasses import dataclass, field

from classes.track import Track
from classes.train import Train

@dataclass
class TrainController:
    trains: List[Train] = field(default_factory=list)

    def update(self, game):
        for train in self.trains:
            train.update(game)

    def hover(self, pos):
        for train in self.trains:
            train.hover(pos)

    def draw(self, win):
        for train in self.trains:
            train.draw(win)

    def remove_train(self, pos: Tuple[int, int]):
        if (train := self.get_first_train_in_position(pos)) is not None:
            self.trains.remove(train)
            train.delete()

    def add_train(self, track: Track, pos: Tuple[int, int], image):
        self.trains.append(Train(pos, track, image, track.start_node if track.start_node.rect.collidepoint(pos) else track.end_node))

    def get_first_train_in_position(self, pos: Tuple[int, int]) -> Train | None:
        return next((train for train in self.trains if train.rect.collidepoint(pos)), None)
