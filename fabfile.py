#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Name			:	
# Description	:	
# Author		: Sven Hergenhahn
#
# $Id$
# 
###################################################

from fabric.api import *
import os
import fabric.contrib.project as project

PROD = 'localhost'
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DEST_PATH = '/var/www/%s/' % ROOT_PATH.split('/')[-1]
DEPLOY_PATH = os.path.join(ROOT_PATH, 'deploy')

def clean():
    local('rm -rf ./deploy')

def generate():
    local('hyde -s . gen')

def regen():
    clean()
    generate()

def serve():
    local('hyde -s . serve')

def reserve():
    regen()
    serve()

def smush():
    local('smusher ./media/images')

@hosts(PROD)
def publish():
    regen()
    project.rsync_project(
        remote_dir=DEST_PATH,
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )
