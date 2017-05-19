"""
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

"""

import csv
import math
import statistics
urls_memory = {}
urls = []
memory = []
with open('slickdeals_private_memory.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        urls_memory[row[0]]=row[1]
        urls.append(row[0])
        memory.append(row[1])

less_than_10k = []
between_10k_and_20k = []
between_20k_and_30k = []
between_30k_and_40k = []
between_40k_and_50k = []
between_50k_and_60k = []
between_60k_and_70k = []
between_70k_and_80k = []
between_80k_and_90k = []
between_90k_and_100k = []
greater_than_100k = []
remove_k = []
for each in memory:
    each = each[:-1]
    y = int(each)
    remove_k.append(y)

scaled_memory = []
#print(sorted(remove_k))
for x in remove_k:
    x = math.log10(x)
    scaled_memory.append(x)

#print(sorted(scaled_memory))

print(statistics.mean(remove_k))
print(statistics.stdev(remove_k))

print(statistics.variance(remove_k))
"""
for each in remove_k:
    if each < 10000:
        less_than_10k.append(each)
    elif 10000 < each <20000:
        between_10k_and_20k.append(each)
    elif 20000 < each < 30000:
        between_20k_and_30k.append(each)
    elif 30000 < each < 40000:
        between_30k_and_40k.append(each)
    elif 40000 < each < 50000:
        between_40k_and_50k.append(each)
    elif 50000 < each < 60000:
        between_40k_and_50k.append(each)
    elif 60000 < each < 70000:
        between_60k_and_70k.append(each)
    elif 70000 < each < 80000:
        between_70k_and_80k.append(each)
    elif 80000 < each < 90000:
        between_80k_and_90k.append(each)
    elif 90000 < each < 100000:
        between_90k_and_100k.append(each)
    else:
        greater_than_100k.append(each)



print(len(memory))

"""
