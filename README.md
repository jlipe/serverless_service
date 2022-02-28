This is my microservice for CS 361.

This service is setup so every 15 minutes the crawl.py function is executed and saves headline results into a DyanmoDB database.

The API runs using the serverless framework and the endpoints are for displaying recent headlines, and generating a quiz that includes a random set of headlines. All the logic for handling the API requests is in handler.js. The logic for what triggers the handler.js to actually run is in the serverless.yml file. The serverless.yml file is a description of how this should be deployed into AWS and makes deploying it (and testing it offline) much easier.

The crawl.py function is working as a standalone lambda funciton hosted on AWS with the required dependencies installed there. Currently this serverless framework is not setup to handle the crawl.py function and it is only in this repo as a reference.