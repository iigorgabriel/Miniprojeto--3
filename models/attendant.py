import random
import time

class Attendant:
    def __init__(self, name):
        self.name = name
        self.is_busy = False
        self.is_failed = False

    def process_request(self, request):
        if not self.is_busy:
            self.is_busy = True
            print(f"Atendente {self.name} processando requisição do tipo {request.type}")
            self.simulate_failure()  # Simula uma falha após algum tempo
            return True
        else:
            print(f"Atendente {self.name} está ocupado.")
            return False

    def simulate_failure(self):
        # Simula uma falha com 10% de probabilidade
        if random.random() < 0.1:  # 10% chance de falha
            self.is_failed = True
            self.is_busy = False
            print(f"Falha detectada no atendente {self.name}.")
            self.reset_availability()  # Resetando após falha

    def reset_availability(self):
        # Resetando a disponibilidade após falha
        if self.is_failed:
            print(f"Atendente {self.name} está disponível novamente após falha.")
            self.is_failed = False
            self.is_busy = False

    def finish_request(self):
        self.is_busy = False
        print(f"Atendente {self.name} terminou a requisição.")
