create schema testSchema;
use testSchema;

create table researchers (
		researcher_ID	varchar(5),
    first_name		varchar(20),
		last_name		varchar(20),
    sex				char   (1), check (sex in ('M', 'F')),
    birth_date		date,
    org_acronym		varchar(20),
    start_date		date,

    primary key (researcher_ID));


insert into researchers values ('123', 'Giannis', 'Rokomos', 'M', '2001-03-01', 'Org1', '2022-05-05');
