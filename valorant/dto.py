class Dto(object):
    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj)

    def __str__(self):
        return str(self.json)

    def set_attributes(self, attrs, sub=False):
        for attr, value in attrs.items():
            if sub and isinstance(value, dict):
                self.__setattr__(attr, Dto(value))
            else:
                self.__setattr__(attr, value)


class ActDto(Dto):
    def __getattribute__(self, name):
        return super(ActDto, self).__getattribute__(name)


class AccountDto(Dto):
    def __getattribute__(self, name):
        return super(AccountDto, self).__getattribute__(name)


class ContentItemDto(Dto):
    def __getattribute__(self, name):
        return super(ContentItemDto, self).__getattribute__(name)


class PlatformDataDto(Dto):
    def __getattribute__(self, name):
        return super(PlatformDataDto, self).__getattribute__(name)
