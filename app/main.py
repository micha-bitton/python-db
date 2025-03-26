import time
import psycopg2

def main():
    print("⏳ Waiting before connecting...")
    time.sleep(2)

    try:
        conn = psycopg2.connect(
            dbname="demo",
            user="user",
            password="pasword",
            host="db",  # <--- connect to container via published port
            port=5432
        )
        print("✅ Connected to DB!")

        cur = conn.cursor()
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Inserted data.")

    except Exception as e:
        print(f"❌ Connection failed: {e}")

if __name__ == "__main__":
    main()
