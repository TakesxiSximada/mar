#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import sys
import argparse


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    args = parser.parse_args(argv)



if __name__ == '__main__':
    sys.exit(main())
