from cryptography.fernet import Fernet
import os
import sys
import tempfile

def load_key():
    return open('secret.key', 'rb').read()

def decrypt_file(encrypted_file, key):
    fernet = Fernet(key)
    with open(encrypted_file, 'rb') as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    
    # Write decrypted content to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.py')
    temp_file.write(decrypted)
    temp_file.close()
    return temp_file.name

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_encrypted.py <file_to_decrypt.enc>")
        sys.exit(1)

    key = load_key()
    decrypted_file = decrypt_file(sys.argv[1], key)
    
    try:
        os.system(f'python {decrypted_file}')  # Execute the decrypted file
    finally:
        os.remove(decrypted_file)  # Clean up the decrypted file
        print(f"Deleted temporary file: {decrypted_file}")
