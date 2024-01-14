# # # # ############## for functions and modules ###########################################################
import time
import extra as extra
# # #########################################################################
print("\n-----------------STELLA'S CELESTIAL AIRLINE-----------------")
while True:
    user_input_SIE = input("\nEnter your Email: ")
    if user_input_SIE.find("@") and user_input_SIE.endswith(".com"):
        break
    else:
        print("-------------------------------------------------------------------")
        print("A Email address should include '@' and '.com' in the end ")
        print("-------------------------------------------------------------------")

user_input_SIP = input("Enter your Password: ")
while True:

    user_input_SIPC = input("Please confirm your password: ")
    if user_input_SIPC == user_input_SIP:
        break
    # Asking for right input
    else:
        print("-------------------------------------")
        print("Please enter the same password!")
        print("-------------------------------------")
print("--------------------------------------")
######## Advertisement
# print("\n------------------ADVERTISEMENT INCOMING------------------")
# time.sleep(1)
# print(" THIS PRODUCT WILL MAKE YOU LOOSE WEIGHT IN \n          ✨THREE DAYS✨")
# time.sleep(1)
####################################################################################
print("-----------------FLIGHTS-----------------")
print("The Available flights are displayed: ")
time.sleep(2)
extra.air_lines()

flight_selection = input("PLease confirm your selection\n(write the code associated with the flight):")


###########noinspection PyGlobalUndefined
def key_checker():
    global selection
    flight = []
    for key, value in extra.flight_codes.items(): #can you add the price?##########################################################################
        if flight_selection == value:
            flight.append(key)
    selection = ''.join(flight)

    return selection


while True:
    if not flight_selection in extra.flight_codes.values():
        print("------------------------------------------")
        print("There are no flights dedicated to this code")
        print("------------------------------------------")
        flight_selection = input("PLease confirm your selection\n(write the code associated with the flight): ")
    else:
        print("------------------------------------------")
        print(f"ok, so you selected;\n{key_checker()}")
        print("------------------------------------------")
        break
###################################################################################11
time.sleep(1)
print("Ok now please give us the following requirements: ")
for i in range(4):
    print(".")
    for j in range(1):
        time.sleep(1)
##########personal information


from msilib.schema import SelfReg
from typing import Self


while True:
    P_Name = input("Your name: ").capitalize()
    if not P_Name.isalpha():
        print("-----------------------------------------------------------------------------------")
        print("The input should contain only letters and more then 3 letters.")
        print("-----------------------------------------------------------------------------------")
    else:
        break

while True:
    P_Age = input("Your age: ")
    if not len(P_Age) > 6 or 20 or P_Age.isdigit():
        print("------------------------------------------------------------")
        print("The input should contain only number and more then 6.")
        print("------------------------------------------------------------")
    else:
        break

while True:
    P_Gender = input("Gender Male/Female: ").lower()
    if P_Gender == 'male' or P_Gender == 'female':
        break
    else:
        print("------------------------------------------------------------")
        print("Please enter a real gender:")
        print("------------------------------------------------------------")

while True:
    P_Nation = input("Please enter your Nationality(Please capitalise the first letter): ")
    if not P_Nation in extra.nationalities:
        print("----------------------------------------------------------------------------------------")
        print("The input should contain only letters and or write your Nationality correctly.")
        print("----------------------------------------------------------------------------------------")
    else:
        break

while True:
    P_Allergies = input("Do you have any of these following Allergies?"'\n'"||Peanuts||Treenuts||Dairy||Gluten||Shellfish"'\n'"Please enter the allergies in letters: ").capitalize()
    if not P_Allergies in ["Peanuts", "Treenuts", "Dairy", "Gluten", "Shellfish"]:
        print("------------------------------------------------------------")
        print("Please spell the allergy correctly.")
        print("------------------------------------------------------------")
    else:
        break

######### flight information
print("------------------------------------------------------------")

while True:
    P_Passport = input("Passport NO: ")
    if not P_Passport.isdigit():
        print("------------------------------------------------------------")
        print("The password should be in numbers: ")
        print("------------------------------------------------------------")
    else:
        break

while True:
    P_luggage_Weight = input("Weight of your luggage: ")
    if P_luggage_Weight > "22":
        print("------------------------------------------------------------")
        input("your baggage exceeds the limit(20kg):")
        print("------------------------------------------------------------")
    else:
        break



while True:
    class_info = input("Which class do you want\na)Economy Class, b)Business Class, c)First Class: ").lower()
    if class_info == "a":
        print(f"The price of this flight will be\n${extra.Economy_class(selection)}")
        break
    if class_info == "b":
        print(f"The price of this flight will be\n${extra.Buisness_class(selection)}")
        break
    if class_info == "c":
        print(f"The price of this flight will be\n${extra.First_class(selection)}")
        break
    else:
        print("There is no class with this attribute", [class_info])

def payment_method():
    P_pay = input("whould you like to pay now with card or in person at the airport\nplease type(pay now  card or pay later): ")
    while True:
        P_card = input(f"What will you pay with your total is {extra.payment} \nwe support these card[American Express, Master card, Visa, Union Pay, JCB]: ")
        if P_card not in extra.card_list:
            print("We do not support this card\nenter again")

        else:
            break

payment_method()


#############################classsssssss##########################################
class P_informal:
    def _init_ (self,name,age,Gender,Nation,Allergies):
        self.name = name
        self.age = age
        self.Gender = Gender
        self.Nation = Nation
        self.Allergies = Allergies

    def print_all(self):
        print(pi.name)
        print(pi.age)
        print(pi.Gender)
        print(pi.Nation)
        print(pi.Allergies)

    
pi=P_informal(P_Name,P_Age,P_Gender,P_Nation,P_Allergies)  

pi.print_all()


class P_pass_wl:
    def _init_(self,Passport_No,Weight_of_luggage):
        self.Passport_No=Passport_No
        self.Weight_of_luggage=Weight_of_luggage

    def Passport_print(self):
        print(p_pass.Passport_No)
        print(p_pass.Weight_of_luggage)

p_pass=P_pass_wl(P_Passport,P_luggage_Weight)
p_pass.Passport_print()