# main.py

from models.attendant import Attendant
from models.server import Server
from simulation.supervisor import Supervisor
from simulation.request_generator import generate_request
from simulation.failure_simulator import simulate_failures
from config import NUM_SERVERS, NUM_ATTENDANTS, MAX_TIMESTEPS
import time

def main():
    attendants = [Attendant("Igor"), Attendant("Luca"), Attendant("Nicolas"), Attendant("João")]
    
    servers = [Server("Servidor 1"), Server("Servidor 2")]
    
    for timestep in range(1, 101):  # Simulando 100 timesteps
        print(f"Timestep {timestep}")
        
        # Gerando nova requisição
        request = generate_request()
        
        # Tentando processar a requisição com os atendentes
        processed = False
        for attendant in attendants:
            if attendant.process_request(request):
                processed = True
                break
        
        if not processed:
            print("Requisição não atendida!")
        
        # Simulando falhas nos atendentes e servidores
        simulate_failures(attendants, servers)
        
        print("\n" + "="*50 + "\n")
        time.sleep(1)  # Pausa de 1 segundo entre os timesteps

if __name__ == "__main__":
    main()