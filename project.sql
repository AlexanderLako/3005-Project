create table employee
	(
	 fname			varchar(15) NOT NULL,
	 minit      char(1),
	 lname      varchar(15) NOT NULL,
	 Ssn 				char(9) NOT NULL,
	 Bdate 			DATE,
   address    varchar(30),
   sex        char(1),
   salary     numeric(10, 2),
	 super_ssn	char(9),
	 Dno				INT NOT NULL,
	 primary key (Ssn),
	 foreign key (super_ssn) references employee(Ssn)
	);

  create table department
    (
      dname			varchar(15) UNIQUE NOT NULL,
   	  dnumber		INT,
      mgr_ssn		char(9),
      mgr_start_date DATE,
			primary key (dnumber),
			foreign key (mgr_ssn) references employee
    );

	ALTER TABLE employee
	ADD FOREIGN KEY (Dno) references department;

  create table dept_locations
    (
			   dnumber   INT NOT NULL,
      dlocation varchar(15) NOT NULL,
      primary key (dnumber, dlocation),
      foreign key (dnumber) references department
    );

  create table project
    (pname varchar(15) UNIQUE NOT NULL,
		      pnumber INT NOT NULL,
      plocation varchar(15),
      dnum	INT NOT NULL,
	 primary key (pnumber),
      foreign key (dnum) references department
    );

  create table works_on
    (
      Essn char(9) NOT NULL,
      Pno   INT NOT NULL,
      hours NUMERIC(3, 1) NOT NULL,
      primary key (Essn, Pno),
      foreign key (Essn) references employee,
      foreign key (Pno) references project
    );

  create table dependent
    (
					Essn char(9),
      dependent_name varchar(15) NOT NULL,
			sex char(1),
      bdate DATE,
      relationship varchar(8),
			primary key (Essn, dependent_name),
			foreign key (Essn) references employee
    );
