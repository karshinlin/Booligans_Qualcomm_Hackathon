# Booligans_Qualcomm_Hackathon

## An Android app made to enhance consumer shopping and travel with convenient downloading of apps. 

This codebase represents the central server that allows clients (Android phones with the installed app) to retrieve apps based on their geolocation. Implemented using a REST API, a phone's GPS location is sent to this server where the Google Maps API is used to find the closest app to it. The app's information can then be sent to the phone's app for download. 

### Use cases:
1. Users of this app that go a mall can instantly see the mall's app downloaded on their phone. They can view the mall's directory, map, and other pertinent information. 
2. Users of this app that go to a store can see the store's app downloaded on their phone, where they can choose to order online if their desired items are not available in store.

### Stretch goals
1. Use a neural net to give better geolocation suggestions to users. 
2. Store state data of users in the area to give suggestions on how others use the application on their phone. 

