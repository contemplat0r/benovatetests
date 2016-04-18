# -*- coding: utf-8 -*-


def reverse_gen(iter_obj):
    for i in iter_obj[::-1]:
        yield i


if __name__ == '__main__':
    
    gen = reverse_gen([1, 2, 3, 4])

    print gen.next()
    print gen.next()
    print gen.next()
    print gen.next()
    print gen.next()
