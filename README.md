# _Tracknap_
![Logo (2) (2)](https://user-images.githubusercontent.com/85924566/128607590-b60d57ed-be85-4e1c-8c50-151ec2f61c53.png)



The **Tracknap** website is designed to help user to track their 
sleep .

## Instructions For Project Setup

- **Step 1.**
You can directly download the zip file or follow next 2 steps to clone the repo.
Install latest version of git. Open the above github repository link in browser. Click on the code button
and copy HTTPS link.



- **Step 2.**
Create new folder and open git bash inside that folder write command-
```
git clone https://github.com/anjali7786/Sleep-Tracker.git
```
- **Step 3.**
  - Install latest version of python and a code editor (Pycharm or Visual Studio Code).
  - Download & Install MYSQLCLIENT For Python : https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient open this link and under MySQLclient select the wheel according to your python version and 32/64 bit windows system. 
  '''
   cmd.

   
- **Step 4.**
   Open the project files in the code editor. Open `main.py` file and if your MySQL username and password are not **root** then you can replace the username and password written in `main.py` file with your MySQL username and password.

- **Step 5.**
  **Installing Packages**

  For Visual Studio Code do the following:
   - Open **New Terminal**

    ![image](https://user-images.githubusercontent.com/64724039/117951623-f7f91e00-b331-11eb-8c7a-2baba835b685.png)

   - And now run the following commands in the terminal:
    ```
    python -m venv env
    Set-ExecutionPolicy Unrestricted -Scope Process
    env\scripts\activate
    pip install flask
    $env:FLASK_APP = "main"
    pip install bcrypt
    pip install flask_mysqldb
    pip install flask_mail
    flask run
    ```
   
    ```
  For Pycharm code editor do the following:
   - Open the terminal

   - And run the following commands:
    ```
    pip install flask,
    pip install bcrypt,
    pip install flask_mysqldb,
    pip install flask_mail
    ```
   
    ```
  

## Snapshots

- Homepage

![Screenshot (383)](https://user-images.githubusercontent.com/85924566/128629949-cdb31644-83ef-400f-8163-d46533710230.png)

![image](https://user-images.githubusercontent.com/85924566/128641160-17d06d82-1c90-460a-909e-929f719a14d2.png)



- Sign Up page

**To activate other pages you have to fill sign up form**

![Screenshot (384)](https://user-images.githubusercontent.com/85924566/128630065-86f2a29f-fa1b-4b8c-bc39-3cf0ae34b3db.png)


- Unable to sleep

**To zoom the content of Yoga, Meditation, Food and Habbits hover on respective image**

![Screenshot (394)](https://user-images.githubusercontent.com/85924566/128641206-c791ae31-8b7c-4ba7-8b71-184cad30deae.png)
![Screenshot (395)](https://user-images.githubusercontent.com/85924566/128641216-8d430a59-52c2-409d-b2fd-f04fba30a558.png)
![Screenshot (395)](https://user-images.githubusercontent.com/85924566/128641228-39fff75e-f99d-41ef-8092-7f8b6ed5b034.png)

- Boostyourself page

![Screenshot (388)](https://user-images.githubusercontent.com/85924566/128630355-3e065252-3cc4-47a9-bad2-7b607780631c.png)

**To zoom the image of Boostyourself click on image**

![Screenshot (389)](https://user-images.githubusercontent.com/85924566/128630410-cf2eecf2-68a5-4f86-b3a3-fec3b833352f.png)


   
- Record page in Track your sleep
**It is compulsory to fill all the entries in Track your nap form**

![Screenshot (391)](https://user-images.githubusercontent.com/85924566/128630489-16bf8ace-865a-4e59-9494-4e12fb3dda06.png)

- Analyze your sleep in Track your sleep

![Screenshot (74)](https://user-images.githubusercontent.com/85924566/128641275-fdc56ccd-009c-4357-a690-b46cc78e039c.png)

-Login page

**Once you logout then to visit website again  you don't need to fill signup form again and again, just fill entries in login in form.**
**It will automatically filled by system if you have saved password in the beginning .**


![Screenshot (392)](https://user-images.githubusercontent.com/85924566/128630528-9a7f4e1d-12d9-4a93-bb1b-58ed9e106915.png)


