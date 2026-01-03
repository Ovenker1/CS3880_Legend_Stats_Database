import mysql.connector
from mysql.connector import Error


DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'derpyface6',     
    'database': 'cs3380project'
}

def create_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    return None


def show_available_seasons(cursor):
    cursor.execute("SELECT DISTINCT season_num FROM Season ORDER BY season_num")
    seasons = [str(row[0]) for row in cursor.fetchall()]
    print(f"Available Seasons: {', '.join(seasons)}")

def show_available_roles(cursor):
    cursor.execute("SELECT role_name FROM Role")
    roles = [row[0] for row in cursor.fetchall()]
    print(f"Available Roles: {', '.join(roles)}")

def show_available_ranks(cursor):
    cursor.execute("SELECT rank_name FROM Ranks")
    ranks = [row[0] for row in cursor.fetchall()]
    print(f"Available Ranks: {', '.join(ranks)}")



def search_champion(cursor):
    """Function 1: Search Champion Performance"""
    print("\n--- Search Champion Stats ---")
    

    name = input("Enter Legend Name (e.g., Ahri, Yasuo): ")
    
  
    show_available_seasons(cursor)
    season = input("Enter Season Number: ")
    
    query = """
        SELECT S.season_num, R.rank_name, ST.win_perc, ST.pick_rate, ST.ban_rate
        FROM Statistics ST
        JOIN Legend L ON ST.legend_id = L.legend_id
        JOIN Season S ON ST.season_id = S.season_id
        JOIN Ranks R ON ST.rank_id = R.rank_id
        WHERE L.name = %s AND S.season_num = %s
        ORDER BY R.rank_id
    """
    cursor.execute(query, (name, season))
    results = cursor.fetchall()
    
    if not results:
        print("No stats found for that combination.")
    else:
        print(f"\nStats for {name} (Season {season}):")
        print(f"{'Rank':<12} {'Win %':<8} {'Pick %':<8} {'Ban %':<8}")
        print("-" * 50)
        for row in results:
            print(f"{row[1]:<12} {row[2]:<8} {row[3]:<8} {row[4]:<8}")

def compare_roles(cursor):
    """Function 2: Compare Champions by Role"""
    print("\n--- Compare by Role ---")
    
    show_available_roles(cursor)
    role = input("Enter Role: ")
    
    show_available_seasons(cursor)
    season = input("Enter Season: ")
    
    show_available_ranks(cursor)
    rank = input("Enter Rank: ")

    query = """
        SELECT L.name, ST.win_perc, ST.pick_rate
        FROM Legend L
        JOIN Statistics ST ON L.legend_id = ST.legend_id
        JOIN Role RO ON L.role_id = RO.role_id
        JOIN Season S ON ST.season_id = S.season_id
        JOIN Ranks RA ON ST.rank_id = RA.rank_id
        WHERE RO.role_name = %s AND S.season_num = %s AND RA.rank_name = %s
        ORDER BY ST.win_perc DESC
    """
    cursor.execute(query, (role, season, rank))
    results = cursor.fetchall()

    if not results:
        print("No data found.")
    else:
        print(f"\n{role} Champs (Season {season}, {rank}):")
        print(f"{'Name':<15} {'Win %':<8} {'Pick %':<8}")
        print("-" * 40)
        for row in results:
            print(f"{row[0]:<15} {row[1]:<8} {row[2]:<8}")

def identify_popular_champs(cursor):
    """Function 3: Identify Most Popular Champs"""
    print("\n--- Most Popular Champions ---")
    
    show_available_seasons(cursor)
    season = input("Enter Season: ")
    
    show_available_ranks(cursor)
    rank = input("Enter Rank: ")
    
    print("Available Metrics: pick_rate, ban_rate")
    metric = input("Enter Metric (default: pick_rate): ").lower()
    if metric not in ['pick_rate', 'ban_rate']:
        metric = 'pick_rate'

    top_k = input("Enter amount:    ")
    top_k = int(top_k) if top_k.isdigit() else 10

    query = f"""
        SELECT L.name, ST.{metric}, ST.win_perc
        FROM Statistics ST
        JOIN Legend L ON L.legend_id = ST.legend_id
        JOIN Season S ON ST.season_id = S.season_id
        JOIN Ranks R ON ST.rank_id = R.rank_id
        WHERE S.season_num = %s AND R.rank_name = %s
        ORDER BY ST.{metric} DESC
        LIMIT %s
    """
    
    cursor.execute(query, (season, rank, top_k))
    results = cursor.fetchall()

    if not results:
        print("No popularity data found.")
    else:
        print(f"\nTop Champions in Season {season} ({rank}) by {metric}:")
        print(f"{'Name':<15} {metric:<10} {'Win %':<8}")
        print("-" * 40)
        for row in results:
            print(f"{row[0]:<15} {row[1]:<10} {row[2]:<8}")

def main():
    conn = create_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    
    while True:
        print("\n=== LoL Database Tool ===")
        print("1. Search Champion")
        print("2. Compare Role")
        print("3. Identify Popular Champions")
        print("4. Exit")
        choice = input("Select: ")

        if choice == '1':
            search_champion(cursor)
        elif choice == '2':
            compare_roles(cursor)
        elif choice == '3':
            identify_popular_champs(cursor)
        elif choice == '4':
            break
            
    conn.close()

if __name__ == "__main__":
    main()