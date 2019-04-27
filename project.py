
from flask import *
import pymysql
app=Flask(__name__)
conn=pymysql.connect(host="localhost",user="root",passwd="",port=3306,db="exam")
cmd=conn.cursor()
app.secret_key='sesskey'

@app.route('/')
def main():
    return render_template("login.html")
@app.route('/login',methods=['get','post'])
def login():
    uname=request.form['textfield']
    password=request.form['textfield2']
    cmd.execute("select * from login where User_name='"+uname+"' and Password='"+password+"'")
    s=cmd.fetchone()
    session['lid'] =s[0]
    print(s[0])
    if s is None:
        return '''<script> alert(" invalid user name or password");window.location='/' </script>'''
    elif s[3]=='controller':

        return '''<script> alert(" login successfull");window.location='/examhome' </script>'''
    elif s[3]=='student':

        return '''<script> alert(" login successfull");window.location='/studenthome' </script>'''
    elif s[3]=='devagiri':

        return '''<script> alert(" login successfull");window.location='/devagirihome' </script>'''
    elif s[3] == 'staff':

        return '''<script> alert(" login successfull");window.location='/depthome' </script>'''

    else:
        return '''<script> alert(" invalid user name or password");window.location='/' </script>'''

@app.route('/examhome',methods=['get','post'])
def examhome():
    return render_template("controllerindex.html")


@app.route('/studenthome',methods=['get','post'])
def studenthome():
    return render_template("Student home.html")

@app.route('/depthome',methods=['get','post'])
def depthome():
    return render_template("staffindex.html")

@app.route('/devagirihome',methods=['get','post'])
def devagirihome():
    return render_template("collegeindex.html")

@app.route('/department',methods=['get','post'])
def department():

    return render_template("Dept.html")

@app.route('/hallticketapprove',methods=['get','post'])
def hallticketapprove():
    val = request.args.get('id')
    cmd.execute("update hall_ticket set status='approved' where id='"+val+"'")
    conn.commit()
    return '''<script> alert("Hall ticket approved");window.location='/viewhallticket' </script>'''




@app.route('/course',methods=['get','post'])
def course():
    return render_template("courses.html")

@app.route('/course1', methods=['get','post'])
def course1():
    Course_name = request.form['textfield']
    Duration = request.form['textfield2']
    cmd.execute("insert into courses values(null,'"+Course_name+"','"+Duration+"')")
    conn.commit()
    return '''<script> alert("Course Added");window.location='/course' </script>'''

@app.route('/subject',methods=['get','post'])
def subject():
    cmd.execute("select Course_id, Course_name from courses")
    a = cmd.fetchall()
    return render_template("subject.html", val=a)

@app.route('/subject1', methods=['get','post'])
def subject1():

    course = request.form['select2']
    sem=request.form['select3']
    subject=request.form['textfield']
    cmd.execute("insert into subject values(null,'"+course+"','"+sem+"','"+subject+"')")
    conn.commit()
    return '''<script> alert("subject Added");window.location='/subject' </script>'''



@app.route('/stdapproval',methods=['get','post'])
def stdapproval():
    cmd.execute("select Course_id, Course_name from courses")
    k = cmd.fetchall()
    return render_template("std verify.html",val1=k )


@app.route('/stdapproval1',methods=['get','post'])
def stdapproval1():
    course = request.form['select']
    sem = request.form['select2']
    print(course)
    print(sem)
    cmd.execute("select std_reg.* from std_reg join login on std_reg.id=login.id where std_reg.Course='"+course+"' and std_reg.sem='"+sem+"' and login.Type='pending'")
    s = cmd.fetchall()
    print("ssss",s)
    cmd.execute("select Course_id, Course_name from courses")
    k = cmd.fetchall()
    return render_template("std verify.html", val3=s,val1=k)


@app.route('/examc',methods=['get','post'])
def examc():
    return render_template("Exam controll reg.html")
@app.route('/examc1', methods=['get','post'])
def examc1():
    First_name = request.form['textfield']
    Last_name = request.form['textfield2']
    Address = request.form['textarea']
    Dob = request.form['textfield8']
    Gender = request.form['radio']
    Qualification = request.form.getlist('checkbox')
    Phone = request.form['textfield4']
    Email = request.form['textfield5']
    Post = request.form['textfield6']
    Doj = request.form['textfield7']
    cmd.execute("insert into login values(null,'"+First_name+"','"+Phone+"','controller')")
    id=conn.insert_id()
    cmd.execute("insert into examc_reg values('"+str(id)+"','"+First_name+"','"+Last_name+"','"+Address+"','"+Dob+"','"+Gender+"','"+str(','.join(Qualification))+"','"+Phone+"','"+Email+"','"+Post+"','"+Doj+"')")
    conn.commit()
    return '''<script> alert("Registered Successfully ");window.location='/examc' </script>'''


@app.route('/examnotification',methods=['get','post'])
def examnotification():
    return render_template("notification.html")
