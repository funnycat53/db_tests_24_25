import sqlite3


conn = sqlite3.connect("dati.db", check_same_thread=False)

def skolenu_tabulas_izveide():
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE skoleni(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL
        )
        """
    )
    conn.commit()

# tabulas_izveide()

def pievienot_skolenu(vards, uzvards):
    print(vards, uzvards)
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO skoleni(vards, uzvards) VALUES("{vards}","{uzvards}")
        """
    )
    conn.commit()

def skolotaju_tabulas_izveide():
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE skolotaji(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL
        )
        """
    )
    conn.commit()

def pievienot_skolotaju(vards, uzvards):
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO skolotaji(vards, uzvards) VALUES("{vards}","{uzvards}")
        """
    )
    conn.commit()

    print(vards, uzvards)

def pievienot_prieksmetu(prieksmets):
    print(prieksmets)

def iegut_skolenus():
    cur = conn.cursor()
    cur.execute(
        """SELECT vards, uzvards FROM skoleni"""
    )
    conn.commit()
    dati = cur.fetchall()
    return dati

def iegut_skolotajus():
    cur = conn.cursor()
    cur.execute(
        """SELECT vards, uzvards, id FROM skolotaji"""
    )
    conn.commit()
    dati = cur.fetchall()
    return dati


