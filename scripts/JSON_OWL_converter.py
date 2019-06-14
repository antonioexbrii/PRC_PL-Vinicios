import json
import re
import time
head = "http://prc.di.uminho.pt/2019/a75870/"
file="output.ttl"
ontology ="../Ontology/wineReviews.ttl"

def convert():
    o=open(ontology,"r",encoding="utf-8")
    f=open(file,"w",encoding="utf-8")
    for line in o:
        f.write(line)
    o.close()
    processJSON(f)
    f.close()
def treatWords(w):
    w = re.sub(r"[ \’\.]",r"_",w)
    w = re.sub(r'[&%$@]',r'et',w)
    w = re.sub(r'[\(\)\[\];°\']',r'',w)
    return w
def mapCountryKey(w):
    return {
        'US':'US',
        'Italy':'IT',
        'Portugal':'PT',
        'Spain':'ES',
        'France': 'FR',
        'Germany':'DE',
        'Argentina':'AR',
        'Chile':'CL',
        'Australia':'AU',
        'Austria':'AT',
        'New Zealand':'NZ',
        'Israel':'IL',
        'Hungary': 'HU',
        'Greece':'GR',
        'Romania':'RO',
        'Mexico':'MX',
        'Canada':'CA',
        'South Africa':'ZA'
    }.get(w,'aa')
def processJSON(f):
    countries=[]
    wines=[]
    provinces=[]
    tasters=[]
    wineries=[]
    reviews=[]
    with open('winemag.json',encoding="utf-8") as jsonfile:
        data=json.load(jsonfile)
        i=0
        for p in data:
            if(i>1000):
                break
            i=i+1
            if not (p['taster_name']):
                p['taster_name']='nd'
            else:
                processTaster(tasters,p['taster_name'],p['taster_twitter_handle'])
            if(p['country']):
                processCountry(countries,p['country'],p['province'],p['title'])
            else:
                p['country']:'nd'
            if(p['province']):
                processProvince(provinces,p['province'],p['country'],p['title'])
            else:
                p['province']='nd'
            if not (p['price']):
                p['price']='nd'
            if not (p['designation']):
                p['designation']='nd'
            if not (p['variety']):
                p['variety']='nd'
            if not (p['region_1']):
                p['region_1']='nd'
            if not (p['region_2']):
                p['region_2']='nd'
            if not (p['description']):
                p['description']='nd'
            if(p['winery']):
                processWinery(wineries,p['winery'],p['country'],p['title'])
            else:
                p['winery']='nd'
            processWine(wines,p['title'],p['price'],p['designation'],p['variety'],p['region_1'],p['region_2'],p['province'],p['country'],p['winery'])
            processReview(reviews,p['points'],p['title'],p['description'],p['taster_name'])
    for winery in wineries:
        generateWineryOWL(winery,f)
    for country in countries:
        generateCountryOWL(country,f)
    for province in provinces:
        generateProvinceOWL(province,f)
    for taster in tasters:
        generateTasterOWL(taster,f)
    for review in reviews:
        generateReviewOWL(review,f)
    for wine in wines:
        generateWineOWL(wine,f)

def generateCountryOWL(country,f):
    h1 = "### " + head + country['countryID']
    h2 = "\n:" + country['countryID'] + " rdf:type owl:NamedIndividual , \n\t\t\t:Country ;\n"
    h3 = "\t\t:countryName \"" + country['countryName']+"\";"
    countryKey = mapCountryKey(country['countryName'])
    h3 = h3 + '\n\t\t:countryKey \"' +countryKey+"\""
    for wn in country['wines']:
        h3 = h3 + ";\n\t\t:hasWine <"+head+wn+">"
    for pr in country['provinces']:
        h3 = h3 + ";\n\t\t:hasProvince <"+head+pr+">"
    fin = h1+h2+h3+".\n"
    f.write(fin)
def generateWineryOWL(winery,f):
    h1 = "### " + head + winery['wineryID']
    h2 = "\n:" + winery['wineryID'] + " rdf:type owl:NamedIndividual , \n\t\t\t:Winery ;\n\t\t:wineryName \""+winery['wineryName']+"\";"
    h3 = "\n\t\t:hasCountry :" + winery['country']
    for wn in winery['wines']:
        h3 = h3 + ";\n\t\t:hasWine <"+head+wn+">"
    fin = h1+h2+h3+".\n"
    f.write(fin)
def generateTasterOWL(taster,f):
    h1 = "### " + head + taster['tasterID']
    h2 = "\n:" + taster['tasterID'] + " rdf:type owl:NamedIndividual , \n\t\t\t:Taster ;\n\t\t:taster_name \""+taster['tasterName']+"\";"
    h3 = "\n\t\t:taster_twitter_handle \"" + taster['tasterTwitter']+"\""
    fin = h1+h2+h3+".\n"
    f.write(fin)
def generateReviewOWL(review,f):
    h1 = "### " + head + review['rid']
    h2 = "\n:" + review['rid'] + " rdf:type owl:NamedIndividual , \n\t\t\t:Review ;\n\t\t:isReviewOf <"+head+review['title']+">;"
    if(review['tasterName'] != 'nd'):
        h2 = h2 + "\n\t\t:hasTaster :"+review['tasterName']+';'
    h3 = "\n\t\t:description \""+review['description']+"\";"
    h4 = "\n\t\t:points \""+ review['points']+"\".\n"
    fin = h1+h2+h3+h4
    f.write(fin)
