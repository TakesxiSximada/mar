#! /usr/bin/env python
# -*- coding: utf-8 -*-
from tasks import recog_image


def main():
    res = recog_image.delay('sample.jpg')
    res.join()

if __name__ == '__main__':
    main()
