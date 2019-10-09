import sturm


def test_something():
    class Impl1(sturm.BaseModel):
        pass

    class Impl2(sturm.BaseModel):
        pass

    # assert {'BaseModel': sturm.BaseModel, 'Impl1': Impl1, 'Impl2': Impl2} == sturm._REGISTRY
