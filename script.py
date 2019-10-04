import MySQLdb

def mysqlDBConnection(self):

        try:
            #mysql db connection
            con = MySQLdb.connect(host=mysqlHost,user=mysqlUser,passwd=mysqlPwd,db=mysqlDB)
            logging.info('MYSQL DB connection is successfull')
            return con

        except Exception as error:
            logging.error('MYSQL DB connection failed '+str(error))
