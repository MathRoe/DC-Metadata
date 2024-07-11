#tutoriel : https://stackoverflow.com/questions/43524943/creating-rdf-file-using-csv-file-as-input
#tutoriel : https://pypi.org/project/rdfpandas/
#guide sur rdflib : https://readthedocs.org/projects/rdflib/downloads/pdf/latest/

import pandas as pd
import rdflib
from rdfpandas.graph import to_graph
from rdflib import Graph, Namespace
from rdflib.namespace import NamespaceManager
from rdflib.namespace import DC

df = pd.read_csv('DC_Metadata.csv', encoding = "ISO-8859-1") #lire le csv
#définir les namespace
namespace_manager = NamespaceManager(Graph())
namespace_manager.bind("dc", DC)
g = to_graph(df, namespace_manager) #transformer le csv en graph

#créer le fichier rdf
serialized_rdf = g.serialize("csvtordf.ttl", format='turtle')
print(serialized_rdf)