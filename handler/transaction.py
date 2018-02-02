from flask import jsonify
from dao.transaction import TransactionDAO


class TransactionHandler():


    def build_transaction_dict(self ,row):
        result={}
        result['ccnum'] = row[0]
        result['userid']=row[1]
        result['ccfirstname']=row[2]
        result['cclastname']=row[3]
        result['expdate']=row[4]
        result['ccv']=row[5]
        result['cctype']=row[6]
        return result

    def build_transactioninfo_dict(self, row):
        result = {}
        result['resourceid'] = row[0]
        result['userid'] = row[1]
        result['ccnumb'] = row[2]
        result['transactionid'] = row[3]
        result['ccfirst'] = row[4]
        result['cclast'] = row[5]
        result['expdate'] = row[6]
        result['ccv'] = row[7]
        result['cctype'] = row[8]
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

    def getAllTransactions(self):
        dao = TransactionDAO()
        transaction_list = dao.getAllTransaction()
        result_list = []
        for row in transaction_list:
            result = self.build_transactioninfo_dict(row)
            result_list.append(result)
            return jsonify(Transactions=result_list)

    def searchTransaction(self, args):
        resourceid = args.get('resourceid')
        userid = args.get('userid')
        ccnumb = args.get('ccnumb')
        transactionid = args.get('transactionid')
        ccfirst = args.get('ccfirst')
        cclast = args.get('cclast')
        expdate = args.get('expdate')
        ccv = args.get('ccv')
        cctype = args.get('cctype')
        user_first_name = args.get('user_fisrt_name')
        user_last_name = args.get('user_last_name')
        user_email = args.get('user_email')
        collectioncenterid = ('collectioncenterid')
        resourcetype = ('resourcetype')
        buy_free = args.get('buy_free')
        market_price = args.get('market_price')
        qty = args.get('qty')

        dao = TransactionDAO()
        if resourceid:
            transaction_list = dao.getTransactionByResourceid(resourceid)
            result_list = []
            for row in transaction_list:
                result = self.build_transactioninfo_dict(row)
                result_list.append(result)
                return jsonify(Transactions=result_list)
        elif userid:
            transaction_list = dao.getTransactionByUserid(userid)
            result_list = []
            for row in transaction_list:
                result = self.build_transactioninfo_dict(row)
                result_list.append(result)
                return jsonify(Transactions=result_list)

        elif ccnumb:
            transaction_list = dao.getTransactionByCCNumb(ccnumb)
            result_list = []
            for row in transaction_list:
                result = self.build_transactioninfo_dict(row)
                result_list.append(result)
                return jsonify(Transactions=result_list)

        elif ccfirst:
            transaction_list = dao.getTransactionByCCFirst(ccfirst)
            result_list = []
            for row in transaction_list:
                result = self.build_transactioninfo_dict(row)
                result_list.append(result)
                return jsonify(Transactions=result_list)

        elif cclast:
            transaction_list = dao.getTransactionByCCLast(cclast)
            result_list = []
            for row in transaction_list:
                result = self.build_transactioninfo_dict(row)
                result_list.append(result)
                return jsonify(Transactions=result_list)

        elif cctype:
            transaction_list = dao.getTransactionByCCType(cctype)
            result_list = []
            for row in transaction_list:
                result = self.build_transactioninfo_dict(row)
                result_list.append(result)
                return jsonify(Transactions=result_list)

        elif resourcetype:
            transaction_list = dao.getTransactionByResourceType(resourcetype)
            result_list = []
            for row in transaction_list:
                result = self.build_transactioninfo_dict(row)
                result_list.append(result)
                return jsonify(Transactions=result_list)

        elif user_first_name:
            transaction_list = dao.getTransactionByUserFirstName(user_first_name)
            result_list = []
            for row in transaction_list:
                result = self.build_transactioninfo_dict(row)
                result_list.append(result)
                return jsonify(Transactions=result_list)

        elif user_last_name:
            transaction_list = dao.getTransactionByUserLastName(user_last_name)
            result_list = []
            for row in transaction_list:
                result = self.build_transactioninfo_dict(row)
                result_list.append(result)
                return jsonify(Transactions=result_list)

        elif collectioncenterid:
            transaction_list = dao.getTransactionByCenter(collectioncenterid)
            result_list = []
            for row in transaction_list:
                result = self.build_transactioninfo_dict(row)
                result_list.append(result)
                return jsonify(Transactions=result_list)

        elif buy_free:
            transaction_list = dao.getTransactionByBF(buy_free)
            result_list = []
            for row in transaction_list:
                result = self.build_transactioninfo_dict(row)
                result_list.append(result)
                return jsonify(Transactions=result_list)

        elif market_price:
            transaction_list = dao.getTransactionByMarketPrice(market_price)
            result_list = []
            for row in transaction_list:
                result = self.build_transactioninfo_dict(row)
                result_list.append(result)
                return jsonify(Transactions=result_list)

        elif user_email:
            transaction_list = dao.getTransactionByEmail(user_email)
            result_list = []
            for row in transaction_list:
                result = self.build_transactioninfo_dict(row)
                result_list.append(result)
                return jsonify(Transactions=result_list)
        else:
            return jsonify(Error="Malformed query string"), 400









