from nose.tools import eq_

from ..import_path import import_path
from .util import submodule, value


def test_import_path():
    my_submodule = import_path("yamlconf.tests.util.submodule")
    eq_(submodule, my_submodule)

    my_attribute = import_path("yamlconf.tests.util.submodule.attribute")
    eq_(submodule.attribute, my_attribute)

    my_sub_attribute = import_path(
        "yamlconf.tests.util.submodule.attribute.attribute")
    eq_(submodule.attribute.attribute, my_sub_attribute)

    my_super_sub_attribute = import_path(
        "yamlconf.tests.util.submodule.attribute.attribute.attribute")
    eq_(submodule.attribute.attribute.attribute, my_super_sub_attribute)
    eq_(my_super_sub_attribute.attribute, "hello")

    my_value = import_path("yamlconf.tests.util.value")
    eq_(value, my_value)
    eq_(my_value, "foo")
