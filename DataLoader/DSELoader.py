from cassandra.cluster import Cluster
import logging

log = logging.getLogger()
log.setLevel('INFO')
logging.disable("DEBUG")

handler = logging.StreamHandler()

handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)



defaultCluster = ['54.224.248.252','52.91.35.155','54.204.206.41']
defaultKeyspace = 'system'

def testConnection (session):
    session.set_keyspace('system')
    rows = session.execute('SELECT * FROM peers')
    for row in rows:
        print row.peer, row.data_center, row.host_id, row.preferred_ip, row.rack, row.release_version, row.rpc_address, row.schema_version, row.tokens, row.workload

def getCluster_status(currSessionIn):

    currStatus = "unknown"
    clusterName="unknown"
    rows = currSessionIn.execute("""select cluster_name from system.local""")
    for row in rows:
        clusterName= row.cluster_name
        print clusterName
    if clusterName == "":
        currStatus="off"
    else:
        currStatus="on"
    return currStatus

def setupCluster():
    cluster = Cluster(defaultCluster)
    return cluster

def connect(clusterIn):
    session = clusterIn.connect()
    return session

def main():
    currCluster = setupCluster()
    currSession = connect(currCluster)

    print currSession.get_pool_state()
    print currSession.hosts
    print currCluster.metadata._hosts

    print "Connected"

    testConnection(currSession)

if __name__ == "__main__":
    main()