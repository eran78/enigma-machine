import string


class Enigma:
  alphabet = list(string.ascii_lowercase)
  rotor1 = list("ghijklmnopqrstuvwxyzabcdef")
  rotor2 = list("mnopqrstuvwxyzabcdefghijkl")
  rotor3 = list("stuvwxyzabcdefghijklmnopqr")

  def _init_(self, pos1, pos2, pos3):
    self.rotate(self.rotor1, pos1)
    self.rotate(self.rotor2, pos2)
    self.rotate(self.rotor3, pos3)

  def rotate(self, rotor, amount):
    print(f"rotor {rotor} set on position {amount}")

  def enigma_encrypt(self,letter):
    idx = self.alphabet.index(letter)
    new_letter = self.rotor1[idx]
    print("letter : " + letter + "\tnew_letter: " + new_letter)
    
    idx = self.alphabet.index(new_letter)
    new_letter = self.rotor2[idx]
    print("letter : " + letter + "\tnew_letter: " + new_letter)

    idx = self.alphabet.index(new_letter)
    new_letter = self.rotor3[idx]
    print("letter : " + letter + "\tnew_letter: " + new_letter)
