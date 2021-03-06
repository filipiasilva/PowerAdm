#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PowerAdm
fields.py

Copyright (c) 2014, 2015 Kairo Araujo

It was created for personal use. There are no guarantees of the author.
Use at your own risk.

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

IBM, Power, PowerVM (a.k.a. VIOS) are registered trademarks of IBM Corporation in
the United States, other countries, or both.
VMware, vCenter, vCenter Orchestrator are registered trademarks of VWware Inc in the United
States, other countries, or both.
'''
#
# Imports
###############################################################################################
#
# Importing classes/modules
import time
import os.path
from globalvar import *
from config import *
from poweradm import *


class Fields:
    ''' This class verify if the fields used is blank or contain spaces.

        Args:
          field (str): The filed variable, like 'name', 'change' etc...
          textField (stg): The question for the field, like 'Whats de LPAR name',
                           'Whats the change number' etc .
    '''

    def __init__(self, field, textField):
        ''' Initial to get field and textField arguments. '''

        self.field = field
        self.textField = textField

    def chkFieldStr(self):
        ''' Check field strings doesn't has a blank or spaces. '''

        while True:

            self.variable = raw_input('%s' % (self.textField))
            if (self.variable.isspace() == True) or ( self.variable == '') or (' ' in self.variable):
                print ("%s can not be blank or contain spaces" % (self.field))
            else:
                break

    def strVarOut(self):
        ''' Returns the answer to question field. '''
        return self.variable
