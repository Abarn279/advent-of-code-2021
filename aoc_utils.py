from collections import defaultdict

v2Cache = {}
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cached_string = f'{self.x},{self.y}'
    @staticmethod
    def create(x, y):
        if (x, y) in v2Cache:
            return v2Cache[(x, y)]
        v = Vector2(x, y)
        v2Cache[(x, y)] = v
        return v
    def to_tuple(self):
        return (self.x, self.y)
    def to_yx_tuple(self):
        return (self.y, self.x)
    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)
    def sqr_magnitude(self):
        return self.x ** 2 + self.y ** 2
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x * other, self.y * other)
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash(self.cached_string)
    def __repr__(self):
        return 'x: ' + str(self.x) + ', y: ' + str(self.y)
    def __str__(self):
        return self.__repr__()

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def to_tuple(self):
        return (self.x, self.y, self.z)
    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)
    def clone(self):
        return Vector3(self.x, self.y, self.z)
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector3(self.x * other, self.y * other, self.z * other)
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    def __hash__(self):
        return hash(f'{self.x},{self.y},{self.z}')
    def __repr__(self):
        return 'x: ' + str(self.x) + ', y: ' + str(self.y) + ', z: ' + str(self.z)
    def __str__(self):
        return self.__repr__()

class Vector4(Vector3):
    def __init__(self, x, y, z, t):
        self.t = t
        super().__init__(x, y, z)
    def to_tuple(self):
        return (self.x, self.y, self.z, self.t)
    def manhattan_distance(self, other):
        return super().manhattan_distance(other) + abs(self.t - other.t)
    def __repr__(self):
        return super().__repr__() + ', t: ' + str(self.t)
    def __add__(self, other):
        return Vector4(self.x + other.x, self.y + other.y, self.z + other.z, self.t + other.t)
    def __hash__(self):
        return hash(f'{self.x},{self.y},{self.z},{self.t}')
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z, self.t == other.t

class Grid2d:
    ''' A 2d grid that has 0,0 at the top-left corner. '''

    def __init__(self, default_val, initial_values = None):
        self._grid = defaultdict(lambda: default_val)
        self._max_x = 0
        self._min_x = 0
        self._max_y = 0
        self._min_y = 0
        self._default_val = default_val
        self._initial_values = initial_values

        if initial_values is not None:
            for y in range(len(initial_values)):
                for x in range(len(initial_values[y])):
                    self._grid[Vector2.create(x, y)] = initial_values[y][x]
                    self._max_x = max(self._max_x, x)
                    self._min_x = min(self._min_x, x)
                    self._max_y = max(self._max_y, y)
                    self._min_y = min(self._min_y, y)

    def copy(self):
        copy = Grid2d(self._default_val)
        min_b, max_b = self.get_bounds()
        for y in range(min_b.y, max_b.y + 1):
            for x in range(min_b.x, max_b.x + 1):
                copy[Vector2.create(x, y)] = self._grid[Vector2.create(x, y)]
        return copy

    def get_bounds(self):
        ''' Get position bounds of this grid. Tuple of min position (x,y) and max position (x,y) '''
        return (Vector2.create(self._min_x, self._min_y), Vector2.create(self._max_x, self._max_y))

    def values(self):
        return self._grid.values()

    def __contains__(self, key: Vector2):
        return key in self._grid

    def __setitem__(self, pos: Vector2, val):
        self._grid[pos] = val
        self._max_x = max(self._max_x, pos.x)
        self._min_x = min(self._min_x, pos.x)
        self._max_y = max(self._max_y, pos.y)
        self._min_y = min(self._min_y, pos.y)
    def __getitem__(self, key: Vector2):
        return self._grid[key]
    def __str__(self):
        st = ""
        for y in range(self._min_y, self._max_y + 1):
            line = ""
            for x in range(self._min_x, self._max_x + 1):
                line += self._grid[Vector2.create(x, y)]
            line += '\n'
            st += line
        return st
    def __repr__(self):
        return self.__str__()

def id_gen(start_at):
    while True:
        yield start_at
        start_at += 1