@app.route('/notification', methods=['get','post'])
def notification():
    date = request.form['textfield2']
    notification = request.form['textarea']
    cmd.execute("insert into notification values(null,'"+date+"','"+notification+"')")
    conn.commit()
    return '''<script> alert("Notification Added");window.location='/examnotification' </script>'''

@app.route('/addexam',methods=['get','post'])
def addexam():
    cmd.execute("select Course_id, Course_name from courses")
    a = cmd.fetchall()

    cmd.execute("select id, Subject from subject")
    b = cmd.fetchall()
    return render_template("Exam add.html",val=a,val2=b)

@app.route('/addexam1', methods=['get','post'])
def addexam1():
    Exam_Name= request.form['textfield']
    Course = request.form['select']
    subject = request.form['select2']
    Date = request.form['textfield2']

    cmd.execute("insert into exam_add values(null,'"+Exam_Name+"','"+Course+"','"+subject+"','"+Date+"')")
    conn.commit()
    return '''<script> alert("Exam Added");window.location='/addexam' </script>'''

@app.route('/publishresu',methods=['get','post'])
def publishresu():
    return render_template("result publish.html")

@app.route('/reg4',methods=['get','post'])
def reg4():
    cmd.execute("select Course_id, Course_name from courses")
    c= cmd.fetchall()

    return render_template("register std.html",val3=c)
@app.route('/reg5', methods=['get','post'])
def reg5():
    Reg_no = request.form['textfield12']
    First_Name = request.form['textfield']
    Last_Name = request.form['textfield2']
    Father_Name=request.form['textfield3']
    Dob = request.form['textfield4']
    Gender = request.form['radio']
    Address = request.form['textarea']
    District = request.form['textfield5']
    Pincode = request.form['textfield6']
    State = request.form['textfield7']
    Nationality = request.form['textfield8']
    Qualification = request.form.getlist('checkbox')
    Phone_number = request.form['textfield9']
    Email = request.form['textfield15']
    Course= request.form['select4']
    Sem= request.form['select6']
    cmd.execute("insert into login values(null,'"+Email+"','"+Phone_number+"','pending')")
    id=conn.insert_id()
    cmd.execute("insert into Std_reg values('"+str(id)+"','"+Reg_no+"','"+First_Name+"','"+Last_Name+"','"+Father_Name+"','"+Dob+"','"+Gender+"','"+Address+"','"+District+"','"+Pincode+"','"+State+"','"+Nationality+"','"+str(','.join(Qualification))+"','"+Phone_number+"','"+Email+"','"+Course+"','"+Sem+"')")
    conn.commit()
    return '''<script> alert(" Successfully Registered");window.location='/reg4' </script>'''
@app.route('/questview',methods=['get','post'])
def questview():


    return render_template("Question view.html")
@app.route('/questviewed',methods=['get','post'])
def questviewed():

    return render_template("Question view.html")



@app.route('/question',methods=['get','post'])
def question():
    btn=request.form['Submit']
    if btn=='Add':
        cmd.execute("select Exam_id, Exam_Name from exam_add")
        h = cmd.fetchall()
        cmd.execute("select id, Subject from subject")
        k = cmd.fetchall()
        return render_template("Question&answer.html", val=h, val5=k)




@app.route('/question1',methods=['get', 'post'])
def question1():
    Select_Exam= request.form['select']
    Subject = request.form['select2']
    Question = request.form['textarea']
    Answer = request.form['textarea2']
    Mark=request.form['textfield']

    cmd.execute("insert into question values(null,'"+Select_Exam+"','"+Subject+"','"+Question+"','"+Answer+"','"+Mark+"')")
    conn.commit()
    return '''<script> alert("Question Added");window.location='/question' </script>'''

@app.route('/staffreg',methods=['get','post'])
def staffreg():
    return render_template("staff reg.html")
@app.route('/staffreg1', methods=['get','post'])
def staffreg1():
    First_name = request.form['textfield']
    Last_name = request.form['textfield2']
    Father_name = request.form['textfield7']
    Address= request.form['textarea2']
    Gender=request.form['radio']
    Dob=request.form['textfield3']
    Qualification= request.form.getlist('checkbox')
    Doj = request.form['textfield4']
    Phone = request.form['textfield5']
    Email = request.form['textfield6']
    Post = request.form['select']
    cmd.execute("insert into login values(null,'" + First_name + "','" + Phone + "','staff')")
    id = conn.insert_id()
    cmd.execute("insert into staff_reg values('"+str(id)+"','"+First_name+"','"+Last_name+"','"+Father_name+"','"+Address+"','"+Gender+"','"+Dob+"','"+str(','.join(Qualification))+"','"+Doj+"','"+Phone+"','"+Email+"','"+Post+"')")
    conn.commit()
    return '''<script> alert("Successfully Registered");window.location='/staffreg' </script>'''
