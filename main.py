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

    
process = Enigma()


def shift(text, amount):
  part1 = text[amount:26]
  part2 = text[0:amount]
  return part1 + part2


sentence = input('Enter sentence here:\n').lower()
newSentence = ""


rotations = 0
# elke letter encrypten
for letter in sentence:
  rotations += 1
  # voor elke letter moet rotor1 één positie opschuiven
  process.rotor1 = shift(process.rotor1, 1)

  # rotor twee schuift één positie naar op als rotor 1 een rondje heeft gemaakt 
  if rotations % 26 == 0:
    process.rotor2 = shift(process.rotor2, 1)

  # rotor ..
  if rotations % (26 * 26) == 0:
    process.rotor3 = shift(process.rotor3, 1)

  if letter == " ":
    newSentence += " "
    continue
  encryptedLetter = process.enigma_encrypt(letter)
  newSentence += encryptedLetter

  
  print(newSentence)
