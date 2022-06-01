import os
from flask import *
from werkzeug.utils import secure_filename

from dbconnector import *
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)
app.secret_key=os.getenv('SECRET_KEY')
import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail









mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'inventionandinventor@gmail.com'
app.config['MAIL_PASSWORD'] = 'invention123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route("/")
def main():
    return render_template("dashboard.html")



import functools
def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return redirect ("/")
        return func()
    return secure_function

@app.route('/logout')
def logout():
    session.clear()
    return render_template("dashboard.html")


@app.route("/indexlogin")
def indexlogin():
    return render_template("login.html")

@app.route("/reg")

def reg():
    return render_template("register.html")

@app.route("/reg1")

def reg1():
    return render_template("register1.html")


@app.route("/login")
def login():
    return render_template("admin/Login.html")



#
# @app.route("/logout")
# def logout():
#     return render_template("admin/Login.html")








@app.route("/newlogin",methods=['post'])

def newlogin():
    uname=request.form['name']
    passw=request.form['pswd']
    qry="select * from login where Username=%s and Password=%s"
    val=(uname,passw)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("invalid"); window.location="/"</script>'''
    elif res[3]=="admin":
        session['lid']=res[0]
        return '''<script>alert("Welcome Admin"); window.location="adminhom"</script>'''
    elif res[3] == "user":
        session['lid']=res[0]
        print(session['lid'])

        return '''<script>alert("Welcome user"); window.location="userhome"</script>'''
    elif res[3]=="inventor":
        session['lid']=res[0]
        return '''<script>alert("Welcome inventor"); window.location="/inventorhome"</script>'''


    else :
        return '''alert("ivalid"); window.location="/"</script>'''






@app.route("/adminhom")
@login_required
def adminhom():
    return render_template("admin/Adminhome.html")


@app.route("/addinfo")
@login_required
def addinfo():
    return render_template("admin/Add info.html")

@app.route("/infoadd",methods=['post'])
@login_required
def infoadd():
     yer=request.form['year']
     ivntn=request.form['inv']
     iname=request.form['inventor']
     dscpn=request.form['description']
     image=request.files['file']
     file=secure_filename(image.filename)
     print(file)
     image.save(os.path.join("static/image/",file))
     vdolnk=request.form['video']
     qry="insert into information values(null,%s,%s,%s,%s,%s,%s,%s,'approved')"
     val=(yer,ivntn,iname,dscpn,file,vdolnk,str(session['lid']))
     iud(qry,val)
     return'''<script>alert("information added");window.location="/manageinfo"</script>'''




@app.route("/addquiz")
@login_required
def addquiz():


    return render_template("admin/Add quiz.html")



@app.route("/addq",methods=['post'])
@login_required
def addq():
    qstn = request.form['question']
    ans = request.form['answer']
    opt1=request.form['op1']
    opt2=request.form['op2']
    opt3=request.form['op3']
    opt4=request.form['op4']
    qry = "insert into quiz values(null,%s,%s,%s,%s,%s,%s)"
    val = (qstn,opt1,opt2,opt3,opt4,ans)
    iud(qry, val)
    return '''<script>alert("quiz added");window.location="/viewquiz"</script>'''



# admin change password


@app.route("/Changepassword")
@login_required
def Changepassword():
    return render_template("admin/Change password.html")


@app.route("/chpsw",methods=['post'])
@login_required
def chpsw():
    id=session['lid']
    opsw=request.form['oldpsw']
    npsw=request.form['newpsw']
    cpsw=request.form['conpsw']
    qry="SELECT * FROM login WHERE `Login_id`=%s AND `Password`=%s"
    val=(id,opsw)
    var=selectone(qry,val)
    if var is None:
        return'''<script>alert("password no match");window.location="/Changepassword"</script>'''

    else:
        if npsw==cpsw:
            qry1="update login set Password=%s where Login_id=%s"
            val1=(cpsw,str(id))
            iud(qry1,val1)





            return'''<script>alert("password changed");window.location="/"</script>'''
        else:
            return'''<script>alert("check password");window.location="/Changepassword"</script>'''


# user change password

@app.route("/userChangepassword")
@login_required
def userChangepassword():
    return render_template("user/userpasswordch.html")

@app.route("/uchpsw",methods=['post'])
@login_required
def uchpsw():
    id=session['lid']
    opsw=request.form['oldpsw']
    npsw=request.form['newpsw']
    cpsw=request.form['conpsw']
    qry="SELECT * FROM login WHERE `Login_id`=%s AND `Password`=%s"
    val=(id,opsw)
    var=selectone(qry,val)
    if var is None:
        return'''<script>alert("password no match");window.location="/userChangepassword"</script>'''

    else:
        if npsw==cpsw:
            qry1="update login set Password=%s where Login_id=%s"
            val1=(cpsw,str(id))
            iud(qry1,val1)





            return'''<script>alert("password changed");window.location="/"</script>'''
        else:
            return'''<script>alert("check password");window.location="/userChangepassword"</script>'''


# inventor change password

@app.route("/InvChangepassword")
@login_required
def InvChangepassword():
    return render_template("Inventor/invchangepwd.html")

@app.route("/inchpsw",methods=['post'])
@login_required
def inchpsw():
    id=session['lid']
    opsw=request.form['oldpsw']
    npsw=request.form['newpsw']
    cpsw=request.form['conpsw']
    qry="SELECT * FROM login WHERE `Login_id`=%s AND `Password`=%s"
    val=(id,opsw)
    var=selectone(qry,val)
    if var is None:
        return'''<script>alert("password no match");window.location="/InvChangepassword"</script>'''

    else:
        if npsw==cpsw:
            qry1="update login set Password=%s where Login_id=%s"
            val1=(cpsw,str(id))
            iud(qry1,val1)





            return'''<script>alert("password changed");window.location="/"</script>'''
        else:
            return'''<script>alert("check password");window.location="/InvChangepassword"</script>'''






@app.route("/commentrelpy",methods=['get'])
@login_required
def commentreply():
    id=request.args.get('id')
    session['cid']=id

    return render_template("admin/Comment reply.html")




@app.route("/addcommk",methods=['post'])
@login_required
def addcommk():
    res=str(session['cid'])
    rply=request.form['reply']
    qry="update comment set Reply=%s where Comment_Id=%s"
    val=(rply,res)
    iud(qry,val)
    return '''<script>alert("replied");window.location="/verifycomment"</script>'''




@app.route("/manageinfo")
@login_required
def manageinfo():
    qry="select * from information"
    val=str(session['lid'])
    res=select(qry)

    return render_template("admin/Manage info.html",val=res)

@app.route("/verifycomment")
@login_required
def verifycomment():
    qry="SELECT `user`.`First_Name`,`Last_Name`,`Emai_id` ,`comment`.* FROM `comment` JOIN `user` ON `user`.`login_id`=`comment`.`User_id` WHERE `comment`.`Reply`='pending'"
    res=select(qry)

    return render_template("admin/Verify comment.html",val=res)

@app.route("/verifyuserinfo")
@login_required
def verifyuserinfo():
    qry="select * from information where Login_id!=1 and status='pending'"
    res=select(qry)


    return render_template("admin/Verify user info.html",val=res)

@app.route("/verifycertificate")
@login_required
def verifycertificate():
    qry="select * from certificate where status='pending'"
    res=select(qry)
    return render_template("admin/Verifycertificate.html",val=res)


@app.route("/acceptcertificate")
@login_required
def acceptcertificate():
    id=request.args.get('id')
    qry="update certificate set status='approved' where Patent_id=%s"
    val=(id)
    iud(qry,val)

    return '''<script>alert("Patent Approved");window.location="/verifycertificate"</script>'''


@app.route("/rejectcertificate")
@login_required
def rejectcertificate():
    id = request.args.get('id')
    qry="update certificate set status='rejected' where Patent_id=%s"
    val=(id)
    iud(qry,val)
    return '''<script>alert("rejected");window.location="/verifycertificate"</script>'''





@app.route("/viewquiz")
@login_required
def viewquiz():
    qry="select * from quiz "
    res=select(qry)
    return render_template("admin/View Quiz.html",val=res)

@app.route("/delquiz")
@login_required
def delquiz():
    id = request.args.get('id')
    qry = "delete from quiz where Quiz_id=%s "
    val = (id)
    iud(qry, val)
    return '''<script>alert("deleted");window.location="/viewquiz"</script>'''


@app.route("/addcerti")
@login_required
def addcerti():
    return render_template("user/Addcertificate.html")

@app.route("/addcomm")
@login_required
def addcomm():
    return render_template("user/Addcomment.html")



@app.route("/commadd",methods=['post'])
@login_required
def commadd():
    res=str(session['lid'])
    comm=request.form['comm']
    qry="insert into comment values(null,%s,%s,'pending',curdate())"
    val=(res,comm)
    iud(qry,val)
    return '''<script>alert("commented");window.location="/viewcomm"</script>'''




@app.route("/userhome")
@login_required
def userhom():
    return render_template("user/Userhome.html")

@app.route("/ans")
@login_required
def ans():
    return render_template("user/Answer.html")
#
# @app.route("/answer")
# def answer():
#     an=request.form['answe']
#     qry
#     return


@app.route("/attendq")
@login_required
def attendq():
    qry="DELETE FROM `attend_quiz` WHERE `uid`=%s"
    val=(session['lid'])
    iud(qry,val)

    qry="SELECT * FROM `quiz` ORDER BY RAND()"
    res=select(qry)
    lis=[]
    for i in res:
        lis.append(str(i[0]))
    session['qlis']=','.join(lis)
    session['pos']=0
    res=res[0]

    return render_template("user/AttendQuiz.html",val=res)

@app.route("/nextt",methods=['post'])
@login_required
def nextt():
    btn=request.form['btn']
    if btn=='NEXT':
        ans=request.form['ans']
        opt=request.form['opt']
        mark="0"
        if ans==opt:
            mark="1"

        qus=session['qlis'].split(',')
        pos=int(session['pos'])

        qid=str(qus[pos])
        qry="INSERT INTO `attend_quiz` VALUES(NULL,%s,%s,%s,%s)"
        val=(qid,session['lid'],opt,mark)
        iud(qry,val)
        pos=pos+1
        session['pos']=pos
        if pos>=len(qus):
            qry="SELECT `quiz`.`Questions`,`attend_quiz`.`ans`,`quiz`.`Answer`,`mark` FROM `attend_quiz` JOIN `quiz` ON `quiz`.`Quiz_id`=`attend_quiz`.`qid` WHERE `attend_quiz`.`uid`=%s"
            val=(session['lid'])
            res=selectall(qry,val)
            qry="SELECT SUM(`mark`),COUNT(*) FROM `attend_quiz` WHERE `uid`=%s"
            mark=selectone(qry,val)
            marks=str(mark[0])+"/"+str(mark[1])
            per=(int(mark[0])/int(mark[1]))*100
            msg="Good"
            if per>90:
                msg="Exellent"
            elif per>50:
                msg="Good"
            else:
                msg="Average"
            return render_template("user/view_result.html",val=res,m=marks,msg=msg)
        else:

            qry = "SELECT * FROM `quiz` where Quiz_id=%s"
            val=(str(qus[pos]))
            res = selectone(qry,val)


            return render_template("user/AttendQuiz.html", val=res)

    else:
        ans = request.form['ans']
        opt = request.form['opt']
        mark = "0"
        if ans == opt:
            mark = "1"

        qus = session['qlis'].split(',')
        pos = int(session['pos'])

        qid = str(qus[pos])
        qry = "INSERT INTO `attend_quiz` VALUES(NULL,%s,%s,%s,%s)"
        val = (qid, session['lid'], opt, mark)
        iud(qry, val)
        pos = pos + 1
        session['pos'] = pos
        if pos >= len(qus):
            qry = "SELECT `quiz`.`Questions`,`attend_quiz`.`ans`,`quiz`.`Answer`,`mark`,solution FROM `attend_quiz` JOIN `quiz` ON `quiz`.`Quiz_id`=`attend_quiz`.`qid` WHERE `attend_quiz`.`uid`=%s"
            val = (session['lid'])
            res = selectall(qry, val)
            qry = "SELECT SUM(`mark`),COUNT(*) FROM `attend_quiz` WHERE `uid`=%s"
            mark = selectone(qry, val)
            marks = str(mark[0]) + "/" + str(mark[1])
            per = (int(mark[0]) / int(mark[1])) * 100
            msg = "Good"
            if per > 90:
                msg = "Exellent"
            elif per > 50:
                msg = "Good"
            else:
                msg = "Average"

        else:

            qry = "SELECT * FROM `quiz` where Quiz_id=%s"
            val = (str(qus[pos]))
            res = selectone(qry, val)




        qry = "SELECT `quiz`.`Questions`,`attend_quiz`.`ans`,`quiz`.`Answer`,`mark`,solution FROM `attend_quiz` JOIN `quiz` ON `quiz`.`Quiz_id`=`attend_quiz`.`qid` WHERE `attend_quiz`.`uid`=%s"
        val = (session['lid'])
        res = selectall(qry, val)
        qry = "SELECT SUM(`mark`),COUNT(*) FROM `attend_quiz` WHERE `uid`=%s"
        mark = selectone(qry, val)
        marks = str(mark[0]) + "/" + str(mark[1])
        per = (int(mark[0]) / int(mark[1])) * 100
        msg = "Good"
        if per > 90:
            msg = "Exellent"
        elif per > 50:
            msg = "Good"
        else:
            msg = "Average"
        return render_template("user/view_result.html", val=res, m=marks, msg=msg)

@app.route("/uploadin")
@login_required
def uploadin():
    return render_template("user/uploadinfo.html")

@app.route("/upinfo",methods=['post'])
@login_required
def upinfo():
     yer=request.form['year']
     invt=request.form['invt']
     iname=request.form['inventor']
     dscpn=request.form['description']
     image=request.files['fileField']
     file=secure_filename(image.filename)
     print(file)
     image.save(os.path.join("static/image/",file))
     vdolnk=request.form['video']
     qry="insert into information values(null,%s,%s,%s,%s,%s,%s,%s,'pending')"
     val=(yer,invt,iname,dscpn,file,vdolnk,str(session['lid']))
     iud(qry,val)
     return'''<script>alert("information added");window.location="/viewupl"</script>'''



#upload certificate
@app.route("/upcerti",methods=['post'])
@login_required
def upcerti():

     dscpn=request.form['descr']
     image=request.files['certi']
     file=secure_filename(image.filename)
     print(file)
     image.save(os.path.join("static/certificate/",file))
     qry="insert into certificate values(null,%s,%s,%s,'pending')"
     val=(str(session['lid']),dscpn,file)
     iud(qry,val)
     return'''<script>alert("certificate added");window.location="/viewcerti"</script>'''


@app.route('/delcerti',methods=['get'])
@login_required
def delcerti():
    id=request.args.get('id')
    qry="delete from certificate where Certificate_id=%s "
    val=(id)
    iud(qry,val)
    return '''<script>alert("certificate deleted");window.location="/viewcerti"</script>'''


@app.route("/usersign")

def usersign():
    return render_template("user/Usersignup.html")



@app.route("/usign",methods=['post'])

def usign():
    try:
        fname=request.form['finame']
        lname=request.form['lsname']
        uname=request.form['usname']
        dobirth=request.form['date']
        gndr=request.form['radio']
        place=request.form['plce']
        pst=request.form['post']
        pcode=request.form['pin']
        emid=request.form['mail']
        phone=request.form['phno']
        pswd=request.form['pwrd']
        cpswd=request.form['pswrd']

        if pswd==cpswd:
            qry="insert into login values(null,%s,%s,'user')"
            val=(uname,pswd)
            lid=iud(qry,val)
            qry1="insert into user values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val1=(fname,lname,dobirth,gndr,place,pst,pcode,emid,phone,str(lid))
            iud(qry1,val1)
            return'''<script>alert("welcome user");window.location="/"</script>'''
        else:
            return'''<script>alert("password not correct"); window.location="/usersign"</script>'''
    except Exception as e:
        return '''<script>alert("Already Exist"); window.location="/usersign"</script>'''





# Admin verify patents
@app.route("/verifypatent")
@login_required
def verifypatent():
    qry="select * from certificate where status='pending'"
    res=select(qry)
    return render_template("admin/Verifycertificate.html",val=res)


# user view patents
@app.route('/userviewpatent')
@login_required
def userviewpatent():
    qry = "SELECT * FROM certificate WHERE STATUS='approved'"

    res = select(qry)

    return render_template("user/viewcertificate.html",val=res)


# user ask doubt
@app.route('/usraskdoubt')
@login_required
def usraskdoubt():
    qry = "SELECT * FROM certificate WHERE STATUS='approved'"

    res = select(qry)


    return render_template("user/doubt.html",val=res)


@app.route('/usrsenddoubt')
@login_required
def usrsenddoubt():
    id = request.args.get('id')
    session['cid'] = id
    return render_template("user/Send_doubt.html")

@app.route('/usddoubt',methods=['post'])
@login_required
def usddoubt():
    res = str(session['cid'])
    uid=str(session['lid'])
    rply = request.form['textarea']
    qry = "INSERT INTO doubt VALUES(NULL,%s,%s,%s,'pending',CURDATE(),'pending')"
    val = (res,uid,rply)
    iud(qry, val)
    return '''<script>alert("send");window.location="/usraskdoubt"</script>'''




 # user ask doubt code end here

@app.route("/viewcerti")
@login_required
def viewcerti():
    qry="select * from certificate where User_id=%s"
    val=str(session['lid'])
    res=selectall(qry,val)
    return render_template("user/viewcertificate.html",val=res)

@app.route("/viewcomm")
@login_required
def viewcomm():
    qry="select * from comment where User_id=%s"
    val=str(session['lid'])
    res=selectall(qry,val)
    return render_template("user/Viewcomment.html",val=res)

@app.route("/viewinfo")
@login_required
def viewinfo():
    qry="SELECT * FROM information WHERE STATUS='approved'"

    res = select(qry)
    return render_template("user/Viewinformation.html",val=res)

@app.route("/viewupl")
@login_required
def viewupl():
    qry="select * from information where Login_id=%s"
    val=session['lid']
    res=selectall(qry,val)
    return render_template("user/viewupload.html",val=res)

@app.route('/delupinfo',methods=['get'])
@login_required
def delupinfo():
    id=request.args.get('id')
    qry="delete from information where Info_id=%s "
    val=(id)
    iud(qry,val)
    return '''<script>alert("information deleted");window.location="/viewupl"</script>'''



@app.route('/delinfo')
@login_required
def delinfo():
    id=request.args.get('id')
    qry="delete from information where Info_id=%s "
    val=(id)
    iud(qry,val)
    return '''<script>alert("information deleted");window.location="/manageinfo"</script>'''

@app.route('/approvinfo')
@login_required
def approvinfo():
    id=request.args.get('id')
    qry="update information set status='approved' where Info_id=%s"
    val=(id)
    iud(qry,val)
    return '''<script>alert("information approved");window.location="/verifyuserinfo"</script>'''

@app.route('/rejectinfo')
@login_required
def rejectinfo():
    id=request.args.get('id')
    qry="update information set status='rejected' where Info_id=%s"
    val=(id)
    iud(qry,val)
    return '''<script>alert("information rejected");window.location="/verifyuserinfo"</script>'''

# patent coding starts here
@app.route('/inventorhome')
@login_required
def inventorhome():
    return render_template("Inventor/Inventor home.html")

@app.route('/uploadpatent')
@login_required
def uploadpatent():
    return render_template("Inventor/Patent.html")

@app.route('/managpatent')
@login_required
def managpatent():
    q="SELECT * FROM certificate where Inv_id=%s"
    val=(str(session['lid']),)
    res=selectall(q,val)




    return render_template("Inventor/Manage_patent.html",val=res)

@app.route('/Addpatent',methods=['post'])
@login_required
def Addpatent():
    title = request.form['title']
    pnumber = request.form['pnum']
    coinv=request.form['coinvt']
    date=request.form['date']
    abstract=request.form['abstract']

    cntry=request.form['conty']
    certi=request.files['certifi']


    file = secure_filename(certi.filename)
    print(file)
    certi.save(os.path.join("static/certificate/", file))
    qry = "insert into certificate values(null,%s,%s,%s,%s,%s,%s,%s,%s,'pending')"
    val = (str(session['lid']), title,pnumber,coinv,cntry,date, file,abstract)
    print(val)
    iud(qry, val)
    return '''<script>alert("Patent added");window.location="/managpatent"</script>'''

@app.route("/viewptnt")
@login_required
def viewptnt():
    qry="select * from certificate where Inv_id=%s"
    val=str(session['lid'])
    res=selectall(qry,val)
    return render_template("user/Manage_patent.html",val=res)



@app.route('/delpatent',methods=['get'])
@login_required
def delpatent():
    id=request.args.get('id')
    qry="delete from certificate where Patent_id=%s "
    val=(id)
    iud(qry,val)
    return '''<script>alert("Patent deleted");window.location="/managpatent"</script>'''

@app.route('/editpatent',methods=['get'])
@login_required
def editpatent():
    id=request.args.get('id')
    session['pid']=id
    q="SELECT * FROM `certificate` WHERE `Patent_id`=%s"
    val=(id)
    res=selectone(q,val)
    print(res)
    return render_template("Inventor/EditPatent.html",val=res)

@app.route('/subeditpat',methods=['post'])
@login_required
def subeditpat():
    try:
        title = request.form['title']
        pnumber = request.form['pnum']
        coinv = request.form['coinvt']
        date = request.form['date']
        abstract = request.form['abstract']

        cntry = request.form['conty']
        certi = request.files['certifi']

        file = secure_filename(certi.filename)
        print(file)
        certi.save(os.path.join("static/certificate/", file))
        qry = "update certificate set title=%s,Patent_no=%s,Co_inventors=%s,Country=%s,Date=%s,Certificate=%s,Abstract=%s where Patent_id=%s"
        val = ( title, pnumber, coinv, cntry, date, file, abstract,str(session['pid']))
        print(val)
        iud(qry, val)
        return '''<script>alert("Patent Edited");window.location="/managpatent"</script>'''
    except Exception as e:
        title = request.form['title']
        pnumber = request.form['pnum']
        coinv = request.form['coinvt']
        date = request.form['date']
        abstract = request.form['abstract']

        cntry = request.form['conty']



        qry = "update certificate set title=%s,Patent_no=%s,Co_inventors=%s,Country=%s,Date=%s,Abstract=%s where Patent_id=%s"
        val = (title, pnumber, coinv, cntry, date, abstract, str(session['pid']))
        print(val)
        iud(qry, val)
        return '''<script>alert("Patent Edited");window.location="/managpatent"</script>'''

        return





@app.route('/addpatent')
@login_required
def addpatent():
    return


@app.route('/doubtview')
@login_required
def doubtview():
    qry="SELECT `doubt`.`Doubt_id`,`doubt`.`Doubt`,`doubt`.`Date`,`user`.`First_Name`,`user`.`Last_Name` FROM `doubt` JOIN `user` ON `doubt`.`User_id`=`user`.`login_id` WHERE `doubt`.`Inv_id`=%s AND `doubt`.`Reply`='pending'"
    val=(str(session['lid']))
    print()
    res=selectall(qry,val)
    return render_template("Inventor/View_doubt.html",val=res)

@app.route('/viewpatent')
@login_required
def viewpatent():
    qry = "SELECT * FROM certificate WHERE STATUS='approved'"

    res = select(qry)

    return render_template("Inventor/View_patent.html",val=res)

@app.route('/viewreply')
@login_required
def viewreply():
    return render_template("Inventor/View_reply.html")







@app.route('/inventorchat')
@login_required
def inventorchat():
    qry = "SELECT * FROM certificate WHERE STATUS='approved' and Inv_id!=%s"
    val=(str(session['lid']))
    res = selectall(qry,val)
    return render_template("Inventor/Inventor_chat.html", val=res)






@app.route('/invdetails')
def invdetails():
    return render_template("Inventor/Inventor.html")

@app.route('/invsignup',methods=['post'])
def invsignup():
    try:
        fname = request.form['finame']
        lname = request.form['lsname']
        uname = request.form['usname']
        dobirth = request.form['date']
        gndr = request.form['radio']
        place = request.form['plce']
        pst = request.form['post']
        pcode = request.form['pin']
        emid = request.form['mail']
        phone = request.form['phno']
        pswd = request.form['pwrd']
        cpswd = request.form['pswrd']

        if pswd == cpswd:
            qry = "insert into login values(null,%s,%s,'inventor')"
            val = (uname, pswd)
            lid = iud(qry, val)
            qry1 = "insert into inventor values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val1 = (fname, lname, dobirth, gndr, place, pst, pcode, emid, phone, str(lid))
            iud(qry1, val1)
            return '''<script>alert("welcome Inventor");window.location="/"</script>'''
        else:
            return '''<script>alert("password not correct"); window.location="/invdetails"</script>'''
    except Exception as e:
        return '''<script>alert("Already Exist"); window.location="/invdetails"</script>'''


@app.route('/reply')
@login_required
def reply():
    id = request.args.get('id')
    session['cid'] = id
    return render_template("Inventor/Reply.html")

@app.route("/invreply",methods=['post'])
@login_required
def invreply():
    res=str(session['cid'])
    rply=request.form['textarea']
    qry="update doubt set Reply=%s where Doubt_Id=%s"
    val=(rply,res)
    iud(qry,val)
    return '''<script>alert("replied");window.location="/doubtview"</script>'''

@app.route("/inventorreply")
@login_required
def inventorreply():
    qry="SELECT `doubt`.`Doubt`,`doubt`.`Reply`,`doubt`.`Date`,`inventor`.`Fname`,`inventor`.`Lname`,`doubt`.`Reply` FROM `inventor` JOIN `doubt` ON `inventor`.`Login_id`=`doubt`.`Inv_id` JOIN `user` ON `user`.`login_id`=`doubt`.`User_id` WHERE `doubt`.`User_id`=%s"
    val=(str(session['lid']))
    res=selectall(qry,val)


    return render_template("user/Inventor_reply.html",val=res)




@app.route("/feedback",methods=['get','post'])
@login_required
def feedback():
    qry="select * from doubt where User_id=%s"
    val=str(1)

    res = selectall(qry,val)
    return render_template("Inventor/Feedback.html",val=res)

@app.route("/feedbackpge",methods=['post','get'])
@login_required
def feedbackpge():
    return render_template("Inventor/feedbackpage.html")

# inventor send feedback
@app.route("/sendfeedback",methods=['get','post'])
@login_required
def sendfeedback():
    feedbck=request.form['textarea']
    print(feedbck)
    q="insert into doubt values(NULL,%s,%s,%s,'pending',curdate(),'pending')"
    val=(session['lid'],str(1),feedbck)
    iud(q,val)
    return '''<script>alert("feedback send");window.location="/feedback"</script>'''




@app.route("/viewfeedback")
@login_required
def viewfeedback():
    qry="SELECT doubt.*,inventor.Fname,inventor.Lname FROM doubt JOIN inventor ON doubt.Inv_id=inventor.Login_id WHERE doubt.User_id=%s AND doubt.Reply='pending'"
    val=str(1)
    res=selectall(qry,val)
    return render_template("admin/View_feedback.html",val=res)

@app.route("/replyfeedback")
@login_required
def replyfeedback():
    id = request.args.get('id')
    session['fid'] = id
    return render_template("admin/Replypage.html")


# admin type reply
@app.route("/Admrplyfdbk",methods=['post'])
@login_required
def Admrplyfdbk():
    res = str(session['fid'])
    rply = request.form['textarea']
    qry = "update doubt set Reply=%s,Status='replied' where Doubt_Id=%s"
    val = (rply, res)
    iud(qry, val)
    return '''<script>alert("replied");window.location="/viewfeedback"</script>'''


@app.route("/chat")
@login_required
def chat():
    tid = request.args.get('id')
    session['tid'] = tid
    qry = "select Fname,Lname from inventor where Login_id=%s"
    val = str(session['tid'])
    s1 = selectone(qry, val)
    print(s1)
    fid = session['lid']
    qry2 = "select * from chat where (Toid=%s and Fromid=%s) or (Toid=%s and Fromid=%s) order by Cid asc"
    val2 = (str(tid), str(fid), str(fid), str(tid))
    s2 = selectall(qry2, val2)
    print(s2)
    return render_template("Inventor/chat.html",fname=s1[0],lname=s1[1],data=s2,fr=str(tid))




@app.route("/send",methods=['post'])
@login_required
def send():
    ffid = session['lid']
    tid = session['tid']
    msg = request.form['textarea']
    qry = "insert into chat values(NULL,%s,%s,%s,curdate())"
    val = (str(ffid), str(tid), msg)
    iud(qry, val)
    # return render_template("Inventor/chat.html")
    return redirect("/usersendchat")

@app.route("/usersendchat")
@login_required
def usersendchat():
    tid=session['tid']
    qry="select Fname,Lname from inventor where Login_id=%s"
    val=str(session['tid'])
    s1=selectone(qry,val)
    print(s1)
    fid=session['lid']
    qry2="select * from chat where (Toid=%s and Fromid=%s) or (Toid=%s and Fromid=%s) order by Cid asc"
    val2 = (str(tid), str(fid), str(fid), str(tid))
    s2=selectall(qry2,val2)
    print(s2 )
    return render_template("Inventor/chat.html",fname=s1[0],lname=s1[1],data=s2,fr=str(tid))





@app.route('/Ancient_World')

def Ancient_World():
    qry="SELECT * FROM `information` WHERE `Year` <=-100"
    res=select(qry)
    return render_template("more_details.html",val=res)

@app.route('/Revolution')

def Revolution():
    qry="SELECT * FROM information WHERE YEAR BETWEEN 0 AND 1799"
    res=select(qry)
    return render_template("more_details.html",val=res)

@app.route('/Industrial_Age')

def Industrial_Age():
    qry="SELECT * FROM information WHERE YEAR BETWEEN 1800 AND 1859"
    res=select(qry)
    return render_template("more_details.html",val=res)

@app.route('/Empires')

def Empires():
    qry="SELECT * FROM information WHERE YEAR BETWEEN 1860 AND 1891"
    res=select(qry)
    return render_template("more_details.html",val=res)

@app.route('/Modern_Age')

def Modern_Age():
    qry="SELECT * FROM information WHERE YEAR BETWEEN 1892 AND 1924"
    res=select(qry)
    return render_template("more_details.html",val=res)

@app.route('/Peace')

def Peace():
    qry="SELECT * FROM information WHERE YEAR BETWEEN 1925 AND 1951"
    res=select(qry)
    return render_template("more_details.html",val=res)

@app.route('/Going_Global')

def Going_Global():
    qry="SELECT * FROM information WHERE YEAR BETWEEN 1952 AND 1968"
    res=select(qry)
    return render_template("more_details.html",val=res)

@app.route('/Internet')

def Internet():
    qry="SELECT * FROM `information` WHERE `Year` >=1969"
    res=select(qry)
    return render_template("more_details.html",val=res)



@app.route('/more_details1')

def more_details1():
    id=request.args.get("id")
    qry="SELECT * FROM `information` WHERE Info_Id=%s"
    val=(id)
    res=selectall(qry,val)
    print(res)
    x = res[0][5].startswith("http")
    print(x,"+++++++++++++++++++++++++++++++++++")
    f="1"
    if x:
        f="0"

    return render_template("descr.html",val=res,f=f)

@app.route("/forgotpwd",methods=['post','get'])

def forgotpwd():
    return render_template("login1.html")


@app.route("/fgrtpwd",methods=['get','post'])

def fgrtpwd():
    username=request.form['uname']
    email=request.form['email']
    qry="SELECT * FROM `login` JOIN `user` ON `login`.`Login_id`=`user`.`login_id` WHERE `login`.`Username`=%s AND `user`.`Emai_id`=%s"
    val=(username,email)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("invalid"); window.location="/forgotpwd"</script>'''
    else:
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('inventonandinventor@gmail.com', 'invention123')
        except Exception as e:
            print("Couldn't setup email!!" + str(e))
        msg = MIMEText("Your password is " + res[2])
        print(msg)
        msg['Subject'] = 'Password'
        msg['To'] = email
        msg['From'] = 'inventonandinventor@gmail.com'
        try:
            gmail.send_message(msg)
        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
        return '''<script>alert("password is sent"); window.location="/indexlogin"</script>'''


