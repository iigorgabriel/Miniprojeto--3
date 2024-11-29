import random

def simulate_failures(attendants, servers):
    # Simula falhas de atendentes e servidores
    for attendant in attendants:
        # Vamos simular falhas nos atendentes
        if random.random() < 0.1:  # 10% de chance de falha
            attendant.is_failed = True
            print(f"Falha detectada no atendente {attendant.name}.")
        else:
            if attendant.is_failed:
                attendant.reset_availability()  # Resetando após falha

    for server in servers:
        # Simulando falha nos servidores com 10% de chance
        if random.random() < 0.1:
            print(f"Falha detectada no servidor {server.name}.")
            server.is_failed = True
        else:
            if server.is_failed:
                server.reset_availability()  # Resetando após falha
