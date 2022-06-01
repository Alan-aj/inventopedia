import requests
import re

from dbconnector import *
for qn in range(1,15):
    res=requests.get("https://www.examveda.com/general-knowledge/practice-mcq-question-on-inventions/?page="+str(qn)).text
    res=res.split('<article class="question single-question question-type-normal">')

    print(len(res))

    for i in range(1,len(res)):
        if '<div class="row">' in res[i]:
            try:
            # print(res[i])
                qstn=res[i].split('<div class="question-main">')[1].split('</div>')[0]
                print(qstn)
                solutions=[]
                ress=res[i].split('<p>')

                for ii in range(1,5):
                    resss=ress[ii].split('</label>')
                    s2 = re.sub(r'<.*?>', '', resss[1])
                    s2=s2.replace("											","")
                    s2 = re.sub(r'\n.*?\n', '', s2)
                    s2=s2.replace("\n                       \n","")
                    solutions.append(s2)

                resss=res[i].split('<div><span class="color">Answer:</span><strong> Option ')[1].split('</strong>')[0]
                ans=solutions[0]
                if resss == 'B':
                    ans = solutions[1]
                if resss == 'C':
                    ans = solutions[2]
                if resss == 'D':
                    ans = solutions[3]
                solutions.append(ans)


                resss=res[i].split('<div><span class="color">Solution: </span></div>')[1].split('</div>')[0]

                resss = re.sub(r'\n.*?\t\t', '', resss)
                resss = re.sub(r'  .*?\n\n.*?  ', '', resss)

                solutions.append(resss)
                qry="INSERT INTO `quiz` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)"
                val=(qstn,solutions[0],solutions[1],solutions[2],solutions[3],solutions[4],solutions[5])
                iud(qry,val)
                print(solutions)

            except:
                pass
        print("+==============================================================================")