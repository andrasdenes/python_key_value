from app.models.KeyValuePair import KeyValuePair
from peewee import SqliteDatabase
from datetime import datetime
class Test:
    kvp = KeyValuePair()
    kvp._meta.database = SqliteDatabase(f"test_database_{datetime.now().time().microsecond}.db")

    def test_KeyValuePair_success(self):
        # Arrange
        self.kvp._meta.database.connect()
        self.kvp._meta.database.create_tables([KeyValuePair])

        # Act
        new_kvp = KeyValuePair()
        new_kvp.key = "key"
        new_kvp.value = "value"
        new_kvp.save()

        # Assert 
        retrieved_kvp = KeyValuePair.get(key="key")
        assert retrieved_kvp.key == new_kvp.key
    
        self.kvp._meta.database.close()