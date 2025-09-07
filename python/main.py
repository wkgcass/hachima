#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hachima

def __main():
    s = 'hello, world! 你好，世界！'
    encoded = hachima.encode(s.encode('utf-8'))
    print(encoded)
    decoded = hachima.decode(encoded)
    print(decoded.decode('utf-8'))

if __name__ == "__main__":
    __main()
