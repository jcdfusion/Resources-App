from config.dbconfig import pg_config
import psycopg2
class ResourcesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResorces(self):
        return "select * from resources;"

    def getResourceById(self):
        return "select * from resources;"

    def getResourceByName(self):
        return "select * from resources;"

    def getResourceByStore(self):
        return "select * from resources;"