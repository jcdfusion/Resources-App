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

    def build_user_attributes(self, userID, userTypeID, user_first_name, user_last_name, user_email):
        result = {}
        result['userID'] = userID
        result['userTypeID'] = userTypeID
        result['user_first_name'] = user_first_name
        result['user_last_name'] = user_last_name
        result['user_email'] = user_email
        return result

    #def build_transaction_dict(self, resourceid, userid, ccnumb, transactionid, ccfirst, cclast, expdate, cvc, ctype, usertypeid, user_first_name, user_last_name, user_email, collectioncenterid, resourcetype, buy_free, market_price, qty):
    def build_transaction_dict(self, row):
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print(row[4])
        print(row[5])
        print(row[6])
        print(row[7])
        print(row[8])
        print(row[9])
        print(row[10])
        print(row[11])
        print(row[12])
        print(row[13])
        print(row[14])
        print(row[15])
        print(row[16])
        print(row[17])
        result = {}
        result['resourceid'] = row[0]
        result['userid'] = row[1]
        result['ccnumb'] = row[2]
        result['transactionid'] = row[3]
        result['ccfirst'] = row[4]
        result['cclast'] = row[5]
        result['expdate'] = row[6]
        result['cvc'] = row[7]
        result['ctype'] = row[8]
        result['usertypeid'] = row[9]
        result['user_first_name'] = row[10]
        result['user_last_name'] = row[11]
        result['user_email'] = row[12]
        result['collectioncenterid'] = row[13]
        result['resourcetype'] = row[14]
        result['buy_free'] = row[15]
        result['market_price'] = row[16]
        result['qty'] = row[17]
        return result

    def build_userinfo_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['ccid'] = row[1]
        result['uid'] = row[2]
        result['street'] = row[3]
        result['town'] = row[4]
        result['state'] = row[5]
        result['country'] = row[6]
        result['ccnane'] = row[7]
        result['zipcode'] = row[8]
        result['rname'] = row[9]
        result['buy_free'] = row[10]
        result['marketPrice'] = row[11]
        result['qtyfromsupplier'] = row[12]
        return result

    def build_userRequest_dict(self, row):
        result = {}
        result['rid'] = row[0]  # request id
        result['uid'] = row[1]  # requesting user id
        result['resourceid'] = row[2]  # resource id
        result['rfname'] = row[3]  # requester first name
        result['rlname'] = row[4]  # requester last name
        result['remail'] = row[5]  # requester email
        result['rphone'] = row[6]  # requester phone
        result['rstreet'] = row[7]  # requester street
        result['rtown'] = row[8]  # requester town
        result['rstate'] = row[9]  # requester state
        result['rcountry'] = row[10]  # requester country
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
            return user  # jsonify(User=user)

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

    def getTransactions(self, userid):
        dao = UsersDAO()
        row = dao.getTransaction(userid)
        if not row:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            location = self.build_transaction_dict(row)
            return jsonify(Location=location)

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
            # self.getUserRequestsByUserIDandResourceID(username, resourceid)
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
            # self.getUserRequestsByRequestID(username)
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
            # self.getUserRequestsByUserID(requestid)
            dao = UsersDAO()
            row = dao.getUserRequestsByRequestID(requestid)
            if not row:
                return jsonify(Error="Request Not Found"), 404
            else:
                user = self.build_userRequest_dict(row)
                return jsonify(User=user)
        else:
            return jsonify(Error="Malformed search string."), 400

    def insertUser(self, form):
        if form and len(form) == 6:
            userID = form['userID']
            userTypeID = form['userTypeID']
            user_first_name = form['user_first_name']
            user_last_name = form['user_last_name']
            user_email = form['user_email']
            user_password = form['user_password']
            if userID and userTypeID and user_first_name and user_last_name and user_email and user_password:
                dao = UsersDAO()
                uid = dao.insert(userID, userTypeID, user_first_name, user_last_name, user_email)
                upw = dao.insertPassword(userID, user_password)
                result = {}
                result['userID'] = uid
                result['userTypeID'] = userTypeID
                result['user_first_name'] = user_first_name
                result['user_last_name'] = user_last_name
                result['user_email'] = user_email
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    def deleteUser(selfself, userID):
        dao = UsersDAO()
        if not dao.getUsersByID(userID):
            return jsonify(Error="User not found."), 404
        else:
            dao.delete(userID)
            return jsonify(DeleteStatus="OK"), 200

    def updateUser(self, userID, form):
        dao = UsersDAO()
        if not dao.getUsersByID(userID):
            return jsonify(Error="User not found."), 404
        else:
            if len(form) != 6:
                return jsonify(Error="Malformed update request"), 400
            else:
                userTypeID = form['userTypeID']
                user_first_name = form['user_first_name']
                user_last_name = form['user_last_name']
                user_email = form['user_email']
                if userTypeID and user_first_name and user_last_name and user_email:
                    dao.update(userID, userTypeID, user_first_name, user_last_name, user_email)
                    result = self.build_users_attributes(userID, userTypeID, user_first_name, user_last_name,
                                                         user_email)
                    return jsonify(Center=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def userLogin(self, args):
        if (len(args) < 2):
            return jsonify(Error="Include both username and password"), 400
        else:
            dao = UsersDAO()
            username = args['username']
            password = args['password']
            user_list = []
            user_list = dao.getUserByPassword(username, password)
            if not user_list:
                return jsonify(Error="Username and password missmatch!")
            else:
                return self.getUserRequestsByUserID(username)

    def userPurchase(self, form):
        dao = UsersDAO()
        if len(form) < 9:
            return jsonify(Error="User Not Found"), 400
        userid = form['userid']
        password = form['password']
        ccnumb = form['ccnumb']
        ccfirst = form['ccfirst']
        cclast = form['cclast']
        expdate = form['expdate']
        cvc = form['cvc']
        ctype = form['ctype']
        resourceid = form['resourceid']
        if not dao.getUsersByID(userid):
            return jsonify(Error="User not found."), 404
        else:
            dao.insertCard(ccnumb, userid, ccfirst, cclast, expdate, cvc, ctype)
            dao.insertTransaction(userid, resourceid, ccnumb)
            return self.getTransactions(userid)


