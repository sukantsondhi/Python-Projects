import matplotlib.pyplot as plt
import pandas as pd
import time
import sys
import csv


print('''                                                                                    
                                                                                      
   SSSSSSSSSSSSSSS    KKKKKKKKK    KKKKKKK   YYYYYYY       YYYYYYY                          
 SS:::::::::::::::S   K:::::::K    K:::::K   Y:::::Y       Y:::::Y                          
S:::::SSSSSS::::::S   K:::::::K    K:::::K   Y:::::Y       Y:::::Y                          
S:::::S     SSSSSSS   K:::::::K   K::::::K   Y::::::Y     Y::::::Y            +++++++       
S:::::S               KK::::::K  K:::::KKK   YYY:::::Y   Y:::::YYY            +:::::+       
S:::::S                 K:::::K K:::::K         Y:::::Y Y:::::Y               +:::::+       
 S::::SSSS              K::::::K:::::K           Y:::::Y:::::Y          +++++++:::::+++++++ 
  SS::::::SSSSS         K:::::::::::K             Y:::::::::Y           +:::::::::::::::::+ 
    SSS::::::::SS       K:::::::::::K              Y:::::::Y            +:::::::::::::::::+ 
       SSSSSS::::S      K::::::K:::::K              Y:::::Y             +++++++:::::+++++++ 
            S:::::S     K:::::K K:::::K             Y:::::Y                   +:::::+       
            S:::::S   KK::::::K  K:::::KKK          Y:::::Y                   +:::::+       
SSSSSSS     S:::::S   K:::::::K   K::::::K          Y:::::Y                   +++++++       
S::::::SSSSSS:::::S   K:::::::K    K:::::K       YYYY:::::YYYY                              
S:::::::::::::::SS    K:::::::K    K:::::K       Y:::::::::::Y                              
 SSSSSSSSSSSSSSS      KKKKKKKKK    KKKKKKK       YYYYYYYYYYYYY
''')

print('''                                          ''')
print('''                                          ''')
print('''                     ,o8888boo.           ''')
print('''               b   d88888888888b          ''')
print('''              d88oo88888888888888o.       ''')
print('''     /\      8888888888P" Y88888888o,b    ''')
print('''  _--/ \     88888888P".''.Y88P" Y8888               Hi! Welcome to SKY+                                                  ''')
print(''' /__/   "\   Y888888P '.-.  Y" _. Y88P    ''')          
print('''<______   "\  "8888P  /  |    '_ '$88                My name is Astrix and I'm here to help you.                          ''')  
print('''       \,    \  888b  Bo |    / \ a8Z     ''')             
print('''         \     \ 8|<  B8/     Bo||P"                 Please read the instructions and type in your response accordingly.  ''')
print('''          '.   /'--\     ._   P8/|        ''')               
print('''            \ /     '\_  \     _/         ''')
print('''             \        /'-----.'           ''')
print('''              \      |  /  |\ \                      #If you want a new connection please type "N"                         ''')
print('''               '-./  | / \./|  \          ''')
print('''                  |  \/   |/    |                    #If you already have a connection and want to alter it then please type "E" ''')
print('''              ,---|       /\__./          ''')
print('''            _/    '-.___./ ;   \                     #If you are a Developer please type "D" ''')
print('''           /             \  \   \         ''')
print('''      --._/               \  \   \_                  #If you want to Register as a Developer type "R" ''')
print('''       \                   \._\    "--.   ''')
print('''        \                    _''-._<''    ''')
print('''         \                  /"            ''')
print('''          '-.            .-"              ''')   
print('''             "----._____-|                ''')
print('''                |    |   |                ''')
print('''               |     |   |                ''')
print('''               |     |   |                ''')
print('''               |      I  |                ''')
print('''               |      |   T               ''')
print('''               |      |   |               ''')
print('''               |      |   |               ''')
print('''               |      |    \              ''')
print('''               |      "|    |             ''')
print('''               |       |    Z             ''')
print('''                "-.__.-P__.--             ''')
print('''                                          ''')
print()
print()
print()


#What are you?
User=input(str("Please type in your response: "))
print()  
print()


#Reading the New Developers CSV File
col_list=["Username","Password"]
DCSV=pd.read_csv("<< FilePath >>\Developers.csv", usecols=col_list)
usn_list=list(DCSV["Username"])     #Storing Usernames in lists
pwd_list=list(DCSV["Password"])     #Storing Password in lists
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


