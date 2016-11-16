

from py2neo import Graph, Node, Relationship
graph_database_location = "http://127.0.0.1:7474/db/data/"
graph = Graph(graph_database_location, user='neo4j', password='cns2202') # connect to the local graph database

tx=graph.begin()

statement = 'MATCH (n:New_Tab) WHERE n.Crawler="local-computer" RETURN n.URL'

count=[]
#print(tx)
#tx.append(statement)
#print(tx.evaluate(statement))
cursor=tx.run(statement).data()
for each in cursor:
    x=list(each.values())
    count.append(x[0])
print(count)
    
#while cursor.forward():
#    print(cursor.current["name"])
#x=cursor[1].values()
#y=cursor[1].keys()
#print(tx.process())
#print(x.split())
#print(y)
tx.commit()