@app.route("/search_info",methods=['post','get'])

def search_info():
    info=request.form['ser']
    qry="SELECT * FROM `information` WHERE Invention like '"+info+"%'"

    res=select(qry)
    return render_template("more_details_1.html", val=res)


@app.route("/usname",methods=['POST'])
def usname():
    print(request.form)
    usrname=request.form['brand']
    qry="SELECT `Username`FROM `login` where Username=%s"
    val=(usrname)

    res=selectone(qry,val)
    print(res)
    if res is None:

        resp = make_response(json.dumps(""))

        resp.status_code = 200
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    else:
        resp = make_response(json.dumps("Username existing"))

        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

# @app.route("/usrname",methods=['POST'])
# def usrname():
#     print(request.form)
#     usrname=request.form['brands']
#     qry="SELECT `Username`FROM `login` where Username=%s"
#     val=(usrname)
#
#     res=selectone(qry,val)
#     print(res)
#     if res is None:
#
#         resp = make_response(json.dumps(""))
#
#         resp.status_code = 200
#         resp.headers['Access-Control-Allow-Origin'] = '*'
#         return resp
#
#     else:
#         resp = make_response(json.dumps("Username existing"))
#
#         resp.headers['Access-Control-Allow-Origin'] = '*'
#         return resp
@app.route("/emailrgs")
def emailrgs():
    return render_template("login2.html")