@app.route('/apprvstudent',methods=['get','post'])
def apprvstudent():
    id=request.args.get('id')
    cmd.execute("update login set type='student' where Id='"+id+"'")
    conn.commit()
    return redirect('stdapproval')


@app.route('/rejectstudent',methods=['get','post'])
def rejectstudent():
    id=request.args.get('id')
    cmd.execute("update login set type='reject' where Id='"+id+"'")
    conn.commit()
    return redirect('stdapproval')

@app.route('/timetable',methods=['get','post'])
def timetable():
    cmd.execute("select Course_id, Course_name from courses")
    a = cmd.fetchall()

    return render_template("upload_timetable.html",val=a)


@app.route('/uploadtimetable',methods=['get','post'])
def uploadtimetable():
    course = request.form['select2']
    sem = request.form['select3']
    timetable = request.files['filefield']
    img_name = timetable.filename
    timetable.save("C:\\Users\\chaitanya\\PycharmProjects\\Answer_Checker\\Answer\\static\\timetable\\" + img_name)
    cmd.execute("insert into timetable values(null,'"+course+"','"+sem+"','"+img_name+"')")
    conn.commit()
    return '''<script> alert("Time table uploaded");window.location='/timetable' </script>'''


@app.route('/viewhallticket',methods=['get','post'])
def viewhallticket():
    cmd.execute("select hall_ticket.*, std_reg.First_Name,Last_Name,Reg_no from hall_ticket,std_reg where hall_ticket.student_id=std_reg.id and hall_ticket.status='pending'")
    a = cmd.fetchall()
    return render_template("hall ticker approval.html", val=a)

@app.route('/exams',methods=['get','post'])
def exams():

    cmd.execute("select * from exam_add")
    a = cmd.fetchall()
    return render_template("Question view.html", val=a)


@app.route('/searchquestions',methods=['get','post'])
def searchquestions():
    cmd.execute("select * from exam_add")
    b = cmd.fetchall()
    exam = request.form['select']
    print(exam)
    cmd.execute("select * from question where exam_id='"+exam+"' and status='pending'")
    a = cmd.fetchall()
    return render_template("Question view.html", data=a,val=b)

@app.route('/questionapprove',methods=['get','post'])
def questionapprove():
    val = request.args.get('id')
    cmd.execute("update question set status='approved' where Qid='"+val+"'")
    conn.commit()
    return '''<script> alert("Questions approved");window.location='/exams' </script>'''

@app.route('/chooseexams',methods=['get','post'])
def chooseexams():

    cmd.execute("select * from exam_add")
    a = cmd.fetchall()
    return render_template("Qustn&answer.html", val=a)



@app.route('/questionadd',methods=['get','post'])
def questionadd():
    examid = request.form['select']
    quest = request.form['textarea']
    answ = request.form['textarea2']
    mark = request.form['textfield2']
    cmd.execute("insert into question values(null,'"+examid+"','"+quest+"','"+answ+"','"+mark+"','pending')")
    conn.commit()
    return '''<script> alert("Questions added");window.location='/chooseexams' </script>'''


@app.route('/hallticket',methods=['get','post'])
def hallticket():

    cmd.execute("select * from std_reg")
    a = cmd.fetchall()
    return render_template("hall ticket.html", val=a)


@app.route('/uploadhallticket',methods=['get','post'])
def uploadhallticket():
    studid = request.form['select']
    mont = request.form['select2']
    year = request.form['select3']
    my= mont+" "+year
    ticket = request.files['filefield']
    img_name = ticket.filename
    ticket.save("C:\\Users\\chaitanya\\PycharmProjects\\Answer_Checker\\Answer\\static\\hallticket\\" + img_name)
    cmd.execute("insert into hall_ticket values(null,'"+studid+"','"+my+"','"+img_name+"','pending')")
    conn.commit()
    return '''<script> alert("Hall ticket uploaded");window.location='/hallticket' </script>'''


@app.route('/viewcourse',methods=['get','post'])
def viewcourse():
    cmd.execute("select Course_id, Course_name from courses")
    a = cmd.fetchall()
    return render_template("view_timetable.html",val=a,data="pdf")

@app.route('/viewtimetable',methods=['get','post'])
def viewtimetable():
    cmd.execute("select Course_id, Course_name from courses")
    a = cmd.fetchall()
    cid = request.form['select2']
    sem = request.form['select3']
    cmd.execute("select time_table from timetable where course_id='"+cid+"' and sem='"+sem+"'")
    b = cmd.fetchone()
    print(b)
    return render_template("view_timetable.html",val=a,data=b)

@app.route('/hallticketdown',methods=['get','post'])
def hallticketdown():
    stid=session['lid']
    print(stid)
    cmd.execute("select * from hall_ticket where student_id='"+str(stid)+"' and status='approved'")
    b = cmd.fetchone()
    return render_template("view_hall_ticket.html",data=b)

if __name__=='__main__':
    app.run(host='127.0.0.1',debug=True,port=8000)
