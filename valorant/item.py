class Item(object):
    def __init__(self, lobj):
        self.all = lobj

        for obj in lobj:
            self.__setattr__(obj["name"], obj)

    def __str__(self):
        return str(self.all)

    def __getattribute__(self, name):
        return super(Item, self).__getattribute__(name)

    def set_attributes(self, attrs):
        for attr, value in attrs.items():
            self.__setattr__(attr, value)
