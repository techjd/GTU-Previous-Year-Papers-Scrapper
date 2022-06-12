from oldpapers import OldPaper
from newpapers import NewPaper
import os


class StartOldPaper:

    def __init__(self, folder_path, codes, name):
        self.folder_path = folder_path
        self.codes = codes
        self.name = name

    def start(self):
        oldpaper = OldPaper(self.folder_path, self.codes, self.name)
        oldpaper.start()


class StartNewPaper:

    def __init__(self, folder_path, codes, name):
        self.folder_path = folder_path
        self.codes = codes
        self.name = name

    def start(self):
        newpaper = NewPaper(self.folder_path, self.codes, self.name)
        newpaper.start()


# Get Subject Name


print('Enter Subject Name')
subjectName = input()

# Get All Subject Codes
print('Enter All Subject Codes of ' + subjectName + ' at Once')
subjectCodes = input().split(' ')

current_directory = os.getcwd()

path = os.path.join(current_directory, subjectName)
os.makedirs(path, exist_ok=True)

path_for_old_paper = os.path.join(path, 'Old Papers ( From 2017 Onwards )')
os.makedirs(path_for_old_paper, exist_ok=True)

path_for_new_paper = os.path.join(path, 'New Papers')
os.makedirs(path_for_new_paper, exist_ok=True)

StartOldPaper(path_for_old_paper, subjectCodes, subjectName).start()
StartNewPaper(path_for_new_paper, subjectCodes, subjectName).start()