def generateProvinceOWL(province,f):
    h1 = "### " + head + province['provinceID']
    h2 = "\n:" + province['provinceID'] + " rdf:type owl:NamedIndividual , \n\t\t\t:Province ;"
    h3 = "\n\t\t:fromCountry :"+province['country']+";\n\t\t:provinceName \""+province['provinceName']+"\""
    for wi in province['wines']:
        h3 = h3 + ";\n\t\t:isOriginOf <"+head+wi+">"
    fin = h1+h2+h3+".\n"
    f.write(fin)
def generateWineOWL(wine,f):
    h1 = "### " + head + wine['wid']
    h1 = h1 + "\n<"+head+wine['wid']+"> "+"rdf:type owl:namedIndividual,\n\t\t\t:Wine ;\n\t\t:title \""+wine['title']+"\";"
    h1 = h1 + "\n\t\t:price \"" + str(wine['price']) + "\";"
    h1 = h1 + "\n\t\t:designation \"" + wine['designation'] + "\";"
    h1 = h1 + "\n\t\t:variety \"" + wine['variety'] + "\";"
    h1 = h1 + "\n\t\t:region_1 \"" + wine['region_1'] + "\";"
    h1 = h1 + "\n\t\t:region_2 \"" + wine['region_2'] + "\";"
    h1 = h1 + "\n\t\t:fromProvince :" + wine['province'] + ";"
    h1 = h1 + "\n\t\t:isFrom :"+ wine['country'] + ";"
    h1 = h1 + "\n\t\t:fromWinery :"+ wine['winery']
    fin = h1 +".\n"
    f.write(fin)
def processCountry(dict,name,province,wine):
    wine = treatWords(wine)
    ctr = treatWords(name)
    if(province):
        province = treatWords(province)
    else:
        province='nd'
    if name and not any(country['countryName'] == name for country in dict):
        tmp = {
            "countryID":ctr,
            "countryName":name,
            "provinces":[province],
            "wines":[wine]
        }
        dict.append(tmp.copy())
    else:
        for country in dict:
            if(country['countryName'] == name):
                if not any(wine == wine_iter for wine_iter in country['wines']):
                    country['wines'].append(wine)
                if not any(province == province_iter for province_iter in country['provinces']):
                    country['provinces'].append(province)
def processWine(dict,title,price,designation,variety,region_1,region_2,province,country,winery):
    if(country):
        country = treatWords(country)
    else:
        country='nd'
    if(province):
        province = treatWords(province)
    else:
        province='nd'
    if(winery):
        winery = treatWords(winery)
    else:
        winery='nd'
    wid = treatWords(title)
    if not any(wine['title'] == title for wine in dict):
        tmp = {
            "wid":wid,
            "title":title,
            "price":price,
            "designation":designation,
            "variety":variety,
            "region_1":region_1,
            "region_2":region_2,
            "province":province,
            "country":country,
            "winery":winery
        }
        dict.append(tmp.copy())
def processReview(dict,points,title,description,taster):
    rid=generateReviewId(points,title,taster)
    if (taster):
        taster = treatWords(taster)
    else:
        taster = 'nd'
    title=treatWords(title)
    tmp = {
        "rid":rid,
        "points":points,
        "title":title,
        "description":description,
        "tasterName":taster,
    }
    dict.append(tmp.copy())
def generateReviewId(points,title,taster):
    if(title and points and taster):
        title = title.split()
        tmp = points+title[0]+title[1]+taster
        tmp = treatWords(tmp)
        return tmp
    else:
        #Some JSON elements need fixing.
        dt = time.time_ns()
        dtt = (str(dt) + 'rr')[-8:-4]
        if (taster and points) and not title:
            tmp = points+taster+dtt
            tmp = treatWords(tmp)
            return tmp
        elif (taster and title) and not points:
            title=title.split()
            tmp = title[0]+title[1]+taster+dtt
            tmp = treatWords(tmp)
            return tmp
        elif (title and points) and not taster:
            title=title.split()
            tmp = points+title[0]+title[1]+dtt
            tmp = treatWords(tmp)
            return tmp
def processProvince(dict,name,country,wine):
    wine = treatWords(wine)
    if name and not any(province['provinceName'] == name for province in dict):
        provid = treatWords(name)
        if(country):
            country =treatWords(country)
        else:
            country='nd'
        tmp = {
            "provinceID":provid,
            "provinceName":name,
            "country":country,
            "wines":[wine]
        }
        dict.append(tmp.copy())
    else:
        for province in dict:
            if(province['provinceName'] == name):
                if not any(wine == wine_iter for wine_iter in province['wines']):
                    province['wines'].append(wine)
def processWinery(dict,name,country,wine):
    if (name is not None):
        wine = treatWords(wine)
        if not any(winery['wineryName'] == name for winery in dict):
            wid = treatWords(name)
            if not (country):
                ctr = 'nd'
            else:
                ctr = treatWords(country)
            tmp = {
                "wineryID":wid,
                "wineryName":name,
                "country":ctr,
                "wines":[wine]
            }
            dict.append(tmp.copy())
        else:
            for winery in dict:
                if(winery['wineryName'] == name):
                    if not any(wine == wine_iter for wine_iter in winery['wines']):
                        winery['wines'].append(wine)
def processTaster(dict,name,twitter):
    if not twitter:
        tw=''
    else:
        tw=twitter
    tid=treatWords(name)
    if name and not any(taster['tasterName'] == name for taster in dict):
        tmp = {
            "tasterID": tid,
            "tasterName":name,
            "tasterTwitter":tw,
        }
        dict.append(tmp.copy())
convert()