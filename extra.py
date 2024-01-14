import random

airlines1 = [
    "London",
    "Delhi",
    "Moscow",
    "Sao Paulo",
    "Dubai",
    "Los Angeles",
    "Washington DC",
    "Houston",
    "San Francisco",
    "Miami"
]
airlines2 = [
    "Paris",
    "Istanbul",
    "Chicago",
    "Tokyo",
    "Denver",
    "Shanghai",
    "Bangkok",
    "Seoul",
    "New York City",
    "Beijing",
]

all_airways = dict(zip(airlines1, airlines2))

# Print both airline list and generated times simultaneously
price = {
    "From London to Paris": 100,
    "From Delhi to Istanbul": 400,
    "From Moscow to Chicago": 600,
    "From Sao Paulo to Tokyo": 1200,
    "From Dubai to Denver": 800,
    "From Los Angeles to Shanghai": 1000,
    "From Washington DC to Bangkok": 900,
    "From Houston to Seoul": 1100,
    "From San Francisco to New York City": 200,
    "From Miami to Beijing": 1300
}

flight_codes = {
    "From London to Paris": "232",
    "From Delhi to Istanbul": "092",
    "From Moscow to Chicago": "536",
    "From Sao Paulo to Tokyo": "978",
    "From Dubai to Denver": "264",
    "From Los Angeles to Shanghai": "876",
    "From Washington DC to Bangkok": "374",
    "From Houston to Seoul": "164",
    "From San Francisco to New York City": "809",
    "From Miami to Beijing": "765"
}
card_list = ["American Express", "JCB", "Union Pay", "Visa", "Master card"]
iterate = iter(flight_codes.values())


def air_lines():
    for key, value in all_airways.items():
        print(f"\nFrom  {key}  to  {value}  |#{next(iterate)}")
        hour = random.randint(1, 12)
        minute = random.randint(0, 59)
        am_pm = random.choice(['AM', 'PM'])
        time = f"{hour:02d}:{minute:02d} {am_pm}"
        print("TIMINGS")
        print(time)
        for j in range(1):
            print("-------------------------------------")


def Economy_class(user_input):
    global payment
    if user_input in price.keys():
        payment =  price.get(user_input)
        return payment


# noinspection PyGlobalUndefined
def Buisness_class(user_input):
    global flight_price
    global payment
    if user_input in price.keys():
        flight_price = price.get(user_input)
    payment =  flight_price * 3
    return payment


# noinspection PyGlobalUndefined
def First_class(user_input):
    global flight_price
    global payment
    if user_input in price.keys():
        flight_price = price.get(user_input)
    payment =  flight_price * 10
    return payment

def payment_method():
    P_pay = input("whould you like to pay now with card or in person at the airport\nplease type(pay now  card or pay later): ")
    while True:
        P_card = input(f"What will you pay with your total is  \nwe support these card[American Express, Master card, Visa, Union Pay, JCB]: ")
        if P_card not in card_list:
            print("We do not support this card\nenter again")

        else:
            break

nationalities = [
    "American",
    "Argentinian",
    "Australian",
    "Austrian",
    "Belizean",
    "Brazilian",
    "British",
    "Bulgarian",
    "Canadian",
    "Chilean",
    "Chinese",
    "Colombian",
    "Costa Rican",
    "Croatian",
    "Cuban",
    "Czech",
    "Danish",
    "Egyptian",
    "Estonian",
    "Finnish",
    "French",
    "German",
    "Greek",
    "Guatemalan",
    "Honduran",
    "Hungarian",
    "Indian",
    "Indonesian",
    "Irish",
    "Israeli",
    "Italian",
    "Jamaican",
    "Japanese",
    "Kenyan",
    "Latvian",
    "Lithuanian",
    "Macedonian",
    "Malaysian",
    "Mexican",
    "Montenegrin",
    "Nigerian",
    "Nicaraguan",
    "Norwegian",
    "Panamanian",
    "Peruvian",
    "Philippine",
    "Polish",
    "Portuguese",
    "Puerto Rican",
    "Romanian",
    "Russian",
    "Saudi Arabian",
    "Serbian",
    "Singaporean",
    "Slovak",
    "Slovenian",
    "South African",
    "South Korean",
    "Spanish",
    "Swedish",
    "Swiss",
    "Thai",
    "Trinidadian",
    "Turkish",
    "Venezuelan",
    "Vietnamese",
    "Pakistan",
]