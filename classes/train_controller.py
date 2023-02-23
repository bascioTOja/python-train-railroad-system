from pygame import Surface
from typing import List, Tuple
from dataclasses import dataclass, field

from classes.track import Track
from classes.train import Train
from enums.train_type import TrainType


@dataclass
class TrainController:
    trains: List[Train] = field(default_factory=list)

    def update(self, game) -> None:
        for train in self.trains:
            train.update(game)

    def hover(self, pos: tuple[int, int]) -> None:
        for train in self.trains:
            train.hover(pos)

    def draw(self, win: Surface) -> None:
        for train in self.trains:
            train.draw(win)

    def remove_train(self, pos: Tuple[int, int]) -> None:
        if (train := self.get_first_train_in_position(pos)) is not None:
            self.trains.remove(train)
            train.delete()

    def add_train(self, train_type: TrainType, track: Track, pos: Tuple[int, int]) -> Train:
        train = Train(train_type, pos, track, track.start_node if track.start_node.rect.collidepoint(pos) else track.end_node)
        self.trains.append(train)

        return train

    def get_first_train_in_position(self, pos: Tuple[int, int]) -> Train | None:
        return next((train for train in self.trains if train.rect.collidepoint(pos)), None)
