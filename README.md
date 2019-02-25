# Log-Analysis

Project is based on analysing the data coming from a website.

1. To run this project install vagrant and virtualbox.
2. Download the data from <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">Here</a>
3. You will need to unzip this file after downloading it.
4. The file inside is called newsdata.sql. Put this file into the vagrant directory.
5. Launch vagrant using command $vagrant up
6.  Then log into it with $vagrant ssh.
7. To build the reporting tool, you'll need to load the site's data into your local database.
8. To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.


<h3>The database includes three tables:</h3>

1.The authors table includes information about the authors of articles.<br/>
2.The articles table includes the articles themselves.<br/>
3.The log table includes one entry for each time a user has accessed the site.<br/>

<h3>Views Created</h3>

create view vw_log as select id, path from log where path != '/' and status = '200 OK'; <br/>
update vw_log set path = replace(path,'/article/',''); <br/>
create view vw_article as select path, count(*) as seen from vw_log group by path order by count(*); <br/>

create view vw_top_authors as select articles.author, vw_log.path from articles inner join vw_log on articles.slug = vw_log.path; <br/>

create view vw_percent as select vw_total_req.date, cast((vw_error.count*1.0/vw_total_req.count)*100.0 as decimal(10,3)) as Percent from vw_total_req inner join vw_error on vw_total_req.date = vw_error.date; <br/>

<h3>Run the program $ python log_analysis.py</h3>
