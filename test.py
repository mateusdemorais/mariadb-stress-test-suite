#!/usr/bin/python

import mysql.connector as mariadb
from faker import Faker
import datetime, hashlib, logging, progressbar, sys,time


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
fake = Faker()

# To use this test suite, you need to provide the correct
# configuration to access a MariaDB database
MARIADB_CONFIG = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'port': '3306',
    'database': 'sbd2'
}

USER_INSERT_ROW_1 = ("INSERT INTO USER_ROW_1 "
            "(username, password, name, email, sex, birthday, address, job, blood_group) "
            "VALUES (%(username)s, %(password)s, %(name)s, %(email)s, %(sex)s, %(birthday)s, %(address)s, %(job)s, %(blood_group)s)")
USER_INSERT_COLUMN_1 = ("INSERT INTO USER_COLUMN_1 "
            "(username, password, name, email, sex, birthday, address, job, blood_group) "
            "VALUES (%(username)s, %(password)s, %(name)s, %(email)s, %(sex)s, %(birthday)s, %(address)s, %(job)s, %(blood_group)s)")
RANDOM_INSERT_ROW_1 = ("INSERT INTO RANDOM_ROW_1 "
            "(field01, field02, field03, field04, field05, field06, field07, field08, field09, field10, field11, field12, field13, field14, field15, field16, field17, field18, field19, field20, field21, field22, field23, field24, field25, field26, field27, field28, field29, field30, field31, field32, field33, field34, field35, field36, field37, field38, field39, field40, field41, field42, field43, field44, field45, field46, field47, field48, field49, field50) "
            "VALUES (%(field01)s, %(field02)s, %(field03)s, %(field04)s, %(field05)s, %(field06)s, %(field07)s, %(field08)s, %(field09)s, %(field10)s, %(field11)s, %(field12)s, %(field13)s, %(field14)s, %(field15)s, %(field16)s, %(field17)s, %(field18)s, %(field19)s, %(field20)s, %(field21)s, %(field22)s, %(field23)s, %(field24)s, %(field25)s, %(field26)s, %(field27)s, %(field28)s, %(field29)s, %(field30)s, %(field31)s, %(field32)s, %(field33)s, %(field34)s, %(field35)s, %(field36)s, %(field37)s, %(field38)s, %(field39)s, %(field40)s, %(field41)s, %(field42)s, %(field43)s, %(field44)s, %(field45)s, %(field46)s, %(field47)s, %(field48)s, %(field49)s, %(field50)s)")
RANDOM_INSERT_COLUMN_1 = ("INSERT INTO RANDOM_COLUMN_1 "
            "(field01, field02, field03, field04, field05, field06, field07, field08, field09, field10, field11, field12, field13, field14, field15, field16, field17, field18, field19, field20, field21, field22, field23, field24, field25, field26, field27, field28, field29, field30, field31, field32, field33, field34, field35, field36, field37, field38, field39, field40, field41, field42, field43, field44, field45, field46, field47, field48, field49, field50) "
            "VALUES (%(field01)s, %(field02)s, %(field03)s, %(field04)s, %(field05)s, %(field06)s, %(field07)s, %(field08)s, %(field09)s, %(field10)s, %(field11)s, %(field12)s, %(field13)s, %(field14)s, %(field15)s, %(field16)s, %(field17)s, %(field18)s, %(field19)s, %(field20)s, %(field21)s, %(field22)s, %(field23)s, %(field24)s, %(field25)s, %(field26)s, %(field27)s, %(field28)s, %(field29)s, %(field30)s, %(field31)s, %(field32)s, %(field33)s, %(field34)s, %(field35)s, %(field36)s, %(field37)s, %(field38)s, %(field39)s, %(field40)s, %(field41)s, %(field42)s, %(field43)s, %(field44)s, %(field45)s, %(field46)s, %(field47)s, %(field48)s, %(field49)s, %(field50)s)")
USER_SELECT_ROW_1 = ("SELECT name FROM USER_ROW_1 "
            "WHERE birthday BETWEEN %s AND %s")
USER_SELECT_COLUMN_1 = ("SELECT name FROM USER_COLUMN_1 "
            "WHERE birthday BETWEEN %s AND %s")
USER_UPDATE_ROW_1 = ("UPDATE USER_ROW_1 SET sex = %s "
            "WHERE sex = %s")
