import requests
import json
import xmltodict
from elasticsearch import Elasticsearch



#funcion

def get_data(date):
    url = "http://openapi.seoul.go.kr:8088/5250614f686b7368363867486c654e/json/CardSubwayStatsNew/1/1000/2020"+str(date)
    req = requests.get(url)
    html = req.text
    json_data = json.loads(html)
    json_data = trim_data(json_data)
    return json_data

def get_location(data,station):
    # lat = -1.0
    # lon = -1.0
    for i in data:
        if i['name'] == station:
            # print("!!!!!",station,"!!!!!!")
            lat = i['lat']
            lon = i['lng']
    # if lat == -1.0:
    #     print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ERROR!: ", station)
        
    return lat,lon

def trim_data(json_data):
    for i in json_data['CardSubwayStatsNew']['row']:
        if(i['SUB_STA_NM']=='서울역'):
            i['SUB_STA_NM'] = '서울'
        elif(i['SUB_STA_NM']=='청량리(서울시립대입구)'):
            i['SUB_STA_NM'] = '청량리'
        elif(i['SUB_STA_NM']=='대림(구로구청)'):
            i['SUB_STA_NM'] = '대림'
        elif(i['SUB_STA_NM']=='동대문역사문화공원(DDP)'):
            i['SUB_STA_NM'] = '동대문역사문화공원'
        elif(i['SUB_STA_NM']=='왕십리(성동구청)'):
            i['SUB_STA_NM'] = '왕십리'
        elif(i['SUB_STA_NM']=='강변(동서울터미널)'):
            i['SUB_STA_NM'] = '강변'
        elif(i['SUB_STA_NM']=='구의(광진구청)'):
            i['SUB_STA_NM'] = '구의'
        elif(i['SUB_STA_NM']=='잠실(송파구청)'):
            i['SUB_STA_NM'] = '잠실'
        elif(i['SUB_STA_NM']=='삼성(무역센터)'):
            i['SUB_STA_NM'] = '삼성'
        elif(i['SUB_STA_NM']=='교대(법원.검찰청)'):
            i['SUB_STA_NM'] = '교대'
        elif(i['SUB_STA_NM']=='낙성대(강감찬)'):
            i['SUB_STA_NM'] = '낙성대'
        elif(i['SUB_STA_NM']=='서울대입구(관악구청)'):
            i['SUB_STA_NM'] = '서울대입구'
        elif(i['SUB_STA_NM']=='충정로(경기대입구)'):
            i['SUB_STA_NM'] = '충정로'
        elif(i['SUB_STA_NM']=='용두(동대문구청)'):
            i['SUB_STA_NM'] = '용두'
        elif(i['SUB_STA_NM']=='경복궁(정부서울청사)'):
            i['SUB_STA_NM'] = '경복궁'
        elif(i['SUB_STA_NM']=='남부터미널(예술의전당)'):
            i['SUB_STA_NM'] = '남부터미널'
        elif(i['SUB_STA_NM']=='양재(서초구청)'):
            i['SUB_STA_NM'] = '양재'
        elif(i['SUB_STA_NM']=='수유(강북구청)'):
            i['SUB_STA_NM'] = '수유'
        elif(i['SUB_STA_NM']=='미아(서울사이버대학)'):
            i['SUB_STA_NM'] = '미아'
        elif(i['SUB_STA_NM']=='성신여대입구(돈암)'):
            i['SUB_STA_NM'] = '성신여대입구'
        elif(i['SUB_STA_NM']=='한성대입구(삼선교)'):
            i['SUB_STA_NM'] = '한성대입구'
        elif(i['SUB_STA_NM']=='회현(남대문시장)'):
            i['SUB_STA_NM'] = '회현'
        elif(i['SUB_STA_NM']=='숙대입구(갈월)'):
            i['SUB_STA_NM'] = '숙대입구'
        elif(i['SUB_STA_NM']=='이촌(국립중앙박물관)'):
            i['SUB_STA_NM'] = '이촌'
        elif(i['SUB_STA_NM']=='동작(현충원)'):
            i['SUB_STA_NM'] = '동작'
        elif(i['SUB_STA_NM']=='총신대입구(이수)'):
            i['SUB_STA_NM'] = '이수'
        elif(i['SUB_STA_NM']=='신정(은행정)'):
            i['SUB_STA_NM'] = '신정'
        elif(i['SUB_STA_NM']=='오목교(목동운동장앞)'):
            i['SUB_STA_NM'] = '오목교'
        elif(i['SUB_STA_NM']=='광화문(세종문화회관)'):
            i['SUB_STA_NM'] = '광화문'
        elif(i['SUB_STA_NM']=='군자(능동)'):
            i['SUB_STA_NM'] = '군자'
        elif(i['SUB_STA_NM']=='아차산(어린이대공원후문)'):
            i['SUB_STA_NM'] = '아차산'
        elif(i['SUB_STA_NM']=='광나루(장신대)'):
            i['SUB_STA_NM'] = '광나루'
        elif(i['SUB_STA_NM']=='천호(풍납토성)'):
            i['SUB_STA_NM'] = '천호'
        elif(i['SUB_STA_NM']=='굽은다리(강동구민회관앞)'):
            i['SUB_STA_NM'] = '굽은다리'
        elif(i['SUB_STA_NM']=='올림픽공원(한국체대)'):
            i['SUB_STA_NM'] = '올림픽공원'
        elif(i['SUB_STA_NM']=='새절(신사)'):
            i['SUB_STA_NM'] = '새절'
        elif(i['SUB_STA_NM']=='증산(명지대앞)'):
            i['SUB_STA_NM'] = '증산'
        elif(i['SUB_STA_NM']=='월드컵경기장(성산)'):
            i['SUB_STA_NM'] = '월드컵경기장'
        elif(i['SUB_STA_NM']=='광흥창(서강)'):
            i['SUB_STA_NM'] = '광흥창'
        elif(i['SUB_STA_NM']=='대흥(서강대앞)'):
            i['SUB_STA_NM'] = '대흥'
        elif(i['SUB_STA_NM']=='녹사평(용산구청)'):
            i['SUB_STA_NM'] = '녹사평'
        elif(i['SUB_STA_NM']=='안암(고대병원앞)'):
            i['SUB_STA_NM'] = '안암'
        elif(i['SUB_STA_NM']=='고려대(종암)'):
            i['SUB_STA_NM'] = '고려대'
        elif(i['SUB_STA_NM']=='월곡(동덕여대)'):
            i['SUB_STA_NM'] = '월곡'
        elif(i['SUB_STA_NM']=='상월곡(한국과학기술연구원)'):
            i['SUB_STA_NM'] = '상월곡'
        elif(i['SUB_STA_NM']=='화랑대(서울여대입구)'):
            i['SUB_STA_NM'] = '화랑대'
        elif(i['SUB_STA_NM']=='봉화산(서울의료원)'):
            i['SUB_STA_NM'] = '봉화산'
        elif(i['SUB_STA_NM']=='공릉(서울과학기술대)'):
            i['SUB_STA_NM'] = '공릉'
        elif(i['SUB_STA_NM']=='상봉(시외버스터미널)'):
            i['SUB_STA_NM'] = '상봉'
        elif(i['SUB_STA_NM']=='용마산(용마폭포공원)'):
            i['SUB_STA_NM'] = '용마산'
        elif(i['SUB_STA_NM']=='어린이대공원(세종대)'):
            i['SUB_STA_NM'] = '어린이대공원'
        elif(i['SUB_STA_NM']=='숭실대입구(살피재)'):
            i['SUB_STA_NM'] = '숭실대입구'
        elif(i['SUB_STA_NM']=='온수(성공회대입구)'):
            i['SUB_STA_NM'] = '온수'
        elif(i['SUB_STA_NM']=='몽촌토성(평화의문)'):
            i['SUB_STA_NM'] = '몽촌토성'
        elif(i['SUB_STA_NM']=='남한산성입구(성남법원.검찰청)'):
            i['SUB_STA_NM'] = '남한산성입구'
        elif(i['SUB_STA_NM']=='마곡나루(서울식물원)'):
            i['SUB_STA_NM'] = '마곡나루'
        elif(i['SUB_STA_NM']=='흑석(중앙대입구)'):
            i['SUB_STA_NM'] = '흑석'
        elif(i['SUB_STA_NM']=='쌍용(나사렛대)'):
            i['SUB_STA_NM'] = '쌍용'
        elif(i['SUB_STA_NM']=='신창(순천향대)'):
            i['SUB_STA_NM'] = '신창'
        
        if i['LINE_NUM'] == '9호선2~3단계' : i['LINE_NUM'] = '9호선'
        elif i['LINE_NUM'] == '공항철도 1호선' : i['LINE_NUM'] = '공항철도'
        elif i['LINE_NUM'] == '경의선' : i['LINE_NUM'] = '경의중앙선'
        elif i['LINE_NUM'] == '중앙선' : i['LINE_NUM'] = '경의중앙선'
        elif i['LINE_NUM'] == '경부선' : i['LINE_NUM'] = '1호선'
        elif i['LINE_NUM'] == '경원선' : i['LINE_NUM'] = '1호선'
        elif i['LINE_NUM'] == '경인선' : i['LINE_NUM'] = '1호선'
    return json_data

