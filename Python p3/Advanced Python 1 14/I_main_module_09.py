# IF __NAME__ == "__MAIN__" - COMPLETE REFERENCE
# ================================================
# WHAT: if __name__ == "__main__" protects code from running
#       when file is imported by another file
# WHY:  When any file is imported - Python reads whole file
#       and all loose code outside functions runs automatically
#       if __name__ protects specific code from running in importer
# WHEN: Use when you have code that should ONLY run in current file
#       Use when you want to test functions in same file
# IMPORTANT: "__main__" is predefined by Python - cannot change it
#            When file runs directly - __name__ = "__main__"
#            When file is imported - __name__ = filename
#            So if condition becomes False when imported


# METHOD 1 - import whole module
# ================================
# BEST METHOD - recommended always
# clearly shows programmer that whole file is being imported
# programmer knows at first glance everything is coming
# use dot notation to access functions
# import main_module
# main_module.myFunc()


# METHOD 2 - from module import specific function
# =================================================
# imports only specific function - looks clean
# BUT secretly Python still reads whole file anyway
# MISLEADING - looks like only one function imported
# but whole file still executes behind scenes
# from main_module import myFunc
# myFunc()


# BEST PRACTICE - always use if __name__ in main_module.py
# =========================================================
# makes BOTH methods safe
# loose code never runs when imported
# clean and professional standard in real projects


def myFunc():
    print("HEllo I am MYFUNC")


myFunc()
if __name__ == "__main__":

    def greet():
        print("Welcome YOu The Original File")

    greet()
    print("this data should only be available in File_1")
