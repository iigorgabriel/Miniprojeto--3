# simulation/supervisor.py

from models.attendant import Attendant
from models.server import Server

class Supervisor:
    def __init__(self, attendants, servers):
        self.attendants = attendants
        self.servers = servers

    def supervise(self, request):
        # Tenta atribuir a requisição a um atendente disponível
        for attendant in self.attendants:
            if attendant.process_request(request):
                return True
        
        # Se nenhum atendente estiver disponível, tenta os servidores
        for server in self.servers:
            if server.process_request(request):
                return True

        return False
