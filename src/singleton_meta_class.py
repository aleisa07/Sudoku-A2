

class SingletonMetaClass(type):

    def __init__(cls, name, bases, dict):
        super(SingletonMetaClass, cls).__init__(cls, bases, dict)
        cls._instance = None
        print 'SingletonMetaClass __init__'

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonMetaClass, cls).__call__(*args, **kwargs)
        print 'SingletonMetaClass __call__'
        return cls._instance