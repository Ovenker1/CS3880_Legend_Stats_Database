DROP DATABASE IF EXISTS cs3380project;
CREATE DATABASE cs3380project;
USE cs3380project;

-- table creation
CREATE TABLE Role (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(100)
);

CREATE TABLE Ranks (
    rank_id INT AUTO_INCREMENT PRIMARY KEY,
    rank_name VARCHAR(100)
);

CREATE TABLE Season (
    season_id INT AUTO_INCREMENT PRIMARY KEY,
    season_num INT,
    total_games_played INT
);

CREATE TABLE Legend (
    legend_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    games_played INT,
    role_id INT,
    FOREIGN KEY (role_id) REFERENCES Role(role_id)
);

CREATE TABLE Statistics (
    stats_id INT AUTO_INCREMENT PRIMARY KEY,
    ban_rate FLOAT,
    pick_rate FLOAT,
    win_perc FLOAT,
    legend_id INT,
    season_id INT,
    rank_id INT,
    FOREIGN KEY (legend_id) REFERENCES Legend(legend_id),
    FOREIGN KEY (season_id) REFERENCES Season(season_id),
    FOREIGN KEY (rank_id) REFERENCES Ranks(rank_id)
);

-- 2. populate static data
INSERT INTO Role (role_name) VALUES 
('Top Lane'), ('Mid Lane'), ('ADC'), ('Support'), ('Jungle');

INSERT INTO Ranks (rank_name) VALUES 
('Iron'), ('Bronze'), ('Silver'), ('Gold'), ('Platinum'), 
('Emerald'), ('Diamond'), ('Master'), ('Grandmaster'), ('Challenger');

INSERT INTO Season (season_num, total_games_played) VALUES 
(10, 450000), (11, 480000), (12, 500000), (13, 550000), (14, 600000), (15, 650000);

INSERT INTO Legend (name, games_played, role_id) VALUES 
('Smolder', 400, 3), ('Sion', 500, 1), ('Rammus', 600, 5),
('Veigar', 1000, 2), ('Ahri', 1200, 2), ('Lee Sin', 2000, 5),
('Ezreal', 3000, 3), ('Thresh', 1500, 4), ('Darius', 800, 1),
('Yasuo', 5000, 2), ('Jinx', 2200, 3), ('Lux', 1800, 4);

-- populate statistics (Seasons 10-15)
INSERT INTO Statistics (ban_rate, pick_rate, win_perc, legend_id, season_id, rank_id) VALUES 
(1.0, 5.0, 45.0, 10, 1, 1),  -- Yasuo (Iron S10)
(5.0, 10.0, 49.0, 9, 1, 1),  -- Darius (Iron S10)
(2.0, 15.0, 50.0, 12, 1, 2), -- Lux (Bronze S10)
(3.0, 12.0, 51.5, 4, 1, 3),  -- Veigar (Silver S10)
(4.0, 8.0, 52.0, 5, 2, 4),   -- Ahri (Gold S11)
(10.0, 20.0, 48.0, 7, 2, 4), -- Ezreal (Gold S11)
(15.0, 5.0, 53.0, 3, 2, 5),  -- Rammus (Plat S11)
(20.0, 18.0, 49.5, 6, 3, 6), -- Lee Sin (Emerald S12)
(30.0, 12.0, 51.0, 11, 3, 7),-- Jinx (Diamond S12)
(2.0, 4.0, 48.0, 2, 3, 7),   -- Sion (Diamond S12)
(40.0, 25.0, 46.0, 10, 4, 8),-- Yasuo (Master S13)
(5.0, 15.0, 52.0, 8, 4, 9),  -- Thresh (GM S13)
(50.0, 30.0, 55.0, 1, 5, 10),-- Smolder (Challenger S14)
(5.0, 10.0, 48.0, 5, 5, 10), -- Ahri (Challenger S14)
(60.0, 22.0, 49.0, 10, 6, 4), -- Yasuo (Gold S15)
(10.0, 12.0, 51.5, 5, 6, 4),  -- Ahri (Gold S15)
(2.0, 25.0, 50.0, 7, 6, 4),   -- Ezreal (Gold S15)
(5.0, 15.0, 52.5, 11, 6, 7),  -- Jinx (Diamond S15)
(25.0, 18.0, 48.5, 6, 6, 10), -- Lee Sin (Challenger S15)
(8.0, 10.0, 53.0, 3, 6, 1);   -- Rammus (Iron S15)