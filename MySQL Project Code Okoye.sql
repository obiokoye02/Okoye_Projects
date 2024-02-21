CREATE TABLE CLUB(
Club_Name Varchar(200),
Club_City VARCHAR(200),
Club_StatWins int not null,
Club_Games int not null,
Players Varchar(200),
PRIMARY KEY(Club_Name)
);

Insert into CLUB(Club_Name,Club_City,Club_StatWins,Club_Games,Players)
Values ('Manchester United','Old Trafford', 19,38,'Marcus Rashford'),
            ('Manchester City','Manchester',26,38,'Erling Haaland'),
            ('Chelsea','W London',11,38,'Kante'),
            ('Liverpool','Liverpool',18,38,'Mohamed Salah'),
            ('Arsenal','London',25,38,'Bukayo Saka');

CREATE TABLE GAMES (
  Club_Games INT NOT NULL,
  Club_City  varchar(50),
  Game_stats int not null,
  AvgAttend int not null,
  Stadium varchar(50),
PRIMARY KEY(Club_Games)
);

Insert into GAMES(Club_Games,Club_City,Game_stats,AvgAttend,Stadium)
Values (38,'Old Trafford',0,73960,'Old Trafford Stadium'),
            (39,'Manchester',0,10000,'Etihad Stadium'),
            (40,'W London',0,53126,'Stamford Bridge'),
            (37,'Liverpool',0,53000,'Anfield'),
            (35, 'London',3,60028,'Emirates Stadium');

CREATE TABLE COACH(
Club_Name VARCHAR(50),
First_Name varchar(50),
Last_Name VARCHAR(50),
Captain_Name Varchar(50),
Club_StatWins int not null,
PRIMARY KEY(Club_Name)
);
Insert into COACH(Club_Name,First_Name,Last_Name,Captain_Name,Club_StatWins)
Values ('Manchester United','Erik',' Hag','Harry Maguire',19),
            ('Manchester City','Pep',' Guardiola','IIkay Gundogan',26),
            ('Chelsea', 'Thomas',' Tuchel','Cesar Tanco',11),
            ('Liverpool', 'Jurgen',' Klopp', 'Jordan Henderson',18),
            ('Arsenal', 'Mikel',' Arteta', 'Martin Odegaard',25);
            
CREATE TABLE PLAYERS(
Club_Name VARCHAR(50),
Players_Num int not null,
Stadium varchar(50),
Coach_Name varchar(50),
primary key(Club_Name,Players_Num),
constraint FK_Club_Name foreign key(Club_Name) references Club(Club_Name)
);
Insert into PLAYERS(Club_Name,Players_Num,Stadium,Coach_Name)
Values ('Manchester United',32,'Old Trafford Stadium','Erik Hag'),
            ('Manchester City',24,'Etihad Stadium','Pep Guardiola'),
            ('Chelsea',32,'Stamford Bridge','Thomas Tuchel'),
            ('Liverpool',30,'Anfield','Jurgen Klopp'),
            ('Arsenal',23,'Emirates Stadium','Mikel Arteta');
            
CREATE TABLE CITY (
Club_City VARCHAR(50),
Club_Name VARCHAR(50),
Stadium varchar(50),
Country varchar(50),
Area_Code int not null,
primary key(Club_City),
FOREIGN KEY (Club_Name) REFERENCES Club(Club_Name)
);

Insert into CITY(Club_City,Club_Name,Stadium,Country,Area_Code)
Values ('Old Trafford','Manchester United','Old Trafford Stadium','England',0161),
            ('Manchester','Manchester City','Etihad Stadium','England',0161),
            ('W London','Chelsea','Stamford Bridge','England',020),
            ('Liverpool','Liverpool','Anfield','England',0151),
            ('London','Arsenal','Emirates Stadium','England',020);