import sqlite3


def connect():
    conn = sqlite3.connect("tags.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS valves (id INTEGER PRIMARY KEY, tag text, pid text, line_equip text,"
                " station text, valve_type text)")
    conn.commit()
    conn.close()


def insert(tag, pid, line_equip, station, valve_type):
    conn = sqlite3.connect("tags.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO valves VALUES (NULL,?,?,?,?,?)", (tag, pid, line_equip, station, valve_type))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("tags.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM valves")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(tag="", pid="", line_equip="", station="", valve_type=""):
    conn = sqlite3.connect("tags.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM valves WHERE tag=? OR pid=? OR line_equip=? OR station=? OR valve_type=?", (tag, pid,
                                                                                                           line_equip,
                                                                                                           station,
                                                                                                           valve_type))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("tags.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM valves WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, tag, pid, line_equip, station, valve_type):
    conn = sqlite3.connect("tags.db")
    cur = conn.cursor()
    cur.execute("UPDATE valves SET tag=?, pid=?, line_equip=?, station=?, valve_type=? WHERE id=?", (tag, pid,
                                                                                                     line_equip,
                                                                                                     station,
                                                                                                     valve_type, id))
    conn.commit()
    conn.close()


connect()

