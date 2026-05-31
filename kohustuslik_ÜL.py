import sqlite3

def get_games_by_publisher(publisher_name):

    with sqlite3.connect("db/TopGamesDB.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT Game.name, Publisher.name
            FROM Game
            JOIN GamePublisher ON Game.id = GamePublisher.gameId
            JOIN Publisher ON Publisher.id = GamePublisher.publisherId
            WHERE LOWER(Publisher.name) = LOWER(?)
            ORDER BY Game.name;
        """, (publisher_name,))

        return cursor.fetchall()


# Kontroll / testimine
games = get_games_by_publisher("Sony Computer Entertainment")

for game in games:
    print(f"{game[0]} - {game[1]}")