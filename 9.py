import os
import shutil

"""Create directory """
# os.mkdir(r"C:\Users\sk21163\Downloads\sunitha")
# print("created")

"""rename directory"""
#os.renames(r"C:\Users\sk21163\Downloads\sunitha", r"C:\Users\sk21163\Downloads\sunithanew")
#print("renamed")

"""Delete directories"""
# os.rmdir(r"C:\Users\sk21163\Downloads\sunitha.txt")
# print("deleted")

"""move directory """
src = (r"C:\Users\sk21163\Downloads\sunithanew")
tar = (r"C:\Users\sk21163\Desktop\sunithanew")
print("moved")

shutil.move(src, tar)
#print(os.listdir(r"C:\Users\sk21163\Downloads\sunitha"))
