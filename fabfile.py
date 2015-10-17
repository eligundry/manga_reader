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
def tests(verbose=True, debugger=False):
    """
    Run unit tests.

    @param verbose: Should the test be run with verbose output
    @type verbose: bool
    @param debugger: Should the tests launch pdb on exceptions
    @type debugger: bool
    """
    cmd = ['nosetests']

    if verbose:
        cmd.append('-v')

    if debugger:
        cmd.append('--pdb')

    local(' '.join(cmd))
