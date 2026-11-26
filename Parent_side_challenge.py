from microbit import *
import radio
import random
import music
import time

#Can be used to filter the communication, only the ones with the same parameters will receive messages
#radio.config(group=23, channel=2, address=0x11111111)
#default : channel=7 (0-83), address = 0x75626974, group = 0 (0-255)

#Initialisation des variables du micro:bit
radio.on()
radio.config(group=1)
connexion_established = False
key = "KEYWORD"
connexion_key = None
nonce_list = set()
baby_state = 0
set_volume(100)

def hashing(string):
	"""
	Hachage d'une chaîne de caractères fournie en paramètre.
	Le résultat est une chaîne de caractères.
	Attention : cette technique de hachage n'est pas suffisante (hachage dit cryptographique) pour une utilisation en dehors du cours.

	:param (str) string: la chaîne de caractères à hacher
	:return (str): le résultat du hachage
	"""
	def to_32(value):
		"""
		Fonction interne utilisée par hashing.
		Convertit une valeur en un entier signé de 32 bits.
		Si 'value' est un entier plus grand que 2 ** 31, il sera tronqué.

		:param (int) value: valeur du caractère transformé par la valeur de hachage de cette itération
		:return (int): entier signé de 32 bits représentant 'value'
		"""
		value = value % (2 ** 32)
		if value >= 2**31:
			value = value - 2 ** 32
		value = int(value)
		return value

	if string:
		x = ord(string[0]) << 7
		m = 1000003
		for c in string:
			x = to_32((x*m) ^ ord(c))
		x ^= len(string)
		if x == -1:
			x = -2
		return str(x)
	return ""
    
def vigenere(message, key, decryption=False):
    text = ""
    key_length = len(key)
    key_as_int = [ord(k) for k in key]

    for i, char in enumerate(str(message)):
        #Letters encryption/decryption
        if char.isalpha():
            key_index = i % key_length
            if decryption:
                modified_char = chr((ord(char.upper()) - key_as_int[key_index] + 26) % 26 + ord('A'))
            else : 
                modified_char = chr((ord(char.upper()) + key_as_int[key_index] - 26) % 26 + ord('A'))
            #Put back in lower case if it was
            if char.islower():
                modified_char = modified_char.lower()
            text += modified_char
        #Digits encryption/decryption
        elif char.isdigit():
            key_index = i % key_length
            if decryption:
                modified_char = str((int(char) - key_as_int[key_index]) % 10)
            else:  
                modified_char = str((int(char) + key_as_int[key_index]) % 10)
            text += modified_char
        else:
            text += char
    return text
    
def send_packet(key, type, content, nonceValue):
    """
    Envoi de données fournies en paramètres
    Cette fonction permet de construire, de chiffrer puis d'envoyer un paquet via l'interface radio du micro:bit

    :param (str) key:       Clé de chiffrement
           (str) type:      Type du paquet à envoyer
           (str) content:   Données à envoyer
	:return none
    """
    radio.send(str(type + " | " + len(content) + " | " + nonceValue))

    


#Unpack the packet, check the validity and return the type, length and content
def unpack_data(encrypted_packet, key):
    """
    Déballe et déchiffre les paquets reçus via l'interface radio du micro:bit
    Cette fonction renvoit les différents champs du message passé en paramètre

    :param (str) encrypted_packet: Paquet reçu
           (str) key:              Clé de chiffrement
	:return (srt)type:             Type de paquet
            (int)length:           Longueur de la donnée en caractères
            (str) message:         Données reçue
    """

def receive_packet(packet_received, key):
    """
    Traite les paquets reçus via l'interface radio du micro:bit
    Cette fonction utilise la fonction unpack_data pour renvoyer les différents champs du message passé en paramètre
    Si une erreur survient, les 3 champs sont retournés vides

    :param (str) packet_received: Paquet reçue
           (str) key:              Clé de chiffrement
	:return (srt)type:             Type de paquet
            (int)lenght:           Longueur de la donnée en caractère
            (str) message:         Données reçue
    """

