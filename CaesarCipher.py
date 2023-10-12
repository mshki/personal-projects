class Cipher:
    def __init__(self, decodeOrEncode, shiftValue, userMessage):
        self.decodeOrEncode = decodeOrEncode.upper()
        self.shiftValue = shiftValue
        self.userMessage = userMessage
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 
            'G', 'H', 'I', 'J', 'K', 'L', 
            'M', 'N', 'O', 'P', 'Q', 'R', 
            'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z']
        self.cipheredString = ''
        
    def unformattingString(self):
        stringToPassToCipher = ''
        for c in self.userMessage:
            c = c.upper()
            stringToPassToCipher += c
        return stringToPassToCipher

    def formattingString(self):
        stringToReturn = ''
        for i, c in enumerate(self.cipheredString):
            if self.userMessage[i].islower() == True:
                c = c.lower()
            stringToReturn += c
        return stringToReturn
    
    def cipher(self):
        userStringFormatted = self.unformattingString()
        for userChar in userStringFormatted:
            if userChar in self.alphabet:
                if self.decodeOrEncode == 'ENCODE':
                    E = (self.alphabet.index(userChar) + self.shiftValue) % 26
                elif self.decodeOrEncode == 'DECODE':
                    E = (self.alphabet.index(userChar) - self.shiftValue) % 26
                encodedChar = self.alphabet[E]
                self.cipheredString += encodedChar
            else:
                self.cipheredString += userChar
        returnString = self.formattingString()
        return returnString

    def __str__(self):
        if self.decodeOrEncode == 'ENCODE':
            return f'The encoded message with a shift of {self.shiftValue} is \n{self.cipher()}'
        elif self.decodeOrEncode == 'DECODE':
            return f'The decoded message with a shift of {self.shiftValue} is \n{self.cipher()}'
        else:
            return 'Not a valid selection between ENCODE or DECODE'

if __name__ == '__main__':
    choice = input('Type ENCODE or DECODE:\n')
    key = int(input('Enter the integer value to shift right by:\n'))
    userMsg = input('Enter the message:\n')
    cipheredMsg = Cipher(choice, key, userMsg)
    print(cipheredMsg)

