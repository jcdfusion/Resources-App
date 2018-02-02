from config.dbconfig import pg_config
import psycopg2
class TransactionDAO:

    def __init__(self):

        connection_url = "host=%s dbname=%s user=%s password=%s port=%s" % (pg_config['host'], pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['port'])
        self.conn = psycopg2._connect(connection_url)

    def getAllTransaction(self):
        cursor = self.conn.cursor()
        query = "select * from transaction natural inner join creditcards natural inner join users natural inner join resources"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByResourceid(self, resourceid):
        cursor = self.conn.cursor()
        query = "select * from transaction natural inner join creditcards natural inner join users natural inner join resources where resourceid = %s"
        cursor.execute(query, (resourceid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByCCFirst(self,ccfirst):
        cursor = self.conn.cursor()
        query = "select * from transaction natural inner join creditcards natural inner join users natural inner join resources where LOWER(ccfirst) = LOWER(%s)"
        cursor.execute(query, (ccfirst,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByCCLast(self,cclast):
        cursor = self.conn.cursor()
        query = "select * from transaction natural inner join creditcards natural inner join users natural inner join resources where LOWER(cclast) = LOWER(%s)"
        cursor.execute(query, (cclast,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByCCNumb(self,ccnumb):
        cursor = self.conn.cursor()
        query = "select * from transaction natural inner join creditcards natural inner join users natural inner join resources where ccnumb = %s"
        cursor.execute(query, (ccnumb,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByCCType(self,cctype):
        cursor = self.conn.cursor()
        query = "select * from transaction natural inner join creditcards natural inner join users natural inner join resources where LOWER(ctype) = LOWER(%s)"
        cursor.execute(query, (cctype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByCenter(self,collectioncenterid):
        cursor = self.conn.cursor()
        query = "select * from transaction natural inner join creditcards natural inner join users natural inner join resources where collectioncenterid = %s"
        cursor.execute(query, (collectioncenterid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByMarketPrice(self,market_price):
        cursor = self.conn.cursor()
        query = "select * from transaction natural inner join creditcards natural inner join users natural inner join resources where market_price = %s"
        cursor.execute(query, (market_price,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByBF(self,buy_free):
        cursor = self.conn.cursor()
        query = "select * from transaction natural inner join creditcards natural inner join users natural inner join resources where buy_free = %s"
        cursor.execute(query, (buy_free,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByResourceType(self,resourcetype):
        cursor = self.conn.cursor()
        query = "select * from transaction natural inner join creditcards natural inner join users natural inner join resources where LOWER(resourcetype) = LOWER(%s)"
        cursor.execute(query, (resourcetype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByUserFirstName(self,user_first_name):
        cursor = self.conn.cursor()
        query = "select * from transaction natural inner join creditcards natural inner join users natural inner join resources where LOWER(user_first_name) = LOWER(%s)"
        cursor.execute(query, (user_first_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByUserLastName(self,user_last_name):
        cursor = self.conn.cursor()
        query = "select * from transaction natural inner join creditcards natural inner join users natural inner join resources where LOWER(user_last_name) = LOWER(%s)"
        cursor.execute(query, (user_last_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByUserid(self,userid):
        cursor = self.conn.cursor()
        query = "select * from transaction natural inner join creditcards natural inner join users natural inner join resources where userid = %s"
        cursor.execute(query, (userid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByEmail(self, user_email):
        cursor = self.conn.cursor()
        query = "select * from transaction natural inner join creditcards natural inner join users natural inner join resources where user_email = %s"
        cursor.execute(query, (user_email,))
        result = []
        for row in cursor:
            result.append(row)
        return result
