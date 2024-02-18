# 2023 SCU INRIX Hackathon

Project Name: High Alert

Team: Yann Chan, Austin Min, Dev Pathak, 

Objective: The goal of the hackathon was centered around smart moving, transportation, and mapping. Our team created a web app aiming to dynamically suggest safer routes on kids' routes to school, integrating the traffic data and routes API that INRIX provided as part of our innovation goal.


This git repo is a personal copy/backup of the code written and deployed as part of the hackathon. I specialized in both data collection and also building the backend server.

The backend was done via Flask: refer to ./flask_server for code, although we no longer have INRIX API access, so many functions will not work. The frontend done using a combination of Leaflet, HTML + JS.  

Should you wish to run the project, use "export FLASK_APP=flaskserver.py" in the directory of the flask server before use.  

External resource from https://www.meganslaw.ca.gov/ was taken for the sex offender data. I used a MITM method in order to pull data in its' raw JSON form, this was done in order to cut down on the amount of storage used and also data processing that had to be done.

Thank you INRIX and SCU's ACM for making this hackathon sucessful and a great experience!  
