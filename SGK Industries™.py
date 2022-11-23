import matplotlib.pyplot as plt
import pandas as pd
import time
import sys

print('''

███████╗ ██████╗ ██╗  ██╗    ██╗███╗   ██╗██████╗ ██╗   ██╗███████╗████████╗██████╗ ██╗███████╗███████╗
██╔════╝██╔════╝ ██║ ██╔╝    ██║████╗  ██║██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔══██╗██║██╔════╝██╔════╝
███████╗██║  ███╗█████╔╝     ██║██╔██╗ ██║██║  ██║██║   ██║███████╗   ██║   ██████╔╝██║█████╗  ███████╗
╚════██║██║   ██║██╔═██╗     ██║██║╚██╗██║██║  ██║██║   ██║╚════██║   ██║   ██╔══██╗██║██╔══╝  ╚════██║
███████║╚██████╔╝██║  ██╗    ██║██║ ╚████║██████╔╝╚██████╔╝███████║   ██║   ██║  ██║██║███████╗███████║
╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
All Fake copyrights are Legally Reserved by the SGK Industries™

''')

print(''' _______________________________________________
|                                               |
|Hello User!! Welcome to SGK Industries™        |
|                                               |
|Please read and follow the below instructions: |
|_______________________________________________|


# Type "G" if you are a Guest User.

# Type "A" if you are an Admin or a Registered User.''')
print()
print()

#Who are You??
User=str(input("Please type your User Status: "))
print()

#Reading the CSV File
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
Read=pd.read_csv("<< FilePath >>\Visitors.csv")

#I am an Admin.
if ((User=="A") or (User=="a")):
    print()
    Admin=str(input("Username: "))
    Password=int(input("Password: "))
    if (Admin=="Sukant") and (Password==1234):
        print()
        print("List of the Guest Users")
        print()
        print(Read)
        print()
        print()
            
        
    else:
        print("(⌐■_■)")
        print("Hey! Don't try to be smart!! I might be a program but I know that you are not an Admin.")
        print("Now run the program again!!")
        print("And this time be Honest.")

