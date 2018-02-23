class SpaceAge(object):
    def __init__(self, age):
        self._seconds = age
        self._SECONDS_IN_YEAR = 31557600
        self._years = age / self._SECONDS_IN_YEAR
        self._DAYS_IN_YEAR = 365.25
        self._MERCURY_RATIO = 0.2408467
        self._VENUS_RATIO = 0.61519726
        self._MARS_RATIO = 1.8808158
        self._JUPITER_RATIO = 11.862615
        self._SATURN_RATIO = 29.447498
        self._URANUS_RATIO = 84.016846
        self._NEPTUNE_RATIO = 164.79132

    @property
    def seconds(self):
        return self._seconds

    def on_earth(self):
        return round(self._years, 2)

    def on_mercury(self):
        return round(self._years / self._MERCURY_RATIO, 2)

    def on_venus(self):
        return round(self._years / self._VENUS_RATIO, 2)

    def on_mars(self):
        return round(self._years / self._MARS_RATIO, 2)

    def on_jupiter(self):
        return round(self._years / self._JUPITER_RATIO, 2)

    def on_saturn(self):
        return round(self._years / self._SATURN_RATIO, 2)

    def on_uranus(self):
        return round(self._years / self._URANUS_RATIO, 2)

    def on_neptune(self):
        return round(self._years / self._NEPTUNE_RATIO, 2)