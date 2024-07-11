import pandas as pd
import rdflib
from rdfpandas.graph import to_graph
from rdflib import Graph, Namespace
from rdflib.namespace import NamespaceManager
from rdflib.namespace import DC

df = pd.read_csv('DC_Metadata.csv', encoding = "ISO-8859-1") #read the csv file localy
#define the namespaces
namespace_manager = NamespaceManager(Graph())
namespace_manager.bind("dc", DC)
g = to_graph(df, namespace_manager) #transform the csv file in graph

#create the turtle file
serialized_rdf = g.serialize("csvtordf.ttl", format='turtle')
print(serialized_rdf)
