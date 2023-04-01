# 5.0 Transaction

For full documentation visit [sqlalchemy.org](https://www.sqlalchemy.org/).

[detail](https://docs.sqlalchemy.org/en/20/orm/session_transaction.html#managing-transactions)


## Code

```py

from pprint import pprint

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# using sqlite memory mode
engine = create_engine("sqlite://", echo=True)

# using sqlite file mode
#engine = create_engine("sqlite:///./file.db", echo=True)

Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)()

new_user = User(id='5', name='Bob')

session.add(new_user)

new_user = User(id='5', name='LILY')

session.add(new_user)

session.commit()

user = session.query(User).filter(User.id=='5').one()
print('type:', type(user))
print('name:', user.name)

session.close()


```

## Output

    2023-04-01 22:50:03,619 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-04-01 22:50:03,619 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user")
    2023-04-01 22:50:03,619 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-04-01 22:50:03,619 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user")
    2023-04-01 22:50:03,619 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-04-01 22:50:03,620 INFO sqlalchemy.engine.Engine 
    CREATE TABLE user (
        id VARCHAR(20) NOT NULL, 
        name VARCHAR(20), 
        PRIMARY KEY (id)
    )


    2023-04-01 22:50:03,620 INFO sqlalchemy.engine.Engine [no key 0.00007s] ()
    2023-04-01 22:50:03,620 INFO sqlalchemy.engine.Engine COMMIT
    2023-04-01 22:50:03,621 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-04-01 22:50:03,621 INFO sqlalchemy.engine.Engine INSERT INTO user (id, name) VALUES (?, ?)
    2023-04-01 22:50:03,621 INFO sqlalchemy.engine.Engine [generated in 0.00011s] [('5', 'Bob'), ('5', 'LILY')]
    Traceback (most recent call last):
    File "C:\Users\fannnqin\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\sqlalchemy\engine\base.py", line 1933, in _exec_single_context
    2023-04-01 22:50:03,622 INFO sqlalchemy.engine.Engine ROLLBACK
        self.dialect.do_executemany(
    File "C:\Users\fannnqin\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\sqlalchemy\engine\default.py", line 745, in do_executemany
        cursor.executemany(statement, parameters)
    sqlite3.IntegrityError: UNIQUE constraint failed: user.id

    The above exception was the direct cause of the following exception:

