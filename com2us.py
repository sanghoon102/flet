import flet as ft
import database as db


name=ft.TextField(hint_text="이름")
grade=ft.TextField(hint_text="등급")
type=ft.TextField(hint_text="카드 종류")
skill1=ft.TextField(hint_text="고유능력1")
skill2=ft.TextField(hint_text="고유능력2")
skill3=ft.TextField(hint_text="고유능력3")
avg=ft.TextField(hint_text="타율")
obp=ft.TextField(hint_text="출루율")
slg=ft.TextField(hint_text="장타율")
ops= ft.TextField(hint_text="ops")
risp=ft.TextField(hint_text="득점권 타율")
era=ft.TextField(hint_text="방어율")
g=ft.TextField(hint_text="경기수")
inning=ft.TextField(hint_text="이닝")
w= ft.TextField(hint_text="승리")
hld=ft.TextField(hint_text="홀드")
sv=ft.TextField(hint_text="세이브")



def main(page: ft.Page):
    t1 = dict()
    bn=[]
    pn=[]
    bp=[0,0,0,0,0,0,0,0,0,0]
    bs=[0,0,0,0,0,0,0,0,0,0]
    pp=[0,0,0,0,0,0,0,0,0,0,0,0]
    ps=[0,0,0,0,0,0,0,0,0,0,0,0]


    def player_input(e):

        db.insert_player(name.value,grade.value,type.value,skill1.value,skill2.value,skill3.value)
        t1[name.value]=len(t1)+1

    def batter_input(a):

        db.insert_batter_stats(t1[name.value],avg.value,obp.value,slg.value,ops.value,risp.value)
        bp[t1[name.value]],bs[t1[name.value]]=db.get_batter_info(t1[name.value])
        bn.append(name.value)
        print(bp[t1[name.value]][1],bs[t1[name.value]][2],bs[t1[name.value]][3],bs[t1[name.value]][4],bs[t1[name.value]][5],bs[t1[name.value]][6],bp[t1[name.value]][2],bp[t1[name.value]][3],bp[t1[name.value]][4],bp[t1[name.value]][5],bp[t1[name.value]][6])
    def pitcher_input(e):
        db.insert_pitcher_stats(t1[name.value],era.value,g.value,inning.value,w.value,hld.value,sv.value)
        pp[t1[name.value]],ps[t1[name.value]]=db.get_pitcher_info(t1[name.value])
        pn.append(name.value)
        print(pp[t1[name.value]][1],ps[t1[name.value]][7],ps[t1[name.value]][8],ps[t1[name.value]][9],ps[t1[name.value]][10],ps[t1[name.value]][11],ps[t1[name.value]][12],pp[t1[name.value]][2],pp[t1[name.value]][3],pp[t1[name.value]][4],pp[t1[name.value]][5],pp[t1[name.value]][6])

    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[

            ft.Tab(
                text="타자 출력",
                icon=ft.icons.BAR_CHART,
                content=ft.DataTable(
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
                    rows=[

                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("맛자욱")),
                                    ft.DataCell(ft.Text("맛자욱")),
                                    ft.DataCell(ft.Text("맛자욱")),
                                    ft.DataCell(ft.Text("맛자욱")),
                                    ft.DataCell(ft.Text("맛자욱")),
                                    ft.DataCell(ft.Text("맛자욱")),
                                    ft.DataCell(ft.Text("맛자욱")),
                                    ft.DataCell(ft.Text("맛자욱")),
                                    ft.DataCell(ft.Text("맛자욱")),
                                    ft.DataCell(ft.Text("맛자욱")),
                                    ft.DataCell(ft.Text("맛자욱"))


                                ],
                            ),


                    ],

                ),
            ),
            ft.Tab(
                text="투수 출력",
                icon=ft.icons.BAR_CHART,
                content=ft.DataTable(
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
                    rows=[

                        ft.DataRow(
                            cells=[


                            ],


                        ),


                    ],
                ),
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
                                   ft.ElevatedButton("입력",on_click=player_input)])

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
                content=ft.TextField(hint_text="고칠 선수의 이름을 입력하세요")
            ),
            ft.Tab(
                text="추천 타순",
                icon=ft.icons.INFO,
                content=ft.DataTable(
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
                    rows=[

                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("박해민")),
                                ft.DataCell(ft.Text("0.300")),
                                ft.DataCell(ft.Text("0.393")),
                                ft.DataCell(ft.Text("0.455")),
                                ft.DataCell(ft.Text("0.848")),
                                ft.DataCell(ft.Text("0.323")),
                                ft.DataCell(ft.Text("플래티넘")),
                                ft.DataCell(ft.Text("시그니처")),
                                ft.DataCell(ft.Text("예지력")),
                                ft.DataCell(ft.Text("게스히터")),
                                ft.DataCell(ft.Text("집중력")),
                            ],
                        ),

                    ],
                ),
            ),

        ],
        expand=1,
    )


    page.add(t)



ft.app(target=main)