import sys
import sqlite3
import os.path
# 1 - help
# 2 - create
# 3 - list
# 4 - add
# 5 - update
# 6 - del

command = sys.argv[1:]


def hlp(com):
    helps = {
        'help' : "Commands:\n- help -\n- create -\n- list -\n- add -\n- update -\n- del -\n- section -\n- schedule -\n- cadet -",
        'section' : "Section module commands:\n- help -\n- list -\n- add -\n -update\n- del -",
        'schedule': "Schedule module commands:\n- help -\n- list -\n- add -\n -update\n- del -",
        'cadet': "Cadet module commands:\n- help -\n- list -\n- add -\n -update\n- del -",
    }
    print(helps.get(com[0], "Unknown command"))

def hlp_2(com):
    helps = {
        ("section", 'list') : "Section list command has no parameters",
        ("section", 'add') : "Section add command parameters:\n-n: section id",
        ('section', 'update') : "Section update command parameters:\n-n: section id\n-i: new value",
        ('section', 'del') : "Section del command parameters:\n-n: section id",
        #
        ("schedule", 'list') : "Section add command parameters:\n-n: section id",
        ("schedule", 'add') : "Schedule list command parameters:\n-d : day\n-n : number section\n-l : list of classes",
        ("schedule", 'update') : "Schedule update command parameters:\n-i : id schedule\n-d : new day\n-n : new number section\n-l : new list of classes",
        ("schedule", 'del') : 'Schedule del command parameters:\n-i : id schedule',
        #
        ('cadet', 'list') : "Cadet list command parameters:\n-i : Id\n-l : last name\n-s : section Id\n-r : rank\n",
        ('cadet', 'add') : "Cadet add command parameters:\n-f : first name\n-m : middle name\n-l : last name\n-r : rank\n-s : section Id",
        ('cadet', 'update') : "Cadet update command parameters:\n-i : id cadet\n-f : new first name\n-m : new middle name\n-l : new last name\n-r : new rank\n-s : new section Id",
        ('cadet', 'del') : "Cadet del command parameters:\n-i : id cadet"
    }
    print(helps.get((com[0], com[1]), 'Unknown command!'))

def crt():
    if not os.path.isfile("data.db"):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        # section ID Number
        # schedule ID Day NumberId ListClass
        # cadets ID FirstName MiddleName LastName Rank SectionId
        cur.execute("CREATE TABLE section (id INTEGER PRIMARY KEY AUTOINCREMENT, number STRING)")
        cur.execute("CREATE TABLE schedule (id INTEGER PRIMARY KEY AUTOINCREMENT, day STRING, number STRING, list STRING)")
        cur.execute("CREATE TABLE cadets (id INTEGER PRIMARY KEY AUTOINCREMENT, first STRING, middle STRING, last STRING,"
                "rank STRING, section STRING)")
        print("Successfully")
    else:
        print("The .db file already exists")

def sctn(com):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    if com[1] == "list":
        pass
    elif com[1] == "add":
        if com[2] == "-n":
            cur.execute("INSERT INTO section (number) VALUES (?)", (str(com[3]),))
            conn.commit()
            print('OK')
        else:
            print("Error")
    elif com[1] == "update":
        pass
    elif com[1] == "del":
        pass
    else:
        print("Unknown command!")

def schd(com):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    if com[1] == "list":
        pass
    elif com[1] == "add":
        grp = {
            ('-d', '-n', '-l'): cur.execute(
                'INSERT INTO schedule (day, number, list) VALUES (?,?,?)', (com[3], com[5], com[7]))
        }
        grp.get((com[2], com[4], com[6]), 'Error')
        conn.commit()
        print('Ok schd')
    elif com[1] == "update":
        pass
    elif com[1] == "del":
        pass
    else:
        print("Unknown command!")


def cdt(com):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    if com[1] == "list":
        pass
    elif com[1] == "add":
        pass

    elif com[1] == "update":
        pass
    elif com[1] == "del":
        pass
    else:
        print("Unknown command!")

#
def main(com):
    if "help" in com:
        if len(com) <= 2:
            hlp(com)
        else:
            hlp_2(com)
    elif com[0] == "create":
        crt()
    elif com[0] == "section":
        if os.path.isfile("data.db"):
            sctn(com)
        else:
            print("Not find file.db")
    elif com[0] == "schedule":
        if os.path.isfile("data.db"):
            schd(com)
        else:
            print("Not find file.db")
    elif com[0] == "cadet":
        if os.path.isfile("data.db"):
            cdt(com)
        else:
            print("Not find file.db")
    else:
        print("Unknown command!")

main(command)