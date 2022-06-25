import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def iud(q, val):
    con = pymysql.connect(host=os.getenv('HOST'), port=int(os.getenv('PORT')), user=os.getenv('USER'), passwd=os.getenv('PASSWD'), db=os.getenv('DB'))
    cmd = con.cursor()
    cmd.execute(q, val)
    id = cmd.lastrowid
    con.commit()
    return id


def select(q):
    con = pymysql.connect(host=os.getenv('HOST'), port=int(os.getenv('PORT')), user=os.getenv('USER'), passwd=os.getenv('PASSWD'), db=os.getenv('DB'))
    cmd = con.cursor()
    cmd.execute(q)
    s = cmd.fetchall()
    return s


def selectall(q, val):
    con = pymysql.connect(host=os.getenv('HOST'), port=int(os.getenv('PORT')), user=os.getenv('USER'), passwd=os.getenv('PASSWD'), db=os.getenv('DB'))
    cmd = con.cursor()
    cmd.execute(q, val)
    s = cmd.fetchall()
    return s


def selectone(q, val):
    con = pymysql.connect(host=os.getenv('HOST'), port=int(os.getenv('PORT')), user=os.getenv('USER'), passwd=os.getenv('PASSWD'), db=os.getenv('DB'))
    cmd = con.cursor()
    cmd.execute(q, val)
    s = cmd.fetchone()
    return s
