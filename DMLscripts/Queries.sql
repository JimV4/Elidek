/*3.3*/
/* this query requires user input for the attribute sector. 
This is an example with sector = ‘C.Science’*/
select p.title
from projects as p, about as a
where p.project_ID = a.project_ID and (datediff(p.end_date, current_date) > 0) and (datediff(current_date, p.start_date) > 0) and a.sector = 'C.Science';


select distinct r.first_name, r.last_name
from researchers as r, works_at as w, about as a, projects as p
where r.researcher_ID = w.researcher_ID and
	  p.project_ID = w.project_ID and
      p.project_ID = a.project_ID and
      a.project_ID = w.project_ID and (((datediff(p.end_date, current_date) > 0) and (datediff(current_date, p.start_date) > 0)) or((datediff(current_date, p.end_date) < 365) and (datediff(current_date, p.end_date) > 0))) and
      a.sector = 'C.Science';

/*3.4*/
with help(project_ID, syear, org_acronym) as
(select project_ID,  extract(year from start_date), org_acronym
from projects),

help2(org_acronym, syear, amount) as
(select org_acronym, syear, count(project_ID)  from help
group by org_acronym, syear
order by org_acronym)

select distinct h1.org_acronym from help2 as h1, help2 as h2
where h1.org_acronym = h2.org_acronym and h1.syear = h2.syear + 1 and h1.amount = h2.amount and h1.amount>0;

/*3.5*/
with help(sector1, sector2, value) as
(select a1.sector, a2.sector, count(*) as "count"
from about as a1, about as a2
where a1.project_ID = a2.project_ID and a1.sector <> a2.sector
	  and a1.sector < a2.sector
group by a1.sector, a2.sector
order by count*(-1) limit 3)
select sector1, sector2 from help;



/*3.6*/
with help(researcher_ID, last_name, first_name, value) as
(select r.researcher_ID, r.last_name, r.first_name, count(w.project_ID)
from researchers as r, works_at as w, projects as p
where r.researcher_ID = w.researcher_ID and p.project_ID = w.project_ID
		and (datediff(p.end_date, current_date) > 0) and (datediff(current_date, p.start_date) > 0) and (datediff(current_date, r.birth_date) < 14600)
group by r.last_name, r.first_name, r.researcher_ID),
help2(value) as
(select MAX(value) from help)
select h1.first_name, h1.last_name, h1.value
from help as h1, help2 as h2
where h1.value = h2.value;



/*3.7*/
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
select r.first_name, r.last_name, count(w.project_ID) as "proj_num"
from researchers as r, works_at as w
where r.researcher_ID = w.researcher_ID and
      w.project_ID not in (select p.project_ID
						   from projects as p, reports as rep
                           where p.project_ID = rep.project_ID)
group by r.first_name, r.last_name, r.researcher_ID
having proj_num >= 5
order by r.researcher_ID;