@app.route("/otp",methods=["POST"])
def otp():
        email=request.form['eml']
        import random
        otp=random.randint(1000,3000)
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('inventonandinventor@gmail.com', 'invention123')
        except Exception as e:
            print("Couldn't setup email!!" + str(e))
        msg = MIMEText("Your otp is " + str(otp))
        session['otp']=otp
        print(msg)
        msg['Subject'] = 'Password'
        msg['To'] = email
        msg['From'] = 'inventonandinventor@gmail.com'
        try:
            gmail.send_message(msg)
            return '''<script>alert("otp is sent"); window.location="/otpverif"</script>'''
        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
            return '''<script>alert("invalid email"); window.location="/emailrgs"</script>'''

@app.route("/otpverif")
def otpverif():
    return render_template("login3.html")

@app.route("/otpveri",methods=["post"])
def otpveri():
    otp=request.form["name"]
    otps=session['otp']
    if int(otp)==int(otps):
        return '''<script>alert("email succrssfully registered"); window.location="/reg"</script>'''
    else:
        return '''<script>alert("incorrect otp"); window.location="/otpverif"</script>'''



# otp registration code for inventor

@app.route("/emailrgstwo")
def emailrgstwo():
    return render_template("login4.html")


@app.route("/otptwo",methods=["POST"])
def otptwo():
        email=request.form['email']
        import random
        otp=random.randint(1000,3000)
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('inventonandinventor@gmail.com', 'invention123')
        except Exception as e:
            print("Couldn't setup email!!" + str(e))
        msg = MIMEText("Your otp is " + str(otp))
        session['otp']=otp
        print(msg)
        msg['Subject'] = 'Password'
        msg['To'] = email
        msg['From'] = 'inventonandinventor@gmail.com'
        try:
            gmail.send_message(msg)
            return '''<script>alert("otp is sent"); window.location="/otpveriftwo"</script>'''
        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
            return '''<script>alert("invalid email"); window.location="/emailrgstwo"</script>'''

@app.route("/otpveriftwo")
def otpveriftwo():
    return render_template("login5.html")

@app.route("/otpveritwo",methods=["post"])
def otpveritwo():
    otp=request.form["name1"]
    otps=session['otp']
    if int(otp)==int(otps):
        return '''<script>alert("email succrssfully registered"); window.location="/reg1"</script>'''
    else:
        return '''<script>alert("incorrect otp"); window.location="/otpveriftwo"</script>'''





app.run(debug=True)



