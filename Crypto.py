# Transposition Cipher

# original: this_is_a_secret_message_that_i_want_to_transmit
# encrypted:hsi__ertmsaeta__att_rnmtti_sasce_esg_htiwn_otasi
from typing import Any, Union


def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText


def encryptMessage():
    msg = input("Enter the message to encrypt:" . replace)
    cipherText = scramble2Encrypt(msg)
    print("The encrypted message is:", cipherText)

# write a stripSpaces(text) function here
def stripSpace(s):
    s.replace(" ", "")

# write a caesarEncrypt(plainText, shift)
def caesarEncrypt(plainText, shift):
  cipherText = ""
  for ch in plainText:
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter

  return cipherText

# write a caesarDecrypt(cipherText, shift)
def caesarDecrypt(cipherText, shift):
    plainText = ""
    for ch in cipherText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            plainText += finalLetter

    return plainText
