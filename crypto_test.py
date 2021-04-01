
import blowfish
import base64

cipher = blowfish.Cipher('testkeyoissenoen'.encode('utf-8'))
data_encrypted = b''.join(cipher.encrypt_ecb("password".encode('utf-8')))
base64_bytes = base64.b64encode(data_encrypted)
print(base64_bytes.decode())
base64_decrypted = base64.b64decode(base64_bytes)
data_decrypted = b''.join(cipher.decrypt_ecb(base64_decrypted))
print(data_decrypted.decode())


