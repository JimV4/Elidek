/*3.2*/
/*find the projects(title) that each researcher works at*/
create view v1 as
select r.first_name, r.last_name, p.title
from researchers as r, projects as p, works_at as w
	 where w.researcher_ID = r.researcher_ID and
	 w.project_ID = p.project_ID
     order by r.last_name;

/*find all the projects(title) for each department of ELIDEK*/
create view v2 as
select prg.department, p.title
from projects as p, programs as prg
where p.program_ID = prg.program_ID
order by prg.department;
