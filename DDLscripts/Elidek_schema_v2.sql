CREATE SCHEMA elidek;
USE elidek;

drop table if exists organizations;
create table organizations (
	org_acronym		varchar(20),
	category		varchar(50), check (category in ('Centr', 'Univ', 'Comp')),
	name			varchar(60),
	street			varchar(60),
	street_number	varchar(5),
	postal_code		char(5),
	city			varchar(50),
	equity 			    int,	check (equity > 0),
	funds_from_ministry int,	check (funds_from_ministry > 0),
	funds_from_actions  int,	check (funds_from_actions > 0),
	primary key (org_acronym));


drop table if exists org_phone;
create table org_phone (
	org_acronym		varchar(20),
	phone_number	char(10),

	primary key (org_acronym, phone_number),
	foreign key (org_acronym) references organizations(org_acronym)
							  on delete cascade
							  on update cascade);


drop table if exists programs;
create table programs (
	program_ID		varchar(20),
    department		varchar(20),
    primary key (program_ID));


drop table if exists executives;
create table executives (
	exec_ID			varchar(5),
	first_name		varchar(20),
	last_name		varchar(20),
    primary key (exec_ID));


drop table if exists fields;
create table fields (
	sector varchar(50),

    primary key(sector));


drop table if exists researchers;
create table researchers (
	researcher_ID	varchar(5),
    first_name		varchar(20),
	last_name		varchar(20),
    sex				char   (1), check (sex in ('M', 'F')),
    birth_date		date,
    org_acronym		varchar(20),
    start_date		date,

    primary key (researcher_ID),
    foreign key (org_acronym) references organizations(org_acronym)
							  on delete set null
							  on update cascade);


drop table if exists projects;
create table projects (
	project_ID	varchar(5),
    title	 	varchar(50),
    abstract 	varchar(10000),
	start_date  date,
	end_date    date,
    duration 	numeric(2, 1)  check (duration > 0.9 and duration < 4.1),
    amount	 	int 		   check (amount >= 100000 and amount <= 1000000),
    org_acronym	varchar(20),
    program_ID	varchar(5),
    exec_ID		varchar(5),
	supervisor_ID varchar(5),
	evaluator_ID varchar(5),
	eval_mark 	int 	     check (eval_mark >= 0 and eval_mark <= 10),
	eval_date   date,

    primary key (project_ID),
    foreign key (program_ID)  	references programs(program_ID)
								on delete set null
								on update cascade,

    foreign key (exec_ID) 	  	references executives(exec_ID)
								on delete set null
								on update cascade,

    foreign key (org_acronym) 	references organizations(org_acronym)
								on delete set null
								on update cascade,

    foreign key (supervisor_ID) references researchers(researcher_ID)
								on delete set null
								on update cascade,

	foreign key (evaluator_ID)  references researchers(researcher_ID)
								on delete set null
								on update cascade);


drop table if exists reports;
create table reports (
	project_ID	varchar(5),
	title		varchar(50),
    summary 	varchar(5000),
    primary key(project_ID, title),
	foreign key (project_ID) references projects(project_ID)
							 on delete cascade
							 on update cascade);


drop table if exists about;
create table about (
	project_ID	varchar(5),
    sector 		varchar(50),

    primary key (project_ID, sector),
	foreign key (project_ID)	references projects(project_ID)
								on delete cascade
								on update cascade,
    foreign key (sector) 		references fields(sector)
								on delete cascade
								on update cascade);


drop table if exists works_at;
create table works_at (
	researcher_ID	varchar(5),
    project_ID		varchar(5),
    primary key (researcher_ID, project_ID),
    foreign key (researcher_ID) references researchers(researcher_ID)
								on delete cascade
								on update cascade,
    foreign key (project_ID) 	references projects(project_ID)
								on delete cascade
								on update cascade);
