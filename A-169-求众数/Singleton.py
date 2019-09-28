class SingleTon(object):
    # _instance = None
    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(cls, SingleTon).__new__(cls, *args, **kwargs)
        return cls._instance

class Myclass(SingleTon):
    a = 1

d = Myclass()
print(id(d))
d1 = Myclass()
print(id(d1))
