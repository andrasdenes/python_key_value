from app.models.KeyValuePair import KeyValuePair
from peewee import SqliteDatabase, IntegrityError
from datetime import datetime
import os
from pytest import raises

class Test:
    kvp = KeyValuePair()
    db_name = f"test_database_{datetime.now().time().microsecond}.db"
    kvp._meta.database = SqliteDatabase(db_name)

    def test_KeyValuePair_success(self):
        # Arrange
        self.kvp._meta.database.create_tables([KeyValuePair])

        # Act
        new_kvp = KeyValuePair()
        new_kvp.key = "key"
        new_kvp.value = "value"
        new_kvp.save()

        # Assert 
        retrieved_kvp = KeyValuePair.get(key="key")
        assert retrieved_kvp.key == new_kvp.key
        assert retrieved_kvp.value == new_kvp.value

        #teardown
        self.kvp._meta.database.close()
        current_path = os.getcwd()
        os.remove("/".join([current_path, self.db_name]))

    def test_KeyValuePair_not_unique_key(self):
        # Arrange
        self.kvp._meta.database.create_tables([KeyValuePair])

        # Act
        new_kvp = KeyValuePair()
        new_kvp.key = "key"
        new_kvp.value = "value"
        new_kvp.save()

        new_kvp_1 = KeyValuePair()
        new_kvp_1.key = "key"
        new_kvp_1.value = "value 1"
        
        # Assert
        with raises(IntegrityError):
            
            new_kvp_1.save()

        #teardown
        self.kvp._meta.database.close()
        current_path = os.getcwd()
        os.remove("/".join([current_path, self.db_name]))
    
    def test_KeyValuePair_allow_duplicate_values(self):
        # Arrange
        self.kvp._meta.database.create_tables([KeyValuePair])

        # Act
        new_kvp = KeyValuePair()
        new_kvp.key = "key"
        new_kvp.value = "value"
        new_kvp.save()

        new_kvp_1 = KeyValuePair()
        new_kvp_1.key = "key1"
        new_kvp_1.value = "value"
        new_kvp_1.save()

        #Assert
        assert new_kvp.key != new_kvp_1.key
        assert new_kvp.value == new_kvp_1.value

        #teardown
        self.kvp._meta.database.close()
        current_path = os.getcwd()
        os.remove("/".join([current_path, self.db_name]))