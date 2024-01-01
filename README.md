# *Eagle-Encryptor 2.1*

Encryptor-Decryptor is a simple Python tool that allows users to encrypt and decrypt text files. It provides a user-friendly interface for securing files with encryption and managing a local list of up to 1000 encrypted files. Additionally, the list of files and their details are stored in a MySQL database for easy & secure retrieval. There is also a password required to open the application. By default the password is `admin` however, the application gives an option to change it.

## Features

1. **Text File Encryption:**
   - The tool supports the encryption of various text file formats such as `.word`, `.py`, `.txt`, `.jpg`, and more.
     

2. **Password Management:**
   - Users can set and change the application password if they wish to.
     

3. **Local File-Location Storage:**
   - The tool can manage a local list of storing up to 1000 file paths so that the user does not have to give the file path every time the user opens the application.
     

4. **MySQL Integration:**
   
   - The list of files, along with their details, is stored in a MySQL database for efficient & secure organization and easy retrieval.



## Getting Started

To use the Encryptor-Decryptor tool, follow these steps:

1. **Clone the Repository:**
   
   ```bash
   git clone https://github.com/deepesh611/Eagle-Encryptor.git
   cd Eagle-Encryptor


3. **Install Dependencies:**
   - Before Installing the Application, make sure that you have the following things installed.
      `Python (3.11.x)`
      `pip3`
      `MySQL` (Along with the Python-MySQL Connector (Available in MySQL Installer - Community))

   - To install the application, all you have to do is clone the repo to the preferred location, and then run the setup file `setup.py`. 
   
   - If the setup does not run, they try the below command after changing the directory to `Eagle-Encryptor`.
   ```bash
   pip3 install -r requirements.txt
   

5. **Run the Tool:**
   ```bash
   python setup.py
   python main.py

## **Usage**
- Launch the tool using `python main.py`
- Type `ls` or `help` to view the list of all the Commands
- Use the given commands to encrypt, decrypt, change password, or use other functions
- Make sure that you do the following things after installation:
  `hide the subfolder where the main Python script is stored`
  `Copy the Application Shortcut to Desktop`

## **Contribution**
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create an issue or submit a pull request.

## **License**
This project is licensed under the MIT License.