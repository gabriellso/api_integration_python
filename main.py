from services.api_client import APIClient
from services.data_processor import DataProcessor
from database.repository import UserRepository

api = APIClient()

def sync_users():
    print("Buscando usuários da API...")
    data = api.get("users")

    if not data:
        print("Falha ao buscar dados.")
        return

    for raw_user in data:
        user = DataProcessor.normalize_user(raw_user)
        UserRepository.insert_user(user)

    print("Sincronização concluída!")

if __name__ == "__main__":
    sync_users()
