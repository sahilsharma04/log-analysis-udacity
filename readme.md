LOG ANALYSIS
This project is part of Full Stack Nanodegree

Aim of this project is to print report based on data in database by using python(2.7.10) and postgresql



REQUIREMENTS AND INSTALLATION
1.)vagrant you can download vagrant here https://www.vagrantup.com/downloads.html install it then go to vagrant directory then run vagrant up to download virtual machine make sure your have oracle virtualbox 
2.) oracle virtualbox 
3.) newsdata.sql file



How to run
change directory to vagrant directory then
vagrant up command to run the vagrant on vm
vagrant ssh to login into vm
change directory to vagrant
use command psql -d news -f newsdata.sql to load database
-use \c to connect to database="news"
-use \dt to see the tables in database
-use \dv to see the views in database
-use \q to quit the database
use command python log.py to run the programm