from flask import jsonify
from dao.users import UsersDAO

class UsersHandler:

    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]  # user id
        result['type'] = row[1]  # user type
        result['fname'] = row[2]  # user first name
        result['lname'] = row[3]  # user last name
        result['email'] = row[4]  # user email
        return result  # return result

    def build_userType_dict(self, row):
        result = {}
        result['utid'] = row[0]  # user type id
        result['utype'] = row[1]  # user type
        return result  # return result

    def build_userRequest_dict(self, row):
        result = {}
        result['rid'] = row[0]  # request id
        result['uid'] = row[1]  # requesting user id
        result['resourceid'] = row[2]  # resource id
        result['rfname'] = row[3]  # requester first name
        result['rlname'] = row[4]  # requester last name
        result['remail'] = row[5]   # requester email
        result['rphone'] = row[6]  # requester phone
        result['rstreet'] = row[7]  # requester street
        result['rtown'] = row[8]  # requester town
        result['rstate'] = row[9]  # requester state
        result['rcountry'] = row[10] # requester country
        result['rzip'] = row[11]  # requester zipcode
        result['ccid'] = row[12]  # collection center id
        return result

    def getAllUserTypes(self):
        dao = UsersDAO()
        location_list = dao.getAllUserTypes()
        result_list = []
        for row in location_list:
            result = self.build_userType_dict(row)
            result_list.append(result)
        return jsonify(UserType=result_list)

    def getAllUsers(self):
        dao = UsersDAO()
        location_list = dao.getAllUsers()
        result_list = []
        for row in location_list:
            result = self.build_userType_dict(row)
            result_list.append(result)
        return jsonify(UserType=result_list)

    def getUserTypeByID(self, utid):
        dao = UsersDAO()
        row = dao.getUserTypeByID(utid)
        if not row:
            return jsonify(Error="User Type Not Found"), 404
        else:
            userType = self.build_userType_dict(row)
            return jsonify(UserType=userType)

    def getUsersByID(self, uid):
        dao = UsersDAO()
        row = dao.getUsersByID(uid)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return user #jsonify(User=user)

    def getUsersByTypeID(self, tid):
        dao = UsersDAO()
        if not dao.getUserTypeByID(tid):
            return jsonify(Error="User Type Not Found"), 404
        request_list = dao.getUsersByTypeID(tid)
        result_list = []
        for row in request_list:
            user = self.build_userRequest_dict(row)
            result_list.append(user)
        return jsonify(User=result_list)

    def getUsersByType(self, tid):
        dao = UsersDAO()
        if not dao.getUserTypeByID(tid):
            return jsonify(Error="User Type Not Found"), 404
        request_list = dao.getUsersByTypeID(tid)
        result_list = []
        for row in request_list:
            user = self.build_userRequest_dict(row)
            result_list.append(user)
        return jsonify(User=result_list)

    def getUserByFirstName(self, fname):
        dao = UsersDAO()
        row = dao.getUserByFirstName(fname)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    def getUserByLastName(self, lname):
        dao = UsersDAO()
        row = dao.getUserByLastName(lname)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    def getUserByEmail(self, email):
        dao = UsersDAO()
        row = dao.getUserByEmail(email)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    def getAllRequests(self):
        dao = UsersDAO()
        location_list = dao.getAllRequests()
        result_list = []
        for row in location_list:
            result = self.build_userRequest_dict(row)
            result_list.append(result)
        return jsonify(UserType=result_list)

    def getUserRequestsByUserID(self, uid):
        dao = UsersDAO()
        if not dao.getUsersByID(uid):
            return jsonify(Error="User Not Found"), 404
        request_list = dao.getUserRequestsByUserID(uid)
        result_list = []
        for row in request_list:
            result = self.build_userRequest_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getUserRequestsByRequestID(self, rid):
        dao = UsersDAO()
        row = dao.getUserRequestsByRequestID(rid)
        if not row:
            return jsonify(Error="Request Not Found"), 404
        else:
            user = self.build_userRequest_dict(row)
            return jsonify(User=user)

    def getUserRequestsByUserIDandResourceID(self, uid, rid):
        dao = UsersDAO()
        if not dao.getUsersByID(uid):
            return jsonify(Error="User Not Found"), 404
        request_list = dao.getUserRequestsByUserIDandResourceID(uid, rid)
        result_list = []
        for row in request_list:
            result = self.build_userRequest_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def searchUsers(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string."), 400
        else:
            username = args.get("username")
            usertype = args.get("usertype")
            firstname = args.get("firstname")
            lastname = args.get("lastname")
            email = args.get("email")

            if username:
                dao = UsersDAO()
                row = dao.getUsersByID(username)
                if not row:
                    return jsonify(Error="User Not Found"), 404
                else:
                    user = self.build_user_dict(row)
                    return jsonify(User=user)
            elif usertype:
                dao = UsersDAO()
                if not dao.getUserTypeByID(usertype):
                    return jsonify(Error="User Type Not Found"), 404
                request_list = dao.getUsersByTypeID(usertype)
                result_list = []
                for row in request_list:
                    user = self.build_userRequest_dict(row)
                    result_list.append(user)
                return jsonify(User=result_list)
            elif firstname:
                dao = UsersDAO()
                row = dao.getUserByFirstName(firstname)
                if not row:
                    return jsonify(Error="User Not Found"), 404
                else:
                    user = self.build_user_dict(row)
                    return jsonify(User=user)
            elif lastname:
                dao = UsersDAO()
                row = dao.getUserByLastName(lastname)
                if not row:
                    return jsonify(Error="User Not Found"), 404
                else:
                    user = self.build_user_dict(row)
                    return jsonify(User=user)
            elif email:
                dao = UsersDAO()
                row = dao.getUserByEmail(email)
                if not row:
                    return jsonify(Error="User Not Found"), 404
                else:
                    user = self.build_user_dict(row)
                    return jsonify(User=user)
            else:
                return jsonify(Error="Malformed search string."), 400

    def searchUsersRequests(self, args):
        if len(args) > 2:
            return jsonify(Error="Malformed search string."), 400
        else:
            username = args.get("username")
            requestid = args.get("requestid")
            resourceid = args.get("requestid")
        if username and resourceid:
            #self.getUserRequestsByUserIDandResourceID(username, resourceid)
            dao = UsersDAO()
            if not dao.getUsersByID(username):
                return jsonify(Error="User Not Found"), 404
            request_list = dao.getUserRequestsByUserIDandResourceID(username, resourceid)
            result_list = []
            for row in request_list:
                result = self.build_userRequest_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)
        elif username:
            #self.getUserRequestsByRequestID(username)
            dao = UsersDAO()
            if not dao.getUsersByID(username):
                return jsonify(Error="User Not Found"), 404
            request_list = dao.getUserRequestsByUserID(username)
            result_list = []
            for row in request_list:
                result = self.build_userRequest_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)
        elif requestid:
            #self.getUserRequestsByUserID(requestid)
            dao = UsersDAO()
            row = dao.getUserRequestsByRequestID(requestid)
            if not row:
                return jsonify(Error="Request Not Found"), 404
            else:
                user = self.build_userRequest_dict(row)
                return jsonify(User=user)
        else:
            return jsonify(Error="Malformed search string."), 400