/*3.1*/
select * from programs;
select * from projects;

/*----CHECKED----*/
/*find the names and IDs of all researchers that work on project pr1*/
select researchers.researcher_ID, researchers.first_name, researchers.last_name
from works_at, researchers
where researchers.researcher_ID = works_at.researcher_ID and works_at.project_ID = 'pr1';

/*find all the projects(ID and title) in the field of Comp*/
select about.sector, projects.project_ID, projects.title
from about, projects
where about.project_ID = projects.project_ID and about.sector = 'Comp';

/*----------CHECKED-------*/
/*3.2
/*find the projects(title) that each researcher works at*/
create view v1 as
select r.researcher_ID, r.last_name, r.first_name, p.title
from researchers as r, projects as p, works_at as w
	 where w.researcher_ID = r.researcher_ID and
	 w.project_ID = p.project_ID
     order by r.last_name;

select * from v1;

/*-------------CHECKED-------------------------------*/
/*find all the reasearchers that work in every project*/
create view v2 as
select p.title, r.last_name, r.first_name
from researchers as r, projects as p, works_at as w
	 where w.researcher_ID = r.researcher_ID and
	 w.project_ID = p.project_ID
     order by p.title;

select * from v2;
/*3.3*/
/*Sci has interest, find all active projects in Sci field, and find
researchers that works at projects about Sci*/
/*------------------CHECKED--------------------------------------*/
select p.title
from projects as p, about as a
where p.project_ID = a.project_ID and (datediff(p.end_date, current_date) > 0) and (datediff(current_date, p.start_date) > 0) and a.sector = 'C.Science';


/*---------------CHECKED-----------------------------------------*/
select distinct r.first_name, r.last_name
from researchers as r, works_at as w, about as a, projects as p
where r.researcher_ID = w.researcher_ID and
	  p.project_ID = w.project_ID and
      p.project_ID = a.project_ID and
      a.project_ID = w.project_ID and (((datediff(p.end_date, current_date) > 0) and (datediff(current_date, p.start_date) > 0)) or (datediff(current_date, p.end_date) < 365)) and
      a.sector = 'C.Science';

/*3.4*/
/*which organizations manage the same number of projects with at
least 10 projects per year*/

select org1.name, count(p.project_ID) as proj_num
from organization as org1, projects as p1, projects as p2
where p1.org_acronym = org1.org_acronym and p2.org_acronym = org2.org_acronym
	and datediff 0 <= (p1.start_date, p2.start_date) <= 2
proj_num >= 10
group_by org1.org_acronnym;


/*3.5*/
/*---------------------------CHECKED------------------ ?? periptwsh isopsifias*/
with help(sector1, sector2, value) as
(select a1.sector, a2.sector, count(*) as "count"
from about as a1, about as a2
where a1.project_ID = a2.project_ID and a1.sector <> a2.sector
	  and a1.sector < a2.sector
group by a1.sector, a2.sector
order by count*(-1) limit 3)
select sector1, sector2 from help;



/*3.6*/
/*find young researchers(age < 40) who work at most projects and
the number of projects they work at*/
/*---------------CHECKED---------------------------*/
with help(researcher_ID, last_name, first_name, value) as
(select r.researcher_ID, r.last_name, r.first_name, count(w.project_ID) as "proj_num"
from researchers as r, works_at as w, projects as p
where r.researcher_ID = w.researcher_ID and p.project_ID = w.project_ID
		and (datediff(p.end_date, current_date) > 0) and (datediff(current_date, r.birth_date) < 14600)
group by r.last_name, r.first_name, r.researcher_ID)
select distinct h1.researcher_ID, h1.last_name, h1.first_name, h1.value
from help as h1, help as h2
where h1.value > h2.value;


/*find the top5 executives(name, name of company, total amount)
 that have given the biggest ammount of money to a company*/

 select e.name, o.name, sum(p.amount) as total_amount
 from executives as e, projects as p, organizations as o
 where e.exec_ID = p.exec_ID and
	   o.org_acronym = p.org_acronym and
	   o.category = 'Company'
	   group by o.name, e.name
	   having total_amount = max(total_amount) limit 5;

 /*find the names and the number of projects of all researchers
 that works on projects that not have deliverables*/
select distinct w.project_ID
from researchers as r, works_at as w, parts as part
where r.researcher_ID = w.researcher_ID and
      w.project_ID not in (select p.project_ID
							from projects as p, parts as par
                            where p.project_ID = par.project_ID);

/*3.7*/
/*-----------------------------CHECKED---------------------*/
with help(v1, v2, first_name, last_name, company_name, amount) as
(select p.project_ID, e.exec_ID, e.first_name, e.last_name, o.name, p.amount
from executives as e, organizations as o, projects as p
where p.exec_ID = e.exec_ID and p.org_acronym = o.org_acronym
	  and o.category = 'Comp'
order by amount*(-1))
select first_name, last_name, company_name, amount
from help
where amount in (select max(amount)
				 from help
                 group by v2) limit 5;







/*3.8*/
/*find the researchers that work on 5(2) or more projects
that dont have deliverables(name and number of projects)*/
/*---------------CHECKED------------------------------------*/
/*select r.researcher_ID, r.first_name, r.last_name, count(w.project_ID) as "proj_num"
from researchers as r, works_at as w
where r.researcher_ID = w.researcher_ID and
      w.project_ID not in (select p.project_ID
						   from projects as p, reports as rep
                           where p.project_ID = rep.project_ID)
group by r.first_name, r.last_name, r.researcher_ID
having proj_num >= 2
order by r.researcher_ID;*/
