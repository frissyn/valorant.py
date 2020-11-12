class Dto(object):
    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj)

    def __str__(self):
        return str(self.json)

    def set_attributes(self, attrs):
        for attr, value in attrs.items():
            self.__setattr__(attr, value)


class ActDto(Dto):
    def __getattribute__(self, name):
        return super(ActDto, self).__getattribute__(name)


class ContentItemDto(Dto):
    def __getattribute__(self, name):
        return super(ContentItemDto, self).__getattribute__(name)
