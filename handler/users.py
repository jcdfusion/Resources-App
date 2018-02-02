from flask import jsonify
from dao.users import UsersDAO


class UsersHandler:

        def build_user_dict(self, row):
        result = {}
        result['username'] = row[0]  # user id
        result['usertype'] = row[1]  # user type
        result['firstname'] = row[2]  # user first name
        result['lastname'] = row[3]  # user last name
        result['email'] = row[4]  # user email
        return result  # return result




    def build_userType_dict(self, row):
        result = {}
        result['utype'] = row[0]  # user type
        return result  # return result

    def build_user_attributes(self, userID, userTypeID, user_first_name, user_last_name, user_email):
        result = {}
        result['userID'] = userID
        result['userTypeID'] = userTypeID
        result['user_first_name'] = user_first_name
        result['user_last_name'] = user_last_name
        result['user_email'] = user_email
        return result
    def build_userinfo_dict(self,row):
        result={}
        result['rid']=row[0]
        result['ccid']=row[1]
        result['uid']=row[2]
        result['street'] = row[3]
        result['town'] = row[4]
        result['state'] = row[5]
        result['country']=row[6]
        result['ccnane'] = row[7]
        result['zipcode']=row[8]
        result['rname']=row[9]
        result['buy_free']=row[10]
        result['marketPrice']=row[11]
        result['qtyfromsupplier']=row[12]
        return result

    def build_userRequest_dict(self, row):
        result = {}
        result['rid'] = row[0]  # request id
        result['userid'] = row[1]  # requesting user id
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
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(UserInfo=result_list)

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
        return jsonify(UserRequest=result_list)

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
            getusertype = args.get("getusertype")

            if username:
                dao = UsersDAO()
                request_list = dao.getUsersByID(username)
                if not request_list:
                    return jsonify(Error="User Not Found"), 404
                else:
                    result_list = []
                    for row in request_list:
                        user = self.build_user_dict(row)
                        result_list.append(user)
                    return jsonify(User=result_list)
            elif usertype:
                dao = UsersDAO()
                if not dao.getUserTypeByID(usertype):
                    return jsonify(Error="User Type Not Found"), 404
                request_list = dao.getUsersByTypeID(usertype)
                result_list = []
                for row in request_list:
                    user = self.build_user_dict(row)
                    result_list.append(user)
                return jsonify(User=result_list)

            elif getusertype:
                dao = UsersDAO()
                dao.getUserTypeByID(usertype)
                request_list = dao.getUserTypeByID(getusertype)
                result_list = []
                for row in request_list:
                    user = self.build_userType_dict(row)
                    result_list.append(user)
                return jsonify(UserType=result_list)


            elif firstname:
                dao = UsersDAO()
                request_list = dao.getUserByFirstName(firstname)
                if not request_list:
                    return jsonify(Error="User Not Found"), 404
                else:
                    result_list = []
                    for row in request_list:
                        user = self.build_user_dict(row)
                        result_list.append(user)
                    return jsonify(User=result_list)

            elif lastname:
                dao = UsersDAO()
                request_list = dao.getUserByLastName(lastname)
                if not request_list:
                    return jsonify(Error="User Not Found"), 404
                else:
                    result_list = []
                    for row in request_list:
                        user = self.build_user_dict(row)
                        result_list.append(user)
                    return jsonify(User=result_list)


            elif email:
                dao = UsersDAO()
                request_list = dao.getUserByEmail(email)
                if not request_list:
                    return jsonify(Error="User Not Found"), 404
                else:
                    result_list = []
                    for row in request_list:
                        user = self.build_user_dict(row)
                        result_list.append(user)
                    return jsonify(User=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def searchUsersRequests(self, args):
        if len(args) > 2:
            return jsonify(Error="Malformed search string."), 400
        else:
            ccid = args.get("ccid")
            rcountry = args.get("rcountry")
            remail = args.get("remail")
            resourceid = args.get("resourceid")
            rfname = args.get("rfname")
            rid = args.get("rid")
            rlname = args.get("rlname")
            rphone = args.get("rphone")
            rstate = args.get("rstate")
            rstreet = args.get("rstreet")
            rtown = args.get("rtown")
            rzip = args.get("rzip")
            userid =args.get("userid")

        dao = UsersDAO()
        if ccid:
            if not dao.getUserRequestsByCollectionCenter(ccid):
                return jsonify(Error="User Not Found"), 404
            request_list = dao.getUserRequestsByCollectionCenter(ccid)
            result_list=[]
            for row in request_list:
                result = self.build_userRequest_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)

        elif rcountry:
            if not dao.getUserRequestByCountry(rcountry):
                return jsonify(Error="User Not Found"), 404
            request_list = dao.getUserRequestByCountry(rcountry)
            result_list=[]
            for row in request_list:
                result = self.build_userRequest_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)

        elif remail:
            if not dao.getUserRequestByEmail(remail):
                return jsonify(Error="User Not Found"), 404
            request_list = dao.getUserRequestByEmail(remail)
            result_list=[]
            for row in request_list:
                result = self.build_userRequest_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)

        elif resourceid:
            if not dao.getUserRequestByResourceID(resourceid):
                return jsonify(Error="User Not Found"), 404
            request_list = dao.getUserRequestByResourceID(resourceid)
            result_list=[]
            for row in request_list:
                result = self.build_userRequest_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)

        elif rfname:
            if not dao.getUserRequestByFirstName(rfname):
                return jsonify(Error="User Not Found"), 404
            request_list = dao.getUserRequestByFirstName(rfname)
            result_list=[]
            for row in request_list:
                result = self.build_userRequest_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)

        elif rlname:
            if not dao.getUserRequestByLastName(rlname):
                return jsonify(Error="User Not Found"), 404
            request_list = dao.getUserRequestByLastName(rlname)
            result_list=[]
            for row in request_list:
                result = self.build_userRequest_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)

        elif rphone:
            if not dao.getUserRequestByPhone(rphone):
                return jsonify(Error="User Not Found"), 404
            request_list = dao.getUserRequestByPhone(rphone)
            result_list=[]
            for row in request_list:
                result = self.build_userRequest_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)

        elif rstate:
            if not dao.getUserRequestByState(rstate):
                return jsonify(Error="User Not Found"), 404
            request_list = dao.getUserRequestByState(rstate)
            result_list=[]
            for row in request_list:
                result = self.build_userRequest_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)

        elif rtown:
            if not dao.getUserRequestByTown(rtown):
                return jsonify(Error="User Not Found"), 404
            request_list = dao.getUserRequestByTown(rtown)
            result_list=[]
            for row in request_list:
                result = self.build_userRequest_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)

        elif rzip:
            if not dao.getUserRequestByZipcode(rzip):
                return jsonify(Error="User Not Found"), 404
            request_list = dao.getUserRequestByZipcode(rzip)
            result_list=[]
            for row in request_list:
                result = self.build_userRequest_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)

        elif userid:
            if not dao.getUserRequestsByUserID(userid):
                return jsonify(Error="User Not Found"), 404
            request_list = dao.getUserRequestsByUserID(userid)
            result_list=[]
            for row in request_list:
                result = self.build_userRequest_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)

        elif rid:
            if not dao.getUserRequestsByRequestID(rid):
                return jsonify(Error="User Not Found"), 404
            request_list = dao.getUserRequestsByRequestID(rid)
            result_list=[]
            for row in request_list:
                result = self.build_userRequest_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)
        
        
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
        ccv = form['ccv']
        ctype = form['ctype']
        resourceid = form['resourceid']
        if not dao.getUsersByID(userid):
            return jsonify(Error="User not found."), 404
        else:
            dao.insertCard(ccnumb, userid, ccfirst, cclast, expdate, ccv, ctype)
            dao.insertTransaction(userid, resourceid, ccnumb)
            return self.getTransactions(userid)


