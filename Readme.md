## PandaBytes-EMR: The simple open source EMR for quick simulation experiments
![Alt text](database/image.png)

### Warning:
#### **Non secure** by design. Everything is human readable.🫠 This could not be any less secure if I tried. Add users on the fly by editing the json file. No form of real patient data or confidential data should be used with this project. This is designed entirely around the premise of using synthetic data to run quick simulation experiments
#### Any experiments run with this project are at your own risk. This was made over a weekend and change and is of the quality you'd expect for that level of commitment.

### Key Features

- **Easy to Use:** Simplest implementation possible for basic EMR data display.
- **Open Source:** Take it and make it yours. 
- **Lightweight:** Designed for quick deployment.
- **Interactive plots:** See patient data using interactive plots made with plotly

### TODO:
- Add support for encounters. My current use case does not need it. I may add this down the line. 
- Improve data structure: The data structures used are not standard datastructures but they can be swapped out with minimal effort.
- Patient search function
- Note entry




https://github.com/Ltrack/PandaBytes-EMR-Sim/assets/36055614/ef9ef8f7-371b-48ab-82eb-5f2f655d8fc1






Intelligence augmentation tools used: Github CoPilot, GPT4. Logo made with GPT4, photopea.com

### How to run:

1. Clone the repository:

~~~
git clone <*repo*>
~~~


2. make a .env file at the base folder with PATIENT_DATA_FILE, USER_DATA_FILE, SECRET_KEY

3. Create a conda environment:

~~~
conda create --name sim_emr --file requirements.txt

conda activate sim_emr

python app.py
~~~

4. Replace patients.json with desired data. 


