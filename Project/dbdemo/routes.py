from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_mysqldb import MySQL
from dbdemo import app, db
from dbdemo.forms import ResearchersForm


from datetime import datetime

def getDuration(start, end):
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")
    days = abs((start - end).days)
    return str(round(days/365, 1))

@app.route("/")
def index():
    try:
        ## create connection to the database
        #conn = db.connect()
        #cur = conn.cursor()
        cur = db.connection.cursor()


        return render_template("landing.html") #pageTitle = "Landing Page")
    except Exception as e:
        print(e)
        return render_template("landing.html") #pageTitle = "Landing Page")

#INSERTS

@app.route("/create/insert_about", methods = [ "POST"]) ## "GET" by default
def create_about():

    ## form = StudentForm()
    ## when the form is submitted
    id = request.form['id']

    sector = request.form['sector']

    # newStudent = form.__dict__
    query = "insert into about(project_iD, sector) values(\""+id+"\", \""+sector+"\" );"
    print(query)

    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("About inserted successfully", "success")
        return redirect(url_for("create_about"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("insert_about.html", pageTitle = "Create About")

@app.route("/create/insert_phone", methods = [ "POST"]) ## "GET" by default
def create_phone():

    ## form = StudentForm()
    ## when the form is submitted
    org = request.form['org']

    phone = request.form['phone']

    # newStudent = form.__dict__
    query = "insert into org_phone(org_acronym, phone_number) values(\""+org+"\", \""+phone+"\" );"
    print(query)

    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Phone inserted successfully", "success")
        return redirect(url_for("create_phone"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("insert_phone.html", pageTitle = "Create About")

@app.route("/create/insert_report", methods = [ "POST"]) ## "GET" by default
def create_report():

    ## form = StudentForm()
    ## when the form is submitted
    id = request.form['id']
    title = request.form['title']
    sum = request.form['sum']

    # newStudent = form.__dict__
    query = "insert into reports(project_iD, title, summary) values(\""+id+"\", \""+title+"\", \""+sum+"\" );"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Report inserted successfully", "success")
        return redirect(url_for("create_report"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("insert_report.html", pageTitle = "Create About")


@app.route("/create/insert_executives", methods = [ "POST"]) ## "GET" by default
def create_exec():

    ## form = StudentForm()
    ## when the form is submitted
    id = request.form['id']

    name = request.form['name']

    last_name = request.form['last_name']

    # newStudent = form.__dict__
    query = "insert into executives(exec_ID, first_name, last_name) values(\""+id+"\", \""+name+"\", \""+ last_name +"\" );"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Executive inserted successfully", "success")
        return redirect(url_for("create_exec"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("insert_executives.html", pageTitle = "Create About")

@app.route("/create/insert_fields", methods = [ "POST"]) ## "GET" by default
def create_filed():

    ## form = StudentForm()
    ## when the form is submitted
    sector = request.form['sector']


    # newStudent = form.__dict__
    query = "insert into fields(sector) values(\""+sector+"\" );"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Field inserted successfully", "success")
        return redirect(url_for("create_field"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("insert_fields.html", pageTitle = "Create About")

@app.route("/create/insert_programs", methods = [ "POST"]) ## "GET" by default
def create_program():

    ## form = StudentForm()
    ## when the form is submitted
    id = request.form['id']
    dep = request.form['dep']


    # newStudent = form.__dict__
    query = "insert into programs(program_ID, department) values(\""+id+"\", \""+dep+"\" );"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Program inserted successfully", "success")
        return redirect(url_for("create_program"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("insert_programs.html", pageTitle = "Create About")


@app.route("/create/insert_works_at", methods = [ "POST"]) ## "GET" by default
def create_works_at():

    ## form = StudentForm()
    ## when the form is submitted
    rid = request.form['rid']
    pid = request.form['pid']


    # newStudent = form.__dict__
    query = "insert into works_at(researcher_ID, project_ID) values(\""+rid+"\", \""+pid+"\" );"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Works_at inserted successfully", "success")
        return redirect(url_for("create_works_at"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("insert_works_at.html", pageTitle = "Create About")

@app.route("/create/insert_researchers", methods = [ "POST"]) ## "GET" by default
def create_res():

    ## form = StudentForm()
    ## when the form is submitted
    id = request.form['id']
    fname = request.form['fname']
    lname =request.form['lname']
    sex = request.form['sex']
    date_birth = request.form['date_birth']
    org = request.form['org']
    work_date = request.form ['work_date']


    # newStudent = form.__dict__
    query = "insert into researchers(researcher_ID, first_name, last_name, sex, birth_date, org_acronym, start_date) values(\""+id+"\", \""+fname+"\", \""+lname+"\", \""+sex+"\", \""+date_birth+"\", \""+org+"\", \""+work_date+"\" );"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Researcher inserted successfully", "success")
        return redirect(url_for("create_res"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("insert_researchers.html", pageTitle = "Create About")


@app.route("/create/insert_organization", methods = [ "POST"]) ## "GET" by default
def create_org():
    ## form = StudentForm()
    ## when the form is submitted
    org = request.form['org']
    categ = request.form['categ']
    name =request.form['name']
    street = request.form['street']
    str_number = request.form['strnumber']
    postal = request.form['postal']
    city = request.form ['city']
    equity = request.form ['equity']
    ffm = request.form ['ffm']
    ffa = request.form ['ffa']
    if (categ == "Univ"):
        equity = "NULL"
        ffa = "NULL"

    if (categ == "Centr"):
        equity = "NULL"

    if (categ == "Comp"):
        ffm = "NULL"
        ffa = "NULL"


    phone1=request.form['phone1']
    phone2=request.form['phone2']


    # newStudent = form.__dict__
    query1 ="insert into organizations(org_acronym, category, name, street, street_number, postal_code, city, equity, funds_from_ministry,funds_from_actions) values(\""+org+"\", \""+categ+"\", \""+name+"\", \""+street+"\", \""+str_number+"\", \""+postal+"\", \""+city+"\", "+equity+", "+ffm+", "+ffa+");"
    query2 ="insert into org_phone(org_acronym, phone_number) values(\""+org+"\", \""+phone1+"\");"
    query3 ="insert into org_phone(org_acronym, phone_number) values(\""+org+"\", \""+phone2+"\");"
    print(query1)
    print(query2)
    print(query3)
    try:
        cur = db.connection.cursor()
        cur.execute(query1)
        cur.execute(query2)
        cur.execute(query3)
        db.connection.commit()
        cur.close()
        flash("Organization inserted successfully", "success")
        return redirect(url_for("create_organization"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")


    ## else, response for GET request
    return render_template("insert_organization.html", pageTitle = "Create About")


@app.route("/create/insert_projects", methods = [ "POST"]) ## "GET" by default
def create_proj():

    ## form = StudentForm()
    ## when the form is submitted
    id = request.form['id']
    title = request.form['title']
    abs =request.form['abs']
    sdate = request.form['sdate']
    edate = request.form['edate']
    amount = request.form['amount']
    org = request.form ['org']
    prog = request.form['prog']
    exec =request.form['exec']
    sup = request.form['sup']
    eval = request.form['eval']
    mark=request.form['mark']
    eval_date=request.form['eval_date']

    duration =  getDuration(sdate, edate)

    # newStudent = form.__dict__
    query = "insert into projects(project_ID, title, abstract, start_date, end_date, duration, amount, org_acronym, program_ID, exec_ID, supervisor_ID, evaluator_ID, eval_mark, eval_date) values(\""+id+"\", \""+title+"\", \""+abs+"\", \""+sdate+"\", \""+edate+"\", "+duration+", "+amount+", \""+org+"\", \""+prog+"\", \""+exec+"\", \""+sup+"\", \""+eval+"\", "+mark+", \""+eval_date+"\" );"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Project inserted successfully", "success")
        return redirect(url_for("create_proj"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("insert_projects.html", pageTitle = "Create About")


#QUERIES
@app.route("/read/query1", methods = ["POST"])
def complicated_query():
    try:
        ## execute query 3
        #conn = db.connect()
        #cur = conn.cursor()
        sdate=request.form['sdate']
        pr = request.form['project']
        edate=request.form['edate']
        duration=request.form['duration']
        exec_id=request.form['exec_id']

        count_conditions = 0
        if(sdate==""):
            sdate_cond = ""
        else:
            sdate_cond = " start_date = " +"\"" + sdate+ "\"and"
            count_conditions = count_conditions + 1

        if(edate==""):
            edate_cond = ""
        else:
            edate_cond = " end_date = " +"\"" + edate+ "\"and"
            count_conditions = count_conditions + 1


        if(duration==""):
            duration_cond = ""
        else:
            duration_cond = " duration = " + duration+ "and"
            count_conditions = count_conditions + 1

        if(exec_id==""):
            exec_id_cond = ""
        else:
            exec_id_cond = " exec_ID = " +"\"" + exec_id+ "\"and"
            count_conditions = count_conditions + 1

        if(count_conditions == 0):
            where = ""
        else:
            where = " where"

        cur = db.connection.cursor()

        if(pr != ""):
            query1="select r.first_name, r.last_name from works_at as w, researchers as r where  w.researcher_ID = r.researcher_ID and w.project_ID = \""+pr+"\";"
        else:
            Query1="select title, program_ID from projects "+where+sdate_cond+edate_cond+duration_cond+exec_id_cond+";"
            query1=Query1.replace("and;", ';')
        print(query1)
        cur.execute(query1)

        #cur.execute("SELECT researcher_ID, last_name, first_name FROM researchers")
        column_names = [i[0] for i in cur.description]
        #res = dict(zip(column_names, cur.fetchone()))
        projects = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        if(pr==""):
            return render_template("result_query1.html", projects = projects, pageTitle = "Fields Page")
        else:
            return render_template("result_query1_res.html", projects = projects, pageTitle = "Fields Page")



    except Exception as e:
        print(e)
        #if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/read/query2/view1", methods = ["GET"])
def view1():
    try:

        cur = db.connection.cursor()

        view1 = "select * from v1;"
        cur.execute(view1)

        column_names = [i[0] for i in cur.description]
        #res = dict(zip(column_names, cur.fetchone()))
        researchers = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("view1.html", researchers = researchers, pageTitle = "View 1")

    except Exception as e:
        print(e)
        #if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)


@app.route("/read/query2/view2", methods = ["GET"])
def view2():
    try:

        cur = db.connection.cursor()

        view2 = "select * from v2;"
        cur.execute(view2)

        column_names = [i[0] for i in cur.description]
        #res = dict(zip(column_names, cur.fetchone()))
        researchers = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        #projects = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("view2.html", researchers = researchers, pageTitle = "View 2")

    except Exception as e:
        print(e)
        #if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)


@app.route("/read/query3", methods = ["POST"])
def field_in_intrest():
    try:
        ## execute query 3
        #conn = db.connect()
        #cur = conn.cursor()
        sector = request.form['sector']
        cur = db.connection.cursor()

        query3="select distinct r.first_name, r.last_name from researchers as r, works_at as w, about as a, projects as p where r.researcher_ID = w.researcher_ID and p.project_ID = w.project_ID and   p.project_ID = a.project_ID and a.project_ID = w.project_ID and (((datediff(p.end_date, current_date) > 0) and (datediff(current_date, p.start_date) > 0)) or (datediff(current_date, p.end_date) < 365)) and a.sector = \'" +sector+"\';"
        cur.execute(query3)

        #cur.execute("SELECT researcher_ID, last_name, first_name FROM researchers")
        column_names = [i[0] for i in cur.description]
        #res = dict(zip(column_names, cur.fetchone()))
        fields = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("result_query3.html", fields = fields, pageTitle = "Fields Page")

    except Exception as e:
        print(e)
        #if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)


@app.route("/read/query5", methods = ["GET"])
def pairFields():
    try:
        ## execute query 5
        #conn = db.connect()
        #cur = conn.cursor()
        cur = db.connection.cursor()


        cur.execute('''with help(sector1, sector2, value) as
                    (select a1.sector, a2.sector, count(*) as "count"
                    from about as a1, about as a2
                    where a1.project_ID = a2.project_ID and a1.sector <> a2.sector
                    and a1.sector < a2.sector
                    group by a1.sector, a2.sector
                    order by count*(-1) limit 3)
                    select sector1, sector2 from help;''')

        #cur.execute("SELECT researcher_ID, last_name, first_name FROM researchers")
        column_names = [i[0] for i in cur.description]
        #res = dict(zip(column_names, cur.fetchone()))
        fields = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("query5.html", fields = fields, pageTitle = "Fields Page")

    except Exception as e:
        print(e)
        #if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/read/query6", methods = ["GET"])
def youngResearchers():
    try:
        form = ResearchersForm()
        ## execute query 6
        #conn = db.connect()
        #cur = conn.cursor()
        cur = db.connection.cursor()


        cur.execute('''with help(researcher_ID, last_name, first_name, value) as
                   (select r.researcher_ID, r.last_name, r.first_name, count(w.project_ID) as "proj_num"
                    from researchers as r, works_at as w, projects as p
                    where r.researcher_ID = w.researcher_ID and p.project_ID = w.project_ID
                    and (datediff(p.end_date, current_date) > 0) and (datediff(current_date, r.birth_date) < 14600)
                    group by r.last_name, r.first_name, r.researcher_ID)
                    select distinct h1.researcher_ID, h1.last_name, h1.first_name, h1.value
                    from help as h1, help as h2
                    where h1.value > h2.value;''')

        #cur.execute("SELECT researcher_ID, last_name, first_name FROM researchers")
        column_names = [i[0] for i in cur.description]
        #res = dict(zip(column_names, cur.fetchone()))
        researchers = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("query6.html", researchers = researchers, pageTitle = "Researchers Page", form = form)

    except Exception as e:
        print(e)
        #if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/read/query7", methods = ["GET"])
def topExec():
    try:
        ## execute query 7

        cur = db.connection.cursor()


        cur.execute('''with help(v1, v2, first_name, last_name, company_name, amount) as
                    (select p.project_ID, e.exec_ID, e.first_name, e.last_name, o.name, p.amount
                    from executives as e, organizations as o, projects as p
                    where p.exec_ID = e.exec_ID and p.org_acronym = o.org_acronym
                    and o.category = 'Comp'
                    order by amount*(-1))
                    select first_name, last_name, company_name, amount
                    from help
                    where amount in (select max(amount)
				    from help
                    group by v2) limit 5;''')

        #cur.execute("SELECT researcher_ID, last_name, first_name FROM researchers")
        column_names = [i[0] for i in cur.description]
        #res = dict(zip(column_names, cur.fetchone()))
        exec = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("query7.html", exec = exec, pageTitle = "Top Executives")

    except Exception as e:
        print(e)
        #if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)


@app.route("/read/query8", methods = ["GET"])
def researchNoReports():
    try:
        ## execute query 7

        cur = db.connection.cursor()


        cur.execute('''select r.researcher_ID, r.first_name, r.last_name, count(w.project_ID) as "proj_num"
                       from researchers as r, works_at as w
                       where r.researcher_ID = w.researcher_ID and
                       w.project_ID not in (select p.project_ID
        						from projects as p, reports as rep
                                where p.project_ID = rep.project_ID)
                                group by r.first_name, r.last_name, r.researcher_ID
                                having proj_num >= 2
                                order by r.researcher_ID;''')

        #cur.execute("SELECT researcher_ID, last_name, first_name FROM researchers")
        column_names = [i[0] for i in cur.description]
        #res = dict(zip(column_names, cur.fetchone()))
        researchers = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("query8.html", researchers = researchers, pageTitle = "Researchers in Projects with no reports")

    except Exception as e:
        print(e)
        #if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)



@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/read")
def read():
    return render_template("read.html")

@app.route("/update")
def update():
    return render_template("update.html")

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/create/insert_organization")
def insert_organization():
    return render_template("insert_organization.html")

@app.route("/create/insert_phone")
def insert_phone():
    return render_template("insert_phone.html")

@app.route("/create/insert_programs")
def insert_programs():
    return render_template("insert_programs.html")

@app.route("/create/insert_executives")
def insert_executives():
    return render_template("insert_executives.html")

@app.route("/create/insert_fields")
def insert_fields():
    return render_template("insert_fields.html")

@app.route("/create/insert_researchers")
def insert_researchers():
    return render_template("insert_researchers.html")

@app.route("/create/insert_projects")
def insert_projects():
    return render_template("insert_projects.html")

@app.route("/create/insert_works_at")
def insert_works_at():
    return render_template("insert_works_at.html")

@app.route("/create/insert_about")
def insert_about():
    return render_template("insert_about.html")

@app.route("/create/insert_report")
def insert_report():
    return render_template("insert_report.html")


@app.route("/read/query1")
def query1():
    return render_template("query1.html")

@app.route("/read/query2")
def query2():
    return render_template("query2.html")

@app.route("/read/query3")
def query3():
    return render_template("query3.html")



#DELETES

@app.route("/delete/delete_organization")
def delete_org():
    return render_template("delete_organization.html")

@app.route("/delete/delete_organization", methods = [ "POST"]) ## "GET" by default
def Delete_org():

    ## form = StudentForm()
    ## when the form is submitted
    id = request.form['id']
    # newStudent = form.__dict__
    query = "delete from organizations where org_acronym = \""+id+"\";"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Organization deleted successfully", "success")
        return redirect(url_for("Delete_org"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("delete_organization.html", pageTitle = "Create About")

@app.route("/delete/delete_about")
def delete_about():
    return render_template("delete_about.html")

@app.route("/delete/delete_about", methods = [ "POST"]) ## "GET" by default
def Delete_about():

    ## form = StudentForm()
    ## when the form is submitted
    id = request.form['id']

    sector = request.form['sector']

    # newStudent = form.__dict__
    query = "delete from about where project_ID = \""+id+"\" and sector = \""+sector+"\";"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("About deleted successfully", "success")
        return redirect(url_for("Delete_about"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("delete_about.html", pageTitle = "Create About")


@app.route("/delete/delete_phone")
def delete_phone():
    return render_template("delete_phone.html")

@app.route("/delete/delete_phone", methods = [ "POST"]) ## "GET" by default
def Delete_phone():

    ## form = StudentForm()
    ## when the form is submitted
    org = request.form['org']

    phone = request.form['phone']

    # newStudent = form.__dict__
    query = "delete from org_phone where org_acronym = \""+org+"\" and phone_number = \""+phone+"\";"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Phone deleted successfully", "success")
        return redirect(url_for("Delete_phone"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("delete_phone.html", pageTitle = "Create About")

@app.route("/delete/delete_programs")
def delete_programs():
    return render_template("delete_programs.html")

@app.route("/delete/delete_programs", methods = [ "POST"]) ## "GET" by default
def Delete_program():

    ## form = StudentForm()
    ## when the form is submitted
    id = request.form['id']
    # newStudent = form.__dict__
    query = "delete from programs where program_ID = \""+id+"\";"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Program deleted successfully", "success")
        return redirect(url_for("Delete_program"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("delete_programs.html", pageTitle = "Create About")

@app.route("/delete/delete_executives")
def delete_executives():
    return render_template("delete_executives.html")

@app.route("/delete/delete_executives", methods = [ "POST"]) ## "GET" by default
def Delete_exec():

    ## form = StudentForm()
    ## when the form is submitted
    id = request.form['id']
    # newStudent = form.__dict__
    query = "delete from executives where exec_ID = \""+id+"\";"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Executive deleted successfully", "success")
        return redirect(url_for("Delete_exec"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("delete_executives.html", pageTitle = "Create About")

@app.route("/delete/delete_fields")
def delete_fields():
    return render_template("delete_fields.html")

@app.route("/delete/delete_fields", methods = [ "POST"]) ## "GET" by default
def Delete_fields():

    ## form = StudentForm()
    ## when the form is submitted
    id = request.form['id']
    # newStudent = form.__dict__
    query = "delete from fields where sector = \""+id+"\";"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Field deleted successfully", "success")
        return redirect(url_for("Delete_fields"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("delete_fields.html", pageTitle = "Create About")

@app.route("/delete/delete_works_at")
def delete_works_at():
    return render_template("delete_works_at.html")


@app.route("/delete/delete_works_at", methods = [ "POST"]) ## "GET" by default
def Delete_works_at():

    ## form = StudentForm()
    ## when the form is submitted
    pid = request.form['pid']

    rid = request.form['rid']

    # newStudent = form.__dict__
    query = "delete from works_at where project_ID = \""+pid+"\" and researcher_ID = \""+rid+"\";"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Work_at deleted successfully", "success")
        return redirect(url_for("Delete_works_at"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("delete_works_at.html", pageTitle = "Create About")


@app.route("/delete/delete_projects")
def delete_projects():
    return render_template("delete_projects.html")

@app.route("/delete/delete_projects", methods = [ "POST"]) ## "GET" by default
def Delete_proj():

    ## form = StudentForm()
    ## when the form is submitted
    id = request.form['id']
    # newStudent = form.__dict__
    query = "delete from projects where project_ID = \""+id+"\";"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Project deleted successfully", "success")
        return redirect(url_for("Delete_proj"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("delete_projects.html", pageTitle = "Create About")

@app.route("/delete/delete_report")
def delete_report():
    return render_template("delete_report.html")

@app.route("/delete/delete_report", methods = [ "POST"]) ## "GET" by default
def Delete_report():

    ## form = StudentForm()
    ## when the form is submitted
    id = request.form['id']
    title = request.form['title']
    # newStudent = form.__dict__
    query = "delete from reports where project_ID = \""+id+"\" and title = \""+title+"\";"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Report deleted successfully", "success")
        return redirect(url_for("Delete_report"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("delete_report.html", pageTitle = "Create About")

@app.route("/delete/delete_researchers")
def delete_researchers():
    return render_template("delete_researchers.html")

@app.route("/delete/delete_researchers", methods = [ "POST"]) ## "GET" by default
def Delete_researcher():

    ## form = StudentForm()
    ## when the form is submitted
    id = request.form['id']
    # newStudent = form.__dict__
    query = "delete from researchers where researcher_ID = \""+id+"\";"
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Researcher deleted successfully", "success")
        return redirect(url_for("Delete_researcher"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("delete_researchers.html", pageTitle = "Create About")


#UPDATES

@app.route("/update/update_executives")
def update_executives():
    return render_template("update_executives.html")

@app.route("/update/update_executives", methods = ["POST"])
def Update_executives():
    id = request.form['id']
    first_name = request.form['name']
    last_name = request.form['last_name']

    if(first_name == ""):
        first_name_cond=""
    else:
        first_name_cond = " first_name = \""+first_name+"\","

    if(last_name == ""):
        last_name_cond=""
    else:
        last_name_cond = " last_name = \""+last_name+"\","

    set = "set"+first_name_cond+last_name_cond

    # newStudent = form.__dict__
    Query = "update executives "+set+" where exec_ID = \""+id+"\";"
    query = Query.replace(", where", " where")
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Executive updated successfully", "success")
        return redirect(url_for("Update_executives"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("update_executives.html", pageTitle = "Create About")

@app.route("/update/update_programs")
def update_programs():
    return render_template("update_programs.html")

@app.route("/update/update_programs", methods = ["POST"])
def Update_programs():

    id = request.form['id']
    dep = request.form['dep']

    if(dep == ""):
        dep_cond=""
    else:
        dep_cond = " department = \""+dep+"\","


    set = "set"+dep_cond

    # newStudent = form.__dict__
    Query = "update programs "+set+" where program_ID = \""+id+"\";"
    query = Query.replace(", where", " where")
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Program updated successfully", "success")
        return redirect(url_for("Update_programs"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("update_programs.html", pageTitle = "Create About")


@app.route("/update/update_researchers")
def update_researchers():
    return render_template("update_researchers.html")

@app.route("/update/update_researchers", methods = ["POST"])
def Update_researchers():

    id = request.form['id']
    fname = request.form['fname']
    lname =request.form['lname']
    sex = request.form['sex']
    date_birth = request.form['date_birth']
    org = request.form['org']
    work_date = request.form ['work_date']

    if(fname == ""):
        fname_cond=""
    else:
        fname_cond = " first_name = \""+fname+"\","

    if(lname == ""):
        lname_cond=""
    else:
        lname_cond = " last_name = \""+lname+"\","

    if(sex == ""):
        sex_cond=""
    else:
        sex_cond = " sex = \""+sex+"\","

    if(date_birth == ""):
        date_birth_cond=""
    else:
        date_birth_cond = " birth_date = \""+date_birth+"\","

    if(org == ""):
        org_cond=""
    else:
        org_cond = " org_acronym = \""+org+"\","

    if(work_date == ""):
        work_date_cond=""
    else:
        work_date_cond = " start_date = \""+work_date+"\","

    set = "set"+fname_cond+lname_cond+sex_cond+date_birth_cond+org_cond+work_date_cond

    # newStudent = form.__dict__
    Query = "update researchers "+set+" where researcher_ID = \""+id+"\";"
    query = Query.replace(", where", " where")
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Researcher updated successfully", "success")
        return redirect(url_for("Update_researchers"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("update_researchers.html", pageTitle = "Create About")

@app.route("/update/update_projects")
def update_projects():
    return render_template("update_projects.html")

@app.route("/update/update_projects", methods = ["POST"])
def Update_projects():

    id = request.form['id']
    title = request.form['title']
    abs =request.form['abs']
    sdate = request.form['sdate']
    edate = request.form['edate']
    amount = request.form['amount']
    org = request.form ['org']
    prog = request.form['prog']
    exec =request.form['exec']
    sup = request.form['sup']
    eval = request.form['eval']
    mark = request.form['mark']
    eval_date = request.form['eval_date']

    if(title == ""):
        title_cond=""
    else:
        title_cond = " title = \""+title+"\","

    if(abs == ""):
        abs_cond=""
    else:
        abs_cond = " abstract = \""+abs+"\","

    if(sdate == ""):
        sdate_cond=""
    else:
        sdate_cond = " start_date = \""+sdate+"\","

    if(edate == ""):
        edate_cond=""
    else:
        edate_cond = " end_date = \""+edate+"\","

    if(edate == ""):
        duration_cond=""
    else:
        duration_cond = " duration = \""+getDuration(sdate, edate)+"\","

    if(amount == ""):
        amount_cond=""
    else:
        amount_cond = " amount = \""+amount+"\","

    if(org == ""):
        org_cond=""
    else:
        org_cond = " org_acronym = \""+org+"\","

    if(prog == ""):
        prog_cond=""
    else:
        prog_cond = " program_ID = \""+prog+"\","

    if(exec == ""):
        exec_cond=""
    else:
        exec_cond = " exec_ID = \""+exec+"\","

    if(sup == ""):
        sup_cond=""
    else:
        sup_cond = " supervisor_ID = \""+sup+"\","

    if(eval == ""):
        eval_cond=""
    else:
        eval_cond = " evaluator_ID = \""+eval+"\","

    if(mark == ""):
        mark_cond=""
    else:
        mark_cond = " eval_mark = "+mark+","

    if(eval_date == ""):
        eval_date_cond=""
    else:
        eval_date_cond = " eval_date = \""+eval_date+"\","

    set = "set"+title_cond+abs_cond+sdate_cond+edate_cond+duration_cond+amount_cond+org_cond+prog_cond+exec_cond+sup_cond+eval_cond+mark_cond+eval_date_cond

    # newStudent = form.__dict__
    Query = "update projects "+set+" where project_ID = \""+id+"\";"
    query = Query.replace(", where", " where")
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Project updated successfully", "success")
        return redirect(url_for("Update_projects"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("update_projects.html", pageTitle = "Create About")


@app.route("/update/update_report")
def update_report():
    return render_template("update_report.html")

@app.route("/update/update_report", methods = ["POST"])
def Update_report():

    id = request.form['id']
    title = request.form['title']
    sum = request.form['sum']

    if(sum == ""):
        sum_cond=""
    else:
        sum_cond = " summary = \""+sum+"\","


    set = "set"+sum_cond

    # newStudent = form.__dict__
    Query = "update reports "+set+" where project_ID = \""+id+"\" and title = \""+title+"\";"
    query = Query.replace(", where", " where")
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Report updated successfully", "success")
        return redirect(url_for("Update_report"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("update_report.html", pageTitle = "Create About")

@app.route("/update/update_organization")
def update_organization():
    return render_template("update_organization.html")

@app.route("/update/update_organization", methods = ["POST"])
def Update_organization():

    org = request.form['org']
    categ = request.form['categ']
    name =request.form['name']
    street = request.form['street']
    str_number = request.form['strnumber']
    postal = request.form['postal']
    city = request.form ['city']
    equity = request.form ['equity']
    ffm = request.form ['ffm']
    ffa = request.form ['ffa']

    if (categ == "Univ"):
        equity = "NULL"
        ffa = "NULL"

    if (categ == "Centr"):
        equity = "NULL"

    if (categ == "Comp"):
        ffm = "NULL"
        ffa = "NULL"

    if(categ == ""):
        categ_cond=""
    else:
        categ_cond = " category = \""+categ+"\","

    if(name == ""):
        name_cond=""
    else:
        name_cond = " name = \""+name+"\","

    if(street == ""):
        street_cond=""
    else:
        street_cond = " street = \""+street+"\","

    if(str_number == ""):
        str_number_cond=""
    else:
        str_number_cond = " street_number = \""+str_number+"\","

    if(postal == ""):
        postal_cond=""
    else:
        postal_cond = " postal_code = \""+postal+"\","

    if(city == ""):
        city_cond=""
    else:
        city_cond = " city = \""+city+"\","

    if(equity == ""):
        equity_cond=""
    else:
        equity_cond = " equity = "+equity+","

    if(ffm == ""):
        ffm_cond=""
    else:
        ffm_cond = " funds_from_ministry = "+ffm+","

    if(ffa == ""):
        ffa_cond=""
    else:
        ffa_cond = " funds_from_actions = "+ffa+","

    set = "set"+categ_cond+name_cond+street_cond+str_number_cond+postal_cond+city_cond+equity_cond+ffm_cond+ffa_cond

    # newStudent = form.__dict__
    Query = "update organizations "+set+" where org_acronym = \""+org+"\";"
    query = Query.replace(", where", " where")
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Organization updated successfully", "success")
        return redirect(url_for("Update_organization"))
    except Exception as e: ## OperationalError
        flash(str(e), "danger")

    ## else, response for GET request
    return render_template("update_organization.html", pageTitle = "Create About")
