#!/usr/bin/env python3
from os import getenv


class AudioFileParser:

    def get_info(self):
        if getenv('NAME') is None:
            name = 'World'
        else:
            name = getenv('NAME')
        return name


