import os
import sqlite3

import _config as cf

def audiofiles_insert(url, desc):

    conn = sqlite3.connect(cf.dbname)
    cursor = conn.cursor()

    insert_stmt = "INSERT INTO audiofiles (AudioUrl, AudioText) VALUES ('%s','%s')" % (url.replace("'", "''"), desc.replace("'", "''"))

    conn.execute(insert_stmt)

    conn.commit()
    conn.close()

def audiofiles_select(where_clause):

    conn = sqlite3.connect(cf.dbname)
    cursor = conn.cursor()

    insert_stmt = "SELECT * FROM audiofiles WHERE %s" % (where_clause)

    cursor.execute(insert_stmt)
    results = cursor.fetchall()

    conn.close()

    return results

def audiofiles_delete(key, value):

    conn = sqlite3.connect(cf.dbname)
    cursor = conn.cursor()

    delete_stmt = "SELECT * FROM audiofiles WHERE %s = %s)" % (key, value)

    conn.execute(delete_stmt)

    conn.commit()
    conn.close()
