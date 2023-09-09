from PIL import Image
import random


class Encrypter:
    def __init__(self, image_path, max_text_size, key=None):
        self.key = key
        self.image = Image.open(image_path, 'r')
        self.seed = f"{max_text_size}.{key}"
        self.max_text_size = max_text_size
        self.encrypted_image = self.image
        self.width, self.height = self.image.size
        self.check_size()

    def set_image_path(self, image_path):
        self.image = Image.open(image_path, 'r')
        self.encrypted_image = self.image
        self.check_size()

    def check_size(self):
        if self.width * self.height < self.max_text_size:
            print("Your text cannot fit in this image")

    def set_key(self, key):
        self.seed = f"{self.max_text_size}.{key}"

    def set_max_text_size(self, max_text_size):
        self.max_text_size = max_text_size

    def get_seed(self):
        return self.seed

    def encrypt(self, message):
        if self.key is None:
            print("You need to se a key")
            return

        pixels = self.encrypted_image.load()

        binary_array = bytearray(message, "utf8")
        binary_message = ''

        for byte in binary_array:
            binary_representation = bin(byte)
            binary = str(binary_representation).replace('b', '')
            while len(binary) < 8:
                binary = '0' + binary
            binary_message += binary

        binary_message_size = len(binary_message)
        spaces = self.max_text_size * 8 - binary_message_size
        spacesNum = int(spaces / 8)

        for i in range(1, spacesNum + 1):
            binary_message += '00100000'

        random.seed(self.seed)
        width_pos = random.sample(range(1, self.width), int(self.max_text_size * 8 / 2))
        height_pos = random.sample(range(1, self.height), int(self.max_text_size * 8 / 2))

        x = 0
        for i in range(1, int(self.max_text_size * 8 / 2) + 1):
            x += 2
            current_pixel = pixels[width_pos[i - 1], height_pos[i - 1]]
            indexes = [0, 1, 2]
            idx = random.randint(0, 2)
            indexes.remove(idx)

            channel = int(current_pixel[idx])

            bit1_val = binary_message[i * 2 - 2]
            bit2_val = binary_message[i * 2 - 1]

            if bit1_val == '1':
                channel |= (1 << 1)
            if bit2_val == '1':
                channel |= (1 << 0)

            if bit1_val == '0':
                channel &= ~(1 << 1)
            if bit2_val == '0':
                channel &= ~(1 << 0)

            if idx == 0:
                pixels[width_pos[i - 1], height_pos[i - 1]] = (channel, current_pixel[1], current_pixel[2])
            if idx == 1:
                pixels[width_pos[i - 1], height_pos[i - 1]] = (current_pixel[0], channel, current_pixel[2])
            if idx == 2:
                pixels[width_pos[i - 1], height_pos[i - 1]] = (current_pixel[0], current_pixel[1], channel)

        return self.encrypted_image

    def save(self, save_name, file_format="png"):
        self.encrypted_image.save(f"{save_name}.{file_format}")


class Decrypter:
    def __init__(self, image_path, seed=None):
        self.image = Image.open(image_path, 'r')
        self.seed = seed

    def set_image_path(self, image_path):
        self.image = Image.open(image_path, 'r')

    def set_seed(self, seed):
        self.seed = seed

    def decrypt(self):
        if self.seed is None:
            print("You need to set a seed")
            return

        pixels = self.image.load()
        width, height = self.image.size

        max_size = int(self.seed.split('.')[0]) * 8

        random.seed(self.seed)
        width_pos = random.sample(range(1, width), int(max_size / 2))
        height_pos = random.sample(range(1, height), int(max_size / 2))
        binary_message = ''

        for i in range(1, int(max_size / 2) + 1):
            current_pixel = pixels[width_pos[i - 1], height_pos[i - 1]]
            indexes = [0, 1, 2]
            idx = random.randint(0, 2)
            indexes.remove(idx)

            channel = int(current_pixel[idx])
            binary_message += bin(channel)[-2:].replace('b', '0')

        binary_int = int(binary_message, 2)
        byte_number = binary_int.bit_length() + 7 // 8
        binary_array = binary_int.to_bytes(byte_number, "big")
        decrypted_message = binary_array.decode()
        return decrypted_message
