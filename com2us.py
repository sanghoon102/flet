import flet as ft
import database as db

name = ft.TextField(hint_text="이름")
grade = ft.TextField(hint_text="등급")
type = ft.TextField(hint_text="카드 종류")
skill1 = ft.TextField(hint_text="고유능력1")
skill2 = ft.TextField(hint_text="고유능력2")
skill3 = ft.TextField(hint_text="고유능력3")
avg = ft.TextField(hint_text="타율(반드시 숫자만 넣을것 어길시 에러)")
obp = ft.TextField(hint_text="출루율(반드시 숫자만 넣을것 어길시 에러)")
slg = ft.TextField(hint_text="장타율(반드시 숫자만 넣을것 어길시 에러)")
ops = ft.TextField(hint_text="ops(반드시 숫자만 넣을것 어길시 에러)")
risp = ft.TextField(hint_text="득점권 타율(반드시 숫자만 넣을것 어길시 에러)")
era = ft.TextField(hint_text="방어율(반드시 숫자만 넣을것 어길시 에러)")
g = ft.TextField(hint_text="경기수(반드시 숫자만 넣을것 어길시 에러)")
inning = ft.TextField(hint_text="이닝(반드시 숫자만 넣을것 어길시 에러)")
w = ft.TextField(hint_text="승리(반드시 숫자만 넣을것 어길시 에러)")
hld = ft.TextField(hint_text="홀드(반드시 숫자만 넣을것 어길시 에러)")
sv = ft.TextField(hint_text="세이브(반드시 숫자만 넣을것 어길시 에러)")
col = ft.TextField(hint_text="수정할 항목을 입력해 주세요")
edit = ft.TextField(hint_text="수정할 값을 입력해 주세요(반드시 숫자만 넣을것 어길시 에러)")


