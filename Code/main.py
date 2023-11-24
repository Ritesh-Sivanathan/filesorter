import os, shutil, sys

try:

    CWD = os.getcwd()
    FOLDERS_CREATED = {}

    def create():

        CWD_CHOICE = input(f"Change the directory executed?: Directory Name: {CWD} | y/n ") 

        if CWD_CHOICE.lower() == 'y':
            CWD_DIRECTORY = input("Change directory name: ")
            shutil.move(f'{CWD}/{"main.py"}', f'{CWD_DIRECTORY}/{"main.py"}')
        
        CHOICE = input("View or Create?: ((v)iew / (c)reate): ")
        
        if CHOICE == 'v':
            reconfigure()

        FOLDER_COUNT = int(input("# of Folders: "))

        for FOLDER_NUM in range(1, FOLDER_COUNT+1):

            CREATE_FOLDERS = input("Create folders: ")
            FOLDERS_CREATED[CREATE_FOLDERS] = 0
            print(f"{CREATE_FOLDERS} | Folder # {FOLDER_NUM}")

        exit

    def values():

        for DIRECTORY in FOLDERS_CREATED:
            FOLDERS_CREATED[DIRECTORY] = input(f"File extension {DIRECTORY}: (.png, .svg): ")

    def folder():
        PARENT_DIR = CWD
        for DIRECTORY in FOLDERS_CREATED:
            path = os.path.join(PARENT_DIR, DIRECTORY)
            os.mkdir(path)

    def files():
        FILES = os.listdir(CWD)
        SPLIT_FILES = []
        DOT_REACHED = 0


        for FILE in FILES:
            DOT_REACHED = 0
            for INDEX, CHAR in enumerate(FILE):
                if CHAR == '.':
                    DOT_REACHED = 1

                if DOT_REACHED == 1:
                    SPLIT_FILES.append(FILE[INDEX:])

                    for KEY, VALUE in FOLDERS_CREATED.items():
                        if VALUE == SPLIT_FILES[-1]:
                            shutil.move(f'{CWD}/{FILE}', f'{CWD}/{KEY}/{FILE}')

                    break

        print('Files moved') 
    
    def reconfigure():
        print(f"Folders in current directory: {[name for name in os.listdir('.') if os.path.isdir(name)]}")
        
        main()  
            

    def main():

        create()
        folder()
        values()
        files()

    main()

except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print (message)