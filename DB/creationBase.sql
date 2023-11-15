CREATE TABLE formation (
    id_formation INT AUTO_INCREMENT,
    nom VARCHAR(255),
    promotion VARCHAR(255),
    PRIMARY KEY (id_formation),
    UNIQUE KEY unique_nom_promotion (nom, promotion)
);

CREATE TABLE student (
    id_student INT AUTO_INCREMENT,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    age int,
    PRIMARY KEY (id_student)
);

ALTER TABLE student
ADD CONSTRAINT uc_nom_prenom_age UNIQUE (nom, prenom, age);

CREATE TABLE resultats (
    periodstr VARCHAR(255),
    nom VARCHAR(255) NOT NULL ,
    prenom VARCHAR(255) NOT NULL ,
    note int NOT NULL ,
    PRIMARY KEY (periodstr,nom,prenom,note)
);

CREATE TABLE resultats (
    periodstr VARCHAR(255),
    nom VARCHAR(255) NOT NULL ,
    prenom VARCHAR(255) NOT NULL ,
    note int NOT NULL ,
    PRIMARY KEY (periodstr,nom,prenom,note)
);

CREATE  TABLE moyennes(
    id_student INT,
    periodstr VARCHAR(255),
    moyenne FLOAT,
    date_calcul DATE,
    FOREIGN KEY (id_student) REFERENCES student(id_student),
    PRIMARY KEY (id_student,periodstr)
)