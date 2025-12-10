from database.connection import get_connection

class UserRepository:
    @staticmethod
    def insert_user(user):
        conn = get_connection()
        cur = conn.cursor()

        query = """
        INSERT INTO users (id, name, email, active)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET
            name = EXCLUDED.name,
            email = EXCLUDED.email,
            active = EXCLUDED.active;
        """

        cur.execute(query, (
            user["id"],
            user["name"],
            user["email"],
            user["active"]
        ))

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def list_users():
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT id, name, email, active FROM users")

        result = cur.fetchall()

        cur.close()
        conn.close()
        return result
