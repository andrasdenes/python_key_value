from pytest import raises
from app.blueprints.Handlers.AddHandler import AddHandler
from app.blueprints.Handlers.GetHandler import GetHandler
from app.models.KeyValuePair import KeyValuePair
from app.tests.TestBase import TestBase
from unittest.mock import MagicMock, Mock
from peewee import PeeweeException

class Test(TestBase):
    def test_AddHandler_with_invalid_request_methods(self):
        # Arrange
        delete_request = super().Request("DELETE", None)
        put_request = super().Request("PUT", None)
        patch_request = super().Request("PATCH", None)
        #...

        # Act
        delete_result = AddHandler().handle(delete_request)
        put_result = AddHandler().handle(put_request)
        patch_result = AddHandler().handle(patch_request)
        results = [delete_result, put_result, patch_result]
        # ...
        
        # Assert
        for result in results:
            assert 400 == result[1]
            assert "Request method not allowed" == result[0]

    def test_GetHandler_with_invalid_request_methods(self):
        # Arrange
        delete_request = super().Request("DELETE", None)
        put_request = super().Request("PUT", None)
        patch_request = super().Request("PATCH", None)
        #...

        # Act
        delete_result = GetHandler().handle(delete_request)
        put_result = GetHandler().handle(put_request)
        patch_result = GetHandler().handle(patch_request)
        results = [delete_result, put_result, patch_result]
        # ...
        
        # Assert
        for result in results:
            assert 400 == result[1]
            assert "Request method not allowed" == result[0]

    def test_KeyValuePair_PeeweeException(self):
        # Arrange
        kvp = KeyValuePair()
        kvp.save = MagicMock(side_effect=PeeweeException())
        form = super().Form("irrelevant key", "irrelevant value", MagicMock(return_value="something irrelevant"))
        request = super().Request("POST", form)

        # Act
        result = AddHandler().handle(request)

        # Assert
        assert "Error" == result[0]
        assert 500 == result[1] 

