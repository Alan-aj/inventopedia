import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
# def iud(q,val):
#      con=pymysql.connect(host='InventionandInventors.mysql.pythonanywhere-services.com',user='InventionandInve',passwd='Aswin123@#',db='InventionandInve$invention_and_inventors')
#      cmd=con.cursor()
#      cmd.execute(q,val)
#      id=cmd.lastrowid
#      con.commit()
#      return id
# def select(q):
#     con=pymysql.connect(host='InventionandInventors.mysql.pythonanywhere-services.com',user='InventionandInve',passwd='Aswin123@#',db='InventionandInve$invention_and_inventors')
#     cmd=con.cursor()
#     cmd.execute(q)
#     s=cmd.fetchall()
#     return s
# def selectall(q,val):
#     con=pymysql.connect(host='InventionandInventors.mysql.pythonanywhere-services.com',user='InventionandInve',passwd='Aswin123@#',db='InventionandInve$invention_and_inventors')
#     cmd=con.cursor()
#     cmd.execute(q,val)
#     s=cmd.fetchall()
#     return s
# def selectone(q,val):
#     con=pymysql.connect(host='InventionandInventors.mysql.pythonanywhere-services.com',user='InventionandInve',passwd='Aswin123@#',db='InventionandInve$invention_and_inventors')
#     cmd=con.cursor()
#     cmd.execute(q,val)
#     s=cmd.fetchone()
#     return s


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
