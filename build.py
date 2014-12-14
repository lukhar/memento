from pybuilder.core import use_plugin, init

use_plugin('python.core')
use_plugin('python.unittest')
use_plugin('python.integrationtest')
use_plugin('python.install_dependencies')
use_plugin('python.flake8')
use_plugin('python.distutils')


name = 'memento'
default_task = 'publish'


@init
def initialize(project):
    project.set_property('unittest_module_glob', 'test_*')
    project.set_property('integrationtest_file_glob', 'test_*')

    project.build_depends_on('flask')
    project.build_depends_on('nose')
    project.build_depends_on('pyassert')
    project.build_depends_on('mongoengine')