USER_UPDATE_COLUMN_1 = ("UPDATE USER_COLUMN_1 SET sex = %s "
            "WHERE sex = %s")


class TestSuite():

    def __init__(self):
        self.mariadb_config = MARIADB_CONFIG
        self.mariadb_connection = None
        self.mariadb_cursor = None
        self.table_orientation = sys.argv[1]
        self.test_type = sys.argv[2]
        self.test_iterations = int(sys.argv[3])

    def connect_to_database(self):
        try:
            self.mariadb_connection = mariadb.connect(**self.mariadb_config)
            self.mariadb_cursor = self.mariadb_connection.cursor()
            logger.info('Database connection successful.')
        except Exception as error:
            logging.error('Database connection failed: %s', error)
            sys.exit('Execution stopped!')

    def close_connection_to_database(self):
        try:
            self.mariadb_cursor.close()
            self.mariadb_connection.close()
            logger.info('Database disconnected successful.')
        except Exception as error:
            logging.error('Database disconnect failed: %s', error)
            sys.exit('Execution stopped!')

    def insert_test(self):
        iterations=self.test_iterations

        logger.info('Insert test on %s-oriented table with %s iterations started!',
                    self.table_orientation.upper(),
                    self.test_iterations)
        start_time = time.time()
        bar = progressbar.ProgressBar()
        for i in bar(range(iterations)):
            user_profile = fake.profile()
            password = user_profile['name'].replace(" ", "").lower()
            hash_object = hashlib.sha256(password.encode())
            password_hash = hash_object.hexdigest()
            user_data = {
                'username': user_profile['username'],
                'password': password_hash,
                'name': user_profile['name'],
                'email': user_profile['mail'],
                'sex': user_profile['sex'],
                'birthday': user_profile['birthdate'],
                'address': user_profile['address'],
                'job': user_profile['job'],
                'blood_group': user_profile['blood_group']
            }
            try:
                if self.table_orientation == 'row':
                    self.mariadb_cursor.execute(USER_INSERT_ROW_1, user_data)
                elif self.table_orientation == 'column':
                    self.mariadb_cursor.execute(USER_INSERT_COLUMN_1, user_data)
            except:
                logging.error('Insert test failed.')
                self.close_connection_to_database()
                sys.exit('Execution stopped!')
            self.mariadb_connection.commit()
            # logger.info('User inserted successful.')

        finish_time = time.time()
        total_time = finish_time-start_time
        logger.info('Insert test took: %.2f seconds.', total_time)

    def insert_test_long_table(self):
        iterations=self.test_iterations

        logger.info('Insert test on long %s-oriented table with %s iterations started!',
                    self.table_orientation.upper(),
                    self.test_iterations)
        start_time = time.time()
        bar = progressbar.ProgressBar()
        for i in bar(range(iterations)):
            random_data = {
                'field01': fake.address(),
                'field02': fake.address(),
                'field03': fake.address(),
                'field04': fake.address(),
                'field05': fake.address(),
                'field06': fake.address(),
                'field07': fake.address(),
                'field08': fake.address(),
                'field09': fake.address(),
                'field10': fake.address(),
                'field11': fake.address(),
                'field12': fake.address(),
                'field13': fake.address(),
                'field14': fake.address(),
                'field15': fake.address(),
                'field16': fake.address(),
                'field17': fake.address(),
                'field18': fake.address(),
                'field19': fake.address(),
                'field20': fake.address(),
                'field21': fake.address(),
                'field22': fake.address(),
                'field23': fake.address(),
                'field24': fake.address(),
                'field25': fake.address(),
                'field26': fake.address(),
                'field27': fake.address(),
                'field28': fake.address(),
                'field29': fake.address(),
                'field30': fake.address(),
                'field31': fake.address(),
                'field32': fake.address(),
                'field33': fake.address(),
                'field34': fake.address(),
                'field35': fake.address(),
                'field36': fake.address(),
                'field37': fake.address(),
                'field38': fake.address(),
                'field39': fake.address(),
                'field40': fake.address(),
                'field41': fake.address(),
                'field42': fake.address(),
                'field43': fake.address(),
                'field44': fake.address(),
                'field45': fake.address(),
                'field46': fake.address(),
                'field47': fake.address(),
                'field48': fake.address(),
                'field49': fake.address(),
                'field50': fake.address()
            }
            try:
                if self.table_orientation == 'row':
                    self.mariadb_cursor.execute(RANDOM_INSERT_ROW_1, random_data)
                elif self.table_orientation == 'column':
                    self.mariadb_cursor.execute(RANDOM_INSERT_COLUMN_1, random_data)
            except:
                logging.error('Insert test failed.')
                self.close_connection_to_database()
                sys.exit('Execution stopped!')
            self.mariadb_connection.commit()
            # logger.info('User inserted successful.')

        finish_time = time.time()
        total_time = finish_time-start_time
        logger.info('Insert test took: %.2f seconds.', total_time)

    def select_test(self):
        iterations=self.test_iterations

        logger.info('Select test on %s-oriented table with %s iterations started!',
                    self.table_orientation.upper(),
                    self.test_iterations)
        start_date = datetime.date(1990, 1, 1)
        end_date = datetime.date(2000, 1, 1)
        start_time = time.time()
        bar = progressbar.ProgressBar()
        for i in bar(range(iterations)):
            try:
                if self.table_orientation == 'row':
                    self.mariadb_cursor.execute(USER_SELECT_ROW_1, (start_date, end_date))
                elif self.table_orientation == 'column':
                    self.mariadb_cursor.execute(USER_SELECT_COLUMN_1, (start_date, end_date))
            except:
                logging.error('Select test failed.')
                self.close_connection_to_database()
                sys.exit('Execution stopped!')
            for (name) in self.mariadb_cursor:
                pass

        finish_time = time.time()
        total_time = finish_time-start_time
        logger.info('Select test took: %.2f seconds.', total_time)

    def update_test(self):
        iterations=self.test_iterations
        if iterations % 2 != 0:
            iterations = iterations + 1

        logger.info('Update test on %s-oriented table with %s iterations started!',
                    self.table_orientation.upper(),
                    self.test_iterations)
        odd_iteration = True
        start_time = time.time()
        bar = progressbar.ProgressBar()
        for i in bar(range(iterations)):
            if odd_iteration:
                new_sex = 'A'
                actual_sex = 'M'
                odd_iteration = False
            else:
                new_sex = 'M'
                actual_sex = 'A'
                odd_iteration = True
            try:
                if self.table_orientation == 'row':
                    self.mariadb_cursor.execute(USER_UPDATE_ROW_1, (new_sex, actual_sex))
                elif self.table_orientation == 'column':
                    self.mariadb_cursor.execute(USER_UPDATE_COLUMN_1, (new_sex, actual_sex))
            except Exception as error:
                logging.error('Update test failed: %s.', error)
                self.close_connection_to_database()
                sys.exit('Execution stopped!')
            self.mariadb_connection.commit()

        finish_time = time.time()
        total_time = finish_time-start_time
        logger.info('Select test took: %.2f seconds.', total_time)

