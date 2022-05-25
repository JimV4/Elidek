/*check if a researcher works at a project that he evaluates*/
drop trigger if exists integrity;
delimiter //
create trigger integrity after insert on works_at
for each row
begin
	declare message_text varchar(50);

	if new.researcher_ID = (select evaluator_ID
								from projects
								where new.project_ID = projects.project_ID)
		
	then 
		signal sqlstate '45000' set message_text = 'Error! Researcher = Evaluator';
	end if;
end;//


drop trigger if exists integrity_update;
delimiter //
create trigger integrity_update after update on works_at
for each row
begin
	declare message_text varchar(50);

	if new.researcher_ID = (select evaluator_ID
								from projects
								where new.project_ID = projects.project_ID)
		
	then 
		signal sqlstate '45000' set message_text = 'Error! Researcher = Evaluator';
	end if;
end;//


/*check if the evaluator of project is the same with supervisor*/
drop trigger if exists integrity_projects;
delimiter //
create trigger integrity_projects after insert on projects
for each row
begin
	declare message_text varchar(50);

	if new.supervisor_ID = new.evaluator_ID then 
    
		signal sqlstate '45000' set message_text = 'Error! Evaluator = Supervisor';
        
	end if;
end;//


drop trigger if exists integrity_projects_update;
delimiter //
create trigger integrity_projects_update after update on projects
for each row
begin
	declare message_text varchar(50);

	if new.supervisor_ID = new.evaluator_ID then 
    
		signal sqlstate '45000' set message_text = 'Error! Evaluator = Supervisor';
        
	end if;
end;//



