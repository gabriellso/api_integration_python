class DataProcessor:
    @staticmethod
    def normalize_user(data):
        """Padronização dos dados retornados pela API"""
        return {
            "id": data.get("id"),
            "name": data.get("name"),
            "email": data.get("email").lower() if data.get("email") else None,
            "active": bool(data.get("active"))
        }
