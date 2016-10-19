import DSELoader
import logging

log = logging.getLogger()
log.setLevel('INFO')
logging.disable("DEBUG")

handler = logging.StreamHandler()

handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)


#create keyspace

#create tables

#create solr Cores
KEYSPACE = "solrdemo"

def main():
    log.info("starting main DemoBuild...")

    currCluster = DSELoader.setupCluster()
    currSession = DSELoader.connect(currCluster)

    #DSELoader.testConnection(currSession)

    status="off"
    status = DSELoader.getCluster_status(currSession)

    log.info("DemoBuild connect status..."+str(status))

    if status == "on":

        log.info(" Connected Building Keyspace and Tables...")
        currSession.execute("""CREATE KEYSPACE IF NOT EXISTS solrdemo WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }""")

        currSession.execute("""
            CREATE TABLE IF NOT EXISTS solrdemo.wikipages (
                title text,
                links text,
                content text,
                parent text,
                category list<text>,
                lang text,
                PRIMARY KEY (title, parent,lang)
            )
            """)


    else:
        log.info("[ERROR] not connected to cluster aborting...")
        print "Error not connected"

if __name__ == "__main__":
    main()