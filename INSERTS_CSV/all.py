print("hello world")

import random
import csv
import time
import radar
from dateutil.relativedelta import relativedelta
from lorem_text import lorem
import os
import sys
from os import listdir

def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

orgList = ['A.C.E.R.', 'B.E.R.E.C.', 'E.A.S.A.', 'E.B.A.', 'E.C.B.',
           'E.C.D.C.', 'E.CH.A.', 'E.D.P.B.', 'E.D.P.S.', 'E.E.A.',
           'E.F.S.A.', 'E.I.G.E.', 'E.I.O.P.A.', 'E.L.A.', 'E.M.S.A.',
           'E.R.A.', 'EU-OSHA', 'E.U.S.P.A.', 'F.R.A.', 'E.S.A.']

# Agency for the Cooperation of Energy Regulations
# BEREC
# European Aviation Safety Agency
# European Banking Authority
# European Central Bank
# European Centre for Disease prevantion and Control
# European CHemicals Agency
# European Data Protection Board
# European Data Protection Supervisor
# European Enviroment Agency
# European Food Safety Authority
# European Institute for Gender Equality
# European Insurance and Occupational Pensions Authority
# European Labour Authority
# European Maritime Safety Agency
# European Railways Agency
# European Agency for Safety and Health at Work
# European Union Agency for the Space Programme
# Fundamental Rights Agency
# European Space Agency

orgNames = ["Agency for the Cooperation of Energy Regulations",
            "BEREC",
            "European Aviation Safety Agency",
            "European Banking Authority",
            "European Central Bank",
            "European Centre for Disease prevantion and Control",
            "European CHemicals Agency",
            "European Data Protection Board",
            "European Data Protection Supervisor",
            "European Environment Agency",
            "European Food Safety Authority",
            "European Institute for Gender Equality",
            "European Insurance and Occupational Pensions Authority",
            "European Labour Authority",
            "European Maritime Safety Agency",
            "European Railways Agency",
            "European Agency for Safety and Health at Work",
            "European Union Agency for the Space Programme",
            "Fundamental Rights Agency",
            "European Space Agency"
            ]

orgCountries = ["Slovenia", "Latvia", "Germany", "France", "Germany", "Sweden", "Finland",
                "Belgium", "Belgium", "Denmark", "Italy", "Lithuania", "Germany", "Slovakia",
                "Portugal", "France", "Spain", "Czechia", "Austria", "France"]

orgCities = ["Ljubljana", "Riga", "Cologne", "Paris", "Frankfurt am Main", "Solna",
             "Helsinki", "Bruxelles", "Bruxelles", "Copenhagen", "Parma", "Vilnius",
             "Frankfurt am Main", "Bratislava", "Lisbon", "Valenciennes", "Bilbao",
             "Prague", "Vienna", "Paris"]

orgStreets = ["republike", "Zigfrida Annas Meierovica boulevard", "Ottoplatz",
              "avenue Andre Prothin", "Sonnemannstrasse", "Gustav III:s Boulevard",
              "Telakkakatu", "Rue Montoyer", "Rue Montoyer", "Kongens Nytorv", "Via Carlo Magno",
              "Gedimino pr.", "Westhafenplatz", "Landererova", "Cais das Pombas", "rue Marc Lefrancq",
              "Santiago de Compostela", "Janovskeho", "Schwarzenbergplatz", "Rue du General Bertrand"]

orgStreetNums = [3, 14, 1, 20, 20, 73, 6, 30, 30, 1, 1, 16, 1, 12, 1, 120, 12, 438, 11, 24]

orgPostalCodes = ["01000", "01050", "50679", "92400", "60314", "16973", "00150", "B1000",
                  "B1000", "01050", "43126", "01103", "60327", "81109", "01272", "59300",
                  "48003", "17000", "A1040", "75007"]

orgPhones = ["+386082053400", "+37129578999", "492218999000", "+33186527000",
             "+496913447455", "+460858601678", "+3589686180", "+3222831900",
             "+3222831900", "+4533367100", "+390521036111", "+37052157400",
             "+4906995111920", "+3706994726458", "+3222999696",
             "+33327096500", "+34944358400", "+420234766000", "431580300",
             "+33153697654"]

print("We have", str(len(orgNames)), "names")
print("We have", str(len(orgCountries)), "organizations")
print("We have", str(len(orgCities)), "cities")
print("We have", str(len(orgStreets)), "streets")
print("We have", str(len(orgStreetNums)), "street numbers")
print("We have", str(len(orgPostalCodes)), "postal codes")
print("We have", str(len(orgPhones)), "phones")


