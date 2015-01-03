from pybuilder.core import use_plugin, init

use_plugin('python.core')
use_plugin('python.unittest')
use_plugin('python.integrationtest')
use_plugin('python.install_dependencies')
use_plugin('python.flake8')
use_plugin('python.distutils')
use_plugin('exec')


name = 'memento'
default_task = 'publish'


@init
def initialize(project):
    project.set_property('run_integration_tests_command',
                         'nosetests src/integrationtest/python')

    project.build_depends_on('flask')
    project.build_depends_on('nose')
    project.build_depends_on('nose-parameterized')
    project.build_depends_on('pyassert')
    project.build_depends_on('mongoengine')
