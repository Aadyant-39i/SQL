-- database: :memory:
CREATE TABLE supplier (
    SNO TEXT PRIMARY KEY, 
    SNAME TEXT,
    STATUS INTEGER,
    CITY TEXT
);

INSERT INTO supplier (SNO, SNAME, STATUS, CITY) VALUES
("S1", "Smith", 20, "South Sandwich Islands"),
("S2", "Jones", 10, "Rio De Janeiro"),
("S3", "Gorgon", 30, "New York"),
("S4", "Mabudo", 20, "New York"),
("S5", "Adams", 30, "South Sandwich Islands");

SELECT * FROM supplier