categories = ["Univ", "Comp", "Centr"]

sectors = ["Physics", "Math", "Chemistry", "Biology", "C.Science"]

titles = [
    "Monte Mirage",
    "Enter Coding",
    "Mustangs",
    "Instant Galaxy",
    "Odyssey",
    "MadMatrix",
    "Titan",
    "Ancient Dots",
    "Himalaya Fly",
    "Xena",
    "Caveman Lawyers",
    "Lonely Fox",
    "Switch and Swift",
    "Illumino Eye",
    "Honeycomb",
    "Vegas",
    "The Social Experiment",
    "sienna",
    "Hades",
    "Longhorns",
    "Aurora",
    "GoodTrace",
    "A Salute to New Workers",
    "Great Marvell",
    "Horned Frogs",
    "Indie Profilers",
    "Casanova",
    "Plutonium",
    "Mentee to Mentor",
    "The Coding Awards",
    "Excalibur Training",
    "Yodha",
    "Great Leadership",
    "Cowbelles",
    "Apollo",
    "RapidBrite",
    "Excel and Elevate Training",
    "The Art of Codes",
    "Coding Region",
    "Cold Fusion",
    "Rhinestone",
    "Disco Ninjas",
    "Kingsmen",
    "Irongate",
    "Poseidon",
    "Cyclone",
    "TruQuest",
    "Pure Panther",
    "Vikings",
    "Bongo",
    "Disco Divas",
    "Associations Now",
    "Diesel",
    "Canary",
    "Nautilus",
    "Colossus",
    "Quadro",
    "Matadors",
    "Olive Ong",
    "HopeStone",
    "Passion Chasers",
    "Social Geek Made",
    "Crusader",
    "The Experienced dude",
    "Code Poltergeists",
    "Rainbow Wish",
    "Rapid Dirt",
    "The Success",
    "Blue Skywalkers",
    "Indigo",
    "Fester",
    "Mango",
    "Limitless Horizons",
    "School Leadership 2.0",
    "Zulu"] # 75




