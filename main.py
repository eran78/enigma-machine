def alphabet():

  alphabet = "abcdefghijklmnopqrstuvwxyz"
  rotor1 = "ghijklmnopqrstuvwxyzabcdef"
  rotor2 = "mnopqrstuvwxyzabcdefghijkl"
  rotor3 = "stuvwxyzabcdefghijklmnopqr"
  
alphabet()

class Enigma:
  def ___init___(self, rotor1=None, rotor2=None, rotor3=None):
    self.alphabet = alphabet
  if rotor1 != None or rotor2 != None or rotor3 != None:
    self.rotor1 = rotor1
    self.rotor2 = rotor2
    self.rotor3 = rotor3
  self.reflector = [letter for letter in reversed(self.alphabet)]

def user_input():

  code = input()
  return code

user_input()

def enigma_encrypt():

  code = user_input()
