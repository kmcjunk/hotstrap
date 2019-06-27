#!/usr/bin/env python

import sys
import os
import subprocess
import shutil


def install_packages():
    package_list = ['python-pip',
                    'gcc',
                    'git',
                    'python-devel',
                    'libyaml-devel',
                    'openssl-devel',
                    'libffi-devel',
                    'libxml2-devel',
                    'libxslt-devel',
                    'puppet']
    print('Installing packages')
    try:
        for package in package_list:
            print('Installing + ' + package)
            os.system('yum install -y ' + package)
            print('Successful\n')
    except:
        print('Unsuccessful')


def pip_down():
    print('\nInstalling OpenStack HEAT requirements via pip')
    os_list = [ 'os-collect-config',
                'os-apply-config',
                'os-refresh-config',
                'dib-utils',
                'gitpython' ]
    try:
        print('Installing decorator')
        os.system('pip install -U decorator')
        for package in os_list:
            print('Installing ' + package)
            os.system('pip install ' + package)
            print('Successful')
        print('Installing ansible')
        os.system('pip install ansible==2.4.3.0')
    except:
        print('Unsuccessful')


def git_configuration():
    import git
    print('Cloning down configuration files')
    git.Git('./').clone('git://github.com/kmcjunk/hotstrap.git')


def ensure_dir():
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def configurate():
    file_list = ['etc/os-collect-config.conf',
                  'opt/stack/os-config-refresh/configure.d/20-os-apply-config',
                  'opt/stack/os-config-refresh/configure.d/55-heat-config',
                  'usr/bin/heat-config-notify',
                  'usr/libexec/os-apply-config/templates/etc/os-collect-config.conf',
                  'usr/libexec/os-apply-config/templates/var/run/heat-config/heat-config',
                  'var/lib/heat-config/hooks/ansible',
                  'var/lib/heat-config/hooks/script' ]
    print('Moving configuration files to the proper locations')
    for file in file_list:
        directory = os.path.dirname('/' + file)
        if not os.path.exists(directory):
            os.makedirs(directory)
        print('hotstrap/' + file + '\t->' + '/' + file)
        shutil.move('hotstrap/' + file, '/' + file)



# [ 'etc/os-collect-config.conf',
# 'opt/stack/os-config-refresh/configure.d/20-os-apply-config',
# 'opt/stack/os-config-refresh/configure.d/55-heat-config',
# 'usr/bin/heat-config-notify',
# 'usr/libexec/os-apply-config/templates/etc/os-collect-config.conf',
# 'usr/libexec/os-apply-config/templates/var/run/heat-config/heat-config'
# 'var/lib/heat-config/hooks/ansible',
# 'var/lib/heat-config/hooks/script' ]


# def touch_some_things():
#     os.system('os-collect-config --one-time --debug')
#     os.system('cat /etc/os-collect-config.conf')
#     os.system('os-collect-config --one-time --debug')
#     os.system('pip install ansible==2.4.3.0')


def delete_some_other_things():
    os.system('rm -rf /var/lib/cloud/instance')
    os.system('rm -rf /var/lib/cloud/instances/*')
    os.system('rm -rf /var/lib/cloud/data/*')
    os.system('rm -rf /var/lib/cloud/sem/config_scripts_per_once.once')
    os.system('rm -rf /var/log/cloud-init.log')
    os.system('rm -rf /var/log/cloud-init-output.log')

# install_packages()
# pip_down()
git_configuration()
configurate()