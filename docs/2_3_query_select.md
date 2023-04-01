# 2.3 Query with Select

For full documentation visit [sqlalchemy.org](https://www.sqlalchemy.org/).

[get started](https://docs.sqlalchemy.org/en/14/orm/quickstart.html#simple-select)


## Code

```py

from pprint import pprint
from sqlalchemy import select
from sqlalchemy import Column, text
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

pprint("---------------------------------")


stmt = select(User).where(User.name.in_(["Bob", "sandy"]))

for user in session.scalars(stmt):
     print(user.__dict__)


```

## Output

    2023-04-01 22:14:50,337 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-04-01 22:14:50,338 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user")
    2023-04-01 22:14:50,338 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-04-01 22:14:50,338 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user")
    2023-04-01 22:14:50,338 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-04-01 22:14:50,338 INFO sqlalchemy.engine.Engine 
    CREATE TABLE user (
        id VARCHAR(20) NOT NULL, 
        name VARCHAR(20), 
        PRIMARY KEY (id)
    )


    2023-04-01 22:14:50,338 INFO sqlalchemy.engine.Engine [no key 0.00006s] ()
    2023-04-01 22:14:50,339 INFO sqlalchemy.engine.Engine COMMIT
    2023-04-01 22:14:50,339 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-04-01 22:14:50,341 INFO sqlalchemy.engine.Engine INSERT INTO user (id, name) VALUES (?, ?)
    2023-04-01 22:14:50,341 INFO sqlalchemy.engine.Engine [generated in 0.00013s] ('5', 'Bob')
    2023-04-01 22:14:50,341 INFO sqlalchemy.engine.Engine COMMIT
    '---------------------------------'
    2023-04-01 22:14:50,342 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-04-01 22:14:50,342 INFO sqlalchemy.engine.Engine SELECT user.id, user.name 
    FROM user 
    WHERE user.name IN (?, ?)
    2023-04-01 22:14:50,342 INFO sqlalchemy.engine.Engine [generated in 0.00012s] ('Bob', 'sandy')
    {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001FA22DD34C0>, 'name': 'Bob', 'id': '5'}

    Process finished with exit code 0
