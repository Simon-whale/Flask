class DataGenerator:
    def __init__(self):
        pass

    @staticmethod
    def create(start: int = 0, end: int = 100) -> list[int]:
        values = []
        for index in range(start, end):
            values.append(index)

        return values
