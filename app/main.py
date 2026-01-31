class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> None:
        return f"Distance(km={self.km})"

    def _get_km(self, other: None) -> None:
        if isinstance(other, Distance):
            return other.km
        return other

    def __add__(self, other: None) -> None:
        return Distance(self.km + self._get_km(other))

    def __iadd__(self, other: None) -> None:
        self.km += self._get_km(other)
        return self

    def __mul__(self, other: None) -> None:
        if isinstance(other, Distance):
            raise TypeError
        return Distance(self.km * other)

    def __truediv__(self, other: None) -> None:
        if isinstance(other, Distance):
            raise TypeError
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: None) -> None:
        return self.km < self._get_km(other)

    def __gt__(self, other: None) -> None:
        return self.km > self._get_km(other)

    def __eq__(self, other: None) -> None:
        return self.km == self._get_km(other)

    def __le__(self, other: None) -> None:
        return self.km <= self._get_km(other)

    def __ge__(self, other: None) -> None:
        return self.km >= self._get_km(other)
