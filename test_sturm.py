import sturm


def test_something():
    class Impl1(sturm.BaseNode):
        pass

    class Impl2(sturm.BaseNode):
        pass

    actual = sturm._REGISTRY
    expected = {'BaseNode': sturm.BaseNode, 'Impl1': Impl1, 'Impl2': Impl2}
    assert actual == expected
