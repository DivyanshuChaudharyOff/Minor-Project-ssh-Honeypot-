import paramiko
import threading
import socket
import sys
import os

# Define the SSH banner
SSH_BANNER = "SSH-2.0-OpenSSH_7.4"

# Define the SSH port to listen on
SSH_PORT = 2222

# Define the path to the RSA key file
HOST_KEY = 'host.key'

# Function to generate RSA key pair if not exists
def generate_rsa_key():
    if not os.path.exists(HOST_KEY):
        print("[*] Generating RSA key pair...")
        key = paramiko.RSAKey.generate(2048)
        key.write_private_key_file(HOST_KEY)
        print("[*] RSA key pair generated.")

# Define the thread handler for each connection
class SSHServerHandler(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_auth_password(self, username, password):
        print(f"Attempted login: {username}/{password}")
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return "password"

# Define the SSH honeypot server
class SSHHoneypotServer(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        generate_rsa_key()  # Generate RSA key pair if not exists

        # Create a new socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the socket to the SSH port
        server_socket.bind(('0.0.0.0', SSH_PORT))
        server_socket.listen(100)

        print(f"[*] Listening for incoming SSH connections on port {SSH_PORT}...")

        while True:
            try:
                client_socket, addr = server_socket.accept()
                print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
                transport = paramiko.Transport(client_socket)
                transport.add_server_key(paramiko.RSAKey(filename=HOST_KEY))
                server = SSHServerHandler()
                transport.start_server(server=server)
                server.event.wait()
                transport.close()
            except Exception as e:
                print(f"[*] Exception: {e}")
                continue  # Continue listening for new connections even if an exception occurs

# Main function
def main():
    # Start the SSH honeypot server
    server = SSHHoneypotServer()
    server.start()

if __name__ == "__main__":
    main()
