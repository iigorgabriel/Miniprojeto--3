import random
from models.request import Request

def generate_request():
    request_type = random.choice(['A', 'B', 'C', 'D'])  # Tipos A, B, C, D de requisições
    request = Request(request_type)
    print(f"Nova requisição gerada: {request.type}")
    return request
