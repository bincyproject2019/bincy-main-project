from cgitb import reset

import os
from flask import *
import pymysql

from Answer.test import text_to_vector, get_cosine

app=Flask(__name__)
conn=pymysql.connect(host="localhost",user="root",passwd="root",port=3306,db="exam")
cmd=conn.cursor()
app.secret_key='sesskey'
path="E:\\New folder\\Answer_Checker\\Answer\\static\\timetable"
@app.route('/')
def main():
    return render_template("login.html")
@app.route('/login',methods=['get','post'])
def login():
    uname=request.form['textfield']
    password=request.form['textfield2']
    cmd.execute("select * from login where User_name='"+uname+"' and Password='"+password+"'")
    s=cmd.fetchone()

    print(s)
    if s is None:
        return '''<script> alert(" invalid user name or password");window.location='/' </script>'''
    elif s[3]=='controller':
        session['lid'] = s[0]
        return '''<script> alert(" login successfull");window.location='/examhome' </script>'''
    elif s[3]=='student':
        session['lid'] = s[0]
        return '''<script> alert(" login successfull");window.location='/studenthome' </script>'''
    elif s[3]=='devagiri':
        session['lid'] = s[0]
        return '''<script> alert(" login successfull");window.location='/devagirihome' </script>'''
    elif s[3] == 'staff':
        session['lid'] = s[0]
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
    cmd.execute("select * from courses where Course_id not in(select course from examc_reg)")
    s=cmd.fetchall()
    return render_template("Exam controll reg.html",val=s)
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
    Post = request.form['crs']
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

    cmd.execute("insert into exam_add values(null,'"+Exam_Name+"','"+Course+"','"+subject+"','"+Date+"','pending')")
    conn.commit()
    return '''<script> alert("Exam Added");window.location='/addexam' </script>'''

@app.route('/publishresu',methods=['get','post'])
def publishresu():
    cmd.execute("select Exam_Name,Exam_id from exam_add where Date<curdate() and publish='pending'")
    c = cmd.fetchall()
    return render_template("result publish.html",val=c)

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

    cmd.execute("select * from Std_reg where Course= "+str(Course))
    regno=''
    if str(Course)=="2":
        regno="MA"
    elif str(Course)=="1":
        regno="BA"
    elif str(Course)=="9":
        regno="MCA"

    s=cmd.fetchall()

    rno=len(s)+1+100

    regno=regno+str(rno)

    cmd.execute("insert into login values(null,'"+Email+"','"+Phone_number+"','pending')")
    id=conn.insert_id()
    cmd.execute("insert into Std_reg values('"+str(id)+"','"+regno+"','"+First_Name+"','"+Last_Name+"','"+Father_Name+"','"+Dob+"','"+Gender+"','"+Address+"','"+District+"','"+Pincode+"','"+State+"','"+Nationality+"','"+str(','.join(Qualification))+"','"+Phone_number+"','"+Email+"','"+Course+"','"+Sem+"')")
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
    timetable.save(os.path.join(path,img_name))
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

    cmd.execute("select * from courses")
    a = cmd.fetchall()
    return render_template("Qustn&answer.html", val=a)



@app.route('/questionadd',methods=['get','post'])
def questionadd():
    examid = request.form['exam']
    quest = request.files['qus']

    quest.save('example.pdf')

    filename = "example.pdf"
    import PyPDF2
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    count = 0
    text = ""
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()
    if text != "":
        text = text

    # print(text)

    questions=text.split('Question')
    print(questions)
    for cqus in questions:
        cquslist=cqus.split('Answer:')
        qus=str(cquslist[0]).split(':') #[1].replace('\n',' ')

        print(qus)
        if len(qus)>1:
            cquss=qus[1].replace('\n',' ')
            print(cquss)

            cans=cquslist[1].split('mark:')

            canss=str(cans[0]).replace('\n','').replace('\t','')
            cmark=cans[1].replace('\n','').replace('\t','')
            print(canss)
            print(cmark)
            cmd.execute(
                "insert into question values(null,'" + examid + "','" + cquss + "','" + canss + "','" + str(cmark) + "','pending','"+str(session['lid'])+"')")
            conn.commit()

            print('-----------------------------------------')




    # cmd.execute("insert into question values(null,'"+examid+"','"+quest+"','"+answ+"','"+mark+"','pending')")
    # conn.commit()
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
    ticket.save("E:\\New folder\\Answer_Checker\\Answer\static\\hallticket" + img_name)
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


@app.route('/viewnotification',methods=['get','post'])
def viewnotification():
    cmd.execute("select * from notification")
    b = cmd.fetchall()
    return render_template("viewnotification.html",data=b)

