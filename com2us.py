import flet as ft
import database as db

name = ft.TextField(hint_text="이름")
grade = ft.TextField(hint_text="등급")
type = ft.TextField(hint_text="카드 종류")
skill1 = ft.TextField(hint_text="고유능력1")
skill2 = ft.TextField(hint_text="고유능력2")
skill3 = ft.TextField(hint_text="고유능력3")
avg = ft.TextField(hint_text="타율")
obp = ft.TextField(hint_text="출루율")
slg = ft.TextField(hint_text="장타율")
ops = ft.TextField(hint_text="ops")
risp = ft.TextField(hint_text="득점권 타율")
era = ft.TextField(hint_text="방어율")
g = ft.TextField(hint_text="경기수")
inning = ft.TextField(hint_text="이닝")
w = ft.TextField(hint_text="승리")
hld = ft.TextField(hint_text="홀드")
sv = ft.TextField(hint_text="세이브")
col = ft.TextField(hint_text="수정할 항목을 입력해 주세요")
edit = ft.TextField(hint_text="수정할 값을 입력해 주세요")


def main(page: ft.Page):
    t1 = dict()
    bn = []
    pn = []
    bp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ps = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    d = {'이름': 'name', '등급': 'grade', '종류': 'type', '고유능력1': 'skill1', '고유능력2': 'skill2', '고유능력3': 'skill3',
         '타율': 'avg', '출루율': 'obp', '장타율': 'slg', 'ops': 'ops', '득점권 타율': 'risp', '방어율': 'era', '경기수': 'g',
         '이닝': 'inning', '승리': 'g', '홀드': 'hld', '세이브': 'sv'}
    bo = []
    po = []
    boc = []
    bso = []
    whattosort = [1]
    def avgdef(e):
        whattosort.clear()
        whattosort.append(1)
    def tasoondef(e):
        pass
    def player_input(e):
        if name.value in t1:

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
                        print(boc)
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
                    name.value = None
                    col.value = None
                    edit.value = None
                    t.tabs[5].content = ft.Column([name,
                                                   col,
                                                   edit,
                                                   ft.ElevatedButton("입력", on_click=update_info_stat),
                                                   ])
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
    if whattosort[0]==0:
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
            rows=bo
        )
        print(whattosort)
    elif whattosort[0]==1:
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
            rows=bso
        )
        print(whattosort)
        print(bso)

    bv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False, on_scroll=True)

    bv.controls.append(btable)

    t.tabs[0].content = ft.Column([bv,ft.Row([ft.ElevatedButton('타율순 정렬',on_click=avgdef),ft.ElevatedButton('출루율순 정렬'),ft.ElevatedButton('장타율순 정렬'),ft.ElevatedButton('ops순 정렬'),ft.ElevatedButton('득점권 타율순 정렬'),ft.ElevatedButton('타선순 정렬',on_click=tasoondef)])])
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
    t.tabs[1].content = ft.Column([pv,ft.Row([ft.ElevatedButton('방어율순 정렬'),ft.ElevatedButton('경기 수 순 정렬'),ft.ElevatedButton('이닝순 정렬'),ft.ElevatedButton('승리순 정렬'),ft.ElevatedButton('홀드순 정렬'),ft.ElevatedButton('세이브순 정렬'),ft.ElevatedButton('보직순 정렬')])])
    t.update()

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


ft.app(target=main)