def make_daylist():
    daylist=[]
    for m in range(6,13,1):
        if(m==6 or m==9 or m==11):
            mm=31
        elif(m==12):
            mm=17
        else:
            mm=32
        for d in range(1, mm, 1):
            if m<10:
                if d < 10:
                    daylist.append('0'+str(m)+'0'+str(d))
                else:
                    daylist.append('0'+str(m)+str(d))
            else:
                if d < 10:
                    daylist.append(str(m)+'0'+str(d))
                else:
                    daylist.append(str(m)+str(d))
    return daylist


#init


data = []
with open('station_coordinate.json', 'r') as f:
    json_location = json.load(f)

#main
def append_data(data):
    daylist=make_daylist()
    for d in daylist:
        json_data = get_data(d)
        doc = {}
        for i in json_data['CardSubwayStatsNew']['row']:
            name = i['SUB_STA_NM']
            if name in doc and (doc[name]['USE_DT'] == i['USE_DT']):
                doc[name]['RIDE_PASGR_NUM'] += i['RIDE_PASGR_NUM']
                doc[name]['ALIGHT_PASGR_NUM'] += i['ALIGHT_PASGR_NUM']
            else:
                doc[name] = i
        for i in doc:
            data.append(doc[i])


append_data(data)

for i in data:
    lat, lon = get_location(json_location,i['SUB_STA_NM'])
    i['location'] = {'lat': lat, 'lon' : lon}
    a = i['USE_DT']
    i['USE_DT'] = a[:4]+'-'+a[4:6]+'-'+a[6:]
    #print(i)



# print(get_location(json_location,'봉은사'))

#print(get_location(json_location,"녹양"))
     
# for i in json_data['CardSubwayStatsNew']['row']:

#     x,y = get_location(json_location, i['SUB_STA_NM'])
#     i['location'] = {'geo_x':x,'geo_y':y} #= 


# for i in json_data['CardSubwayStatsNew']['row']:
#     print(i)



with open("mapping.json", 'r') as f:
        mapping = json.load(f)

es = Elasticsearch('localhost:9200')
index = "seoul_gyeonggi_metro"
es.indices.create(index=index, body=mapping)
for i in data:
    es.index(index=index, doc_type="_doc", body=i)

