#!/usr/bin/env python3.8

import hidden_4
import sys

if __name__ == "__main__":
    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)