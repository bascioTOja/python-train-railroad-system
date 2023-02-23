from classes.node import Node
from classes.track import Track
from classes.train import Train
from enums.train_type import TrainType

def create_tracks_and_trains() -> tuple[list[Track], list[Train]]:
    track = Track((100, 255, 100), Node(400, 400), Node(200, 400))

    train = Train(TrainType.CLASSIC, track.start_node.get(), track)

    track2 = Track((255, 100, 100), Node(200, 200), Node(200, 100))
    train2 = Train(TrainType.CLASSIC, track2.start_node.get(), track2)

    track3 = Track((255, 100, 255), Node(100, 400), Node(200, 500))
    train3 = Train(TrainType.CLASSIC, track3.start_node.get(), track3)


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

    train4 = Train(TrainType.FAST_CLASSIC, track4.start_node.get(), track4)

    return [track, track2, track3, track4, track5, track6, track7], [train, train2, train3, train4]
