/*check if a researcher works at a project that he evaluates*/
delimiter //
create trigger integrity after insert on works_at
for each row
begin
	declare message_text varchar(20);

	if new.researcher_ID = (select evaluator_ID
								from projects
								where new.project_ID = projects.project_ID)
		
	then 
		signal sqlstate '45000' set message_text = 'Error';
	end if;
end;//


/*create trigger integrity after update on works_at
referencing new row as nrow
for each row
when (nrow.researcher_ID = (select evaluator_ID
							from projects
							where nrow.project_ID = projects.project_ID))
begin atomic
	rollback
end;

/* make sure that when a project is inserted or updated, supervisor works at this project
create trigger existence after insert on projects
referencing new row as nrow
for each row
begin atomic
	insert in works_at values (nrow.project_ID, nrow.supervisor_ID)
end;

create trigger existence after update on projects
referencing new row as nrow
for each row
begin atomic
	insert in works_at values (nrow.project_ID, nrow.supervisor_ID)
end;



