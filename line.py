class Line(object):
    def __init__(self, slope, intercept):
        self._slope = slope
        self._intercept = intercept
        self._line_threshold = 0

    def y_value_at(self, x):
        return self._slope * x + self._intercept

    def x_value_at(self, y):
        return (y - x + self._intercept) / self._slope

    def above(self, point):
        return self.y_difference(point) < self._line_threshold

    def below(self, point):
        return self.y_difference(point) > self._line_threshold

    def at(self, point):
        return self.y_difference(point) == self._line_threshold

    def y_difference(self, point):
        return self.y_value_at(point[0]) - point[1]

    def __repr__(self):
        return str(self._slope) + "x + " + str(self._intercept)

    @classmethod
    def create(cls, a, b):
        slope = 0 if b[0] == a[0] else (b[1] - a[1]) / (b[0] - a[0])
        return cls(slope, a[1] - slope*a[0])
