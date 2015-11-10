#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import logging
from utils import remove_comments, merge_dict

CURRENT_DIRECTORY = os.getcwd()
DIR = os.path.dirname(os.path.realpath(__file__))

class ManageFile(object):

    def __init__(self, fm, ff, sf):

        self.file_merged = fm
        self.first_file = self.generate_dict_libs(ff)
        self.second_file = self.generate_dict_libs(sf)

    def open_file(self, file):

        try:

            path_file = '{}/{}'.format(CURRENT_DIRECTORY, file)
            f = open(file, 'r').read()

            return f

        except Exception as e:
            return logging.error(e)

    def generate_dict_libs(self, file):

        text = remove_comments(self.open_file(file))

        lib_list = []

        for item in text.split('\n'):

            item = item.split('==')

            if len(item) == 1:
                item.append('')

            lib_list.append(tuple(item))

        return dict(lib_list)

    def see(self):

        print('------------ file_merged ------------')
        print(self.file_merged)

        print('------------ first_file ------------')
        print(self.first_file)

        print('------------ second_file ------------')
        print(self.second_file)

class Merge(object):

    def __init__(self, mf):

        self.manage_file = mf
        self.dict_libs = {}

        self.merge_dict_libs()

    def merge_dict_libs(self):

        self.dict_libs = merge_dict(
            self.manage_file.first_file,
            self.manage_file.second_file
        )

    def generate_requirements_txt(self):

        txt = ''.join(
          '{}=={}\n'.format(key, value) for key, value in self.dict_libs.items()
        )

        f = open('requirements-merged.txt', 'x')
        f.write(txt)
        f.close()

        print('create file requirements-merged.txt')
