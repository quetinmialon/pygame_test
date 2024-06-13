from tkinter import *

window = Tk()

window.title('bagarre')
window.geometry('1080x720')
window.minsize(480,360)
window.iconbitmap('')
window.config(background='#6C6C6C')


label_window = Label(window, text='coucou', font=('Courrier',40),bg='#6C6C6C',fg='white').pack(expand = YES)

window.mainloop()




class Player : 

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack

        print('bienvenue au joueur', pseudo,'point de vie :',health,' attaque :', attack )
    
    def get_pseudo (self):
        return self.pseudo
    
    def get_health(self):
        return self.health
    
    def get_attack(self):
        return self.attack
    
    def damage (self, damage):
        self.health -= damage

    def attack_player(self, target_player):
        target_player.damage(self.attack)

player = Player('Quentin_Le_Serpentard', 500, 50)

class Warrior (Player):
    def __init__(self, pseudo, health, attack, shield):
        super.__init__(pseudo, health, attack)
        self.shield = shield
    
    def damage (self, damage) :
        if self.armor > 0 :
            self.armor  -= 1
            damage = 0
        super().damage(damage)

    def get_shield (self,shield):
        self.shield += shield 

