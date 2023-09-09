import image_encrypter

message = ""
save_name = ""
print(len(message))
encrypter = image_encrypter.Encrypter(image_path="", max_text_size=100, key="")
seed = encrypter.get_seed()
encrypter.encrypt(message)
encrypter.save(save_name=save_name)

decrypter = image_encrypter.Decrypter(image_path=save_name + ".png", seed=seed)
decrypted_message = decrypter.decrypt()
print(decrypted_message)




