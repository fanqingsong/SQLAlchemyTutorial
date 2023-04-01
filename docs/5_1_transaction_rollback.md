# 5.1 Transaction Rollback

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

session.rollback()


new_user = User(id='7', name='hanmeimei')

session.add(new_user)

session.commit()

user = session.query(User).filter(User.id=='7').one()
print('type:', type(user))
print('name:', user.name)

session.close()



```

## Output


    2023-04-01 22:57:38,618 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-04-01 22:57:38,618 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user")
    2023-04-01 22:57:38,618 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-04-01 22:57:38,618 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user")
    2023-04-01 22:57:38,618 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-04-01 22:57:38,618 INFO sqlalchemy.engine.Engine 
    CREATE TABLE user (
        id VARCHAR(20) NOT NULL, 
        name VARCHAR(20), 
        PRIMARY KEY (id)
    )


    2023-04-01 22:57:38,619 INFO sqlalchemy.engine.Engine [no key 0.00008s] ()
    2023-04-01 22:57:38,619 INFO sqlalchemy.engine.Engine COMMIT
    2023-04-01 22:57:38,619 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-04-01 22:57:38,620 INFO sqlalchemy.engine.Engine INSERT INTO user (id, name) VALUES (?, ?)
    2023-04-01 22:57:38,620 INFO sqlalchemy.engine.Engine [generated in 0.00010s] ('7', 'hanmeimei')
    2023-04-01 22:57:38,621 INFO sqlalchemy.engine.Engine COMMIT
    2023-04-01 22:57:38,621 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-04-01 22:57:38,622 INFO sqlalchemy.engine.Engine SELECT user.id AS user_id, user.name AS user_name 
    FROM user 
    WHERE user.id = ?
    2023-04-01 22:57:38,622 INFO sqlalchemy.engine.Engine [generated in 0.00009s] ('7',)
    type: <class '__main__.User'>
    name: hanmeimei
    2023-04-01 22:57:38,622 INFO sqlalchemy.engine.Engine ROLLBACK

    Process finished with exit code 0

