from pygame import image
from typing import Optional, Union

from enums.train_type import TrainType

_TrainTypeClasses = Union['ClassicTrain', 'FastClassicTrain']

def get_train_type_class(train_type: TrainType) -> Optional[_TrainTypeClasses]:
    match train_type:
        case TrainType.CLASSIC:
            return ClassicTrain()
        case TrainType.FAST_CLASSIC:
            return FastClassicTrain()
        case _:
            return None

class ClassicTrain:
    image = image.load("images/train.png")
    speed = 80

class FastClassicTrain:
    image = image.load("images/train.png")
    speed = 150
