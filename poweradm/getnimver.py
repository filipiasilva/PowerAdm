#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PowerAdm
getnimver.py

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
from globalvar import *
from config import *
##############################################################################################
#
# Class GetNimVer
##############################################################################################

class GetNimVer:
    ''' An text menu to get the NIM version informations.'''

    def selectOsVersion(self):
        ''' Prompt the NIM version list based on config. '''

        print ("\n[DEPLOY OS Nim Server Configuration]\n"
               "\nSelect the version OS for LPAR")
        nim_os_deploy_keys = list(nim_os_deploy.keys())
        nim_os_deploy_length = (len(nim_os_deploy.keys()))-1
        count = 0
        while count <= nim_os_deploy_length:
            print ("%s : %s" % (count, nim_os_deploy_keys[count]))
            count += 1

        while True:
            try:
	        nim_os_deploy_option = int(raw_input("Version: "))
        	self.osversion = (nim_os_deploy_keys[nim_os_deploy_option])
                break
            except(IndexError):
                print('\tERROR: Select an existing option between 0 and %s.' % (nim_os_deploy_length))	
        self.mksysblpp = nim_os_deploy[('%s' % nim_os_deploy_keys[nim_os_deploy_option])][0]
        self.spot = nim_os_deploy[('%s' % nim_os_deploy_keys[nim_os_deploy_option])][1]

    def getOsVersion(self):
        ''' After selection on selectOsVersion() returns OS Version. '''

        return self.osversion

    def getMksysbLpp(self):
        ''' After selection on selectOsVersion() returns OS MKSYSB or LPP. '''

        return self.mksysblpp

    def getSpot(self):
        ''' After selection on selectOsVersion() returns OS SPOT. '''

        return self.spot