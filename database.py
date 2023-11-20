from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    grade = Column(String)
    type = Column(String)
    skill1 = Column(String)
    skill2 = Column(String)
    skill3 = Column(String)
    stats = relationship('PlayerStats', back_populates='player')

class PlayerStats(Base):
    __tablename__ = 'player_stats'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    avg = Column(Float)
    obp = Column(Float)
    slg = Column(Float)
    ops = Column(Float)
    risp = Column(Float)
    era = Column(Float)
    g = Column(Integer)
    inning = Column(Float)
    w = Column(Integer)
    hld = Column(Integer)
    sv = Column(Integer)
    player = relationship('Player', back_populates='stats')

# SQLite 데이터베이스에 연결
engine = create_engine('sqlite:///baseball.db', echo=True)

# 테이블 생성
Base.metadata.create_all(engine)

# 세션 생성
session = Session(engine)

# 함수 정의
def insert_player(name, grade, type,skill1,skill2,skill3):
    new_player = Player(name=name,grade=grade, type=type,skill1=skill1,skill2=skill2,skill3=skill3)
    session.add(new_player)
    session.commit()

def insert_batter_stats(player_id, avg=None, obp=None, slg=None,
                        ops=None, risp=None):
    new_stats = PlayerStats(player_id=player_id, avg=avg,
                            obp=obp, slugging_percentage=slugging_percentage,
                            ops=ops, clutch_hitting_average=clutch_hitting_average)
    session.add(new_stats)
    session.commit()

def insert_pitcher_stats(player_id, earned_run_average=None, games_played=None,
                         innings_pitched=None, wins=None, holds=None, saves=None):
    new_stats = PlayerStats(player_id=player_id, pos='pitcher', earned_run_average=earned_run_average,
                            games_played=games_played, innings_pitched=innings_pitched,
                            wins=wins, holds=holds, saves=saves)
    session.add(new_stats)
    session.commit()



# 사용 예시
insert_player('Player1', 'batter', 'A', 'Gold')
insert_batter_stats(2, 0.300, 0.400, 0.500, 0.900, 0.320)

insert_player('Player2', 'pitcher', 'B', 'Silver')
insert_pitcher_stats(1, 3.50, 20, 150.0, 10, 5, 3)

players = session.query(Player).join(PlayerStats).all()
for player in players:
        print(f"Player ID: {player.id}, Name: {player.name},  Grade: {player.grade}, Type: {player.type}")
# 세션 종료