#I am a Guest.
elif ((User=="G") or (User=="g")):
    print("Hi _______!  Wait a second who are you? ")
    print("Tell me something about yourself.")
    print()
    Name=str(input("My name is: ").capitalize())
    print()
    Age=int(input("I am this many years old: "))
    print()
    Gender=str(input("I am (M/F/O): ").capitalize())
    print()
    Email=str(input("My Email address is: ").lower())
    print()
    print("I live in:- ")
    print()
    Country=str(input("Country: ").capitalize())
    State=str(input("State: ").capitalize())
    City=str(input("City: ").capitalize())
    print()
    Profession=str(input("I am a (Student/ Business Man/ MIB): ").capitalize())
    
    #Saving the CSV File
    Guest={" Name " :Name, " Age ":Age, " Gender ":Gender, " Email ":Email, " Country ":Country, " State ":State, " City ":City, " Profession ":Profession}
    Df=pd.DataFrame(Guest, columns=[" Name "," Age "," Gender "," Email "," Country "," State "," City "," Profession "], index=["Guest"])
    Df.to_csv("<< FilePath >>\Visitors.csv", mode="a", header=False, index=True)
 
    # I am MIB
    if (Profession.startswith("M") or Profession.startswith("S") or Profession.startswith("B") or Profession.startswith("m") or Profession.startswith("b") or Profession.startswith("s")):
        print()
        print()
        print("        _.---._              ")
        print("     .-' ((O)) '-.           ")
        print("      \ _.\_/._ /            ")
        print("       /..___..\       PAL I don't Trust you, you need to give ME some ID First!!      ")
        print("       ;-.___.-;             ") 
        print("      (| e ) e |)     .;.    ")
        print("       \  /_   /      ||||   ") 
        print("       _\__-__/_    (\|'-|   ")
        print("     /` / \V/ \ `\   \ )/    ")
        print("    /   \  Y  /   \  /=/     ")
        print("   /  |  \ | / {}  \/ /      ")
        print("  /  /|   `|'   |\   /       ")
        print("  \  \|    |.   | \_/        ")
        print("   \ /\    |.   |            ")
        print("    \_/\   |.   |            ")
        print("   // ',__.'.__,'            ")
        print("  //   |   |   |             ")
        print(" //    |   |   |             ")
        print("(/     |   |   |             ")
        print("       |   |   |             ")
        print("       | _ | _ |             ")
        print("       |   |   |             ")
        print("       |   |   |             ")
        print("       |   |   |             ")
        print("       |___|___|             ")
        print("       /  J L  \             ")
        print("      (__/   \__)            ")
        print("******************************************************************************************************************")
        print()
        time.sleep(6)
        print()
        print('''  , , ,   .-'"""'-.    , , ,  ''')
        print(" \\|/   .'         '.  \|//        Ha Ha!! I'm just kidding")
        print("   \-;-/   ()   ()   \-;-/     ")
        print("   // ;               ; \\     ")
        print("  //__; :.         .; ;__\\    ")
        print(" `-----\'.'-.....-'.'/-----'   ")
        print("        '.'.-.-,_.'.'          ")
        print("          '(  (..-'            ")
        print("            '-'                ")
        time.sleep(4)
        print()
        print(" -----------------------------------------------------------------------------------------")
        print("|Now, since I've got to know you a bit, What would you like to know about SGK Industries™ |")
        print(" -----------------------------------------------------------------------------------------")
        print()
        print("Type 1 for SGK Industries™ Profits of the previous years.")
        print("Type 2 for SGK Industries™ Current Balance Sheet.")
        print("Type any-other number to Exit.")
        print()
        Choice=int(input("Please type your answer here: "))
        print()


        #Profits
        if Choice==1:
            y=[10,20,30,20,40,50,30,70,60,50,80,90,100,80,120]
            x=[" 2006 "," 2007 "," 2008 "," 2009 "," 2010 "," 2011 "," 2012 "," 2013 "," 2014 "," 2015 "," 2016 "," 2017 "," 2018 "," 2019 "," 2020 "]
            plt.plot(x, y, marker="D", color="Green")
            plt.xlabel("Years ---->")
            plt.ylabel("Profits (in Lakhs) ---->")
            plt.title("Profits of SGK Industries™")
            plt.grid(True)
            plt.show()
            print()
            print()

        
        #Balance Scheet
        elif (Choice==2):
            print()
            print("                                 Balance Sheet of SGK Industries™                                                ")
            print("                                          as on 31/03/2020                                                      ")
            print(" ____________________________________________________________________________________________________________ ")
            print("|         LIABILITIES                    |      ₹      |                ASSETS                 |      ₹      |")
            print("| _______________________________________|_____________|_______________________________________|_____________|")
            print("| Capitals:                              |             | Cash in Hand                          |   2,50,000  |")
            print("| Sukant                     3,00,000    |             | Land and Building                     |   1,90,000  |")
            print("| Gursimran                  3,00,000    |             | Stock                                 |   1,22,000  |")
            print("| Kashvi                     3,00,000    |             | Scooter                               |     57,000  |")
            print("|                           ____________ |             | Bills Receivable                      |     65,000  |")
            print("|                            9,00,000    |             | Furniture and Fixtures                |   4,50,000  |")
            print("|(+) Net Profit                27,000    |             | Prepaid Expenses                      |      7,500  |")
            print("|                           ____________ |   9,27,000  | Debtors                    1,50,000   |             |")
            print("| Reserves & Surplus                     |   1,75,000  |(-)provision for D/D          23,500   |             |")
            print("| Outstanding Expenses                   |     57,000  |                           ____________|   1,26,500  |")
            print("| Trade Creditors                        |   1,00,000  |                                       |             |")
            print("| Bills Payable                          |      9,000  |                                       |             |")
            print("|                                        |_____________|                                       |_____________|")
            print("|                                        |  12,68,000  |                                       |  12,68,000  |")
            print("|________________________________________|_____________|_______________________________________|_____________|")
            print()
            print()
            print()
            

    #I am Not MIB
    else:
        print("Sorry Something went Wrong....")
        sys.exit()

#I am No-one
else:
    print("Sorry Something went Wrong....")
    sys.exit()