def help():
    print('MariaDB Stress Test Suite (v1.0.0)\n')
    print('Usage: python test.py <table orientation> <test type> <iterations>\n')
    print('Example: python test.py row insert 100')
    print('It will run 100 iterations of the insert test in a row table.\n')
    print('Available table orientations:')
    print('row | column\n')
    print('Available test types:')
    print('insert | long_insert | select | update\n')
    print('Number of iterations:')
    print('[1, 1000000]')

def main():
    if len(sys.argv) == 4:
        if not sys.argv[1] == 'row' and not sys.argv[1] == 'column':
            logging.error('Unkown table orientation.')
            logging.info('Available options: row | column')
            sys.exit('Execution stopped!')
        try:
            if int(sys.argv[3]) < 1 or int(sys.argv[3]) > 1000000:
                logging.error('Number of iterations should be between 0 and 1000001.')
                sys.exit('Execution stopped!')
        except ValueError as error:
            logging.error('Number of iterations should be a number: %s', error)
            sys.exit('Execution stopped!')
        tester = TestSuite()
        tester.connect_to_database()
        if tester.test_type == 'insert':
            tester.insert_test()
        elif tester.test_type == 'long_insert':
            tester.insert_test_long_table()
        elif tester.test_type == 'select':
            tester.select_test()
        elif tester.test_type == 'update':
            tester.update_test()
        else:
            logging.error('Unknown test type.')
            tester.close_connection_to_database()
            logging.info('Available options: insert | long_insert | select | update')
            sys.exit('Execution stopped!')
        tester.close_connection_to_database()
    else:
        help()

if __name__ == '__main__':
    main()
