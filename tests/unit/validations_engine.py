from validations_engine.validations_engine import DummyClass

class TestDummyClass:
    def test_dummy_method(self):
        # given
        dummy_object = DummyClass()
        # when
        expected_result = 42
        # then
        assert dummy_object.dummy_method() == expected_result