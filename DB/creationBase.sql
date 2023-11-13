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