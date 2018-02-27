from typing import Tuple
from planet import Direction

class CommClient:

    def __init__(self, planet, mqtt_client):
        self.planet = planet
        self.client = mqtt_client
        self.client.on_message = self.__on_message

    def __on_message(self, client, data, message):
        """ In this method you will define how to react to incoming messages """
        pass

    def send(self, message: str):
        """ Send messages to the mqtt-server """
        pass

    def parse_path(self, message: str) -> Tuple[Tuple[int, int, Direction], Tuple[int, int, Direction]]:
        """ Parse a message to a path """
        pass

    def parse_target(self, message: str) -> Tuple[int, int]:
        """ Parse a recieved message to a target node """
        pass
