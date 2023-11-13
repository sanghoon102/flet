from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)
    grade = Column(String)
    card_type = Column(String)
    stats = relationship('PlayerStats', back_populates='player')

class PlayerStats(Base):
    __tablename__ = 'player_stats'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    position = Column(String)
    batting_average = Column(Float)
    on_base_percentage = Column(Float)
    slugging_percentage = Column(Float)
    ops = Column(Float)
    clutch_hitting_average = Column(Float)
    earned_run_average = Column(Float)
    games_played = Column(Integer)
    innings_pitched = Column(Float)
    wins = Column(Integer)
    holds = Column(Integer)
    saves = Column(Integer)
    player = relationship('Player', back_populates='stats')

# SQLite 데이터베이스에 연결
engine = create_engine('sqlite:///baseball.db', echo=True)

# 테이블 생성
Base.metadata.create_all(engine)

# 세션 생성
session = Session(engine)

# 함수 정의
def insert_player(name, position, grade, card_type):
    new_player = Player(name=name, position=position, grade=grade, card_type=card_type)
    session.add(new_player)
    session.commit()

def insert_batter_stats(player_id, batting_average=None, on_base_percentage=None, slugging_percentage=None,
                        ops=None, clutch_hitting_average=None):
    new_stats = PlayerStats(player_id=player_id, position='타자', batting_average=batting_average,
                            on_base_percentage=on_base_percentage, slugging_percentage=slugging_percentage,
                            ops=ops, clutch_hitting_average=clutch_hitting_average)
    session.add(new_stats)
    session.commit()

def insert_pitcher_stats(player_id, earned_run_average=None, games_played=None,
                         innings_pitched=None, wins=None, holds=None, saves=None):
    new_stats = PlayerStats(player_id=player_id, position='투수', earned_run_average=earned_run_average,
                            games_played=games_played, innings_pitched=innings_pitched,
                            wins=wins, holds=holds, saves=saves)
    session.add(new_stats)
    session.commit()

def select_player_info_and_stats():
    players = session.query(Player).join(PlayerStats).all()
    for player in players:
        print(f"Player ID: {player.id}, Name: {player.name}, Position: {player.position}, Grade: {player.grade}, Card Type: {player.card_type}")
        print(f"Stats - Batting Average: {player.stats.batting_average}, OPS: {player.stats.ops}, Earned Run Average: {player.stats.earned_run_average}")
        print("\n")

# 사용 예시
insert_player('Player1', '타자', 'A', 'Gold')
insert_batter_stats(1, 0.300, 0.400, 0.500, 0.900, 0.320)

insert_player('Player2', '투수', 'B', 'Silver')
insert_pitcher_stats(2, 3.50, 20, 150.0, 10, 5, 3, 2)

print("Player Info and Stats:")
select_player_info_and_stats()

# 세션 종료
session.close()
