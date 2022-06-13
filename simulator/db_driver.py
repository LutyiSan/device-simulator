import pymysql
import pymysql.cursors
from loguru import logger
from env import DB


class DBDriver:
    def __init__(self):
        logger.add("logs/db.log", format="{time:DD-MM-YYYY at HH:mm:ss} | {level} | {message}", rotation="2MB")
        self.cursor = None
        self.connector = None

    def connect(self):
        try:
            self.connector = pymysql.connect(host=DB['HOST'], port=DB['PORT'], user=DB['USERNAME'],
                                             password=DB['PASSWD'], database=DB['DBNAME'],
                                             cursorclass=pymysql.cursors.DictCursor, autocommit=True)
            self.cursor = self.connector.cursor()
            logger.info('READY Connect to data base')
            return True
        except Exception as e:
            logger.exception('FAIL Connect to data base', e)
        return False

    def db_get(self, query):
        result = None
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
        except Exception as e:
            logger.exception(f'FAIL SELECT QUERY: {query}', e)
        return result

    def db_update(self, query):
        try:
            self.cursor.execute(query)
            logger.debug("UPDATE is DONE")
            return True
        except Exception as e:
            logger.exception(f'FAIL UPDATE QUERY: {query}', e)
            return False

    def disconnect(self):
        try:
            self.cursor.close()
            logger.info('Connection to DB closed')
        except Exception as e:
            logger.exception('FAIL close connection to DB', e)
#sc = DBDriver()
#sc.connect()
#query = f"UPDATE `vbas`.`objects` SET `value`='779.01' WHERE `device_id`=30007 AND `Object_Name`='Site:TECH_UCHYOT/heat-water.volume';"
#sc.db_update(query)
#sc.disconnect()
