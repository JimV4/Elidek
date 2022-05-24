/*----------CHECKED-------*/
/*3.2
/*find the projects(title) that each researcher works at*/
create view v1 as
select r.first_name, r.last_name, p.title
from researchers as r, projects as p, works_at as w
	 where w.researcher_ID = r.researcher_ID and
	 w.project_ID = p.project_ID
     order by r.last_name;


/*-------------CHECKED-------------------------------*/
/*find all the reasearchers that work in every project*/
create view v2 as
select p.title, r.first_name, r.last_name
from researchers as r, projects as p, works_at as w
	 where w.researcher_ID = r.researcher_ID and
	 w.project_ID = p.project_ID
     order by p.title;