@app.route('/myexams',methods=['get','post'])
def myexams():
    stid = session['lid']
    cmd.execute("select exam_add.Exam_Name,Exam_id from exam_add,std_reg,subject where std_reg.Course=exam_add.Course and std_reg.id='"+str(stid)+"' and exam_add.Subject=subject.id and std_reg.sem=subject.sem")
    b = cmd.fetchall()
    return render_template("view_my_exam.html",data=b)

@app.route('/viewexamquestions',methods=['get','post'])
def viewexamquestions():
    val = request.args.get('id')
    stid = session['lid']
    # SELECT * FROM
    # table_name
    # ORDER
    # BY
    # RANDOM()
    # cmd.execute("select distinct question.tid from write_exam,question where stud_id='" + str(
    #     stid) + "' and write_exam.ques_id=question.Qid and question.exam_id='" + str(val) + "' order by question.tid RANDOM() limit 1")
    # s=cmd.fetchone()

    cmd.execute("select * from write_exam,question where stud_id='"+str(stid)+"' and write_exam.ques_id=question.Qid and question.exam_id='"+str(val)+"'")
    b = cmd.fetchall()
    if len(b)>0:
        return '''<script> alert("Already Attended");window.location='/myexams' </script>'''
    else:
        cmd.execute("select distinct tid  from question where exam_id='" + str(val) + "' order by RAND() limit 1")
        s=cmd.fetchone()
        if len(s)>0:
            cmd.execute("select Qid,Question from question where exam_id='" + str(val) + "' and tid='"+str(s[0])+"'")
            b = cmd.fetchall()
            return render_template("view_my_questions.html", data=b)
        else:
            return '''<script> alert("No questions");window.location='/myexams' </script>'''


@app.route('/answer',methods=['get','post'])
def answer():
    stid = session['lid']
    qid=request.form.getlist('quesid')
    ans=request.form.getlist('answer')
    leng=len(qid)
    for i in range(0,leng):
        cmd.execute("select Answer,exam_id,Mark from question where Qid='"+qid[i]+"'")
        b = cmd.fetchone()
        # vector1 = text_to_vector(ans[i])
        # vector2 = text_to_vector(b[0])
        # cosine = float(get_cosine(vector1, vector2))
        # print(cosine)
        # session['cos'] = cosine
        # res = ''
        # if cosine == 1.0:
        #     res = 10
        # elif cosine >= 0.7:
        #     res = 10
        #     #         session['res']=int(res)
        # elif cosine < 0.7:
        #     res = 7
        # elif cosine >= 0.5:
        #     res = 7
        #     #         session['res']=int(res)
        # elif cosine < 0.5:
        #     res = 5
        # elif cosine >= 0.4:
        #     res = 5
        #     #         session['res']=int(res)
        # elif cosine < 0.4:
        #     res = 0
        #     #         session['res']=int(res)
        #     #     print(str(res),"ui")
        # session['res'] = res

        from sklearn.feature_extraction.text import TfidfVectorizer
        print(ans[i])

        print(b[0])

        documents = [ans[i],b[0]]
        tfidf = TfidfVectorizer().fit_transform(documents)
        # no need to normalize, since Vectorizer will return normalized tf-idf
        pairwise_similarity = tfidf * tfidf.T

        print(pairwise_similarity)

        ps=str(pairwise_similarity).split('\n')
        gmark=0
        print(len(ps))
        if(len(ps)>=4):

            print(ps)
            pss=ps[0].split('\t')[1]
            print(pss)
            mark=int(b[2])
            print(mark)
            gmark=round(float(pss)*float(mark))


        print(gmark)

        cmd.execute("insert into write_exam values(null,'" + str(stid) + "','"+str(b[1])+"','" + qid[i] + "','" + ans[i] + "','"+str(gmark)+"')")
        conn.commit()


    return '''<script> alert("Exam Complete");window.location='/studenthome' </script>'''


@app.route('/resultpublish',methods=['get','post'])
def resultpublish():
    examid = request.args.get('id')
    cmd.execute("update exam_add set publish='published' where Exam_id='"+examid+"'")
    conn.commit()
    cmd.execute("select Exam_Name,Exam_id from exam_add where Date<curdate() and publish='pending'")
    c = cmd.fetchall()
    return render_template("result publish.html",val=c)

@app.route('/stud_viewresult',methods=['get','post'])
def stud_viewresult():
    stid = session['lid']
    per=''
    cmd.execute("select distinct(examid) from write_exam,exam_add where stud_id='"+str(stid)+"' and exam_add.Exam_id=write_exam.examid and exam_add.publish='published'")
    a = cmd.fetchall()
    result=[]
    for x in a:
        curres=[]
        cmd.execute("select sum(Mark), exam_add.Exam_Name,count(ques_id) from write_exam,exam_add where write_exam.stud_id='"+str(stid)+"' and write_exam.examid='"+str(x[0])+"' and write_exam.examid=exam_add.Exam_id")
        c = cmd.fetchone()
        curres.append(c[1])
        per=c[0]/(c[2]*10)*100
        curres.append(per)
        result.append(curres)
    return render_template("view_my_result.html",val=result)

