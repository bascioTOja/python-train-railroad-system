import pygame
from enums.train_type import TrainType


def get_train_type_class(type: TrainType):
    match type:
        case TrainType.CLASSIC:
            return ClassicTrain()
        case TrainType.FAST_CLASSIC:
            return FastClassicTrain()
        case _:
            return None

class ClassicTrain:
    image = pygame.image.load("images/train.png")
    speed = 80

class FastClassicTrain:
    image = pygame.image.load("images/train.png")
    speed = 150
