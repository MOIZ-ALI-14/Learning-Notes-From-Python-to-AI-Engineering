days = {
    "sanwar": "monday",
    "mangal": "tuesday",
    "budh": "wednesday",
    "jumeraat": "thursday",
    "jumma": "friday",
    "hafta": "saturday",
    "itwar": "sunday",
}
while True:
    lafz = input("Daso ki translate kran: ")
    try:
        print(days[lafz])
        break
    except KeyError:
        print("sai lafz daso yaar")
