import random
import os
# The following line does work, but Pylance does not recognize it
from cryptography.fernet import Fernet # type: ignore

chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = [';',':','/','?','\\','|','[','{','}','=','+','-','_',')','(','*','&','^','$','#','@','!','~',]
nums = ['1','2','3','4','5','6','7','8','9','0']
options = [1,2,3,4] # lower, capital, symbol, number

# File information. Path example: Here/Is/My/Path/
encryptor_path = ""
password_path = ""
encryptorName = "encryptor.bin"
passwordFileName = "password.bin"

def main(key):
    cipher = Fernet(key)
    yesNo = "no"
    option = input("Would you like to import, make, or view a password? Or would you like to quit? ")
    if option.lower() == "make":
        passwordLength = int(input("How long would you like your password to be: "))
        while yesNo.lower() == "no":
            # Generates the passwords using Symbols, Numbers, and Characters
            password = passwordMake(passwordLength)
            
            # If user inputs yes, asks for use. If user inputs anything else, regenerates password
            yesNo = input(f"Your generated password is {password}. Would you like to use this password (yes or no)? ")
            if yesNo.lower() == 'yes':

                # Figures out what the use is for so the user can see that when viewing
                use = input("What is this password for: ")
                line = f"Password: {password}||Use: {use}"
                encrypted = cipher.encrypt(line.encode())
                path = password_path + passwordFileName

                # Opens the password file and writes to it
                with open(path, 'ab') as passwordFile:
                    passwordFile.write(encrypted + b'\n')
                    passwordFile.close()
                    print("Password added to file.\n")

    elif option.lower() == "import":
        # Asks the user for the password they want to import and its use
        password = input("What is the password you are importing? ")
        use = input("What is this password being used for? ")
        line = f"Password: {password}||Use: {use}"
        encrypted = cipher.encrypt(line.encode())
        path = password_path + passwordFileName

        # Opens the password file and writes to it
        with open(path, 'ab') as passwordFile:
            passwordFile.write(encrypted + b'\n')
            passwordFile.close()
            print("Password added to file.\n")

    elif option.lower() == "view":
        path = password_path + passwordFileName
        passwordArr = []
        splitArr = []
        if os.path.exists(path): # If a password file exists
            with open(path, 'rb') as passwordFile:
                for line in passwordFile:
                    decrypted = cipher.decrypt(line).decode()
                    splitArr = decrypted.split('||')
                    splitArr = [splitArr[0], splitArr[1].split(' ')]
                    passwordArr.append(splitArr)
                passwordFile.close()
            passwordArr.sort(key=lambda x: x[1][1])
            for item in passwordArr:
                print(f"{item[0]} {item[1][0]} {item[1][1]}")

        else: # If a password file does not exist
            print("Please import or add a password first.")
            exit()
    elif option.lower() == "quit":
        print("Quitting")
        return 0
    else:
        print("Invalid option. Please try again")
        return 1
    return 2

def passwordMake(length):
    password = ""
    while length != 0:
        charType = random.choice(options)
        if charType == 1:
            char = random.choice(chars)
        elif charType == 2:
            char = (random.choice(chars)).upper()
        elif charType == 3:
            char = random.choice(symbols)
        elif charType == 4:
            char = random.choice(nums)
        password += char
        length -= 1
    return password

if __name__ == "__main__":
    key = ""
    # Does the encryption key file exist in the given path with the given name?
    fullPath = encryptor_path + encryptorName
    if not os.path.exists(fullPath): # Does not exist
        with open(fullPath, 'xb') as keyFile:
            key = Fernet.generate_key()
            keyFile.write(key)
            keyFile.close()
    else: # Exists
        with open(fullPath, 'rb') as keyFile:
            key = keyFile.readline()
            keyFile.close()
    while True:
        status = main(key)
        if status == 0 or status == 1:
            break
