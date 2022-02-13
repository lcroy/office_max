import sqlite3
from sqlite3 import Error
from configure import Config
import datetime
from configure import Config

#=================================================================
# Public functions for DB query
#=================================================================
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

#=================================================================
# Public functions for message table
# return: 0 - find recorder; 1 - successfully add recorder; 2 - update status; 3 - error
#=================================================================
def save_record_to_db(db_file, id, sender, receiver, record_file_path, operation):
    conn = create_connection(db_file)
    if conn != None:
        cur = conn.cursor()
        if (operation == 'add'):
            # search if the name is exist
            sql_serch_content = "SELECT * FROM message WHERE content='" + record_file_path + "'"
            cur.execute(sql_serch_content)
            rows = cur.fetchall()
            if (len(rows)>0):
                return "0"
            else:
                today = datetime.datetime.now().strftime('%y-%m-%d')
                sql_add_message = "INSERT INTO message(receiver, sender, content, read, add_date) VALUES('" + receiver + "','" + sender + "','" + record_file_path + "','" + "No" + "','" + today + "')"
                print(sql_add_message)
                # try:
                cur.execute(sql_add_message)
                conn.commit()
                return "1"
                # except:
                #     return "3"
        elif (operation == 'check'):
            # search unread messages
            sql_serch_content = "SELECT receiver, COUNT(id) FROM message GROUP BY receiver, read HAVING read='No'"
            cur.execute(sql_serch_content)
            rows = cur.fetchall()
            if (len(rows) > 0):
                return rows
            else:
                return "null"
        elif (operation == 'update'):
            # if the message is read then the status should be updated
            sql_update = "UPDATE message SET read ='Yes' WHERE id=" + str(id)
            try:
                cur.execute(sql_update)
                conn.commit()
                return "2"
            except:
                return "3"
    else:
        return "3"


#=================================================================
# Public functions for message status table
# return: 0 - read successfully; 2 - update successfully; 3 - error
#=================================================================
def status(db_file, operation, new_status, reader):
    conn = create_connection(db_file)
    if conn != None:
        cur = conn.cursor()
        if (operation == 'check'):
            # read status
            sql_serch_content = "SELECT curstatus,user FROM msgstatus"
            try:
                cur.execute(sql_serch_content)
                rows = cur.fetchall()
                if (len(rows)>0):
                    return rows
            except:
                return "3"
        elif (operation == 'update'):
            sql_update = "UPDATE msgstatus SET curstatus ='" + new_status + "', user = '" + reader + "'"
            try:
                cur.execute(sql_update)
                conn.commit()
                return "2"
            except:
                return "3"
    else:
        return "3"


#=================================================================
# Public functions for user authentication table
# return: 0 - read successfully; 1 - no such user; 3 - error
#=================================================================
def auth(db_file, username, password):
    conn = create_connection(db_file)
    if conn != None:
        cur = conn.cursor()
        sql_serch_content = "SELECT * FROM user WHERE username='" + username + "' AND password='" + password + "'"
        print(sql_serch_content)
        try:
            cur.execute(sql_serch_content)
            rows = cur.fetchall()
            if (len(rows) > 0):
                return "0"
            else:
                return "1"
        except:
            return "3"

# cfg = Config()
# result = auth(cfg.dataset_path_db,'Chen', 'clock')


#=================================================================
# Public functions for message table
# return: 0 - find recorder; 1 - successfully read; 2 - update status; 3 - error
#=================================================================
def read_record_from_db(db_file, receiver):
    conn = create_connection(db_file)
    if conn != None:
        cur = conn.cursor()
        sql_serch_content = "SELECT id, sender, content FROM message WHERE receiver='" + receiver + "' AND read = '" + "No'"
        try:
            cur.execute(sql_serch_content)
            rows = cur.fetchall()
            return rows
        except:
            return "3"
    else:
        return "3"

#=================================================================
# Public functions for message table
# return: 0 - successfully updated; 1 - update error ; 3 - connection error
#=================================================================
def update_record(db_file, id):
    conn = create_connection(db_file)
    if conn != None:
        cur = conn.cursor()
        sql_update = "UPDATE message SET read ='Yes' WHERE id=" + str(id)
        try:
            cur.execute(sql_update)
            conn.commit()
            return "0"
        except:
            return "3"
    else:
        return "3"



#=================================================================
# Public functions for display max reply
# return: 0 - read successfully; 2 - update successfully; 3 - error
#=================================================================
def res_max(db_file, operation, replyframax):
    conn = create_connection(db_file)
    if conn != None:
        cur = conn.cursor()
        if (operation == 'read'):
            # read status
            sql_serch_content = "SELECT replyframax FROM maxres"
            try:
                cur.execute(sql_serch_content)
                rows = cur.fetchall()
                if (len(rows)>0):
                    return rows
            except:
                return "3"
        elif (operation == 'write'):
            sql_update = "UPDATE maxres SET replyframax ='" + replyframax + "'"
            try:
                cur.execute(sql_update)
                conn.commit()
                return "2"
            except:
                return "3"
    else:
        return "3"