from copy import deepcopy


class Grid:
    def __init__(self, width, height):
        self.array = [[None for x in range(width)] for y in range(height)]
        self.width = width
        self.height = height

    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """

    def get(self, x, y):
        if self.in_bounds(x, y):
            return self.array[y][x]

    def set(self, x, y, value):
        if self.in_bounds(x, y):
            self.array[y][x] = value
            return (None)

    def in_bounds(self, x, y):
        if (x >= 0 and x < self.width and y >= 0 and y < self.height):
            return True
        raise IndexError

    def __str__(self):

        return f'Grid({self.height}, {self.width}, first = {self.array[0][0]})'

    def __repr__(self):
        return f'Grid.build({repr(self.array)})'

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other.array
        elif isinstance(other, list):
            return self.array == other
        else:
            return False

    @staticmethod
    def check_list_malformed(lst):
        if not isinstance(lst, list):
            raise ValueError
        if len(lst) == 0:
            raise ValueError
        for l in lst:
            if not isinstance(l, list):
                raise ValueError
            if len(l) != len(lst[0]):
                raise ValueError

    @staticmethod
    def build(lst):
        Grid.check_list_malformed(lst)
        height = len(lst)
        width = len(lst[0])
        new_grid = Grid(width, height)
        new_grid.array = deepcopy(lst)
        return new_grid

    def copy(self):
        return Grid.build(self.array)