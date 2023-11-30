import sqlite3

# SQLite 데이터베이스 연결
conn = sqlite3.connect('baseball.db',check_same_thread=False)
cursor = conn.cursor()

# 플레이어(Player) 테이블 생성 쿼리
create_players_table = '''
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY,
        name TEXT,
        grade TEXT,
        type TEXT,
        skill1 TEXT,
        skill2 TEXT,
        skill3 TEXT
    )
'''
cursor.execute(create_players_table)
conn.commit()

# 플레이어 스탯(PlayerStats) 테이블 생성 쿼리
create_player_stats_table = '''
    CREATE TABLE IF NOT EXISTS player_stats (
        id INTEGER PRIMARY KEY,
        player_id INTEGER,
        avg REAL,
        obp REAL,
        slg REAL,
        ops REAL,
        risp REAL,
        era REAL,
        g INTEGER,
        inning REAL,
        w INTEGER,
        hld INTEGER,
        sv INTEGER,
        FOREIGN KEY (player_id) REFERENCES players(id)
    )
'''
cursor.execute(create_player_stats_table)
conn.commit()

# 데이터 삽입 함수 정의
def insert_player(name, grade, type, skill1, skill2, skill3):
    cursor.execute(
        "INSERT INTO players (name, grade, type, skill1, skill2, skill3) VALUES (?, ?, ?, ?, ?, ?)",
        (name, grade, type, skill1, skill2, skill3)
    )
    conn.commit()

def insert_batter_stats(player_id, avg=None, obp=None, slg=None, ops=None, risp=None):
    cursor.execute(
        "INSERT INTO player_stats (player_id, avg, obp, slg, ops, risp) VALUES (?, ?, ?, ?, ?, ?)",
        (player_id, avg, obp, slg, ops, risp)
    )
    conn.commit()

def insert_pitcher_stats(player_id, era=None, g=None, inning=None, w=None, hld=None, sv=None):
    cursor.execute(
        "INSERT INTO player_stats (player_id, era, g, inning, w, hld, sv) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (player_id, era, g, inning, w, hld, sv)
    )
    conn.commit()

def get_batter_info(player_id):
    cursor.execute("SELECT * FROM players WHERE id=?", (player_id,))
    player = cursor.fetchone()
    cursor.execute("SELECT * FROM player_stats WHERE player_id=?", (player_id,))
    stats = cursor.fetchone()
    return player,stats

def get_pitcher_info(player_id):
    cursor.execute("SELECT * FROM players WHERE id=?", (player_id,))
    player = cursor.fetchone()
    cursor.execute("SELECT * FROM player_stats WHERE player_id=?", (player_id,))
    stats = cursor.fetchone()
    return player,stats
def update_player_info_and_stats(player_id, column, new_value):
    if column in ['name', 'grade', 'type', 'skill1', 'skill2', 'skill3']:
        # 선수 정보 수정
        cursor.execute(f'''
            UPDATE players
            SET {column}=?
            WHERE id=?
        ''', (new_value, player_id))
        conn.commit()
        print("선수 정보가 업데이트되었습니다.")
    elif column in ['avg', 'obp', 'slg', 'ops', 'risp', 'era', 'g', 'inning', 'w', 'hld', 'sv']:
        # 선수 스탯 수정
        cursor.execute(f'''
            UPDATE player_stats
            SET {column}=?
            WHERE player_id=?
        ''', (new_value, player_id))
        conn.commit()
        print("선수 스탯이 업데이트되었습니다.")
    else:
        print("올바른 항목이 아닙니다.")



def initialize_database():
    cursor.execute("DROP TABLE IF EXISTS players")
    cursor.execute("DROP TABLE IF EXISTS player_stats")

    # 플레이어(Player) 테이블 생성
    cursor.execute('''
        CREATE TABLE players (
            id INTEGER PRIMARY KEY,
            name TEXT,
            grade TEXT,
            type TEXT,
            skill1 TEXT,
            skill2 TEXT,
            skill3 TEXT
        )
    ''')

    # 플레이어 스탯(PlayerStats) 테이블 생성
    cursor.execute('''
        CREATE TABLE player_stats (
            id INTEGER PRIMARY KEY,
            player_id INTEGER,
            avg REAL,
            obp REAL,
            slg REAL,
            ops REAL,
            risp REAL,
            era REAL,
            g INTEGER,
            inning REAL,
            w INTEGER,
            hld INTEGER,
            sv INTEGER,
            FOREIGN KEY (player_id) REFERENCES players(id)
        )
    ''')

    conn.commit()
    print("데이터베이스 초기화 및 테이블 재생성이 완료되었습니다.")
initialize_database()
# 데이터 삽입

# 연결 종료

