from collections import namedtuple

Attribute = namedtuple("Attribute", ["attribute"])

super_sub_attribute = Attribute("hello")
sub_attribute = Attribute(super_sub_attribute)
attribute = Attribute(sub_attribute)