def main(aboutNum = 50, researchersNum = 100, executivesNum = 30, projectsNum = 50,
         organizationsNum = 20, programsNum = 30, reportsNum = 10):
    f = open('firstNames.txt')
    first = f.read().split('\n')
    f.close()

    f = open('lastNames.txt')
    last = f.read().split('\n')
    f.close()

    f = open('firstMaleNames.txt')
    firstMale = f.read().split('\n')
    f.close()

    f = open('firstFemaleNames.txt')
    firstFemale = f.read().split('\n')
    f.close()

    """aboutNum = 1000
    researchersNum = 1000
    executivesNum = 1000
    projectsNum = len(titles)
    organizationsNum = 10
    programsNum = 100
    reportsNum = 100"""
    phonesNum = 2*organizationsNum

    lorems = []
    for words in range(75, 75 + projectsNum):
        lorems.append(lorem.words(words))

    about = []
    researchers = []
    executives = []
    projects = []
    organizations = []
    programs = []
    reports = []
    phones = []
    works_at = []
    works_atNum = 0

    for i in range(researchersNum):
        #for exIndex in range(executivesNum):
        ### RESEARCHERS BEGIN ###
        curResFirst = round(random.random()*len(first))
        curResLast = round(random.random()*len(last))
        randomResBirth = radar.random_datetime(start='1960-01-01', stop='2001-11-28T23:59:59')
        randomResStart = radar.random_datetime(start='2019-06-06', stop='2022-05-10T23:59:59')
        if (random.randint(0, 1)):
            curResMaleFirst = round(random.random()*len(firstMale))
            researchersData = ['r' + (4-len(str(i)))*'0'+str(i), random.choice(firstMale), random.choice(last), 'M', randomResBirth.strftime('%Y-%m-%d'), random.choice(orgList), randomResStart.strftime('%Y-%m-%d')]
            researchers.append(researchersData)
        else:
            curResFemaleFirst = round(random.random()*len(firstFemale))
            researchersData = ['r' + (4-len(str(i)))*'0'+str(i), random.choice(firstFemale), random.choice(last), 'F', randomResBirth.strftime('%Y-%m-%d'), random.choice(orgList), randomResStart.strftime('%Y-%m-%d')]
            researchers.append(researchersData)
        ### RESEARCHERS END ###

        ### EXECUTIVES BEGIN ###
        # curExFirst = round(random.random()*len(first))
        # curExLast = round(random.random()*len(last))
        if (i < executivesNum):
            executivesData = ['e' + (4-len(str(i)))*'0'+str(i), random.choice(first), random.choice(last)]
            executives.append(executivesData)
        ### EXECUTIVES END ###
        #print(str(i + 1)+"/1000 thousant loops")

    for i in range(aboutNum):
        fieldsNum = random.randint(1, 3)
        sectorList = []
        for j in range(fieldsNum):
            while (True):
                newSector = random.choice(sectors)
                if (newSector not in sectorList):
                    break
            sectorList.append(newSector)
        
        for j in range(fieldsNum):
            aboutData = ['prj' + (2-len(str(i)))*'0'+str(i), sectorList[j]]
            about.append(aboutData)

    for i in range(organizationsNum):
        print(i, orgNames[i])
        # orgIndex = random.randint(0, len(orgCountries) - 2)
        categ = random.choice(categories)
        ["Univ", "Comp", "Centr"]
        if (categ == "Univ"):
            eq = "NULL"
            fm = random.randint(1, 100)*1000
            fa = "NULL"
        elif (categ == "Comp"):
            eq = random.randint(1, 100)*1000
            fm = "NULL"
            fa = "NULL"
        else:
            eq = "NULL"
            fm = random.randint(1, 100)*1000
            fa = random.randint(1, 100)*1000
        organizationsData = [orgList[i], categ, orgNames[i], orgStreets[i],
                             orgStreetNums[i], orgPostalCodes[i], orgCities[i], eq, fm, fa]
        phonesData = [orgPhones[i], orgPhones[i][:-2] + str(int(orgPhones[i][-1]) + 1)]
        organizations.append(organizationsData)
        phones.append(phonesData)

    for i in range(programsNum):
        dep = random.randint(1, 7)
        dep = "dep0"+str(dep)
        programsData = ['prg' + (2-len(str(i)))*'0'+str(i), dep]
        programs.append(programsData)

    for i in range(projectsNum):
        if (i < 30):
            randomStart = radar.random_datetime(start='2021-06-06', stop='2024-05-10T23:59:59')
            newStart = str(randomStart.year + 1)+'-'+str(randomStart.month)+'-'+str(randomStart.day)
            newStop = str(randomStart.year + 4)+'-'+str(randomStart.month)+'-'+str(randomStart.day)+'T23:59:59'
            randomEnd = radar.random_datetime(newStart, newStop)
            evalDate = radar.random_datetime('2019-06-06', '2022-05-10T23:59:59').strftime('%Y-%m-%d')
        elif (i >= 30 and i < 40):
            randomStart = radar.random_datetime(start='2019-06-06', stop='2022-05-10T23:59:59')
            newStart = str(randomStart.year + 1)+'-'+str(randomStart.month)+'-'+str(randomStart.day)
            newStop = str(randomStart.year + 4)+'-'+str(randomStart.month)+'-'+str(randomStart.day)+'T23:59:59'
            randomEnd = radar.random_datetime(newStart, newStop)
            evalDate = (randomStart + relativedelta(months = -1)).strftime('%Y-%m-%d')
        else:
            randomStart = radar.random_datetime(start='2022-07-10', stop='2025-07-04T23:59:59')
            newStart = str(randomStart.year + 1)+'-'+str(randomStart.month)+'-'+str(randomStart.day)
            newStop = str(randomStart.year + 4)+'-'+str(randomStart.month)+'-'+str(randomStart.day)+'T23:59:59'
            randomEnd = radar.random_datetime(newStart, newStop)
            evalDate = radar.random_datetime('2019-06-06', '2022-05-10T23:59:59').strftime('%Y-%m-%d')  #randomStart + relativedelta(months = -1).strftime('%Y-%m-%d')
        monthsDuration = randomEnd.month - randomStart.month
        yearsDuration = randomEnd.year - randomStart.year
        if (monthsDuration == 12):
            monthsDuration = 0
            yearsDuration += 1

        yearsDuration += monthsDuration/12
        randomAmount = random.randint(100, 1000)*1000   # Thousants of $
        while (True):
            codeRes = str(random.randint(0, researchersNum - 1))
            initCodeRes = int(codeRes)
            codeEv = str(random.randint(0, researchersNum - 1))
            randomResearcher = 'r' + (4-len(codeRes))*'0'+codeRes
            randomEvaluator = 'r' + (4-len(codeEv))*'0'+codeEv
            if (randomResearcher != randomEvaluator):
                break
        
        codeEx = str(random.randint(0, executivesNum - 1))
        randomExecutive = 'e' + (4-len(codeEx))*'0'+codeEx
        prgNum = random.randint(0, 29)
        projectData = ['prj' + (2-len(str(i)))*'0'+str(i), titles[i], lorems[i],
                randomStart.strftime('%Y-%m-%d'), randomEnd.strftime('%Y-%m-%d'),
                round(yearsDuration, 1), randomAmount, researchers[initCodeRes][-2],
                'prg' + (2-len(str(prgNum)))*'0'+str(prgNum),
                randomExecutive, randomResearcher, randomEvaluator, random.randint(5, 10),
                evalDate]
        projects.append(projectData)

    for i in range(reportsNum):
        reportData = [projects[(i+random.randint(0, 49))%35][0],
                        projects[(i+random.randint(0, 49))%35][1],
                        projects[(i+random.randint(0, 49))%35][2]]
        reports.append(reportData)

    for project in projects:
        print(project[0], ": OK :D", sep = '')

        randResNum = random.randint(2, 5)
        works_at.append(['r' + (4-len(str(researchersNum - 1)))*'0'+
                            str(project[-4][-len(str(researchersNum - 1)):]), project[0]])
        # print(project[-4])
        works_atNum += 1
        codes = []
        
        for j in range(randResNum):
            patates = 0
            start = time.time()
            while (True):       # While loop
                codeRes = str(random.randint(0, researchersNum - 1))
                codes.append(codeRes)
                randomResearcher = 'r' + (4-len(codeRes))*'0' + codeRes
                # print("projectAcronym:", project[-7], "\tresAcronym:", researchers[int(project[0][-2:])][-2])
                end = time.time()
                if (end - start > 0.3):
                    patates = 1
                    break
                if ((randomResearcher != project[-3]) and (randomResearcher != project[-4])
                     and (project[-7] == researchers[int(codeRes)][-2]) and
                     [randomResearcher, project[0]] not in works_at):
                    print(codes)
                    break
            if (patates):
                print("patates1")
                continue
            print("patates2")
            print("========")
            works_atData = [randomResearcher, project[0]]
            works_at.append(works_atData)
            works_atNum += 1


    print("DONE!! :D")

    # Write researchers
    with open(str(researchersNum)+'researchers.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["researcher_ID", "first_name", "last_name", "sex", "birth_date", "org_acronym", "start_date"])
        for data in researchers:
            writer.writerow(data)
    f.close()

    # Write executives
    with open(str(executivesNum)+'executives.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["exec_ID", "first_name", "last_name"])
        for data in executives:
            writer.writerow(data)
    f.close()

    # Write about
    with open(str(len(about))+'about.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["project_ID", "sector"])
        for data in about:
            writer.writerow(data)
    f.close()

    # Write organizations
    with open(str(organizationsNum)+'organizations.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["org_acronym", "category", "name", "street", "street_number",
                         "postal_code", "city", "equity", "funds_from_ministry",
                         "funds_from_actions"])
        for data in organizations:
            writer.writerow(data)
    f.close()

    # Write programs
    with open(str(programsNum)+'programs.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["program_ID", "department"])
        for data in programs:
            writer.writerow(data)
    f.close()

    # Write projects
    with open(str(projectsNum)+'projects.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["project_ID", "title", "abstract", "start_date", "end_date", "duration", "amount", "org_acronym",
                         "program_ID", "exec_ID", "supervisor_ID", "evaluator_ID", "eval_mark", "eval_date"])
        for data in projects:
            writer.writerow(data)
    f.close()

    # Write reports
    with open(str(reportsNum)+'reports.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["project_ID", "title", "summary"])
        for data in reports:
            writer.writerow(data)
    f.close()

    # Write phones
    with open(str(phonesNum)+'phones.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["org_acronym", "phone_number"])
        for i in range(organizationsNum):
            writer.writerow([orgList[i], phones[i][0][-10:-1]])
            writer.writerow([orgList[i], phones[i][1][-10:-1]])
    f.close()

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if f.endswith("works_at.csv"):
            os.remove(f)
    
    # Write works_at
    with open(str(works_atNum)+'works_at.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["researcher_ID", "project_ID"])
        for data in works_at:
            writer.writerow(data)

    return

main()
