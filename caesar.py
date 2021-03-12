alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
encrypted = ""
msg = input("Message to Encrypt > ")

print("Encrypting...")
for i in range(len(msg)):
	if msg[i] == " ":
		encrypted += " "
	else:
		j = msg[i]
		k = alpha.find(j)
		q = k + 3
		encrypted += alpha[q]
print(encrypted)

decrypted = ""

print("Now decrypting...")
for i in range(len(msg)):
	if encrypted[i] == " ":
		decrypted += " "
	else:
		j = encrypted[i]
		k = alpha.find(j)
		q = k - 3
		decrypted += alpha[q]

print(decrypted)

