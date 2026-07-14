Request Flow of python-voting-app
==================================
User
 │
 │ 1. Opens http://localhos
 ▼
Nginx (web)
 │
 │ 2. Receives HTTP request
 │
 │ 3. Forwards request to Flask
 ▼
Flask (app)
 │
 │ 4. Processes vote
 │
 │ 5. Stores/Retrieves vote
 ▼
MySQL (db)
 │
 │ 6. Returns voting data
 ▼
Flask
 │
 │ 7. Sends HTML response
 ▼
Nginx
 │
 │ 8. Returns web page
 ▼
User Browser
==================================================
Docker compose voting Application
==================================

**Deploy a 3-tier Voting Application using Docker Compose.**

Components:
Frontend: Nginx
Backend: Python Flask
Database: MySQL

* Then I have taken the one Ec2 Instance and installed required softwares
-> Docker
-> docker compose
Then i have created a directory called voting app by using the command like

 ====> mkdir voting-app
====>  cd voting-app

Then i have created a backed files nothing but code
===================================================

==> app.py  (Code)
==> requirements.txt (Installed required Python packages)
==> Dockerfile  
==> templates/index.html

Then i have configured the nginx.conf its acts as a reverse proxy for example client access the application request goes to the nginx the nginx send a request to the flask here its acts as a reverse proxy 

After that i have created a docker compose file

After creating the docker compose file i have run the command like 
==> Docker compose up 

once everything run successfuly you can access the site from the web
  http://publicip:5000
