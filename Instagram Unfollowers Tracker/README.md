<!--Please do not remove this part-->
![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

# Instagram Unfollowers Tracker

## 🛠️ Description

Tired of people unfollowing you after you follow them back? Have apps for removing followers caused your account to be flagged by Instagram? This Python script is designed just to work around that issue without risking your account's security and compliance with Instagram's guidelines.

### Features

- Track and list users who have unfollowed you on Instagram.
- Generates an Excel file containing username and the link to their profile for easy navigation.
- Minimizes the risk of violating Instagram's policies.
- Maintains account security without compromise by not requiring your password.

## ⚙️ Languages or Frameworks Used

This code is written using Python Programming Language. You can see the modules required to be able to use the following scripts in the `requirement.txt` file.

## 🌟 How to run

1. Make sure you have Python installed on your system.

1. Download Your Instagram Data:
    - Go to your Instagram profile.
    - Navigate to `Accounts Center`.
    - Select `Your information and permissions`.
    - Choose `Download your information`.
    - Create a new download request for your data.
    - It is advised to choose the option `Some of your information` under the `How much information do you want` tab.
    - **NOTE**: For the program to work, the files must be downloaded in JSON format. **Make sure you extract the zip file before proceeding.**

2. Navigate to the `Instagram Unfollowers Tracker` folder:
    ```sh
    cd "Instagram-Unfollowers-Tracker"
    ```
3. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```
4. Run The Script.
   ```sh
    python unfollowers.py
    ```

5. Copy The File Path for ```followers_1.json``` and ```following.json``` and paste it into the respective fields. No need to make changes to the file path manually, the code does it for you.

6. Search for ```unfollow.xlsx``` to recieve your unfollower data. (Username & Link To Their Profile)

## 🤖 Author

This script is witten by Niranjay Ajayan -> https://github.com/dyingpotato890