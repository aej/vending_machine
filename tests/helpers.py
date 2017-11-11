def assert_list_instances_equal(list_one, list_two):
    for i, j in zip(list_one, list_two):
        if not i.__class__ is j.__class__:
            assert False
    assert True