# 5. Relationship with backref

For full documentation visit [sqlalchemy.org](https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#one-to-many).

[relationship](https://docs.sqlalchemy.org/en/14/orm/relationship_api.html#sqlalchemy.orm.relationship).

[backref](https://docs.sqlalchemy.org/en/14/orm/relationship_api.html#sqlalchemy.orm.relationship.params.backref).

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

class Parent(Base):
    __tablename__ = "parent_table"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # children = relationship("Child", back_populates="parent")


class Child(Base):
    __tablename__ = "child_table"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("parent_table.id"))
    parent = relationship("Parent", backref="children")


engine = create_engine("sqlite:///./file.db", echo=True)
Base.metadata.create_all(engine)

session = sessionmaker(engine)()


p = Parent()
p.name = "father"

c1 = Child()
c1.name = "son"
p.children = [c1]

session.add_all([p, c1])
session.commit()


p = session.query(Parent).all()

pprint("-------- p[0] ----------")

pprint(p[0])
pprint(p[0].__dict__)


pprint("-------- p[0].children[0] ----------")

pprint(p[0].children[0])

pprint(p[0].children[0].__dict__)


c = session.query(Child).all()

pprint("-------- c[0] ----------")

pprint(c[0])

pprint(c[0].__dict__)

pprint("-------- c[0].parent ----------")

pprint(c[0].parent)

pprint(c[0].parent.__dict__)


pprint("-------- c[0].parent.children[0] ----------")

pprint(c[0].parent.children[0])

pprint(c[0].parent.children[0].__dict__)


```


## Output

    2023-03-31 22:29:48,276 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-03-31 22:29:48,276 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("node")
    2023-03-31 22:29:48,276 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-03-31 22:29:48,277 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("node")
    2023-03-31 22:29:48,277 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-03-31 22:29:48,277 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("edge")
    2023-03-31 22:29:48,277 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-03-31 22:29:48,277 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("edge")
    2023-03-31 22:29:48,277 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-03-31 22:29:48,277 INFO sqlalchemy.engine.Engine 
    CREATE TABLE node (
        node_id INTEGER NOT NULL, 
        PRIMARY KEY (node_id)
    )


    2023-03-31 22:29:48,277 INFO sqlalchemy.engine.Engine [no key 0.00006s] ()
    2023-03-31 22:29:48,277 INFO sqlalchemy.engine.Engine 
    CREATE TABLE edge (
        lower_id INTEGER NOT NULL, 
        higher_id INTEGER NOT NULL, 
        PRIMARY KEY (lower_id, higher_id), 
        FOREIGN KEY(lower_id) REFERENCES node (node_id), 
        FOREIGN KEY(higher_id) REFERENCES node (node_id)
    )


    2023-03-31 22:29:48,278 INFO sqlalchemy.engine.Engine [no key 0.00008s] ()
    2023-03-31 22:29:48,278 INFO sqlalchemy.engine.Engine COMMIT
    2023-03-31 22:29:48,282 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-03-31 22:29:48,283 INFO sqlalchemy.engine.Engine INSERT INTO node (node_id) VALUES (NULL), (NULL), (NULL), (NULL), (NULL), (NULL), (NULL) RETURNING node_id
    2023-03-31 22:29:48,283 INFO sqlalchemy.engine.Engine [generated in 0.00009s (insertmanyvalues)] ()
    2023-03-31 22:29:48,284 INFO sqlalchemy.engine.Engine INSERT INTO edge (lower_id, higher_id) VALUES (?, ?)
    2023-03-31 22:29:48,284 INFO sqlalchemy.engine.Engine [generated in 0.00010s] [(1, 2), (2, 1), (2, 3), (2, 4), (1, 5), (5, 6)]
    2023-03-31 22:29:48,284 INFO sqlalchemy.engine.Engine COMMIT
    2023-03-31 22:29:48,285 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-03-31 22:29:48,287 INFO sqlalchemy.engine.Engine SELECT node.node_id AS node_node_id 
    FROM node 
    WHERE node.node_id = ?
    2023-03-31 22:29:48,287 INFO sqlalchemy.engine.Engine [generated in 0.00009s] (5,)
    2023-03-31 22:29:48,287 INFO sqlalchemy.engine.Engine SELECT edge.lower_id AS edge_lower_id, edge.higher_id AS edge_higher_id 
    FROM edge 
    WHERE edge.lower_id = ?
    2023-03-31 22:29:48,288 INFO sqlalchemy.engine.Engine [generated in 0.00008s] (5,)
    2023-03-31 22:29:48,288 INFO sqlalchemy.engine.Engine SELECT node.node_id AS node_node_id 
    FROM node 
    WHERE node.node_id = ?
    2023-03-31 22:29:48,288 INFO sqlalchemy.engine.Engine [cached since 0.001406s ago] (6,)
    2023-03-31 22:29:48,289 INFO sqlalchemy.engine.Engine SELECT edge.lower_id AS edge_lower_id, edge.higher_id AS edge_higher_id 
    FROM edge 
    WHERE edge.higher_id = ?
    2023-03-31 22:29:48,289 INFO sqlalchemy.engine.Engine [generated in 0.00008s] (5,)
    2023-03-31 22:29:48,289 INFO sqlalchemy.engine.Engine SELECT node.node_id AS node_node_id 
    FROM node 
    WHERE node.node_id = ?
    2023-03-31 22:29:48,289 INFO sqlalchemy.engine.Engine [cached since 0.002424s ago] (1,)
    2023-03-31 22:29:48,289 INFO sqlalchemy.engine.Engine SELECT node.node_id AS node_node_id 
    FROM node 
    WHERE node.node_id = ?
    2023-03-31 22:29:48,289 INFO sqlalchemy.engine.Engine [cached since 0.002752s ago] (2,)
    2023-03-31 22:29:48,290 INFO sqlalchemy.engine.Engine SELECT edge.lower_id AS edge_lower_id, edge.higher_id AS edge_higher_id 
    FROM edge 
    WHERE edge.higher_id = ?
    2023-03-31 22:29:48,290 INFO sqlalchemy.engine.Engine [cached since 0.001027s ago] (2,)
    2023-03-31 22:29:48,290 INFO sqlalchemy.engine.Engine SELECT edge.lower_id AS edge_lower_id, edge.higher_id AS edge_higher_id 
    FROM edge 
    WHERE edge.lower_id = ?
    2023-03-31 22:29:48,290 INFO sqlalchemy.engine.Engine [cached since 0.002493s ago] (2,)
    2023-03-31 22:29:48,290 INFO sqlalchemy.engine.Engine SELECT node.node_id AS node_node_id 
    FROM node 
    WHERE node.node_id = ?
    2023-03-31 22:29:48,290 INFO sqlalchemy.engine.Engine [cached since 0.00361s ago] (3,)
    2023-03-31 22:29:48,291 INFO sqlalchemy.engine.Engine SELECT node.node_id AS node_node_id 
    FROM node 
    WHERE node.node_id = ?
    2023-03-31 22:29:48,291 INFO sqlalchemy.engine.Engine [cached since 0.003911s ago] (4,)

