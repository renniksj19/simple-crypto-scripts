alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encrypt(msg, shift=13):
	output = ""
	for i in range(len(msg)):
		c = msg[i]
		j = alpha.find(c)
		k = (j + shift)%len(alpha)
		output += alpha[k]
	return output

def decrypt(msg, shift=13):
	output = ""
	for i in range(len(msg)):
		c = msg[i]
		j = alpha.find(c)
		k = (j - shift)%len(alpha)
		output += alpha[k]
	return output

inp = input("Enter message to encrypt: ")

out = encrypt(inp)

print(out)

print("Decrypted it's "+decrypt(out))

