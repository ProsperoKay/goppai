"""Board tile module"""


class Tile:
    """board tile"""

    def __init__(self) -> None:
        self.__value = 0

    def setvalue(self, value):
        """set tile value and return self"""
        self.__value = value
        return self

    def getvalue(self):
        """get tile value"""
        return self.__value

    def move_to(self, tile) -> int:
        """move tile value to another tile"""

        tile.setvalue(self.getvalue())
        self.setvalue(0)
        return self.__value

    def merge_with(self, tile) -> int:
        """merge tile value with another tile"""

        tile.setvalue(self.getvalue() * 2)
        self.setvalue(0)
        return tile.getvalue()
