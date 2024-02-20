from random import choice

from .tile import Tile


TILE_VALUES = [pow(2, x) for x in range(1, 11)]
DOMINANT_VALUE = [2, 2, 2, 2, 2, 2, 2, 4]


class Board:
    """
    Board of tiles
    """

    DOMINANT_VALUE = [2, 2, 2, 4]

    def __init__(self, size=4):
        self.size = size
        self.tiles = [[Tile() for _ in range(self.size)] for _ in range(self.size)]
        self.reset()

    def move_tiles(self, direction: str) -> int:
        """
        Move the tiles in the given direction.

        Args:
            direction: A string representing the direction in which to move the tiles.

        Returns:
            int: The score of the move.
        """
        score = 0

        directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        delta_y, delta_x = directions[direction]

        # Create a new grid
        new_tiles = [[Tile() for _ in range(self.size)] for _ in range(self.size)]

        # Traverse the grid in the correct order
        traverse_order = {
            "up": [(x, y) for x in range(self.size) for y in range(self.size)],
            "down": [
                (x, y) for x in range(self.size - 1, -1, -1) for y in range(self.size)
            ],
            "left": [(x, y) for y in range(self.size) for x in range(self.size)],
            "right": [
                (x, y) for y in range(self.size) for x in range(self.size - 1, -1, -1)
            ],
        }

        for x, y in traverse_order[direction]:
            if self.tiles[y][x].getvalue() != 0:
                new_y, new_x = y, x

                # Keep moving the tile in the direction
                while (
                    0 <= new_y + delta_y < self.size
                    and 0 <= new_x + delta_x < self.size
                    and new_tiles[new_y + delta_y][new_x + delta_x].getvalue() == 0
                ):
                    new_y += delta_y
                    new_x += delta_x

                # Merge the tiles if they have the same value
                if new_tiles[new_y][new_x].getvalue() == self.tiles[y][x].getvalue():
                    new_tiles[new_y][new_x].setvalue(
                        new_tiles[new_y][new_x].getvalue() * 2
                    )
                    score += new_tiles[new_y][new_x].getvalue()
                else:
                    # Move the tile to the new location
                    new_tiles[new_y][new_x].setvalue(self.tiles[y][x].getvalue())

        self.tiles = new_tiles

        return score

    def clear(self):
        self.tiles = [[Tile() for _ in range(self.size)] for _ in range(self.size)]

    def reset(self):
        self.tiles = [[Tile() for _ in range(self.size)] for _ in range(self.size)]
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        y, x = choice(
            [
                (i, j)
                for i in range(self.size)
                for j in range(self.size)
                if self.tiles[i][j].getvalue() == 0
            ]
        )
        value = choice(self.DOMINANT_VALUE)
        self.tiles[y][x].setvalue(value)

    def set_tiles(self, tiles):
        """
        Set the tiles of the board to the given values.

        Args:
            tiles (List[List[str]]): The new values for the tiles.

        Raises:
            ValueError: If the dimensions of the new tiles do not match the dimensions of the board.

        Returns:
            None
        """
        row_size = col_size = len(self.tiles)

        if len(tiles) != row_size or len(tiles[0]) != col_size:
            raise ValueError(
                f"List provided doesn't match the sizes of this board ({row_size} x {col_size})"
            )

        self.clear()
        self.tiles = [
            [x.setvalue(y) for x, y in zip(i, j)] for i, j in zip(self.tiles, tiles)
        ]

    def __str__(self) -> str:
        string = ""
        for _ in self.tiles:
            string += "  ".join([f"{x.getvalue()}" for x in _])
            string += "\n"

        return string
