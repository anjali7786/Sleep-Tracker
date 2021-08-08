
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
    flask run
    ```
   
    ```
  For Pycharm code editor do the following:
   - Open the terminal

   - And run the following commands:
    ```
    pip install flask,
    pip install bcrypt,
    pip install flask_mysqldb,pip install -U Werkzeug,pip install mysqlclient
    
      

## Some glimpse of Tracknap

- Homepage
![Screenshot (372)](https://user-images.githubusercontent.com/85924566/128605314-f9082fe3-9abd-4007-a481-1f0073b49452.png)
![Screenshot (375)](https://user-images.githubusercontent.com/85924566/128606246-ac6ed249-65b3-45fd-95df-0d722d19db9f.png)

- Login page

![Screenshot (373)](https://user-images.githubusercontent.com/85924566/128606078-8d93bebb-9023-49f3-9df5-d743f31ffb60.png)
**Once you login only then you will be able to see remaining pages**
- Sign Up page

![Screenshot (374)](https://user-images.githubusercontent.com/85924566/128606118-e452eafb-1f63-4c59-b485-ced74ae072f3.png)

- Unable to sleep page
**To zoom the content of Yoga, Meditation, Food and Habbits hover on respective image**
![Screenshot (378)](https://user-images.githubusercontent.com/85924566/128606782-566ef7fc-b6a8-4b32-87bc-b55c8db7787c.png)
![Screenshot (379)](https://user-images.githubusercontent.com/85924566/128606914-0c0beb50-694d-48d3-87b4-84a8c9ba987d.png)
![Screenshot (380)](https://user-images.githubusercontent.com/85924566/128606930-da2e24e6-244d-4947-b511-dc2c63383f0e.png)


- Boostyourself page
![Screenshot (376)](https://user-images.githubusercontent.com/85924566/128606486-22f9f48e-050b-4405-b851-36568b4ed0fb.png)

**To zoom the image of Boostyourself click on image**

![Screenshot (377)](https://user-images.githubusercontent.com/85924566/128607821-46d5fc5a-454e-42b2-94bb-6193dc86c72b.png)

   
- Record page in Track your sleep
**It is compulsory to fill all the entries in Track your nap form**

![Screenshot (381)](https://user-images.githubusercontent.com/85924566/128607191-95b36e52-13bc-4d0f-8add-064d356d5392.png)


