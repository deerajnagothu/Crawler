import csv
from py2neo import Graph, Node, Relationship
delete_graph_history = "no"
database = "localhost"
graph_database_location = "http://"+database+":7474/db/data/"
graph = Graph(graph_database_location, user='neo4j', password='cns2202') # connect to the local graph database
gp = graph.begin()


statement = 'MATCH (n:New_Tab) WHERE ((n.Crawled_by="CRAWLER-1")) RETURN n.URL,n.Memory_percentage'
urls=[]
memory=[]
cursor = gp.run(statement).data()
for each in cursor:
    x = list(each.values())
    print(x[0])
    if len(str(x[0])) > 25:
        urls.append(x[0])
        memory.append(x[1])
    else:
        urls.append(x[1])
        memory.append(x[0])

xaxis = []
for each in range(0,len(urls)):
    xaxis.append(each)
#print((urls))
#print(len(memory)

with open('output.csv', 'w') as file:
    for i in range(0,len(urls)):
        k = urls[i]+","+str(memory[i])+"\n"
        file.write(k)

