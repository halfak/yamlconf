import yamlconf

doc = yamlconf.loads("""
test: demo_test

tests:
    defaults:
        foo: 5
    demo_test:
        bar: 6
""")

doc['tests'][doc['test']]['foo']
doc['tests'][doc['test']]['bar']
