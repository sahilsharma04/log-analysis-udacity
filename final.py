#!/usr/bin/env python3

import psycopg2


def connect(database_name="news"):
    db = psycopg2.connect("dbname={}".format(database_name))
    return db


def first_querry():
    db = connect()
    c = db.cursor()
 c.execute("create view result as select title\
        ,concat('/article/',slug) as sl from articles")
    c.execute("create view name as select path , count(*)\
     as num from log Join result on result.sl like log.path\
      group by path order by num desc limit 3")
    c.execute("select title,num from name Join result on\
     result.sl like name.path order by num desc")
    row = c.fetchall()
    print("Most popular articles:")
    for i in range(len(row)):
        print row[i][0], ',', row[i][1], 'views'
    print("------------------------------------------")


def second_querry():
    db = connect()
    c = db.cursor()
     c.execute("create view result1 as select author,\
        concat('/article/',slug) as sl1 from articles")
    c.execute("create view name as select path , count(*)\
     as num from log Join result1 on result1.sl1 like log.path group\
        by path order by num desc")
    c.execute("create view name1 as select author,num from name\
     Join result1 on result1.sl1 like name.path order by num desc")
    c.execute("select name,sum(num) from name1 Join authors on\
     authors.id=name1.author group by name order by sum desc")
    row = c.fetchall()
    print("Most popular authors:")
    for i in range(len(row)):
        print row[i][0], ',', row[i][1], 'views'
    print("-------------------------------------------")


def third_querry():
    db = connect()
    c = db.cursor()
  c.execute("create view status as select date(time) as date1,\
        count(status) as stat from log group by date(time)")
    c.execute("create view status4 as select date(time) as date1,\
        status from log where status like '404%'")
    c.execute("create view status2 as select date1,count(status) as\
     notf from status4 group by date1")
    c.execute("create view status5 as select status2.date1 as fdate,\
        cast(notf as float),cast(stat as float) from status join status2 on\
         status.date1=status2.date1")
    c.execute("select fdate,(notf*100)/stat from status5 where\
     (notf*100)/stat > 1")
    row = c.fetchall()
    print("Days with more than 1% errors:")
    for i in range(len(row)):
        print row[i][0], ',', row[i][1], '%'
    print("\n")

# calling function for first query
print "\n\nWhat are the most popular three articles of all time?\n"
first_querry()



# calling function for second query
print "\n\nWho are the most popular authors of all time?\n"
second_querry()



# calling function for third query
print "\n\nOn which days did more than 1% of requests lead to errors?\n"
third_querry()
