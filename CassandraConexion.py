from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('termometro')
session.set_keyspace('termometro')


def getCluster():
    return session