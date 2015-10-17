from fabric.api import *

@task
def clean():
    local('rm mangareader.db')

@task
def build_android():
    pass

@task
def build_ios():
    pass

@task
def tests():
    pass
