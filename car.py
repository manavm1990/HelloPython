class Car:
    def __init__(self, speed: float = 0):
        # A single leading underscore indicates that an attribute or method is intended to be private or protected.
        self._speed = speed
        self._odometer = 0
        self._time = 0

    @property
    def odometer(self) -> float:
        """Returns the current speed of the car in km/h."""
        return self._odometer

    @property
    def speed(self) -> float:
        """Returns the current speed of the car in km/h."""
        return self._speed

    @property
    def time(self) -> int:
        """Returns the current time of the car in seconds."""
        return self._time

    def get_average_speed(self) -> float:
        """Returns the average speed of the car in km/h."""
        if self._time == 0:
            return 0.0
        return self._odometer / self._time

    def accelerate(self) -> float:
        """Increases the speed of the car by 5 km/h."""
        self._speed += 5
        return self._speed

    def brake(self) -> float:
        """Reduces the speed of the car by 5 km/h (or to 0)."""
        self._speed = max(0.0, self._speed - 5)  # `max` expects both arguments to be of same type.
        return self._speed

    def step(self) -> (float, int):
        """Advances the car by one second."""
        self._odometer += self._speed
        self._time += 1
        return self._odometer, self._time
