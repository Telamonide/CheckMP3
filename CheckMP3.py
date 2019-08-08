#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------
# Name:        CheckMP3
# Purpose:     Delete non .mp3 files
#
# Author:      Osipenko O.V.
#
# Created:     08.08.2016
# Copyright:   2016 Oleksandr Osipenko <oleosi@meta.ua>
# Licence:     GNU GPL v3.0 https://www.gnu.org/licenses/gpl.html
#----------------------------------------------------------------------


import os
import sys


##---------------------------------------------------------------------
# Function to print list of strings
def printList(prnLst):
    for elm in prnLst:
        printString(elm)
##---------------------------------------------------------------------


##---------------------------------------------------------------------
# Function to print some string
# If string cannot be printed in console
# function print sting with message about error
def printString(mystr):
    try:
        print(mystr)
    except:
        print("Name contain non ASCII symbols")
##---------------------------------------------------------------------


##---------------------------------------------------------------------
# Function to delete users folder
# Return true if folder was deleted
# else return false
def deleteFolder(folderName):
    try:
        os.rmdir(folderName)
        return True
    except os.error as msg:
        return False
##---------------------------------------------------------------------


##---------------------------------------------------------------------
# Clear terminal screen

def clear_screen():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
##---------------------------------------------------------------------


##---------------------------------------------------------------------
# Get path to search folder
def getFolderPath():
    while True:
        folderPath = input("Input folder for check (empty string to exit): ")
        if(folderPath == ""):
            sys.exit(0)
        if(os.path.exists(folderPath)):
            clear_screen()
            break
        else:
            clear_screen()
            print("Folder " + folderPath + " is not exist")
    return folderPath
##---------------------------------------------------------------------


##---------------------------------------------------------------------
# Check path to folder
def checkFoldersPath(pathToFolder):
    if(not os.path.exists(pathToFolder)):
        pathToFolder = getFolderPath()
    return pathToFolder
##---------------------------------------------------------------------


# This pattern is file extention and using for file searching.
# Can be changed to looking for other files.
pattern = r".mp3"

mp3files = []
nonmp3files = []

if len(sys.argv) < 2:
    pathString = getFolderPath()
else:
    pathString = checkFoldersPath(sys.argv[1])

print("Path to folder is: " + pathString)

while True:
    for root, dirs, files in os.walk(pathString):
        for name in files:
            if name.endswith(pattern):
                mp3files.append(os.path.join(root, name))
            else:
                nonmp3files.append(os.path.join(root, name))

    print("mp3 files: ")
    printList(mp3files)

    print("\nOther file(s) and folder(s): ")
    printList(nonmp3files)

    if len(nonmp3files) != 0:
        print("\nStart delete non mp3 file(s) ...")
        for delFile in nonmp3files:
            os.remove(delFile)
            printString("File " + delFile + " was removed!")
    else:
        print("File(s) to remove not detected!")

    alldirsList = []

    for root, dirs, files in os.walk(pathString):
        for fold in dirs:
            alldirsList.append(os.path.join(root, fold))

    alldirsList.reverse()

    print("\nStart delete empty folder(s)")
    i = 0
    for delDir in alldirsList:
        if deleteFolder(delDir):
            printString("Folder " + delDir + " was deleted!")
            i += 1
    if i == 0:
        print("Empty folder(s) not detected!")
    while True:
        ans = input("Check other folder? (y/n)")
        if(ans == "Y" or ans == "y"):
            clear_screen()
            pathString = getFolderPath()
            break
        else:
            if sys.platform == "win32":
                input("\nPress any key...")
            sys.exit(0)
