from sys import argv

def tester_hook_factory(name: str):
    def tester_hook(cls):
        if ("test") in argv:
            print(f"testing! {cls.__name__} {name}")

        return cls
    return tester_hook