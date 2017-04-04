class add(int):
    def __call__(self, value):
        return add(self + value)
