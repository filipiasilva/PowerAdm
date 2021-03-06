#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PowerAdm
newid.py

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

# Imports
###############################################################################################
import time
import os.path
from globalvar import *
from config import *

# get a next free id on systems
class NewID:
    ''' Find the next LPAR ID free to use. For more informations access http://poweradm.org '''

    def mkID(self):
        ''' Find the next LPAR ID '''

        ids = []
        systems_keys = list(systems.keys())
        systems_length = (len(systems.keys()))-1
        count = 0
        while count <= systems_length:
            os.system('ssh -l poweradm %s lssyscfg -m %s -r lpar -F lpar_id >> %s/poweradm/tmp/ids_%s'
                      % (hmcserver, systems_keys[count], pahome, timestr))
            os.system('cat %s/poweradm/data/reserved_ids >> %s/poweradm/tmp/ids_%s' % (pahome, pahome, timestr))
            if os.path.isfile('%s/poweradm/tmp/reserved_ids_%s' % (pahome, timestr)):
                os.system('cat %s/poweradm/tmp/reserved_ids_%s >> %s/poweradm/tmp/ids_%s' % (pahome,
                          timestr, pahome, timestr))
            count += 1
        fileids = open('%s/poweradm/tmp/ids_%s' % (pahome, timestr), 'r')
        ids = fileids.readlines()
        ids.sort(key=int)
        lastid = len(ids)-1
        self.newid = int(ids[lastid])+1
        # if id < 10 add 0 left, view ticket #5 github
        if self.newid < 10:
            self.newid = ('0%s' % (self.newid))
        fileids.close()
        os.system('rm %s/poweradm/tmp/ids_%s' % (pahome, timestr))

    def getID(self):
        ''' Return the next ID from mkID() '''
        return self.newid
