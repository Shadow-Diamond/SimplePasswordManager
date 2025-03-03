# SimplePasswordManager

## How To Run
To run this password manager, you are going to need a terminal that can run Python.
Navitage to the location that the program is stored in using the cd command.
run "python passwordManager.py" and the program should start

## How to change Paths
To change where you want your password file and your encryption key location, add the path you want them to be at into the encryptor_path or password_path field.
Example of a path: C:/Users/username/

## How to change file names
If you want to change the file name of your password file or your encryption file, change the encryptorName or passwordFileName field to what you want them to be. There is no specific file type they need to be.

## Running the Program
When you first run the program, it will give you 4 options. Make, Import, View, and Quit.
### Make
Running the make option will prompt you to input a password length. Then, the program will give you a generated password. If you like the password, type 'yes' and it will ask you what it is used for. If you type no, it will regenerate the password.
Once given what the password is used for, the program will tell you that the password was added to the password file, and then take you back to the main 4 options.
### Import
When running the import option, it will let you input your own password that you have made. After submitting the premade password, it will ask what it is used for, just like with the make option.
Once given what the password is used for, it will continue on like the make option and take you back to the main 4 options.
### View
When running this option, it will list all of your passwords in the terminal sorted alphabetically by what the password is used for.
### Quit
Exits the program.
