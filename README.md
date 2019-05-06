# Politics Through Social Media (DAP Project MVP)
### By Muf Tayebaly, Rohit Dalal, Phani Valasa, Venkat Gangireddy

## Objective
Provide users a smart view into popular trending topics in our growing social world and what people are talking about them near real-time.  Differentiating ourselves from news media sources.
(The current high level topic is focused on Politics for the Minimum Viable Product)

## Benefits
Aggregation of sources, like social media, in a single view while using intelligence (machine learning & natural language processing) to classify and analyze.  Providing users a new perspective on what is happening in the world on specific and hot topics.  Users can stay current without the need of reading long and single perspective news articles, saving time, and focusing on the right topics.

## How it works
We aggreegate the data from social media sources (Twitter for Sprint 1) and leverage existing ML/NLP packages to classify the content and analyze the sentiment analysis.  
As part of Sprint 1 - we monitor any tweets related to Politics and topic entities we have identify as trending right now ("Health Care", "Education", "Immigration", "Trump", "White House").  All MVP services are currently working, however, we have not completed integration to the front end Web App yet.  
Planned for Sprint 2 - Integration to the Web App using the REST API service.  Docker for easy running.  Amazon Web Services (AWS) implementation.  Smarter intelligence using IBM Watson's Natural Language Understanding (potentially).
  
### Architecture
![alt text](imgs/MVP-Architecture.png "MVP Architecture")

### JIRA Board
https://toydemoproject.atlassian.net/jira/software/projects/PTSM/boards/22 

### The Web App
**Located at:**  http://muftayebaly.com/apps/DAPPROJ/ 

**Description:**  
The UI web app was built using Bootstrap as a base framework.  The design is completed using custom HTML/CSS/JS.  The files are currently hosted at the URL below and also on Github.  The UI service currently does not integrate with the REST API service to update the topics and tweets.  The integration with the REST API service will be in Sprint 2.  Only the homepage works from Sprint 1.  
  
![alt text](imgs/MVP-WebApp.png "MVP Web App")

### The REST API Service
**Located at:**  API/api.py

**Description:**  
The REST API service was built in Python using flask.  It currently runs on your local machine and leverages the dataServices DataClient in the TwitterData folder.  The service pulls the data from the MySQL database based on api GET calls and then publishes them to the user as a JSON string.

**Requirements:**  Python 3, Flask, MySql.Connector, MySQL Client, Pandas, ConfigParser, JSON, Sys

**Run by:**  In terminal, navigate to the API folder.  Use command    python api.py  
  
![alt text](imgs/MVP-RunAPI.png "MVP Run API")

**Sample Inputs:**
* http://127.0.0.1:5000/api/get/tweets
* http://127.0.0.1:5000/api/get/topics
* http://127.0.0.1:5000/api/get/trending/topics  (has parameter limit that takes integer) e.g. ?limit=100
  
**Sample Outputs:**  
![alt text](imgs/MVP-APIOutputs.png "MVP API Sample Outputs")
