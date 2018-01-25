from config.dbconfig import pg_config
import psycopg2
class UsersDAO:

    def __init__(self):

        connection_url = "host=%s dbname=%s user=%s password=%s port=%s" % (pg_config['host'], pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['port'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUserTypes(self):
        cursor = self.conn.cursor()
        query = "select * from userType;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserRequests(self):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join userRequest;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserTypeByID(self, type):
        cursor = self.conn.cursor()
        query = "select user_type from userType where usertypeid = %s;"
        cursor.execute(query, (type,))
        result = cursor.fetchone()
        return result

    def getUsersByID(self, uid):
        cursor = self.conn.cursor()
        query = "select * from users where userid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getUsersByTypeID(self, utid):
        cursor = self.conn.cursor()
        query = "select * from users where userTypeID = %s;"
        cursor.execute(query, (utid,))
        result = cursor.fetchone()
        return result

    def getUsersByType(self, usertype):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join user_type where user_type = %s;"
        cursor.execute(query, (usertype,))
        result = cursor.fetchone()
        return result

    def getUserByFirstName(self, fname):
        cursor = self.conn.cursor()
        query = "select * from users where user_first_name = %s;"
        cursor.execute(query, (fname,))
        result = cursor.fetchone()
        return result

    def getUserByLastName(self, lname):
        cursor = self.conn.cursor()
        query = "select * from users where user_last_name = %s;"
        cursor.execute(query, (lname,))
        result = cursor.fetchone()
        return result

    def getUserByEmail(self, uemail):
        cursor = self.conn.cursor()
        query = "select * from users where user_email = %s;"
        cursor.execute(query, (uemail,))
        result = cursor.fetchone()
        return result

    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select * from userRequest;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserRequestsByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select * from userRequest where userid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserRequestsByRequestID(self, rid):
        cursor = self.conn.cursor()
        query = "select * from userRequest where requestid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getUserRequestsByUserIDandResourceID(self, uid, rid):
        cursor = self.conn.cursor()
        query = "select * from userRequest where userid = %s and requestid = %s;"
        cursor.execute(query, (uid,rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, userID, userTypeID, user_first_name, user_last_name, user_email):
        cursor = self.conn.cursor()
        query = "insert into users(userID, userTypeID, user_first_name, user_last_name, user_email) values (%s, %s, %s, %s, %s) returning userID;"
        cursor.execute(query, (userID, userTypeID, user_first_name, user_last_name, user_email))
        userID = cursor.fetchone()[0]
        self.conn.commit()
        return userID

    def delete(self, userID):
        cursor = self.conn.cursor()
        query = "delete from users where userID = %s;"
        cursor.execute(query, (userID,))
        self.conn.commit()
        return userID

    def update(self, userID, userTypeID, user_first_name, user_last_name, user_email):
        cursor = self.conn.cursor()
        query = "update users set userTypeID = %s,user_first_name = %s, user_last_name = %s, user_email = %s where userID = %s;"
        cursor.execute(query, (userTypeID, user_first_name, user_last_name, user_email, userID,))
        self.conn.commit()
        return userID