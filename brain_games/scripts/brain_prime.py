#!/usr/bin/env python3
from brain_games.games.prime import generation
from brain_games.engine import dialogue


def main():
    dialogue(*generation())


if __name__ == '__main__':
    main()
