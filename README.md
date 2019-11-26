## Links
Youtube/VoiceFlow Demo: https://youtu.be/Fxb96g8-exg


## Inspiration
Having grown up in developing countries, our team understands that there are many people who simply cannot afford to visit doctors frequently (distance, money, etc.), even when regular check-ups are required. This brings forth the problem - patients in developing countries often have the money to buy medicine but not enough money to visit the doctor every time. Not only does this disparity lead to lower mortality rates for citizens and children but makes it difficult to seek help when you truly need it.

Our team aims to bridge that gap and provide patients with the healthcare they deserve by implementing "Pillar" stations in settings of need.

## What it does
Patients visit the pillar stations for at least one of three purposes: 
1. Update doctor with medical symptoms
2. Get updates from doctors regarding their past symptoms and progress 
3. Get medicine prescribed by doctors

For the first purpose, patients activate the Pillar stations (Amazon Echo) and are called on a secure, private line to discuss symptoms and describe how they've been feeling. Pillar's algorithm processes that audio and summarizes it through machine learning APIs and sends it to the remote doctor in batches. Our reason for choosing phone calls is to increase privacy, accessibility and feasibility. The summarized information which includes sentiment analysis, key word detection and entity identification is stored in the doctor's dashboard and the doctor can update fields as required such as new notes, medicine to dispense, specific instructions etc. The purpose of this action is to inform the doctor of any updates so the doctor is briefed and well-prepared to speak to the patient next time they visit the village. There are also emergency update features that allow the doctor to still be connected with patients he sees less often.

For the second purpose, patients receive updates and diagnosis from the doctor regarding the symptoms they explained during their last Pillar visit. This diagnosis is not based purely on a patient's described symptoms, it is an aggregation of in-person checkups and collected data on the patient that can be sent at any time. This mitigates the worry and uncertainty patients may have of not knowing whether their symptoms are trivial or severe. Most importantly it provides a sense of connection and comfort knowing knowledgable guidance is always by their side. 

Finally, for the third purpose, patients receive medicine prescribed by doctors instantly (given the Pillar station has been loaded). This prevents patients' conditions from worsening early-on. The hardware dispenses exactly the prescribed amount while also reciting instructions from the doctor and sends SMS notifications along with it. The Pillar prototype dispenses one type of pill but there is evident potential for more complicated systems. 

## How we built it
We built this project using a number of different software and hardware programs that were seamlessly integrated to provide maximum accessibility and feasibility. To begin, the entry point to the Pillar stations is through a complex **Voiceflow** schema connected to **Amazon Echo** that connects to our servers to process what patients describe and need. Voiceflow gives us the ability to easily make API calls and integrate voice, something we believe is more accessible than text or writing for the less-educated populations of developing countries. The audio is summarized by **Meaning Cloud API** and a custom algorithm and is sent to the Doctor's dashboard to evaluate. The dashboard uses **MongoDB Altas** to store patients' information, it allows for high scalability and flexibility for our document oriented model. The front-end of the the dashboard is built using jQuery, HTML5, CSS (Bootstrap) and JavaScript. It provides a visual model for doctors to easily analyze patient data. Doctors can also provide updates and prescriptions for the customer through the dashboard. The Pillar station can dispense prescription pills through the use of **Arduino** (programmed with C). The pill dispense mechanism is triggered through a Voiceflow trigger and a Python script that polls for that trigger. This makes sense for areas with weak wi-fi. Finally, everything is connected through a **Flask** server which creates a host of endpoints and is deployed on **Heroku** for other components to communicate. Another key aspect is that patients can also be reminded of periodic visits to local Pillar stations using **Avaya's SMS & Call Transcription** services. Again, for individuals surviving more than living, often appointments and prescriptions are forgotten.

Through this low-cost and convenient service, we hope to create a world of more accessible healthcare for everyone.


## Challenges and What We Learned
- Hardware issues, we had a lot of difficulties getting the Raspberry Pi to work with the SD card. We are proud that we resolved this hardware issue by switching to Arduino. This was a risk but our problem solving abilities endured.
- The heavy theme of voice throughout our hack was new to most of the team and was a hurdle at first to adapt to non-text data analysis
- For all of us, we also found it to be a huge learning curve to connect both hardware and software for this project. We are proud that we got the project to work after hours on end of Google searches, Stack Overflow Forums and YouTube tutorials. 


## What's next for Pillar
- We originally integrated Amazon Web Services (Facial Recognition) login for our project but did not have enough time to polish it. For added security reasons, we would polish and implement this feature in the future. This would also be used to provide annotated and analyzed images for doctors to go with symptom descriptions.
- We also wanted to visualize a lot of the patient's information in their profile dashboard to demonstrate change over time and save that information to the database
- Hardware improvements are boundless and complex pill dispensary systems would be the end goal
