'''
 *
 * Copyright (C) 2020 Universitat Politècnica de Catalunya.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at:
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
'''

# -*- coding: utf-8 -*-

import json
import tensorflow as tf
import sys
import os





class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_failure(msg):
    tf.print(bcolors.FAIL + msg + bcolors.ENDC, output_stream=sys.stderr)
    sys.exit(1)

def print_info(msg):
    tf.print(bcolors.OKGREEN + msg + bcolors.ENDC, output_stream=sys.stderr)

def print_header(msg):
    tf.print(bcolors.OKGREEN + msg + bcolors.ENDC, output_stream=sys.stderr)


def stream_read_json(f):
    end_symbol = bytes(']', 'utf-8')
    start_pos = 1
    while True:
        try:
            obj = json.load(f)
            yield obj
            return
        except json.JSONDecodeError as e:
            f.seek(start_pos)
            json_str = f.read(e.pos)
            obj = json.loads(json_str)
            start_pos += e.pos + 1
            a = f.read(1)
            if a == end_symbol:
                yield obj
                return
            yield obj


def str_to_bool(a):
    """
    Parameters
    ----------
    a:    str
       Input
    """

    if a == 'True':
        return True
    else:
        return False



