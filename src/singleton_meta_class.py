

class SingletonMetaClass(type):

    def __init__(cls, name, bases, dict):
        super(SingletonMetaClass, cls).__init__(cls, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonMetaClass, cls).__call__(*args, **kwargs)
        return cls._instance