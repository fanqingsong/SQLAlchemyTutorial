# 2. Query

For full documentation visit [sqlalchemy.org](https://www.sqlalchemy.org/).

[get started](https://docs.sqlalchemy.org/en/14/orm/quickstart.html)


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

session.commit()

user = session.query(User).filter(User.id=='5').one()
print('type:', type(user))
print('name:', user.name)

session.close()
```

## Output

    2023-03-28 23:15:44,854 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-03-28 23:15:44,854 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user")
    2023-03-28 23:15:44,854 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-03-28 23:15:44,854 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user")
    2023-03-28 23:15:44,854 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-03-28 23:15:44,854 INFO sqlalchemy.engine.Engine 
    CREATE TABLE user (
        id VARCHAR(20) NOT NULL, 
        name VARCHAR(20), 
        PRIMARY KEY (id)
    )


    2023-03-28 23:15:44,854 INFO sqlalchemy.engine.Engine [no key 0.00005s] ()
    2023-03-28 23:15:44,854 INFO sqlalchemy.engine.Engine COMMIT
    C:\Users\fannnqin\PycharmProjects\test\query.py:11: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()
    2023-03-28 23:15:44,871 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-03-28 23:15:44,872 INFO sqlalchemy.engine.Engine INSERT INTO user (id, name) VALUES (?, ?)
    2023-03-28 23:15:44,872 INFO sqlalchemy.engine.Engine [generated in 0.00012s] ('5', 'Bob')
    2023-03-28 23:15:44,872 INFO sqlalchemy.engine.Engine COMMIT
    2023-03-28 23:15:44,873 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-03-28 23:15:44,874 INFO sqlalchemy.engine.Engine SELECT user.id AS user_id, user.name AS user_name 
    FROM user 
    WHERE user.id = ?
    2023-03-28 23:15:44,874 INFO sqlalchemy.engine.Engine [generated in 0.00009s] ('5',)
    type: <class '__main__.User'>
    name: Bob
    2023-03-28 23:15:44,875 INFO sqlalchemy.engine.Engine ROLLBACK
