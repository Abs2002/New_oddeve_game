================================= CS Project- Odd-Eve Game =================================

The game is designed in 4 main functions and play against computer. The game supports the 
feature to store the scorein MYSQL and can be later retrieved. User can only acess to his 
records when he uses his correct username and password. The passwords are protected by 
MD-5 hash. The scores of each player can acessed by superuser by entering the 2 passwords. 
The player can play the game by entering his username or play as guest. While Playing with 
username the player has the option to save or not to save his game. 

Main Functions of Game

1. full login game- player can play the game with unlimited number of balls and save his game
2. full guest game- player can play the game with unlimited number of balls but he cannot save
		    the game .
3. small login game- player can play the game with only 6-6 balls and can save game 
4. small guest game- player can play the game with only 6-6 balls but cannot save the game.

Main Features

1. Toss will be done in the beggining.
2. If the match gets draw in the full games then a feature of superover will be there to 
   decide the win. if match even gets draw after superover then the feature of toss is there
   to decide at last.
3. If the match gets draw in the small games then toss will be done to decide the win


The Superuser details (Under work)

Username     -     admin
password     -     456@admin
2nd password -     admin@123

Problems in the code

1 - Overall there is no problem in the code with minor typo issues that can be resolved.
2 - User cannot see his Win percentage
3 - Master acess is not available in this version of code. future updates may bring this feature.


Total Modules -6


$$$ MYSQL table structure $$$

create database oddeve_game;

create table score_table(
name varchar(20) ,
date date,
score varchar(3),
match_status varchar(10)
);

create table login_details(
username varchar(20) primary key not null,
password varchar(32),
pass2opt varchar(32)
);

insert into login_details values("admin", "7ef946bd11662478569b92e181302e57", 
"e6e061838856bf47e1de730719fb2609");

Creator -Anirudh Bishnoi 12th-A 