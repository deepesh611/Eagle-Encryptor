# 🦅 *Eagle-Encryptor 2.1*

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-%235391FE.svg?style=for-the-badge&logo=powershell&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

This simple Python tool allows users to encrypt and decrypt files of a certain format. It provides a user-friendly interface for securing files with encryption and managing a local list of up to 1000 encrypted files. Additionally, the list of files and their details are stored in a MySQL database for easy & secure retrieval. There is also a password required to open the application. By default the password is `admin` however, the application gives an option to change it.


## Table of Contents
- 🚀 [Features](#-features)
- 🛠️ [Getting Started](#-getting-started)
- 📝 [Usage](#-usage)
- 🤝 [Contribution](#-contribution)
- 📄 [License](#license)

## 🚀 Features

1. **File Encryption:**
   - The tool supports the encryption of various text file formats such as `.word`, `.py`, `.txt`, `.jpg`, and more.
   - A list of all supported formats is given below.

2. **Password Management:**
   - Users can set and change the application password if they wish to.

3. **Local File-Location Storage:**
   - The tool can manage a local list of storing up to 1000 file paths so that the user does not have to give the file path every time the user opens the application.

4. **MySQL Integration:**
   - The list of files, along with their details, is stored in a MySQL database for efficient & secured organization and easy retrieval.


## 🛠️ Getting Started

To use the Encryptor-Decryptor tool, follow these steps:

1. **Clone the Repository:**
   - You can clone this repository by executing the following command on the terminal (cmd).
   ```bash
   git clone https://github.com/deepesh611/Eagle-Encryptor.git
   ```


3. **Install Dependencies:**
   - Before Installing the Application, make sure that you have the following things installed.
      `Python (3.11.x)`
      `pip3`
      `MySQL` (Along with the `Python-MySQL Connector` (Available in MySQL Installer - Community))

   - To install the application, all you have to do is clone the repository to the preferred location, then enter the following commands in `Powershell`/`CMD`. **(RUN AS ADMINISTRATOR)**
  ```bash
cd '.\Eagle Encryptor'
.\setup.ps1
   ```
   - If the terminal shows an error to run the script, try the following commands:
```bash
Set-ExecutionPolicy RemoteSigned
.\setup.ps1
```
     
  
5. **Run the Tool:**
   If the setup is complete, then there should a new application in the folder.
   `Eagle-Encryptor`
   

## 📝 **Usage**
- Launch the tool using 
```bash
& '.\Eagle Encryptor'
```

- Here is a list of accepted file formats:
   |    ***Domain***     |           ***Extensions***          |
   | ------------------- | ----------------------------------  |
   |        Text         | `.txt`,`.py`, `.pdf`,`.word`,`.xlsx`, `.html`, `.css`, `.c`, `.cpp`, `.php`|
   |       Images        |             `.png`, `.ico`, `.jpg`, `.jpeg`, `.img`                |
 <br>
- Type `help` to view the list of all the Commands:
<br> <!-- Add a blank line here -->

  |   ***COMMANDS***     |   ***TASK***                           |
  | ------------------   | -------------------------------------- |
  |        `ls`          |   Shows List of all Commands           |
  |   `encf` / `ef`      |   Encrypt a File from Your List        |
  |   `decf` / `df`      |   Decrypt a File from Your List        |
  |   `view` / `v`       |   View List of Files                   |
  |   `add` / `a`        |   Add a File in your List              |
  |   `del` / `d`        |   Delete a File from Your List         |
  |   `delall` / `da`    |   Delete All Files from the List       |
  |   `pwd` / `cp`       |   Change Password                      |
  |   `quit` / `q`       |   Exit the Application                 |
  
- Use the given commands to encrypt, decrypt, change password, or use other functions
- Make sure that you do the following things after installation:
- `hide the subfolder where the main Python script is stored`
- `Create the Application Shortcut to Desktop`

## 🤝 **Contribution**
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create an issue or submit a pull request.

## 📄**License**
This project is licensed under the MIT License.
