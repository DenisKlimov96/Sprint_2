class PointsForPlace:
    def __init__(self):
        self.points = 0

    @staticmethod
    def get_points_for_place(place):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place <= 0:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            return 101 - place


class PointsForMeters:
    def __init__(self):
        self.points = 0

    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            return meters * 0.5


class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        super().__init__()

    def get_total_points(self, meters, place):
        points_for_place = self.get_points_for_place(place)
        points_for_meters = self.get_points_for_meters(meters)
        total = points_for_place + points_for_meters
        return total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10)) 