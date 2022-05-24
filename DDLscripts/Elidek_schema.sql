
create table organizations (
		org_acronym		varchar(20),
  	category		varchar(50),
    name			varchar(20),
		street			varchar(20),
		street_number	varchar(5),
		postal_code		char(5),
		city			varchar(20),
    primary key (org_acronym));

/*create table company
	org_acronym		varchar(20),
	own_capital		int,

	primary key (org_acronym),
	foreign key (org_acronym) references organizations(org_acronym));

create table university
	org_acronym		varchar(20),
	fund_fom_min	int,

	primary key (org_acronym),
	foreign key (org_acronym) references organizations(org_acronym));

create table research_centre
	org_acronym		varchar(20),
	fund_fom_min	int,
	fund_from_other	int,

	primary key (org_acronym),
	foreign key (org_acronym) references organizations(org_acronym));*/


create table org_phone (
	org_acronym		varchar(20),
	phone_number	char(10),

	primary key (org_acronym, phone_number),
	foreign key (org_acronym) references organizations(org_acronym));

create table programs (
		program_ID		varchar(20),
    department		varchar(20),
    primary key (program_ID));

create table executives (
		exec_ID			varchar(5),
		first_name		varchar(20),
		last_name		varchar(20),
    primary key (exec_ID));

create table fields (
		sector varchar(50),

    primary key(sector));


create table researchers (
		researcher_ID	varchar(5),
    first_name		varchar(20),
		last_name		varchar(20),
    sex				char   (1), check (sex in ('M', 'F')),
    birth_date		date,
    org_acronym		varchar(20),
    start_date		date,

    primary key (researcher_ID),
    foreign key (org_acronym) references organizations(org_acronym));

create table projects (
		project_ID	varchar(5),
    title	 	varchar(20),
    abstract 	varchar(1024),
		start_date  date,
		end_date    date,
    duration 	numeric(2, 1)  check (duration > 0.9 and duration < 4.1),
    amount	 	int 		   check (amount > 0),
    org_acronym	varchar(20),
    program_ID	varchar(5),
    exec_ID		varchar(5),
		supervisor_ID varchar(5),
		evaluator_ID varchar(5),

    primary key (project_ID),
    foreign key (program_ID)  	references programs(program_ID),
    foreign key (exec_ID) 	  	references executives(exec_ID),
    foreign key (org_acronym) 	references organizations(org_acronym),
    foreign key (supervisor_ID) references researchers(researcher_ID),
		foreign key (evaluator_ID)  references researchers(researcher_ID));

create table reports (
		project_ID	varchar(5),
		title		varchar(20),
    summary 	varchar(50),
    primary key(project_ID, title));


create table about (
		project_ID	varchar(5),
    sector 		varchar(50),

    primary key (project_ID, sector),
		foreign key (project_ID)	references projects(project_ID),
    foreign key (sector) 		references fields(sector));

create table works_at (
		researcher_ID	varchar(5),
    project_ID		varchar(5),
    primary key (researcher_ID, project_ID),
    foreign key (researcher_ID) references researchers(researcher_ID),
    foreign key (project_ID) 	references projects(project_ID));


/*create table supervisor (
	project_ID		varchar(50),
    researcher_ID	varchar(50),
	primary key (project_ID, researcher_ID),
    foreign key (project_ID) references projects(project_ID),
    foreign key (researcher_ID) references researchers(researcher_ID));

create table evaluation (
	project_ID		varchar(50),
    researcher_ID	varchar(50),
    date			varchar(50),
    mark			int,
    primary key (project_ID, researcher_ID, date, mark),
    foreign key (project_ID) references projects(project_ID),
    foreign key (researcher_ID) references researchers(researcher_ID));*/
