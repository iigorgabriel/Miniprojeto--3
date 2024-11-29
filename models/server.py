class Server:
    def __init__(self, name):
        self.name = name
        self.is_failed = False

    def reset_availability(self):
        # Resetando o servidor após falha
        if self.is_failed:
            print(f"Servidor {self.name} está disponível novamente após falha.")
            self.is_failed = False
