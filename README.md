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


  CI-CD Project
===============================
Project: Python Voting Application CI/CD Pipeline

tools Used:
* Git, Github
* Jenkins
* Docker
* Docker Compose
* Docker Hub
* linux
* AWS EC2
1. GITHUB Source Code Management
The applicataion source code is stored in github, This repository contains docker file, docker compose file, and jenkins file and python code

Work Flow
Developer → GitHub Repository

2. Webhook Integration
I configured a GitHub webhook to automatically trigger the Jenkins pipeline whenever code is pushed to the repository. This automates the build, deployment, and Docker image push process without any manual intervention.

Webhooks workflow
===============
GitHub Push
    ↓
GitHub Webhook
    ↓
Jenkins Trigger

webhook url
http://jenkinsIp:8080/github-webhook/
3. Jenkins CI Pipeline
========================
Jenkins countniously Integrate the application building and deploying whenever code changes are pushed

Pipeline stages:
* Check out the code: Jenkins pulls the latest code from GitHub.
* Docker Image Build: Jenkins uses the Dockerfile to create a Docker image.
* Docker Hub Push: After building the image, Jenkins authenticates with Docker Hub and pushes the image.
4. Application Deployment
==========================
Jenkins deploys the application using Docker Compose.


Challenges Faced
=====================
Jenkins Docker permission issues
Docker Compose installation issues
Jenkins user not in docker group
Webhook configuration
Container deployment troubleshooting


Deployment Workflow
======================
Developer Pushes Code
          ↓
GitHub Repository
          ↓
GitHub Webhook
          ↓
Jenkins Pipeline Triggered
          ↓
Source Code Checkout
          ↓
Docker Image Build
          ↓
Push Image to Docker Hub
          ↓
Docker Compose Deployment
          ↓
Application Available to Users



