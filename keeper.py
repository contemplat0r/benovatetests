# -*- code: utf-8 -*-

class Keeper(object):

    list_instances = []

    def __init__(self):
        self.list_instances.append(self)


if __name__ == '__main__':

    a = Keeper()
    b = Keeper()
    c = Keeper()

    for i in Keeper.list_instances:
        print i, i.__class__ #, dir(i)
