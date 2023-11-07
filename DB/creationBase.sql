CREATE TABLE formation (
    id_formation INT AUTO_INCREMENT,
    nom VARCHAR(255),
    promotion VARCHAR(255),
    PRIMARY KEY (id_formation),
    UNIQUE KEY unique_nom_promotion (nom, promotion)
);