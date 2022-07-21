from constants import *
from game.script.action import Action
from game.cast.point import Point


class MoveBarricadeAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        barricades = cast.get_actors(BARRICADE_GROUP)
        for barricade in barricades:
            if barricade == None:
                return

            body = barricade.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)