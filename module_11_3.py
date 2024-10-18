import inspect
import pprint


class Car:
    def __init__(self, name):
        super().__init__()
        self.model = name
        self.wheels = 4

    def drr(self):
        print('dr-rr-r')


def introspection_info(obj):
    var = list(vars(obj).keys())
    met = list(set(dir(obj)) - set(var))
    result = {'type': type(obj),
              'attributes': var,
              'methods': met,
              'module': inspect.getmodule(obj)
              }
    return result


my_car = Car('Ford')
pprint.pprint(introspection_info(my_car))
