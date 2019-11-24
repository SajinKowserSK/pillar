## Inspiration
Having grown up in developing countries, our team understands that there are many people who simply cannot afford to visit doctors frequently (distance, money, etc.), even when regular check-ups are required. This brings forth the problem - patients in developing countries often have the money to buy medicine but not enough money to visit the doctor every time.

Our team aims to bridge that gap and provide patients with the healthcare they deserve by implementing "Pillar" stations.

## What It Does
Patients visit the pillar stations for at least one of three purposes:

Update doctor with medical symptoms
Get updates from doctors regarding their past symptoms
Get medicine prescribed by doctors
For the first purpose, patients speak into the Pillar stations (Amazon Echo) and describe how they've been feeling. Pillar's algorithm processes that audio and summarizes it, sending it to the remote doctor. The information is stored in the doctor's dashboard and the doctor can update fields as required such as new notes, medicine to dispense, etc. The purpose of this action is to inform the doctor of any updates so the doctor is briefed and well-prepared to speak to the patient next time they visit the village.

For the second purpose, patients receive updates from the doctor regarding the symptoms they explained during their last Pillar visit. This mitigates the worry and uncertainty patients may have of not knowing whether their symptoms are trivial or severe.

Finally, for the third purpose, patients receive medicine prescribed by doctors instantly (given the Pillar station has been loaded). This prevents patients' conditions from worsening early-on.

## How We Built It 
We built this project using a number of different software and hardware programs. To begin, we created the Pillar stations using Amazon Echo and Voiceflow to process what patients describe. The audio is summarized by Meaning Cloud API and sent to the Doctor's dashboard. The dashboard uses MongoDB Altas to store patients' information. Furthermore, the dashboard is also built using jQuery, HTML5, CSS (Bootstrap) and JavaScript. Finally, the doctor can provide prescriptions for the customer through the dashboard. The Pillar station can dispense prescription pills through the use of Arduino (programmed with C). Everything is connected through a Flask server which creates a host of endpoints and is deployed on heroku for other components to communicate. Patients can also be reminded of periodic visits to local Pillar stations using Avaya's SMS & Call Transcription services.

Through this low-cost and convenient service, we hope to create a world of more accessible healthcare for everyone.

## Challenges/Accomplishments/Learnings 
Hardware issues, we had a lot of difficulties getting the Raspberry Pi to work with the SD card. We are proud that we resolved this hardware issue by switching to Arduino.

For all of us, we also found it to be a huge learning curve to connect both hardware and software for this project. We are proud that we got the project to work after hours on end of Google searches, Stack Overflow Forums and YouTube tutorials.

## What's Next For Pillar
We originally integrated Amazon Web Services (Facial Recognition) login for our project but did not have enough time to polish it. For added security reasons, we would polish and implement this feature in the future.
We also wanted to visualize a lot of the patient's information in their profile dashboard to demonstrate change over time and save that information to the database

## Pictures to Come Soon
