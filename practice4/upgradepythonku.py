#__author:"longjin"
#date:  2019/9/19
# -*- coding: UTF-8 -*-

import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call('pip.exe install --upgrade ' + dist.project_name, shell=True)