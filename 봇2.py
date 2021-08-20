import discord, datetime
import requests
import os
from bs4 import BeautifulSoup
import urllib
token = "ODc4MDY1NTY1NzA3NjY1NDE4.YR7wSA.v0bKKqlqaLEauaLTZ0zK1dOT66U"
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("시스템 가동중...")
    print(client.user)
    print("=====================================")

@client.event
async def on_message(message):
    if message.content == "안녕":
        await message.channel.send("안녕하세요 오늘도 좋은하루되세요!")

    if message.content == "ㅎㅇ":
        await message.channel.send("ㅂㅇ")

    if message.content == "이다윤":
        await message.channel.send("징징징징 투덜투덜 방장 줘어어ㅓㅓ ㅇㅈㄹ하는 탐켄치")

    if message.content == "이찬우":
        await message.channel.send("저의 제작자 이면서도 김도현의 노예입니다.")

    if message.content == "박민":
        await message.channel.send("박민서는 대가리 빡빡이입니다.")

    if message.content == "김도현":
        await message.channel.send("이 서버의 관리자 이면서 겜돌이입니다.")

    if message.content == "머리숱":
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.dark_green(), title="머리숱 확인을 요청하셨습니다!", description="개인적으로 문의시 추가 가능.")
        embed.add_field(name="머리숱이 없는 사람", value="박민서, 이다윤", inline=True)
        embed.add_field(name="머리숱이 있는 사람", value="이찬우, 김도현, 김지민", inline=True)
        await message.channel.send(embed=embed)
    
    if message.content.startswith(f"메세지"):
        ch = client.get_channel(int(message.content[7:25]))
        await ch.send(message.content[26:])

    if message.content == '내 정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        print(date)
        await message.channel.send(f"{message.author.mention} : {date.year}/{date.month}/{date.day}입니다.")
        await message.channel.send(f"{message.author.mention} : {user.name} / {user.id} / {user.display_name}")
        await message.channel.send(message.author.avatar_url)

    if message.content.startswith("청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지 삭제됨!")

    if message.content.startswith("밴"):
        member = message.guild.get_member(int(message.content.split(" ")[1]))
        await message.guild.kick(member, reason=' '.join(message.content.split(" ")[2:]))
        await message.channel.send("일반 밴 완료하였습니다")

    if message.content.startswith("차단밴"):
        member = message.guild.get_member(int(message.content.split(" ")[1]))
        await message.guild.ban(member, reason=' '.join(message.content.split(" ")[2:]))
        await message.channel.send("차단 밴 완료하였습니다")

    if message.content == "김지민":
        await message.channel.send("단발 존버합니다.")

    if message.content == "?":
        await message.channel.send("????")

    if message.content == '한강온도':
        json = requests.get('http://hangang.dkserver.wo.tc/').json()
        temp = json.get("temp") # 한강온도
        time = json.get("time") # 측정시간
        embed = discord.Embed(title='💧 한강온도', description=f'{temp}°C', colour=discord.Colour.blue())
        embed.set_footer(text=f'{time}에 측정됨')
        await message.channel.send(embed=embed)

    if message.content == '코로나':
        url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        datecr = soup.find('span', {'class': 't_date'}) #기준날짜
        #print(f'기준일: {datecr.string}')

        totalcovid = soup.select('dd.ca_value')[0].text #누적 확진자수
        #print(f'누적 확진자: {totalcovid} 명')

        todaytotalcovid = soup.select('p.inner_value')[0].text #당일 확진자수 소계
        #print(f'확진자 소계: {todaytotalcovid} 명')

        todaydomecovid = soup.select('p.inner_value')[1].text #당일 국내발생 확진자수
        #print(f'국내발생: {todaydomecovid} 명')

        todayforecovid = soup.select('p.inner_value')[2].text #당일 해외유입 확진자수
        #print(f'해외유입: {todayforecovid} 명')

        totalca = soup.select('dd.ca_value')[2].text #누적 격리해제
        #print(f'누적 격리해제: {totalca} 명')

        todayca = soup.select('span.txt_ntc')[0].text #당일 격리해제
        #print(f'격리해제: {todayca} 명')

        totalcaing = soup.select('dd.ca_value')[4].text #누적 격리중
        #print(f'누적 격리중: {totalcaing}')

        todaycaing = soup.select('span.txt_ntc')[1].text #당일 격리중
        #print(f'격리중: {todaycaing} 명')

        totaldead = soup.select('dd.ca_value')[6].text #누적 사망자
        #print(f'누적 사망자: {totaldead} 명')

        todaydead = soup.select('span.txt_ntc')[2].text #당일 사망자
        #print(f'사망자: {todaydead} 명')

        covidembed = discord.Embed(title='코로나19 국내 발생현황', description="", color=0xFF0F13, url='http://ncov.mohw.go.kr/')
        covidembed.add_field(name='🦠 확진환자', value=f'{totalcovid}({todaytotalcovid}) 명'
                                                f'\n\n국내발생: {todaydomecovid} 명\n해외유입: {todayforecovid} 명', inline=False)
        covidembed.add_field(name='😷 격리중', value=f'{totalcaing}({todaycaing}) 명', inline=False)
        covidembed.add_field(name='🆓 격리해제', value=f'{totalca}({todayca}) 명', inline=False)
        covidembed.add_field(name='💀 사망자', value=f'{totaldead}({todaydead}) 명', inline=False)
        covidembed.set_footer(text=datecr.string)
        await message.channel.send(embed=covidembed)

    if message.content.startswith('위성'):
        url = 'https://www.weather.go.kr/weather/images/satellite_service.jsp'
        res = urllib.request.urlopen(url).read()

        soup = BeautifulSoup(res, 'html.parser')
        soup = soup.find("div", class_="image-player-slide")
        imgUrl = 'https://www.weather.go.kr' + soup.find("img")["src"]

        typoonEmbed = discord.Embed(title='천리안 2A호 위성사진', description='제공: 기상청', colour=discord.Colour.dark_grey())
        typoonEmbed.set_image(url=imgUrl)
        await message.channel.send(embed=typoonEmbed)

access_token = os.environ["BOT_TOKEN"]
client.run('access_token')
