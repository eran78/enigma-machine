import string

def shift(text, amount):
  part1 = text[amount:26]
  part2 = text[0:amount]  
  return part1 + part2

class Enigma:
  alphabet = string.ascii_lowercase
  rotor1 = "ghijklmnopqrstuvwxyzabcdef"
  rotor2 = "mnopqrstuvwxyzabcdefghijkl"
  rotor3 = "stuvwxyzabcdefghijklmnopqr"
  rotations = 0

  def __init__(self, pos1, pos2, pos3):
    self.rotor1 = shift(self.rotor1, pos1)
    self.rotor2 = shift(self.rotor2, pos2)
    self.rotor3 = shift(self.rotor3, pos3)    

  def encrypt(self, sentence):

    newSentence = ""
    
    for letter in sentence:
      self.rotations += 1

      print(letter, self.rotor1)

      # voor elke letter moet rotor1 één positie opschuiven
      self.rotor1 = shift(self.rotor1, 1)

      print(letter, self.rotor1)

      # rotor twee schuift één positie naar op als rotor 1 een rondje heeft gemaakt 
      if self.rotations % 26 == 0:
        self.rotor2 = shift(self.rotor2, 1)

      # rotor ..
      if self.rotations % (26 * 26) == 0:
        self.rotor3 = shift(self.rotor3, 1)

      # haal letter door rotoren
      newSentence += self.encrypt_letter(letter)
    
    return newSentence
  
  def encrypt_letter(self,letter):
    idx = self.alphabet.index(letter)
    new_letter = self.rotor1[idx]    
    
    idx = self.alphabet.index(new_letter)
    new_letter = self.rotor2[idx]    

    idx = self.alphabet.index(new_letter)
    new_letter = self.rotor3[idx]    

    reflector_1 = {'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m'}

    # letter door reflector
    newletter = reflector_1[new_letter]
    
    idx = self.alphabet.index(newletter)
    new_letter = self.rotor3[idx]    
    
    idx = self.alphabet.index(new_letter)
    new_letter = self.rotor2[idx]    

    idx = self.alphabet.index(new_letter)
    new_letter = self.rotor1[idx]
    
    return new_letter
    

machineA = Enigma(1,2,3)
sentence = input('Enter sentence here:\n').lower()

output = machineA.encrypt(sentence)
print(output)