def main(page: ft.Page):
    t1 = dict()
    bn = []
    pn = []
    bp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ps = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    d = {'이름': 'name', '등급': 'grade', '카드 종류': 'type', '고유능력1': 'skill1', '고유능력2': 'skill2', '고유능력3': 'skill3',
         '타율': 'avg', '출루율': 'obp', '장타율': 'slg', 'ops': 'ops', '득점권 타율': 'risp', '방어율': 'era', '경기 수': 'g',
         '이닝': 'inning', '승리': 'g', '홀드': 'hld', '세이브': 'sv'}
    bo = []
    po = []

    boc = []
    bso = []
    boc1=[]
    bso1=[]
    boc2=[]
    bso2=[]
    boc3=[]
    bso3=[]
    boc4=[]
    bso4=[]

    poc1=[]
    pso1=[]
    poc2 = []
    pso2 = []
    poc3 = []
    pso3 = []
    poc4 = []
    pso4 = []
    poc5 = []
    pso5 = []
    poc6 = []
    pso6 = []

    def avgdef(e):



        bso.clear()

        for player_name, avg_value in boc:
            player_id = t1[player_name]
            bso.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(bp[player_id][1])),
                    ft.DataCell(ft.Text(bs[player_id][2])),
                    ft.DataCell(ft.Text(bs[player_id][3])),
                    ft.DataCell(ft.Text(bs[player_id][4])),
                    ft.DataCell(ft.Text(bs[player_id][5])),
                    ft.DataCell(ft.Text(bs[player_id][6])),
                    ft.DataCell(ft.Text(bp[player_id][2])),
                    ft.DataCell(ft.Text(bp[player_id][3])),
                    ft.DataCell(ft.Text(bp[player_id][4])),
                    ft.DataCell(ft.Text(bp[player_id][5])),
                    ft.DataCell(ft.Text(bp[player_id][6])),
                ]
            ))
        btable.rows = bso
        t.tabs[0].content = ft.Column([bv,ft.Row([ft.ElevatedButton('타율순 정렬',on_click=avgdef),ft.ElevatedButton('출루율순 정렬',on_click=obpdef),ft.ElevatedButton('장타율순 정렬',on_click=slgdef),ft.ElevatedButton('ops순 정렬',on_click=opsdef),ft.ElevatedButton('득점권 타율순 정렬',on_click=rispdef),ft.ElevatedButton('타선순 정렬',on_click=tasoondef)])])
        t.update()
    def obpdef(e):
        bso1.clear()

        for player_name, avg_value in boc1:
            player_id = t1[player_name]
            bso1.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(bp[player_id][1])),
                    ft.DataCell(ft.Text(bs[player_id][2])),
                    ft.DataCell(ft.Text(bs[player_id][3])),
                    ft.DataCell(ft.Text(bs[player_id][4])),
                    ft.DataCell(ft.Text(bs[player_id][5])),
                    ft.DataCell(ft.Text(bs[player_id][6])),
                    ft.DataCell(ft.Text(bp[player_id][2])),
                    ft.DataCell(ft.Text(bp[player_id][3])),
                    ft.DataCell(ft.Text(bp[player_id][4])),
                    ft.DataCell(ft.Text(bp[player_id][5])),
                    ft.DataCell(ft.Text(bp[player_id][6])),
                ]
            ))
        btable.rows = bso1
        t.tabs[0].content = ft.Column([bv,ft.Row([ft.ElevatedButton('타율순 정렬',on_click=avgdef),ft.ElevatedButton('출루율순 정렬',on_click=obpdef),ft.ElevatedButton('장타율순 정렬',on_click=slgdef),ft.ElevatedButton('ops순 정렬',on_click=opsdef),ft.ElevatedButton('득점권 타율순 정렬',on_click=rispdef),ft.ElevatedButton('타선순 정렬',on_click=tasoondef)])])
        t.update()
    def slgdef(e):
        bso2.clear()

        for player_name, avg_value in boc2:
            player_id = t1[player_name]
            bso2.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(bp[player_id][1])),
                    ft.DataCell(ft.Text(bs[player_id][2])),
                    ft.DataCell(ft.Text(bs[player_id][3])),
                    ft.DataCell(ft.Text(bs[player_id][4])),
                    ft.DataCell(ft.Text(bs[player_id][5])),
                    ft.DataCell(ft.Text(bs[player_id][6])),
                    ft.DataCell(ft.Text(bp[player_id][2])),
                    ft.DataCell(ft.Text(bp[player_id][3])),
                    ft.DataCell(ft.Text(bp[player_id][4])),
                    ft.DataCell(ft.Text(bp[player_id][5])),
                    ft.DataCell(ft.Text(bp[player_id][6])),
                ]
            ))
        btable.rows = bso2
        t.tabs[0].content = ft.Column([bv,ft.Row([ft.ElevatedButton('타율순 정렬',on_click=avgdef),ft.ElevatedButton('출루율순 정렬',on_click=obpdef),ft.ElevatedButton('장타율순 정렬',on_click=slgdef),ft.ElevatedButton('ops순 정렬',on_click=opsdef),ft.ElevatedButton('득점권 타율순 정렬',on_click=rispdef),ft.ElevatedButton('타선순 정렬',on_click=tasoondef)])])
        t.update()
    def opsdef(e):
        bso3.clear()

        for player_name, avg_value in boc3:
            player_id = t1[player_name]
            bso3.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(bp[player_id][1])),
                    ft.DataCell(ft.Text(bs[player_id][2])),
                    ft.DataCell(ft.Text(bs[player_id][3])),
                    ft.DataCell(ft.Text(bs[player_id][4])),
                    ft.DataCell(ft.Text(bs[player_id][5])),
                    ft.DataCell(ft.Text(bs[player_id][6])),
                    ft.DataCell(ft.Text(bp[player_id][2])),
                    ft.DataCell(ft.Text(bp[player_id][3])),
                    ft.DataCell(ft.Text(bp[player_id][4])),
                    ft.DataCell(ft.Text(bp[player_id][5])),
                    ft.DataCell(ft.Text(bp[player_id][6])),
                ]
            ))
        btable.rows = bso3
        t.tabs[0].content = ft.Column([bv,ft.Row([ft.ElevatedButton('타율순 정렬',on_click=avgdef),ft.ElevatedButton('출루율순 정렬',on_click=obpdef),ft.ElevatedButton('장타율순 정렬',on_click=slgdef),ft.ElevatedButton('ops순 정렬',on_click=opsdef),ft.ElevatedButton('득점권 타율순 정렬',on_click=rispdef),ft.ElevatedButton('타선순 정렬',on_click=tasoondef)])])
        t.update()
    def rispdef(e):
        bso4.clear()

        for player_name, avg_value in boc4:
            player_id = t1[player_name]
            bso4.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(bp[player_id][1])),
                    ft.DataCell(ft.Text(bs[player_id][2])),
                    ft.DataCell(ft.Text(bs[player_id][3])),
                    ft.DataCell(ft.Text(bs[player_id][4])),
                    ft.DataCell(ft.Text(bs[player_id][5])),
                    ft.DataCell(ft.Text(bs[player_id][6])),
                    ft.DataCell(ft.Text(bp[player_id][2])),
                    ft.DataCell(ft.Text(bp[player_id][3])),
                    ft.DataCell(ft.Text(bp[player_id][4])),
                    ft.DataCell(ft.Text(bp[player_id][5])),
                    ft.DataCell(ft.Text(bp[player_id][6])),
                ]
            ))
        btable.rows = bso4
        t.tabs[0].content = ft.Column([bv, ft.Row(
            [ft.ElevatedButton('타율순 정렬', on_click=avgdef), ft.ElevatedButton('출루율순 정렬', on_click=obpdef),
             ft.ElevatedButton('장타율순 정렬', on_click=slgdef), ft.ElevatedButton('ops순 정렬', on_click=opsdef),
             ft.ElevatedButton('득점권 타율순 정렬', on_click=rispdef), ft.ElevatedButton('타선순 정렬', on_click=tasoondef)])])
        t.update()
    def tasoondef(e):

        btable.rows=bo
        t.tabs[0].content = ft.Column([bv,ft.Row([ft.ElevatedButton('타율순 정렬',on_click=avgdef),ft.ElevatedButton('출루율순 정렬',on_click=obpdef),ft.ElevatedButton('장타율순 정렬',on_click=slgdef),ft.ElevatedButton('ops순 정렬',on_click=opsdef),ft.ElevatedButton('득점권 타율순 정렬',on_click=rispdef),ft.ElevatedButton('타선순 정렬',on_click=tasoondef)])])
        t.update()

    def workdef(e):
        ptable.rows=po
        t.tabs[1].content = ft.Column([pv,ft.Row([ft.ElevatedButton('방어율순 정렬',on_click=eradef),ft.ElevatedButton('경기 수 순 정렬',on_click=gdef),ft.ElevatedButton('이닝순 정렬',on_click=inningdef),ft.ElevatedButton('승리순 정렬',on_click=wdef),ft.ElevatedButton('홀드순 정렬',on_click=hddef),ft.ElevatedButton('세이브순 정렬',on_click=svdef),ft.ElevatedButton('보직순 정렬',on_click=workdef)])])
        t.update()
    def eradef(e):
        pso1.clear()

        for player_name, avg_value in poc1:
            player_id = t1[player_name]
            pso1.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(pp[player_id][1])),
                    ft.DataCell(ft.Text(ps[player_id][7])),
                    ft.DataCell(ft.Text(ps[player_id][8])),
                    ft.DataCell(ft.Text(ps[player_id][9])),
                    ft.DataCell(ft.Text(ps[player_id][10])),
                    ft.DataCell(ft.Text(ps[player_id][11])),
                    ft.DataCell(ft.Text(ps[player_id][12])),
                    ft.DataCell(ft.Text(pp[player_id][2])),
                    ft.DataCell(ft.Text(pp[player_id][3])),
                    ft.DataCell(ft.Text(pp[player_id][4])),
                    ft.DataCell(ft.Text(pp[player_id][5])),
                    ft.DataCell(ft.Text(pp[player_id][6])),
                ]
            ))
        ptable.rows = pso1
        t.tabs[1].content = ft.Column([pv,ft.Row([ft.ElevatedButton('방어율순 정렬',on_click=eradef),ft.ElevatedButton('경기 수 순 정렬',on_click=gdef),ft.ElevatedButton('이닝순 정렬',on_click=inningdef),ft.ElevatedButton('승리순 정렬',on_click=wdef),ft.ElevatedButton('홀드순 정렬',on_click=hddef),ft.ElevatedButton('세이브순 정렬',on_click=svdef),ft.ElevatedButton('보직순 정렬',on_click=workdef)])])
        t.update()
    def gdef(e):
        pso2.clear()

        for player_name, avg_value in poc2:
            player_id = t1[player_name]
            pso2.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(pp[player_id][1])),
                    ft.DataCell(ft.Text(ps[player_id][7])),
                    ft.DataCell(ft.Text(ps[player_id][8])),
                    ft.DataCell(ft.Text(ps[player_id][9])),
                    ft.DataCell(ft.Text(ps[player_id][10])),
                    ft.DataCell(ft.Text(ps[player_id][11])),
                    ft.DataCell(ft.Text(ps[player_id][12])),
                    ft.DataCell(ft.Text(pp[player_id][2])),
                    ft.DataCell(ft.Text(pp[player_id][3])),
                    ft.DataCell(ft.Text(pp[player_id][4])),
                    ft.DataCell(ft.Text(pp[player_id][5])),
                    ft.DataCell(ft.Text(pp[player_id][6])),
                ]
            ))
        ptable.rows = pso2
        t.tabs[1].content = ft.Column([pv, ft.Row(
            [ft.ElevatedButton('방어율순 정렬', on_click=eradef), ft.ElevatedButton('경기 수 순 정렬', on_click=gdef),
             ft.ElevatedButton('이닝순 정렬', on_click=inningdef), ft.ElevatedButton('승리순 정렬', on_click=wdef),
             ft.ElevatedButton('홀드순 정렬', on_click=hddef), ft.ElevatedButton('세이브순 정렬', on_click=svdef),
             ft.ElevatedButton('보직순 정렬', on_click=workdef)])])
        t.update()
    def inningdef(e):
        pso3.clear()

        for player_name, avg_value in poc3:
            player_id = t1[player_name]
            pso3.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(pp[player_id][1])),
                    ft.DataCell(ft.Text(ps[player_id][7])),
                    ft.DataCell(ft.Text(ps[player_id][8])),
                    ft.DataCell(ft.Text(ps[player_id][9])),
                    ft.DataCell(ft.Text(ps[player_id][10])),
                    ft.DataCell(ft.Text(ps[player_id][11])),
                    ft.DataCell(ft.Text(ps[player_id][12])),
                    ft.DataCell(ft.Text(pp[player_id][2])),
                    ft.DataCell(ft.Text(pp[player_id][3])),
                    ft.DataCell(ft.Text(pp[player_id][4])),
                    ft.DataCell(ft.Text(pp[player_id][5])),
                    ft.DataCell(ft.Text(pp[player_id][6])),
                ]
            ))
        ptable.rows = pso3
        t.tabs[1].content = ft.Column([pv, ft.Row(
            [ft.ElevatedButton('방어율순 정렬', on_click=eradef), ft.ElevatedButton('경기 수 순 정렬', on_click=gdef),
             ft.ElevatedButton('이닝순 정렬', on_click=inningdef), ft.ElevatedButton('승리순 정렬', on_click=wdef),
             ft.ElevatedButton('홀드순 정렬', on_click=hddef), ft.ElevatedButton('세이브순 정렬', on_click=svdef),
             ft.ElevatedButton('보직순 정렬', on_click=workdef)])])
        t.update()
    def wdef(e):
        pso4.clear()

        for player_name, avg_value in poc4:
            player_id = t1[player_name]
            pso4.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(pp[player_id][1])),
                    ft.DataCell(ft.Text(ps[player_id][7])),
                    ft.DataCell(ft.Text(ps[player_id][8])),
                    ft.DataCell(ft.Text(ps[player_id][9])),
                    ft.DataCell(ft.Text(ps[player_id][10])),
                    ft.DataCell(ft.Text(ps[player_id][11])),
                    ft.DataCell(ft.Text(ps[player_id][12])),
                    ft.DataCell(ft.Text(pp[player_id][2])),
                    ft.DataCell(ft.Text(pp[player_id][3])),
                    ft.DataCell(ft.Text(pp[player_id][4])),
                    ft.DataCell(ft.Text(pp[player_id][5])),
                    ft.DataCell(ft.Text(pp[player_id][6])),
                ]
            ))
        ptable.rows = pso4
        t.tabs[1].content = ft.Column([pv, ft.Row(
            [ft.ElevatedButton('방어율순 정렬', on_click=eradef), ft.ElevatedButton('경기 수 순 정렬', on_click=gdef),
             ft.ElevatedButton('이닝순 정렬', on_click=inningdef), ft.ElevatedButton('승리순 정렬', on_click=wdef),
             ft.ElevatedButton('홀드순 정렬', on_click=hddef), ft.ElevatedButton('세이브순 정렬', on_click=svdef),
             ft.ElevatedButton('보직순 정렬', on_click=workdef)])])
        t.update()
    def hddef(e):
        pso5.clear()

        for player_name, avg_value in poc5:
            player_id = t1[player_name]
            pso5.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(pp[player_id][1])),
                    ft.DataCell(ft.Text(ps[player_id][7])),
                    ft.DataCell(ft.Text(ps[player_id][8])),
                    ft.DataCell(ft.Text(ps[player_id][9])),
                    ft.DataCell(ft.Text(ps[player_id][10])),
                    ft.DataCell(ft.Text(ps[player_id][11])),
                    ft.DataCell(ft.Text(ps[player_id][12])),
                    ft.DataCell(ft.Text(pp[player_id][2])),
                    ft.DataCell(ft.Text(pp[player_id][3])),
                    ft.DataCell(ft.Text(pp[player_id][4])),
                    ft.DataCell(ft.Text(pp[player_id][5])),
                    ft.DataCell(ft.Text(pp[player_id][6])),
                ]
            ))
        ptable.rows = pso5
        t.tabs[1].content = ft.Column([pv, ft.Row(
            [ft.ElevatedButton('방어율순 정렬', on_click=eradef), ft.ElevatedButton('경기 수 순 정렬', on_click=gdef),
             ft.ElevatedButton('이닝순 정렬', on_click=inningdef), ft.ElevatedButton('승리순 정렬', on_click=wdef),
             ft.ElevatedButton('홀드순 정렬', on_click=hddef), ft.ElevatedButton('세이브순 정렬', on_click=svdef),
             ft.ElevatedButton('보직순 정렬', on_click=workdef)])])
        t.update()
    def svdef(e):
        pso6.clear()

        for player_name, avg_value in poc6:
            player_id = t1[player_name]
            pso6.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(pp[player_id][1])),
                    ft.DataCell(ft.Text(ps[player_id][7])),
                    ft.DataCell(ft.Text(ps[player_id][8])),
                    ft.DataCell(ft.Text(ps[player_id][9])),
                    ft.DataCell(ft.Text(ps[player_id][10])),
                    ft.DataCell(ft.Text(ps[player_id][11])),
                    ft.DataCell(ft.Text(ps[player_id][12])),
                    ft.DataCell(ft.Text(pp[player_id][2])),
                    ft.DataCell(ft.Text(pp[player_id][3])),
                    ft.DataCell(ft.Text(pp[player_id][4])),
                    ft.DataCell(ft.Text(pp[player_id][5])),
                    ft.DataCell(ft.Text(pp[player_id][6])),
                ]
            ))
        ptable.rows = pso6
        t.tabs[1].content = ft.Column([pv, ft.Row(
            [ft.ElevatedButton('방어율순 정렬', on_click=eradef), ft.ElevatedButton('경기 수 순 정렬', on_click=gdef),
             ft.ElevatedButton('이닝순 정렬', on_click=inningdef), ft.ElevatedButton('승리순 정렬', on_click=wdef),
             ft.ElevatedButton('홀드순 정렬', on_click=hddef), ft.ElevatedButton('세이브순 정렬', on_click=svdef),
             ft.ElevatedButton('보직순 정렬', on_click=workdef)])])
        t.update()

    def player_input(e):
        if name.value=='':
            name.value = None
            grade.value = None
            type.value = None
            skill1.value = None
            skill2.value = None
            skill3.value = None
            t.tabs[2].content = ft.Column([name,
                                           grade,
                                           type,
                                           skill1,
                                           skill2,
                                           skill3,
                                           ft.ElevatedButton("입력", on_click=player_input),
                                           ft.Text("선수 이름이 없습니다")])
            page.update()
        elif name.value in t1:

            name.value=None
            grade.value=None
            type.value=None
            skill1.value=None
            skill2.value=None
            skill3.value=None
            t.tabs[2].content=ft.Column([name,
                       grade,
                       type,
                       skill1,
                       skill2,
                       skill3,
                       ft.ElevatedButton("입력", on_click=player_input),
                       ft.Text("이미 있는 선수 이름입니다")])
            page.update()

        else:

            db.insert_player(name.value, grade.value, type.value, skill1.value, skill2.value, skill3.value)
            t1[name.value] = len(t1) + 1

            name.value = None
            grade.value = None
            type.value = None
            skill1.value = None
            skill2.value=None
            skill3.value = None
            t.tabs[2].content = ft.Column([name,
                                           grade,
                                           type,
                                           skill1,
                                           skill2,
                                           skill3,
                                           ft.ElevatedButton("입력", on_click=player_input),
                                          ])
            page.update()
    def batter_input(a):
        if name.value not in t1:
            name.value = None
            avg.value = None
            obp.value = None
            slg.value = None
            ops.value = None
            risp.value = None
            t.tabs[3].content = ft.Column([name,
                                           avg,
                                           obp,
                                           slg,
                                           ops,
                                           risp,
                                           ft.ElevatedButton("입력", on_click=batter_input),
                                           ft.Text("등록되지 않은 선수 성적입니다")
                                           ])
            page.update()
        elif name.value in bn:

            name.value = None
            avg.value = None
            obp.value = None
            slg.value = None
            ops.value=None
            risp.value = None
            t.tabs[3].content = ft.Column([name,
                                           avg,
                                           obp,
                                           slg,
                                           ops,
                                           risp,
                                           ft.ElevatedButton("입력", on_click=batter_input),
                                           ft.Text("이미 입력한 선수 성적입니다")
                                           ])
            page.update()

        else:

            db.insert_batter_stats(t1[name.value], avg.value, obp.value, slg.value, ops.value, risp.value)
            bp[t1[name.value]], bs[t1[name.value]] = db.get_batter_info(t1[name.value])
            bn.append(name.value)

            bo.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(bp[t1[name.value]][1])),
                    ft.DataCell(ft.Text(bs[t1[name.value]][2])),
                    ft.DataCell(ft.Text(bs[t1[name.value]][3])),
                    ft.DataCell(ft.Text(bs[t1[name.value]][4])),
                    ft.DataCell(ft.Text(bs[t1[name.value]][5])),
                    ft.DataCell(ft.Text(bs[t1[name.value]][6])),
                    ft.DataCell(ft.Text(bp[t1[name.value]][2])),
                    ft.DataCell(ft.Text(bp[t1[name.value]][3])),
                    ft.DataCell(ft.Text(bp[t1[name.value]][4])),
                    ft.DataCell(ft.Text(bp[t1[name.value]][5])),
                    ft.DataCell(ft.Text(bp[t1[name.value]][6])),
                ]
            ))
            btable.rows = bo
            page.update()

            boc.append([name.value,bs[t1[name.value]][2]])
            boc.sort(key=lambda x: x[1], reverse=True)
            bso.clear()

            for player_name, avg_value in boc:
                player_id = t1[player_name]
                bso.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(bp[player_id][1])),
                        ft.DataCell(ft.Text(bs[player_id][2])),
                        ft.DataCell(ft.Text(bs[player_id][3])),
                        ft.DataCell(ft.Text(bs[player_id][4])),
                        ft.DataCell(ft.Text(bs[player_id][5])),
                        ft.DataCell(ft.Text(bs[player_id][6])),
                        ft.DataCell(ft.Text(bp[player_id][2])),
                        ft.DataCell(ft.Text(bp[player_id][3])),
                        ft.DataCell(ft.Text(bp[player_id][4])),
                        ft.DataCell(ft.Text(bp[player_id][5])),
                        ft.DataCell(ft.Text(bp[player_id][6])),
                    ]
                ))
            bsotable.rows=bso
            page.update()

            boc1.append([name.value, bs[t1[name.value]][3]])
            boc1.sort(key=lambda x: x[1], reverse=True)
            bso1.clear()

            for player_name, avg_value in boc1:
                player_id = t1[player_name]
                bso1.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(bp[player_id][1])),
                        ft.DataCell(ft.Text(bs[player_id][2])),
                        ft.DataCell(ft.Text(bs[player_id][3])),
                        ft.DataCell(ft.Text(bs[player_id][4])),
                        ft.DataCell(ft.Text(bs[player_id][5])),
                        ft.DataCell(ft.Text(bs[player_id][6])),
                        ft.DataCell(ft.Text(bp[player_id][2])),
                        ft.DataCell(ft.Text(bp[player_id][3])),
                        ft.DataCell(ft.Text(bp[player_id][4])),
                        ft.DataCell(ft.Text(bp[player_id][5])),
                        ft.DataCell(ft.Text(bp[player_id][6])),
                    ]
                ))
            bsotable.rows = bso1
            page.update()

            boc2.append([name.value, bs[t1[name.value]][4]])
            boc2.sort(key=lambda x: x[1], reverse=True)
            bso2.clear()

            for player_name, avg_value in boc2:
                player_id = t1[player_name]
                bso2.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(bp[player_id][1])),
                        ft.DataCell(ft.Text(bs[player_id][2])),
                        ft.DataCell(ft.Text(bs[player_id][3])),
                        ft.DataCell(ft.Text(bs[player_id][4])),
                        ft.DataCell(ft.Text(bs[player_id][5])),
                        ft.DataCell(ft.Text(bs[player_id][6])),
                        ft.DataCell(ft.Text(bp[player_id][2])),
                        ft.DataCell(ft.Text(bp[player_id][3])),
                        ft.DataCell(ft.Text(bp[player_id][4])),
                        ft.DataCell(ft.Text(bp[player_id][5])),
                        ft.DataCell(ft.Text(bp[player_id][6])),
                    ]
                ))
            bso2table.rows = bso2
            page.update()

            boc3.append([name.value, bs[t1[name.value]][5]])
            boc3.sort(key=lambda x: x[1], reverse=True)
            bso3.clear()
            for player_name, avg_value in boc3:
                player_id = t1[player_name]
                bso3.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(bp[player_id][1])),
                        ft.DataCell(ft.Text(bs[player_id][2])),
                        ft.DataCell(ft.Text(bs[player_id][3])),
                        ft.DataCell(ft.Text(bs[player_id][4])),
                        ft.DataCell(ft.Text(bs[player_id][5])),
                        ft.DataCell(ft.Text(bs[player_id][6])),
                        ft.DataCell(ft.Text(bp[player_id][2])),
                        ft.DataCell(ft.Text(bp[player_id][3])),
                        ft.DataCell(ft.Text(bp[player_id][4])),
                        ft.DataCell(ft.Text(bp[player_id][5])),
                        ft.DataCell(ft.Text(bp[player_id][6])),
                    ]
                ))
            bso3table.rows = bso3
            page.update()

            boc4.append([name.value, bs[t1[name.value]][6]])
            boc4.sort(key=lambda x: x[1], reverse=True)
            bso4.clear()
            for player_name, avg_value in boc4:
                player_id = t1[player_name]
                bso4.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(bp[player_id][1])),
                        ft.DataCell(ft.Text(bs[player_id][2])),
                        ft.DataCell(ft.Text(bs[player_id][3])),
                        ft.DataCell(ft.Text(bs[player_id][4])),
                        ft.DataCell(ft.Text(bs[player_id][5])),
                        ft.DataCell(ft.Text(bs[player_id][6])),
                        ft.DataCell(ft.Text(bp[player_id][2])),
                        ft.DataCell(ft.Text(bp[player_id][3])),
                        ft.DataCell(ft.Text(bp[player_id][4])),
                        ft.DataCell(ft.Text(bp[player_id][5])),
                        ft.DataCell(ft.Text(bp[player_id][6])),
                    ]
                ))
            bso4table.rows = bso4
            page.update()

            name.value = None
            avg.value = None
            obp.value = None
            slg.value = None
            ops.value = None
            risp.value = None
            t.tabs[3].content = ft.Column([name,
                                           avg,
                                           obp,
                                           slg,
                                           ops,
                                           risp,
                                           ft.ElevatedButton("입력", on_click=batter_input),

                                           ])
            page.update()



    def pitcher_input(e):
        if name.value not in t1:
            name.value = None
            era.value = None
            g.value = None
            inning.value = None
            w.value = None
            hld.value = None
            sv.value=None
            t.tabs[4].content = ft.Column([name,
                                           era,
                                           g,
                                           inning,
                                           w,
                                           hld,
                                           sv,
                                           ft.ElevatedButton("입력", on_click=pitcher_input),
                                           ft.Text("등록되지 않은 선수 성적입니다")
                                           ])
            page.update()
        elif name.value in pn:
            name.value = None
            era.value = None
            g.value = None
            inning.value = None
            w.value = None
            hld.value = None
            sv.value = None
            t.tabs[4].content = ft.Column([name,
                                           era,
                                           g,
                                           inning,
                                           w,
                                           hld,
                                           sv,
                                           ft.ElevatedButton("입력", on_click=pitcher_input),
                                           ft.Text("이미 입력한 선수 성적입니다")
                                           ])
            page.update()

        else:
            db.insert_pitcher_stats(t1[name.value], era.value, g.value, inning.value, w.value, hld.value, sv.value)
            pp[t1[name.value]], ps[t1[name.value]] = db.get_pitcher_info(t1[name.value])
            pn.append(name.value)

            po.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(pp[t1[name.value]][1])),
                    ft.DataCell(ft.Text(ps[t1[name.value]][7])),
                    ft.DataCell(ft.Text(ps[t1[name.value]][8])),
                    ft.DataCell(ft.Text(ps[t1[name.value]][9])),
                    ft.DataCell(ft.Text(ps[t1[name.value]][10])),
                    ft.DataCell(ft.Text(ps[t1[name.value]][11])),
                    ft.DataCell(ft.Text(ps[t1[name.value]][12])),
                    ft.DataCell(ft.Text(pp[t1[name.value]][2])),
                    ft.DataCell(ft.Text(pp[t1[name.value]][3])),
                    ft.DataCell(ft.Text(pp[t1[name.value]][4])),
                    ft.DataCell(ft.Text(pp[t1[name.value]][5])),
                    ft.DataCell(ft.Text(pp[t1[name.value]][6])),
                ]
            ))
            ptable.rows = po
            page.update()


            poc1.append([name.value, ps[t1[name.value]][7]])
            poc1.sort(key=lambda x: x[1], reverse=False)
            pso1.clear()

            for player_name, avg_value in poc1:
                player_id = t1[player_name]
                pso1.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(pp[player_id][1])),
                        ft.DataCell(ft.Text(ps[player_id][7])),
                        ft.DataCell(ft.Text(ps[player_id][8])),
                        ft.DataCell(ft.Text(ps[player_id][9])),
                        ft.DataCell(ft.Text(ps[player_id][10])),
                        ft.DataCell(ft.Text(ps[player_id][11])),
                        ft.DataCell(ft.Text(ps[player_id][12])),
                        ft.DataCell(ft.Text(pp[player_id][2])),
                        ft.DataCell(ft.Text(pp[player_id][3])),
                        ft.DataCell(ft.Text(pp[player_id][4])),
                        ft.DataCell(ft.Text(pp[player_id][5])),
                        ft.DataCell(ft.Text(pp[player_id][6])),
                    ]
                ))
            pso1table.rows = pso1
            page.update()



            poc2.append([name.value, ps[t1[name.value]][8]])
            poc2.sort(key=lambda x: x[1], reverse=True)
            pso2.clear()

            for player_name, avg_value in poc2:
                player_id = t1[player_name]
                pso2.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(pp[player_id][1])),
                        ft.DataCell(ft.Text(ps[player_id][7])),
                        ft.DataCell(ft.Text(ps[player_id][8])),
                        ft.DataCell(ft.Text(ps[player_id][9])),
                        ft.DataCell(ft.Text(ps[player_id][10])),
                        ft.DataCell(ft.Text(ps[player_id][11])),
                        ft.DataCell(ft.Text(ps[player_id][12])),
                        ft.DataCell(ft.Text(pp[player_id][2])),
                        ft.DataCell(ft.Text(pp[player_id][3])),
                        ft.DataCell(ft.Text(pp[player_id][4])),
                        ft.DataCell(ft.Text(pp[player_id][5])),
                        ft.DataCell(ft.Text(pp[player_id][6])),
                    ]
                ))
            pso2table.rows = pso2
            page.update()




            poc3.append([name.value, ps[t1[name.value]][9]])
            poc3.sort(key=lambda x: x[1], reverse=True)
            pso3.clear()

            for player_name, avg_value in poc3:
                player_id = t1[player_name]
                pso3.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(pp[player_id][1])),
                        ft.DataCell(ft.Text(ps[player_id][7])),
                        ft.DataCell(ft.Text(ps[player_id][8])),
                        ft.DataCell(ft.Text(ps[player_id][9])),
                        ft.DataCell(ft.Text(ps[player_id][10])),
                        ft.DataCell(ft.Text(ps[player_id][11])),
                        ft.DataCell(ft.Text(ps[player_id][12])),
                        ft.DataCell(ft.Text(pp[player_id][2])),
                        ft.DataCell(ft.Text(pp[player_id][3])),
                        ft.DataCell(ft.Text(pp[player_id][4])),
                        ft.DataCell(ft.Text(pp[player_id][5])),
                        ft.DataCell(ft.Text(pp[player_id][6])),
                    ]
                ))
            pso3table.rows = pso3
            page.update()


            poc4.append([name.value, ps[t1[name.value]][10]])
            poc4.sort(key=lambda x: x[1], reverse=True)
            pso4.clear()

            for player_name, avg_value in poc4:
                player_id = t1[player_name]
                pso4.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(pp[player_id][1])),
                        ft.DataCell(ft.Text(ps[player_id][7])),
                        ft.DataCell(ft.Text(ps[player_id][8])),
                        ft.DataCell(ft.Text(ps[player_id][9])),
                        ft.DataCell(ft.Text(ps[player_id][10])),
                        ft.DataCell(ft.Text(ps[player_id][11])),
                        ft.DataCell(ft.Text(ps[player_id][12])),
                        ft.DataCell(ft.Text(pp[player_id][2])),
                        ft.DataCell(ft.Text(pp[player_id][3])),
                        ft.DataCell(ft.Text(pp[player_id][4])),
                        ft.DataCell(ft.Text(pp[player_id][5])),
                        ft.DataCell(ft.Text(pp[player_id][6])),
                    ]
                ))
            pso4table.rows = pso4
            page.update()


            poc5.append([name.value, ps[t1[name.value]][11]])
            poc5.sort(key=lambda x: x[1], reverse=True)
            pso5.clear()

            for player_name, avg_value in poc5:
                player_id = t1[player_name]
                pso5.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(pp[player_id][1])),
                        ft.DataCell(ft.Text(ps[player_id][7])),
                        ft.DataCell(ft.Text(ps[player_id][8])),
                        ft.DataCell(ft.Text(ps[player_id][9])),
                        ft.DataCell(ft.Text(ps[player_id][10])),
                        ft.DataCell(ft.Text(ps[player_id][11])),
                        ft.DataCell(ft.Text(ps[player_id][12])),
                        ft.DataCell(ft.Text(pp[player_id][2])),
                        ft.DataCell(ft.Text(pp[player_id][3])),
                        ft.DataCell(ft.Text(pp[player_id][4])),
                        ft.DataCell(ft.Text(pp[player_id][5])),
                        ft.DataCell(ft.Text(pp[player_id][6])),
                    ]
                ))
            pso5table.rows = pso5
            page.update()


            poc6.append([name.value, ps[t1[name.value]][12]])
            poc6.sort(key=lambda x: x[1], reverse=True)
            pso6.clear()

            for player_name, avg_value in poc6:
                player_id = t1[player_name]
                pso6.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(pp[player_id][1])),
                        ft.DataCell(ft.Text(ps[player_id][7])),
                        ft.DataCell(ft.Text(ps[player_id][8])),
                        ft.DataCell(ft.Text(ps[player_id][9])),
                        ft.DataCell(ft.Text(ps[player_id][10])),
                        ft.DataCell(ft.Text(ps[player_id][11])),
                        ft.DataCell(ft.Text(ps[player_id][12])),
                        ft.DataCell(ft.Text(pp[player_id][2])),
                        ft.DataCell(ft.Text(pp[player_id][3])),
                        ft.DataCell(ft.Text(pp[player_id][4])),
                        ft.DataCell(ft.Text(pp[player_id][5])),
                        ft.DataCell(ft.Text(pp[player_id][6])),
                    ]
                ))
            pso6table.rows = pso6
            page.update()


            name.value = None
            era.value = None
            g.value = None
            inning.value = None
            w.value = None
            hld.value = None
            sv.value = None
            t.tabs[4].content = ft.Column([name,
                                           era,
                                           g,
                                           inning,
                                           w,
                                           hld,
                                           sv,
                                           ft.ElevatedButton("입력", on_click=pitcher_input),

                                           ])
            page.update()

    def update_info_stat(e):


        if name.value not in bn and name.value not in pn:
            name.value=None
            col.value=None
            edit.value=None
            t.tabs[5].content=ft.Column([name,
                                   col,
                                   edit,
                                   ft.ElevatedButton("입력", on_click=update_info_stat),
                                   ft.Text("성적이 등록되지 않은 선수입니다") ]    )
            page.update()
        else:


            if name.value in bn:
                if col.value not in ['이름','등급','카드 종류','고유능력1','고유능력2','고유능력3','타율','출루율','장타율','ops','득점권 타율']:
                    name.value = None
                    col.value = None
                    edit.value = None
                    t.tabs[5].content = ft.Column([name,
                                                   col,
                                                   edit,
                                                   ft.ElevatedButton("입력", on_click=update_info_stat),
                                                   ft.Text("올바르지 않은 항목입니다")])
                    page.update()
                else:
                    db.update_player_info_and_stats(t1[name.value], d[col.value], edit.value)
                    bp[t1[name.value]], bs[t1[name.value]] = db.get_batter_info(t1[name.value])
                    bo[t1[name.value] - 1-len(po)] = ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(bp[t1[name.value]][1])),
                            ft.DataCell(ft.Text(bs[t1[name.value]][2])),
                            ft.DataCell(ft.Text(bs[t1[name.value]][3])),
                            ft.DataCell(ft.Text(bs[t1[name.value]][4])),
                            ft.DataCell(ft.Text(bs[t1[name.value]][5])),
                            ft.DataCell(ft.Text(bs[t1[name.value]][6])),
                            ft.DataCell(ft.Text(bp[t1[name.value]][2])),
                            ft.DataCell(ft.Text(bp[t1[name.value]][3])),
                            ft.DataCell(ft.Text(bp[t1[name.value]][4])),
                            ft.DataCell(ft.Text(bp[t1[name.value]][5])),
                            ft.DataCell(ft.Text(bp[t1[name.value]][6])),
                        ]

                    )
                    btable.rows = bo
                    page.update()

                    if col.value == '타율':
                        for i in range(len(boc)):
                            if boc[i][0]==name.value:
                                boc[i][1]=float(edit.value)

                        boc.sort(key=lambda x: x[1], reverse=True)
                        bso.clear()

                        for player_name, avg_value in boc:
                            player_id = t1[player_name]
                            bso.append(ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(bp[player_id][1])),
                                    ft.DataCell(ft.Text(bs[player_id][2])),
                                    ft.DataCell(ft.Text(bs[player_id][3])),
                                    ft.DataCell(ft.Text(bs[player_id][4])),
                                    ft.DataCell(ft.Text(bs[player_id][5])),
                                    ft.DataCell(ft.Text(bs[player_id][6])),
                                    ft.DataCell(ft.Text(bp[player_id][2])),
                                    ft.DataCell(ft.Text(bp[player_id][3])),
                                    ft.DataCell(ft.Text(bp[player_id][4])),
                                    ft.DataCell(ft.Text(bp[player_id][5])),
                                    ft.DataCell(ft.Text(bp[player_id][6])),
                                ]
                            ))
                        bsotable.rows = bso
                        page.update()
                    if col.value == '출루율':
                        for i in range(len(boc1)):
                            if boc1[i][0]==name.value:
                                boc1[i][1]=float(edit.value)

                        boc1.sort(key=lambda x: x[1], reverse=True)
                        bso1.clear()

                        for player_name, avg_value in boc1:
                            player_id = t1[player_name]
                            bso1.append(ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(bp[player_id][1])),
                                    ft.DataCell(ft.Text(bs[player_id][2])),
                                    ft.DataCell(ft.Text(bs[player_id][3])),
                                    ft.DataCell(ft.Text(bs[player_id][4])),
                                    ft.DataCell(ft.Text(bs[player_id][5])),
                                    ft.DataCell(ft.Text(bs[player_id][6])),
                                    ft.DataCell(ft.Text(bp[player_id][2])),
                                    ft.DataCell(ft.Text(bp[player_id][3])),
                                    ft.DataCell(ft.Text(bp[player_id][4])),
                                    ft.DataCell(ft.Text(bp[player_id][5])),
                                    ft.DataCell(ft.Text(bp[player_id][6])),
                                ]
                            ))
                        bso1table.rows = bso1
                        page.update()
                    if col.value == '장타율':
                        for i in range(len(boc2)):
                            if boc2[i][0]==name.value:
                                boc2[i][1]=float(edit.value)

                        boc2.sort(key=lambda x: x[1], reverse=True)
                        bso2.clear()

                        for player_name, avg_value in boc2:
                            player_id = t1[player_name]
                            bso2.append(ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(bp[player_id][1])),
                                    ft.DataCell(ft.Text(bs[player_id][2])),
                                    ft.DataCell(ft.Text(bs[player_id][3])),
                                    ft.DataCell(ft.Text(bs[player_id][4])),
                                    ft.DataCell(ft.Text(bs[player_id][5])),
                                    ft.DataCell(ft.Text(bs[player_id][6])),
                                    ft.DataCell(ft.Text(bp[player_id][2])),
                                    ft.DataCell(ft.Text(bp[player_id][3])),
                                    ft.DataCell(ft.Text(bp[player_id][4])),
                                    ft.DataCell(ft.Text(bp[player_id][5])),
                                    ft.DataCell(ft.Text(bp[player_id][6])),
                                ]
                            ))
                        bso2table.rows = bso2
                        page.update()
                    if col.value == 'ops':
                        for i in range(len(boc3)):
                            if boc3[i][0]==name.value:
                                boc3[i][1]=float(edit.value)

                        boc3.sort(key=lambda x: x[1], reverse=True)
                        bso3.clear()

                        for player_name, avg_value in boc3:
                            player_id = t1[player_name]
                            bso3.append(ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(bp[player_id][1])),
                                    ft.DataCell(ft.Text(bs[player_id][2])),
                                    ft.DataCell(ft.Text(bs[player_id][3])),
                                    ft.DataCell(ft.Text(bs[player_id][4])),
                                    ft.DataCell(ft.Text(bs[player_id][5])),
                                    ft.DataCell(ft.Text(bs[player_id][6])),
                                    ft.DataCell(ft.Text(bp[player_id][2])),
                                    ft.DataCell(ft.Text(bp[player_id][3])),
                                    ft.DataCell(ft.Text(bp[player_id][4])),
                                    ft.DataCell(ft.Text(bp[player_id][5])),
                                    ft.DataCell(ft.Text(bp[player_id][6])),
                                ]
                            ))
                        bso3table.rows = bso3
                        page.update()
                    if col.value == '득점권 타율':
                        for i in range(len(boc4)):
                            if boc4[i][0]==name.value:
                                boc4[i][1]=float(edit.value)

                        boc4.sort(key=lambda x: x[1], reverse=True)
                        bso4.clear()

                        for player_name, avg_value in boc4:
                            player_id = t1[player_name]
                            bso4.append(ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(bp[player_id][1])),
                                    ft.DataCell(ft.Text(bs[player_id][2])),
                                    ft.DataCell(ft.Text(bs[player_id][3])),
                                    ft.DataCell(ft.Text(bs[player_id][4])),
                                    ft.DataCell(ft.Text(bs[player_id][5])),
                                    ft.DataCell(ft.Text(bs[player_id][6])),
                                    ft.DataCell(ft.Text(bp[player_id][2])),
                                    ft.DataCell(ft.Text(bp[player_id][3])),
                                    ft.DataCell(ft.Text(bp[player_id][4])),
                                    ft.DataCell(ft.Text(bp[player_id][5])),
                                    ft.DataCell(ft.Text(bp[player_id][6])),
                                ]
                            ))
                        bso4table.rows = bso4
                        page.update()
                    else:
                        bso.clear()
                        for player_name, avg_value in boc:
                            player_id = t1[player_name]
                            bso.append(ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(bp[player_id][1])),
                                    ft.DataCell(ft.Text(bs[player_id][2])),
                                    ft.DataCell(ft.Text(bs[player_id][3])),
                                    ft.DataCell(ft.Text(bs[player_id][4])),
                                    ft.DataCell(ft.Text(bs[player_id][5])),
                                    ft.DataCell(ft.Text(bs[player_id][6])),
                                    ft.DataCell(ft.Text(bp[player_id][2])),
                                    ft.DataCell(ft.Text(bp[player_id][3])),
                                    ft.DataCell(ft.Text(bp[player_id][4])),
                                    ft.DataCell(ft.Text(bp[player_id][5])),
                                    ft.DataCell(ft.Text(bp[player_id][6])),
                                ]
                            ))
                        bsotable.rows = bso
                        page.update()
                    name.value = None
                    col.value = None
                    edit.value = None
                    t.tabs[5].content = ft.Column([name,
                                                   col,
                                                   edit,
                                                   ft.ElevatedButton("입력", on_click=update_info_stat),
                                                   ])
                    page.update()

                    t.tabs[0].content=ft.Column([bv,ft.Row([ft.ElevatedButton('타율순 정렬',on_click=avgdef),ft.ElevatedButton('출루율순 정렬',on_click=obpdef),ft.ElevatedButton('장타율순 정렬',on_click=slgdef),ft.ElevatedButton('ops순 정렬',on_click=opsdef),ft.ElevatedButton('득점권 타율순 정렬',on_click=rispdef),ft.ElevatedButton('타선순 정렬',on_click=tasoondef)])])
                    page.update()

            elif name.value in pn:
                if col.value not in ['이름','등급','카드 종류','고유능력1','고유능력2','고유능력3','승리','이닝','경기 수','홀드','세이브','방어율']:
                    name.value = None
                    col.value = None
                    edit.value = None
                    t.tabs[5].content = ft.Column([name,
                                                   col,
                                                   edit,
                                                   ft.ElevatedButton("입력", on_click=update_info_stat),
                                                   ft.Text("올바르지 않은 항목입니다")
                                                   ])
                    page.update()
                else:
                    db.update_player_info_and_stats(t1[name.value], d[col.value], edit.value)
                    pp[t1[name.value]], ps[t1[name.value]] = db.get_pitcher_info(t1[name.value])
                    po[t1[name.value] - 1-len(bo)] = ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(pp[t1[name.value]][1])),
                            ft.DataCell(ft.Text(ps[t1[name.value]][7])),
                            ft.DataCell(ft.Text(ps[t1[name.value]][8])),
                            ft.DataCell(ft.Text(ps[t1[name.value]][9])),
                            ft.DataCell(ft.Text(ps[t1[name.value]][10])),
                            ft.DataCell(ft.Text(ps[t1[name.value]][11])),
                            ft.DataCell(ft.Text(ps[t1[name.value]][12])),
                            ft.DataCell(ft.Text(pp[t1[name.value]][2])),
                            ft.DataCell(ft.Text(pp[t1[name.value]][3])),
                            ft.DataCell(ft.Text(pp[t1[name.value]][4])),
                            ft.DataCell(ft.Text(pp[t1[name.value]][5])),
                            ft.DataCell(ft.Text(pp[t1[name.value]][6])),
                        ]
                    )
                    ptable.rows = po
                    page.update()


                    if col.value=='방어율':
                        for i in range(len(poc1)):
                            if poc1[i][0]==name.value:
                                poc1[i][1]=float(edit.value)

                        poc1.sort(key=lambda x: x[1], reverse=False)
                        pso1.clear()

                        for player_name, avg_value in poc1:
                            player_id = t1[player_name]
                            pso1.append(ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(pp[player_id][1])),
                                    ft.DataCell(ft.Text(ps[player_id][7])),
                                    ft.DataCell(ft.Text(ps[player_id][8])),
                                    ft.DataCell(ft.Text(ps[player_id][9])),
                                    ft.DataCell(ft.Text(ps[player_id][10])),
                                    ft.DataCell(ft.Text(ps[player_id][11])),
                                    ft.DataCell(ft.Text(ps[player_id][12])),
                                    ft.DataCell(ft.Text(pp[player_id][2])),
                                    ft.DataCell(ft.Text(pp[player_id][3])),
                                    ft.DataCell(ft.Text(pp[player_id][4])),
                                    ft.DataCell(ft.Text(pp[player_id][5])),
                                    ft.DataCell(ft.Text(pp[player_id][6])),
                                ]
                            ))
                        pso1table.rows = pso1
                        page.update()

                    if col.value=='경기 수':
                        for i in range(len(poc2)):
                            if poc2[i][0]==name.value:
                                poc2[i][1]=float(edit.value)

                        poc2.sort(key=lambda x: x[1], reverse=True)
                        pso2.clear()

                        for player_name, avg_value in poc2:
                            player_id = t1[player_name]
                            pso2.append(ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(pp[player_id][1])),
                                    ft.DataCell(ft.Text(ps[player_id][7])),
                                    ft.DataCell(ft.Text(ps[player_id][8])),
                                    ft.DataCell(ft.Text(ps[player_id][9])),
                                    ft.DataCell(ft.Text(ps[player_id][10])),
                                    ft.DataCell(ft.Text(ps[player_id][11])),
                                    ft.DataCell(ft.Text(ps[player_id][12])),
                                    ft.DataCell(ft.Text(pp[player_id][2])),
                                    ft.DataCell(ft.Text(pp[player_id][3])),
                                    ft.DataCell(ft.Text(pp[player_id][4])),
                                    ft.DataCell(ft.Text(pp[player_id][5])),
                                    ft.DataCell(ft.Text(pp[player_id][6])),
                                ]
                            ))
                        pso2table.rows = pso2
                        page.update()
                    if col.value=='이닝':
                        for i in range(len(poc3)):
                            if poc3[i][0]==name.value:
                                poc3[i][1]=float(edit.value)

                        poc3.sort(key=lambda x: x[1], reverse=True)
                        pso3.clear()

                        for player_name, avg_value in poc3:
                            player_id = t1[player_name]
                            pso3.append(ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(pp[player_id][1])),
                                    ft.DataCell(ft.Text(ps[player_id][7])),
                                    ft.DataCell(ft.Text(ps[player_id][8])),
                                    ft.DataCell(ft.Text(ps[player_id][9])),
                                    ft.DataCell(ft.Text(ps[player_id][10])),
                                    ft.DataCell(ft.Text(ps[player_id][11])),
                                    ft.DataCell(ft.Text(ps[player_id][12])),
                                    ft.DataCell(ft.Text(pp[player_id][2])),
                                    ft.DataCell(ft.Text(pp[player_id][3])),
                                    ft.DataCell(ft.Text(pp[player_id][4])),
                                    ft.DataCell(ft.Text(pp[player_id][5])),
                                    ft.DataCell(ft.Text(pp[player_id][6])),
                                ]
                            ))
                        pso3table.rows = pso3
                        page.update()
                    if col.value=='승리':
                        for i in range(len(poc4)):
                            if poc4[i][0]==name.value:
                                poc4[i][1]=float(edit.value)

                        poc4.sort(key=lambda x: x[1], reverse=True)
                        pso4.clear()

                        for player_name, avg_value in poc4:
                            player_id = t1[player_name]
                            pso4.append(ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(pp[player_id][1])),
                                    ft.DataCell(ft.Text(ps[player_id][7])),
                                    ft.DataCell(ft.Text(ps[player_id][8])),
                                    ft.DataCell(ft.Text(ps[player_id][9])),
                                    ft.DataCell(ft.Text(ps[player_id][10])),
                                    ft.DataCell(ft.Text(ps[player_id][11])),
                                    ft.DataCell(ft.Text(ps[player_id][12])),
                                    ft.DataCell(ft.Text(pp[player_id][2])),
                                    ft.DataCell(ft.Text(pp[player_id][3])),
                                    ft.DataCell(ft.Text(pp[player_id][4])),
                                    ft.DataCell(ft.Text(pp[player_id][5])),
                                    ft.DataCell(ft.Text(pp[player_id][6])),
                                ]
                            ))
                        pso4table.rows = pso4
                        page.update()
                    if col.value=='홀드':
                        for i in range(len(poc5)):
                            if poc5[i][0]==name.value:
                                poc5[i][1]=float(edit.value)

                        poc5.sort(key=lambda x: x[1], reverse=True)
                        pso5.clear()

                        for player_name, avg_value in poc5:
                            player_id = t1[player_name]
                            pso5.append(ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(pp[player_id][1])),
                                    ft.DataCell(ft.Text(ps[player_id][7])),
                                    ft.DataCell(ft.Text(ps[player_id][8])),
                                    ft.DataCell(ft.Text(ps[player_id][9])),
                                    ft.DataCell(ft.Text(ps[player_id][10])),
                                    ft.DataCell(ft.Text(ps[player_id][11])),
                                    ft.DataCell(ft.Text(ps[player_id][12])),
                                    ft.DataCell(ft.Text(pp[player_id][2])),
                                    ft.DataCell(ft.Text(pp[player_id][3])),
                                    ft.DataCell(ft.Text(pp[player_id][4])),
                                    ft.DataCell(ft.Text(pp[player_id][5])),
                                    ft.DataCell(ft.Text(pp[player_id][6])),
                                ]
                            ))
                        pso5table.rows = pso5
                        page.update()
                    if col.value=='세이브':
                        for i in range(len(poc6)):
                            if poc6[i][0]==name.value:
                                poc6[i][1]=float(edit.value)

                        poc6.sort(key=lambda x: x[1], reverse=True)
                        pso6.clear()

                        for player_name, avg_value in poc6:
                            player_id = t1[player_name]
                            pso6.append(ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(pp[player_id][1])),
                                    ft.DataCell(ft.Text(ps[player_id][7])),
                                    ft.DataCell(ft.Text(ps[player_id][8])),
                                    ft.DataCell(ft.Text(ps[player_id][9])),
                                    ft.DataCell(ft.Text(ps[player_id][10])),
                                    ft.DataCell(ft.Text(ps[player_id][11])),
                                    ft.DataCell(ft.Text(ps[player_id][12])),
                                    ft.DataCell(ft.Text(pp[player_id][2])),
                                    ft.DataCell(ft.Text(pp[player_id][3])),
                                    ft.DataCell(ft.Text(pp[player_id][4])),
                                    ft.DataCell(ft.Text(pp[player_id][5])),
                                    ft.DataCell(ft.Text(pp[player_id][6])),
                                ]
                            ))
                        pso6table.rows = pso6
                        page.update()
                    name.value = None
                    col.value = None
                    edit.value = None
                    t.tabs[5].content = ft.Column([name,
                                                   col,
                                                   edit,
                                                   ft.ElevatedButton("입력", on_click=update_info_stat),
                                                   ])
                    page.update()

                    t.tabs[1].content = ft.Column([pv,ft.Row([ft.ElevatedButton('방어율순 정렬',on_click=eradef),ft.ElevatedButton('경기 수 순 정렬',on_click=gdef),ft.ElevatedButton('이닝순 정렬',on_click=inningdef),ft.ElevatedButton('승리순 정렬',on_click=wdef),ft.ElevatedButton('홀드순 정렬',on_click=hddef),ft.ElevatedButton('세이브순 정렬',on_click=svdef),ft.ElevatedButton('보직순 정렬',on_click=workdef)])])




                    page.update()




    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[

            ft.Tab(
                text="타자 출력",
                icon=ft.icons.BAR_CHART,

            ),
            ft.Tab(
                text="투수 출력",
                icon=ft.icons.BAR_CHART,

            ),
            ft.Tab(
                text="선수 입력",
                icon=ft.icons.ADD,
                content=ft.Column([name,
                                   grade,
                                   type,
                                   skill1,
                                   skill2,
                                   skill3,
                                   ft.ElevatedButton("입력", on_click=player_input)])

            ),
            ft.Tab(
                text="타자 성적 입력",
                icon=ft.icons.ADD,

                content=ft.Column([name,
                                   avg,
                                   obp,
                                   slg,
                                   ops,
                                   risp,
                                   ft.ElevatedButton("입력", on_click=batter_input)
                                   ])
            ),
            ft.Tab(
                text="투수 성적 입력",
                icon=ft.icons.ADD,
                content=ft.Column([name,
                                   era,
                                   g,
                                   inning,
                                   w,
                                   hld,
                                   sv,
                                   ft.ElevatedButton("입력", on_click=pitcher_input)
                                   ])
            ),
            ft.Tab(
                text="선수 정보 및 성적 편집",
                icon=ft.icons.EDIT,
                content=ft.Column([name,
                                   col,
                                   edit,
                                   ft.ElevatedButton("입력", on_click=update_info_stat)])

            ),
            ft.Tab(
                text="추천 타순",
                icon=ft.icons.INFO,


            ),

        ],
        expand=1,
    )

    page.add(t)
    page.update()

    btable = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("이름")),
            ft.DataColumn(ft.Text("타율")),
            ft.DataColumn(ft.Text("출루율")),
            ft.DataColumn(ft.Text("장타율")),
            ft.DataColumn(ft.Text("ops")),
            ft.DataColumn(ft.Text("득점권 타율")),
            ft.DataColumn(ft.Text("등급")),
            ft.DataColumn(ft.Text("카드 종류")),
            ft.DataColumn(ft.Text("고유능력1")),
            ft.DataColumn(ft.Text("고유능력2")),
            ft.DataColumn(ft.Text("고유능력3")),
        ],
        rows=[]
    )



    bv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False, on_scroll=True)
    bv.controls.append(btable)
    t.tabs[0].content = ft.Column([bv,ft.Row([ft.ElevatedButton('타율순 정렬',on_click=avgdef),ft.ElevatedButton('출루율순 정렬',on_click=obpdef),ft.ElevatedButton('장타율순 정렬',on_click=slgdef),ft.ElevatedButton('ops순 정렬',on_click=opsdef),ft.ElevatedButton('득점권 타율순 정렬',on_click=rispdef),ft.ElevatedButton('타선순 정렬',on_click=tasoondef)])])
    t.update()





    ptable = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("이름")),
            ft.DataColumn(ft.Text("방어율")),
            ft.DataColumn(ft.Text("경기 수")),
            ft.DataColumn(ft.Text("이닝")),
            ft.DataColumn(ft.Text("승리")),
            ft.DataColumn(ft.Text("홀드")),
            ft.DataColumn(ft.Text("세이브")),
            ft.DataColumn(ft.Text("등급")),
            ft.DataColumn(ft.Text("카드 종류")),
            ft.DataColumn(ft.Text("고유능력1")),
            ft.DataColumn(ft.Text("고유능력2")),
            ft.DataColumn(ft.Text("고유능력3")),
        ],
        rows=po
    )

    pv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False, on_scroll=True)
    pv.controls.append(ptable)
    t.tabs[1].content = ft.Column([pv,ft.Row([ft.ElevatedButton('방어율순 정렬',on_click=eradef),ft.ElevatedButton('경기 수 순 정렬',on_click=gdef),ft.ElevatedButton('이닝순 정렬',on_click=inningdef),ft.ElevatedButton('승리순 정렬',on_click=wdef),ft.ElevatedButton('홀드순 정렬',on_click=hddef),ft.ElevatedButton('세이브순 정렬',on_click=svdef),ft.ElevatedButton('보직순 정렬',on_click=workdef)])])
    t.update()

    pso1table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("이름")),
            ft.DataColumn(ft.Text("방어율")),
            ft.DataColumn(ft.Text("경기 수")),
            ft.DataColumn(ft.Text("이닝")),
            ft.DataColumn(ft.Text("승리")),
            ft.DataColumn(ft.Text("홀드")),
            ft.DataColumn(ft.Text("세이브")),
            ft.DataColumn(ft.Text("등급")),
            ft.DataColumn(ft.Text("카드 종류")),
            ft.DataColumn(ft.Text("고유능력1")),
            ft.DataColumn(ft.Text("고유능력2")),
            ft.DataColumn(ft.Text("고유능력3")),
        ],
        rows=pso1
    )

    pso1v = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False, on_scroll=True)
    pso1v.controls.append(pso1table)

    pso2table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("이름")),
            ft.DataColumn(ft.Text("방어율")),
            ft.DataColumn(ft.Text("경기 수")),
            ft.DataColumn(ft.Text("이닝")),
            ft.DataColumn(ft.Text("승리")),
            ft.DataColumn(ft.Text("홀드")),
            ft.DataColumn(ft.Text("세이브")),
            ft.DataColumn(ft.Text("등급")),
            ft.DataColumn(ft.Text("카드 종류")),
            ft.DataColumn(ft.Text("고유능력1")),
            ft.DataColumn(ft.Text("고유능력2")),
            ft.DataColumn(ft.Text("고유능력3")),
        ],
        rows=pso2
    )

    pso2v = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False, on_scroll=True)
    pso2v.controls.append(pso2table)

    pso3table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("이름")),
            ft.DataColumn(ft.Text("방어율")),
            ft.DataColumn(ft.Text("경기 수")),
            ft.DataColumn(ft.Text("이닝")),
            ft.DataColumn(ft.Text("승리")),
            ft.DataColumn(ft.Text("홀드")),
            ft.DataColumn(ft.Text("세이브")),
            ft.DataColumn(ft.Text("등급")),
            ft.DataColumn(ft.Text("카드 종류")),
            ft.DataColumn(ft.Text("고유능력1")),
            ft.DataColumn(ft.Text("고유능력2")),
            ft.DataColumn(ft.Text("고유능력3")),
        ],
        rows=pso3
    )

    pso3v = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False, on_scroll=True)
    pso3v.controls.append(pso3table)

    pso4table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("이름")),
            ft.DataColumn(ft.Text("방어율")),
            ft.DataColumn(ft.Text("경기 수")),
            ft.DataColumn(ft.Text("이닝")),
            ft.DataColumn(ft.Text("승리")),
            ft.DataColumn(ft.Text("홀드")),
            ft.DataColumn(ft.Text("세이브")),
            ft.DataColumn(ft.Text("등급")),
            ft.DataColumn(ft.Text("카드 종류")),
            ft.DataColumn(ft.Text("고유능력1")),
            ft.DataColumn(ft.Text("고유능력2")),
            ft.DataColumn(ft.Text("고유능력3")),
        ],
        rows=pso4
    )

    pso4v = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False, on_scroll=True)
    pso4v.controls.append(pso4table)

    pso5table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("이름")),
            ft.DataColumn(ft.Text("방어율")),
            ft.DataColumn(ft.Text("경기 수")),
            ft.DataColumn(ft.Text("이닝")),
            ft.DataColumn(ft.Text("승리")),
            ft.DataColumn(ft.Text("홀드")),
            ft.DataColumn(ft.Text("세이브")),
            ft.DataColumn(ft.Text("등급")),
            ft.DataColumn(ft.Text("카드 종류")),
            ft.DataColumn(ft.Text("고유능력1")),
            ft.DataColumn(ft.Text("고유능력2")),
            ft.DataColumn(ft.Text("고유능력3")),
        ],
        rows=pso5
    )

    pso5v = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False, on_scroll=True)
    pso5v.controls.append(pso5table)

    pso6table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("이름")),
            ft.DataColumn(ft.Text("방어율")),
            ft.DataColumn(ft.Text("경기 수")),
            ft.DataColumn(ft.Text("이닝")),
            ft.DataColumn(ft.Text("승리")),
            ft.DataColumn(ft.Text("홀드")),
            ft.DataColumn(ft.Text("세이브")),
            ft.DataColumn(ft.Text("등급")),
            ft.DataColumn(ft.Text("카드 종류")),
            ft.DataColumn(ft.Text("고유능력1")),
            ft.DataColumn(ft.Text("고유능력2")),
            ft.DataColumn(ft.Text("고유능력3")),
        ],
        rows=pso6
    )

    pso6v = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False, on_scroll=True)
    pso6v.controls.append(pso6table)









    bsotable=ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("이름")),
            ft.DataColumn(ft.Text("타율")),
            ft.DataColumn(ft.Text("출루율")),
            ft.DataColumn(ft.Text("장타율")),
            ft.DataColumn(ft.Text("ops")),
            ft.DataColumn(ft.Text("득점권 타율")),
            ft.DataColumn(ft.Text("등급")),
            ft.DataColumn(ft.Text("카드 종류")),
            ft.DataColumn(ft.Text("고유능력1")),
            ft.DataColumn(ft.Text("고유능력2")),
            ft.DataColumn(ft.Text("고유능력3")),
        ],
        rows=bso
    )
    bsov = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False, on_scroll=True)
    bsov.controls.append(bsotable)
    t.tabs[6].content = bsov
    t.update()
    page.update()

    bso1table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("이름")),
            ft.DataColumn(ft.Text("타율")),
            ft.DataColumn(ft.Text("출루율")),
            ft.DataColumn(ft.Text("장타율")),
            ft.DataColumn(ft.Text("ops")),
            ft.DataColumn(ft.Text("득점권 타율")),
            ft.DataColumn(ft.Text("등급")),
            ft.DataColumn(ft.Text("카드 종류")),
            ft.DataColumn(ft.Text("고유능력1")),
            ft.DataColumn(ft.Text("고유능력2")),
            ft.DataColumn(ft.Text("고유능력3")),
        ],
        rows=bso1
    )
    bsov1=ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False, on_scroll=True)
    bsov1.controls.append(bso1table)

    bso2table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("이름")),
            ft.DataColumn(ft.Text("타율")),
            ft.DataColumn(ft.Text("출루율")),
            ft.DataColumn(ft.Text("장타율")),
            ft.DataColumn(ft.Text("ops")),
            ft.DataColumn(ft.Text("득점권 타율")),
            ft.DataColumn(ft.Text("등급")),
            ft.DataColumn(ft.Text("카드 종류")),
            ft.DataColumn(ft.Text("고유능력1")),
            ft.DataColumn(ft.Text("고유능력2")),
            ft.DataColumn(ft.Text("고유능력3")),
        ],
        rows=bso2
    )
    bsov2 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False, on_scroll=True)
    bsov2.controls.append(bso2table)

    bso3table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("이름")),
            ft.DataColumn(ft.Text("타율")),
            ft.DataColumn(ft.Text("출루율")),
            ft.DataColumn(ft.Text("장타율")),
            ft.DataColumn(ft.Text("ops")),
            ft.DataColumn(ft.Text("득점권 타율")),
            ft.DataColumn(ft.Text("등급")),
            ft.DataColumn(ft.Text("카드 종류")),
            ft.DataColumn(ft.Text("고유능력1")),
            ft.DataColumn(ft.Text("고유능력2")),
            ft.DataColumn(ft.Text("고유능력3")),
        ],
        rows=bso3
    )
    bsov3 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False, on_scroll=True)
    bsov3.controls.append(bso3table)

    bso4table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("이름")),
            ft.DataColumn(ft.Text("타율")),
            ft.DataColumn(ft.Text("출루율")),
            ft.DataColumn(ft.Text("장타율")),
            ft.DataColumn(ft.Text("ops")),
            ft.DataColumn(ft.Text("득점권 타율")),
            ft.DataColumn(ft.Text("등급")),
            ft.DataColumn(ft.Text("카드 종류")),
            ft.DataColumn(ft.Text("고유능력1")),
            ft.DataColumn(ft.Text("고유능력2")),
            ft.DataColumn(ft.Text("고유능력3")),
        ],
        rows=bso4
    )
    bsov4 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False, on_scroll=True)
    bsov4.controls.append(bso4table)

ft.app(target=main)

