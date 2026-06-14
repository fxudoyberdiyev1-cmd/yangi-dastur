import random

print("Bolalar o'quv dasturiga xush kelibsiz!")

def kundalik():
    print("\n--- Kundalik bo'limi ---")
    print("Bugungi vazifalar:")
    print("1. Matematikadan misollar yechish.")
    print("2. Mashinalar va motorlar qanday ishlashi haqida kitob o'qish.")

def matematika():
    print("\n--- Matematika mashqi ---")
    
    # Kompyuter 5 dan 30 gacha bo'lgan ixtiyoriy sonlarni tanlaydi
    mashinalar = random.randint(5, 30)
    motorlar = random.randint(5, 30)
    
    print(f"Tasavvur qiling: Poygada {mashinalar} ta sport mashinasi qatnashyapti.")
    print(f"Garajda esa ularga zaxira sifatida {motorlar} ta yangi motor olib kelindi.")
    
    togri_javob = mashinalar + motorlar
    javob = input("Jami bo'lib nechta mashina va motor bo'ldi? Javobni hisoblab yozing: ")
    
    # Javobni tekshiramiz
    if javob == str(togri_javob):
        print("Qoyilmaqom! To'ppa-to'g'ri topdingiz! 🏆")
    else:
        print(f"Xato. To'g'ri javob {togri_javob} edi. Hechqisi yo'q, keyingi safar albatta topasiz!")

while True:
    print("\nQaysi bo'limga kiramiz?")
    print("1. Kundalik")
    print("2. Matematika")
    print("3. Dasturdan chiqish")
    
    tanlov = input("Raqamni tanlang (1/2/3): ")
    
    if tanlov == '1':
        kundalik()
    elif tanlov == '2':
        matematika()
    elif tanlov == '3':
        print("Xayr! Yana kutib qolamiz.")
        break
    else:
        print("Noto'g'ri raqam. Iltimos, faqat 1, 2 yoki 3 ni bosing.")