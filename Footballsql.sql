CREATE TABLE IF NOT EXISTS FOOTBALL (
    player_id TEXT PRIMARY KEY,
    player_name TEXT NOT NULL,
    team_name TEXT NOT NULL,
    position TEXT NOT NULL,
    age INTEGER
);

INSERT INTO FOOTBALL VALUES (1, 'Harry Kane', 'Bayern Munich', 'Striker', 33);
INSERT INTO FOOTBALL VALUES (2, 'Kylian Mbappe', 'Real Madrid', 'Striker', 27);
INSERT INTO FOOTBALL VALUES (3, 'Lamine Yamal', 'Barcelona', 'Left Winger', 19);
INSERT INTO FOOTBALL VALUES (4, 'Cristiano Ronaldo', 'Al Nassr', 'Striker', 41);
INSERT INTO FOOTBALL VALUES (5, 'Jude Bellingham', 'Real Madrid', 'Midfielder', 24);
INSERT INTO FOOTBALL VALUES (6, 'Erling Haaland', 'Manchester City', 'Striker', 27);
INSERT INTO FOOTBALL VALUES (7, 'Enzo Fernandez', 'Manchester City', 'Midfielder', 24);
SELECT * FROM FOOTBALL;
SELECT DISTINCT team_name FROM FOOTBALL;
SELECT COUNT(DISTINCT team_name) FROM FOOTBALL;
SELECT SUM(age) FROM FOOTBALL;
SELECT AVG(age) FROM FOOTBALL;
SELECT COUNT(player_name) FROM FOOTBALL WHERE age > 26;
SELECT player_name FROM FOOTBALL WHERE age > 26
SELECT player_name FROM FOOTBALL WHERE position = 'Striker'; 
SELECT
    COUNT(player_id) AS total_players,
    COUNT(DISTINCT team_name) AS unique_teams,
    SUM(age) AS total_age,
    AVG(age) AS average_age
FROM FOOTBALL;