#Reading the User CSV File
CSV=pd.read_csv("<< FilePath >>\SKY.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


#Developer
if (User=="D") or (User=="d"):
    print()
    AA=str(input("Username: "))
    BB=int(input("Password: "))
    print()
    if (AA in usn_list) and (BB in pwd_list):
        print()
        print("List of the Users")
        print()
        print(CSV)
        print()
        print()

    else:
        print("(⌐■_■)")
        print("Hey! Don't try to be smart!! I might be a program but I know that you are not an Admin.")
        print("Now run the program again!!")
        print("And this time be Honest.")


#New Developer
elif (User=="R") or (User=="r"):
    print("Hi Buddy!! Welcome to SKY+")
    print("Lets get you started by setting up your Username and Password.")
    print()
    AA=str(input("Username: "))
    BB=int(input("Password: "))
    New_Developer={"Username":AA,"Password":BB}
    NCSV=pd.DataFrame(New_Developer, columns=["Username","Password"], index=["New Developer"])
    NCSV.to_csv("<< FilePath >>\Developers.csv", mode="a", header=False, index=True)
    print()
    print("You have successfuly registered yourself as a Developer.")
    print("Please run the Programme again.")
    print()

    
#Existing User
elif (User=="E") or (User=="e"):
    print()
    EUsername=str(input("Username: "))
    EPassword=str(input("Password: "))

    #Correct Username
    if EUsername==("User") and EPassword==("User"):
        A=['Chanel','Type','Price']
        B=['A1 TV channel','Aaj Tak','ABP News','Aryan TV','CNBC Awaaz','DD News','Dilli Aaj Tak','India News','India TV','Jan TV','Janta TV',
                     'Khabar Bharti']
        C=['News','News','News','News','News','News','News','News','News','News','News','News']
        D=[13.4,18.4,11.4,13.1,16.4,16.4,15.9,19.3,13.4,13.6,11.8,14.8]
        E={'Chanel':B,"Type":C,"Price":D}
        F=pd.DataFrame(E, columns=A)
        print(F)
        print()
        G=int(input("Please type the number of the Chanel you would like to remove: "))
        print()
        print(F.drop(index=G))
        print()
        print("Thank you for your valuable time. Our Customer Service Provider will soon be in touch with you within 2-3 Working Days.")
        print("Have a Nice Day.")

    #Incorrect Username
    else:
        print()
        print("Sorry Something went wrong. Please try again after some time.")
        print("Have a Nice Day.")

        
#New User
elif (User=='N') or (User=='n'):
    print("Inorder to get you a new connection I need some details.")
    print()
    print()
    Name=str(input("Name: ").capitalize())
    print()
    print()
    print()
    print("        _.---._              ")
    print("     .-' ((O)) '-.           ")
    print("      \ _.\_/._ /            ")
    print("       /..___..\       PAL I don't Trust you, you need to give ME some ID First!! ")
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
    time.sleep(1)
    print()
    print(''', , ,    .-'"""'-.   , , ,  ''')
    print("  \\|/  .'         '.  \|//        Ha Ha!! I'm just kidding. Keep filling the Details")
    print("   \-;-/   ()   ()   \-;-/     ")
    print("   // ;               ; \\     ")
    print("  //__; :.         .; ;__\\    ")
    print(" `-----\'.'-.....-'.'/-----'   ")
    print("        '.'.-.-,_.'.'          ")
    print("          '(  (..-'            ")
    print("            '-'                ")
    time.sleep(1)
    print()
    print()
    Age=int(input("Age: "))
    print()
    Gender=str(input("I am (M/F/O): ").capitalize())
    print()
    Email=str(input("Email: ").lower())
    print()
    Phone=int(input("Phone: "))
    print()
    Country=str(input("Country: ").capitalize())
    State=str(input("State: ").capitalize())
    City=str(input("City: ").capitalize())
    print()
    print()

    #Saving the CSV File
    Users={"Name" :Name, "Age":Age, "Gender":Gender, "Email":Email, "Phone":Phone, "Country":Country, "State":State, "City":City}
    Df=pd.DataFrame(Users, columns=["Name","Age","Gender","Email","Phone","Country","State","City"], index=["New User"])
    Df.to_csv("<< FilePath >>\Sky.csv", mode="a", header=False, index=True)

    #Would you like to know about us
    print("Hi",Name,"would you like to know a bit more about SKY+ before installing/ordering a connection.")
    SKY=str(input("(Yes/No): "))
    print()
    
    #If yes to more info
    if (SKY.startswith("Y") or SKY.startswith("y")):
        print("#Type 1 for all the countries we cover.")
        print("#Type 2 for our Growth Charts.")
        print("#Type 3 for the varriety of chanels we offer.")
        print("#Type 4 to see all.")
        print("#Type 5 to Exit.")
        print()
        print()
        View=int(input("What would you like to view: "))
        print()
        
        #Countries we cover
        if View==1:
            Countries=pd.DataFrame(['India','Switzerland','Canada','Japan','Germany','Australia','United Kingdom','United States','Sweden','New Zealand',
                                'Norway'], columns=["Countries"])
            print(Countries)
            print()
            print("Thank you", Name,"for your valuable time. Our Customer Service Provider will soon be in touch with you within 2-3 Working Days.")
            print("Have a Nice Day.")
            sys.exit()

        #Growth Charts    
        elif View==2:
            y=[10,20,30,20,40,50,30,70,60,50,80,90,100,80,120]
            x=[" 2006 "," 2007 "," 2008 "," 2009 "," 2010 "," 2011 "," 2012 "," 2013 "," 2014 "," 2015 "," 2016 "," 2017 "," 2018 "," 2019 "," 2020 "]
            plt.plot(x, y, marker="D", color="Green")
            plt.xlabel("Years ---->")
            plt.ylabel("Growth Rate (in Lakhs) ---->")
            plt.title("Growth Chart of SKY+")
            plt.grid(True)
            plt.show()
            print()
            print()
            print("Thank you", Name,"for your valuable time. Our Customer Service Provider will soon be in touch with you within 2-3 Working Days.")
            print("Have a Nice Day.")
            sys.exit()

        #Varriety of Channels
        elif View==3:
            X=[50,10,20,14,16]
            Y=['Entertainment','Religious','News','Kids','Games']
            plt.pie(X,labels=Y, shadow=True, startangle=190)
            plt.show()
            print()
            print()
            print("Thank you", Name,"for your valuable time. Our Customer Service Provider will soon be in touch with you within 2-3 Working Days.")
            print("Have a Nice Day.")
            sys.exit()

        #All
        elif View==4:
            print("Countries we Serve")
            print()
            Countries=pd.DataFrame(['India','Switzerland','Canada','Japan','Germany','Australia','United Kingdom','United States','Sweden','New Zealand',
                                'Norway'], columns=["Countries"])
            print(Countries)
            print()
            print()
            print("Our Growth Charts")
            print()
            y=[10,20,30,20,40,50,30,70,60,50,80,90,100,80,120]
            x=[" 2006 "," 2007 "," 2008 "," 2009 "," 2010 "," 2011 "," 2012 "," 2013 "," 2014 "," 2015 "," 2016 "," 2017 "," 2018 "," 2019 "," 2020 "]
            plt.plot(x, y, marker="D", color="Green")
            plt.xlabel("Years ---->")
            plt.ylabel("Growth Rate (in Lakhs) ---->")
            plt.title("Growth Chart of SKY+")
            plt.grid(True)
            plt.show()
            print()
            print()
            print("Chanels we Offer")
            X=[50,10,20,14,16]
            Y=['Entertainment','Religious','News','Kids','Games']
            plt.pie(X,labels=Y, shadow=True, startangle=190)
            plt.show()
            print()
            print()
            sys.exit()
            

        #Wrong input
        else:
            print()
            print("Thank you", Name,"for your valuable time. Our Customer Service Provider will soon be in touch with you within 2-3 Working Days.")
            print("Have a Nice Day.")
            sys.exit
                
    #If no to more info
    else:
        sys.exit()
        print()
        print()
        print("Thank you", Name,"for your valuable time. Our Customer Service Provider will soon be in touch with you within 2-3 Working Days.")
        print("Have a Nice Day.")
        

#Wrong User Type
else:
    print("Something went wrong!! Pleae try again Later.")
    sys.exit()
        
      



    















