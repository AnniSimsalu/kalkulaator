import math #impordib math funktsioonid

class cal():   #loob classi nimega cal
    def __init__(self,a,b):   #loob muutujad a ja b
        self.a = a   #nimetab a nimeks self.a
        self.b = b   #nimetab b nimeks self.b

    # Määrab funktsioonid näiteks muutujate liitmine ja lahutamine
    def liitmine(self):
        return self.a + self.b
    def lahutamine(self):
        return self.a - self.b
    def korrutamine(self):
        return self.a * self.b
    def jagamine(self):
        return self.a / self.b
    def jaak(self):
        return self.a % self.b
    def ruutjuur(self):
        return math.sqrt(self.a)
    def astendamine(self):
        return self.a ** self.b
    def protsent(self):
        return self.a / self.b * 100
    def protsendi_liitmine(self):
        return self.a + (self.b * self.a / 100)

a = int(input("Sisesta esimene number: "))   #küsib kasutajalt muutujat a
b = int(input("Sisesta teine number: "))   #küsib kasutajalt muutujat b

kalk = cal(a,b)  #annab cal() klassile ja sinna sisse kuuluvatele muutujatele a ja b nime kalk
while True:  #skript toimib kuni tuleb break käsk
    def menu():  #defineerib menüü
        # annab tekstile nime x ja prindib selle
        x = ('1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Ruutjuure leidmine\n7. Astendamine\n8. Protsent\n9. Protsent liitmine')
        print(x)
    menu()
    valik = int(input('Sisesta üks valikutest: '))  #küsib kasutajalt millist funktsiooni kasutatakse
    # käivitavad vastavalt valitud funktsioonile üleval tehtud classi funktsiooni
    if valik == 1:
        print("Vastus: ",kalk.liitmine())
        break
    elif valik == 2:
        print("Vastus: ",kalk.lahutamine())
        break
    elif valik == 3:
        print("Vastus: ",kalk.korrutamine())
        break
    elif valik == 4:
        print("Vastus: ",kalk.jagamine())
        break
    elif valik == 5:
        print("Vastus: ",kalk.jaak())
        break
    elif valik == 6:
        print("Vastus: ",kalk.ruutjuur())
        break
    elif valik == 7:
        print("Vastus: ",kalk.astendamine())
        break
    elif valik == 8:
        print("Vastus:",kalk.protsent())
        break
    elif valik == 9:
        print("Vastus: ",kalk.protsendi_liitmine())
        break
    else:  #kui sisestati number mis ei ole valikus siis prinditakse all määratud tekst
        print('Sisesta uuesti üks liitmise operaator')
        break
#20:07