#Calculate the challenge response
def calculate_challenge_response(challenge):
    """
    Calcule la réponse au challenge initial de connection envoyé par l'autre micro:bit

    :param (str) challenge:            Challenge reçu
	:return (srt)challenge_response:   Réponse au challenge
    """
    random.seed(challenge)
    random.randint(0, 99999)
    challenge_response = random.randint(0, 99999)
    return challenge_response


#Respond to a connexion request by sending the hash value of the number received
def respond_to_connexion_request(key):
    """
    Réponse au challenge initial de connection avec l'autre micro:bit
    Si il y a une erreur, la valeur de retour est vide

    :param (str) key:                   Clé de chiffrement
	:return (srt) challenge_response:   Réponse au challenge
    """

def main():

    menuOpen = False
    resetOption = False
    count = 0
    amountOfMilk = 0

    input_code = ""
    secret_key = 739
    counter = 1
    password = False


    dodo = radio.receive()
    if dodo == "Test1" :
    
        for j in range(3) :
            speaker.on()
            music.play(music.DADADADUM)
            for i  in range(5) :
                display.show(Image( '50905:'
                            '50905:'
                            '50905:'
                            '00000:'
                            '50905'))
                sleep(400)
                display.clear()
                sleep(400)
            display.show(" Agiter ")
            speaker.off
    if dodo == "Test2":
        speaker.on()
        music.play(music.BADDY)
        display.show(" Mouvement ")


input_code = ""
secret_key = 739
counter = 1

while True:

    if button_a.is_pressed() and button_b.is_pressed():
        if len(input_code) > 0:
            numeric_input = int(input_code)
            encrypted_token = (numeric_input * secret_key) + counter
            radio.send(str(encrypted_token))
            
            counter += 1
            input_code = ""
            display.show(Image.DIAMOND_SMALL)
            sleep(400)

  

    while True:

        if button_a.is_pressed() and button_b.is_pressed():
            if len(input_code) > 0:
                numeric_input = int(input_code)
                encrypted_token = (numeric_input * secret_key) + counter
                radio.send(str(encrypted_token))
                
                counter += 1
                input_code = ""
                display.show(Image.DIAMOND_SMALL)
                sleep(400)
                display.clear()
            sleep(300)


        elif button_a.was_pressed():
            input_code += "1"
            display.set_pixel(2, 2, 9)
            sleep(100)
            display.clear()


        elif button_b.was_pressed():
            input_code += "2"
            display.set_pixel(2, 2, 9)
            sleep(100)
            display.clear()


        elif accelerometer.was_gesture("shake"):
            input_code = ""
            display.show(Image.NO)
            sleep(300)
            display.clear()


        #CODE PARTIE INTERFACE / DE ANDRADE GABRIEL    
        while password == True:

            if button_a.is_pressed() and resetOption == False:
                display.clear()
                count = 1
                display.show(count)
                menuOpen = True

            while menuOpen == True:
                if button_a.is_pressed():
                    display.clear()
                    count -= 1
                    display.show(count)
                    sleep(500)
                    print(count)
                        
                elif button_b.is_pressed():
                    display.clear()
                    count += 1
                    display.show(count)
                    sleep(500)
                    print(count)
            
                elif pin_logo.is_touched():
                    start_time = time.ticks_ms()
                    while pin_logo.is_touched():
                        if time.ticks_ms() >= 2000:
                            display.clear()
                            amountOfMilk += count
                            break
                    sleep(1000)
                    display.scroll("Value :")
                    display.scroll(amountOfMilk)
                    menuOpen = False
                    break

            if button_b.is_pressed() and menuOpen == False:
                display.scroll("Reset?")
                resetOption = True
                
            while resetOption == True:
                if button_a.is_pressed():
                    display.clear()
                    display.scroll("Cancelled")
                    resetOption = False
                    break
                        
                elif button_b.is_pressed():
                    display.clear()
                    amountOfMilk = 0
                    display.scroll("Count reset")
                    resetOption = False
                    break

            if pin_logo.is_touched():
                display.clear()
                display.scroll("Value is ")
                display.show(amountOfMilk)