@app.route('/viewresultcourse',methods=['get','post'])
def viewresultcourse():
    cmd.execute("select Course_id, Course_name from courses")
    a = cmd.fetchall()
    return render_template("view_result.html",val=a)

@app.route('/viewresultexam',methods=['get','post'])
def viewresultexam():
    cid = request.form['select']
    cmd.execute("select Course_id, Course_name from courses")
    a = cmd.fetchall()
    cmd.execute("select exam_add.Exam_id,Exam_Name from exam_add where Course='"+str(cid)+"' and publish='published'")
    b = cmd.fetchall()
    return render_template("view_result.html",val=a,val1=b)

@app.route('/viewresultexam1',methods=['get','post'])
def viewresultexam1():
    examid = request.args.get('id')
    examname = request.args.get('name')
    per = ''
    cmd.execute("select distinct(stud_id) from write_exam where examid='"+str(examid)+"'")
    a = cmd.fetchall()
    result = []
    for x in a:
        curres = []
        cmd.execute("select sum(Mark), exam_add.Exam_Name,count(ques_id),std_reg.Reg_no,First_Name,Last_Name from write_exam,exam_add,std_reg where write_exam.stud_id='" + str(x[0]) + "' and write_exam.examid='" + str(examid) + "' and write_exam.examid=exam_add.Exam_id and write_exam.stud_id=std_reg.id")
        c = cmd.fetchone()
        curres.append(c[1])
        per = c[0] / (c[2] * 10) * 100
        curres.append(per)
        curres.append(c[3])
        curres.append(c[4])
        curres.append(c[5])
        result.append(curres)
    return render_template("view_result1.html",val=result,name=examname)

@app.route('/searchsub', methods=['get','post'])
def searchsub():
    output=""
    sid = request.form['search'];
    cour_id = request.form['idd'];

    cmd.execute("select id,Subject from subject where Course_id='"+str(cour_id)+"' and sem='"+str(sid)+"'")
    c=cmd.fetchall()
    output += ' <select name="select2" id="select2"> <option value="">Select</option>'
    for d in c:
        output += '<option value="'+str(d[0])+'">' + d[1] + '</option>'

    output += '</select>'
    return json.dumps({'status': output});



@app.route('/searchsub1', methods=['get','post'])
def searchsub1():
    output=""
    sid = request.form['search'];
    cour_id = request.form['idd'];

    cmd.execute("select id,Subject from subject where Course_id='"+str(cour_id)+"' and sem='"+str(sid)+"'")
    c=cmd.fetchall()
    output += ' <select name="select2" id="select2" onchange="hai1(this.value)" > <option value="">Select</option>'
    for d in c:
        output += '<option value="'+str(d[0])+'">' + d[1] + '</option>'

    output += '</select>'
    return json.dumps({'status': output});


@app.route('/searchexam', methods=['get','post'])
def searchexam():
    output=""
    sid = request.form['search'];

    cmd.execute("select Exam_id,Exam_Name from exam_add where Subject='"+str(sid)+"'")
    c=cmd.fetchall()
    output += ' <select name="exam" id="exam"  > <option value="">Select</option>'
    for d in c:
        output += '<option value="'+str(d[0])+'">' + d[1] + '</option>'

    output += '</select>'
    return json.dumps({'status': output});



@app.route('/staffviewnotification',methods=['get','post'])
def staffviewnotification():
    cmd.execute("select * from notification")
    b = cmd.fetchall()
    return render_template("staffviewnotification.html",data=b)

@app.route('/applyexam',methods=['get','post'])
def applyexam():
    cmd.execute("select subject.Subject,exam_add.* from exam_add join std_reg on std_reg.course=exam_add.course join subject on exam_add.subject=subject.id and subject.sem=std_reg.sem where std_reg.id='"+str(session['lid'])+"' and exam_add.Exam_id not in( select Exam_id from apply_exam where Std_id='"+str(session['lid'])+"')")
    k = cmd.fetchall()
    return render_template("Apply Exam.html",val=k)

@app.route('/applay_exam1')
def applay_exam1():
    id=request.args.get('id')
    uid=session['lid']
    cmd.execute("insert into apply_exam values(null,'" + str(uid) + "','" + str(id) + "',curdate())")
    conn.commit()
    return  ''' <script>alert('applayed');window.location='applyexam'</script>'''

@app.route('/viewexam',methods=['get','post'])
def viewexam():
    m = cmd.fetchall()
    return render_template("View Exam.html",data=m)




if __name__=='__main__':
    app.run(host='127.0.0.1',debug=True,port=8000)
