TotalGuestsMoney = 0

GuestsCount = int(input("Hello! How many guests are you?: "))
print("Alright! So:", GuestsCount, "guests!")
print("--------------------------------------")

for i in range(GuestsCount):
    name = input("Give Me Your Name: ")
    age = int(input("Give Me Your Age: "))
    if age <18:
        TotalGuestsMoney += 15
        print("Pays 15$")
    else:
        TotalGuestsMoney += 25
        print("Pays 25$")

Nights = int(input("How many nights are you staying?: "))

NightsAmount = TotalGuestsMoney * Nights

print("Total Amount:", NightsAmount,"$")
