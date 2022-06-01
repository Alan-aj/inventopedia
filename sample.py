import re
import requests
# def searchfn(key):
#     res1=requests.get("https://en.wikipedia.org/wiki/"+key).text
#     res=res1.split('<div id="toc"')[0]
#     res=res.split('</table>')
#     print (len(res))
#
#     res=res[len(res)-1].split("<p>")
#
#     txt=""
#
#     for i in res:
#
#         htmlString=i.replace("</p>","")
#         s2 = re.sub(r'<.*?>', '', htmlString)
#         s2=re.sub(r'&#91;.*?#93;', '', s2)
#         print(s2)
#         txt=txt+s2+". "
#
#
#
#     res=res1.split('class="image"')[0].split("<a href=")
#     res=res[len(res)-1].split('"')
#
#     print (res[1],"============")
#
#     res2=requests.get("https://en.wikipedia.org"+res[1]).text
#
#     res=res2.split('<img')[2].split('src="')[1].split('"')[0]
#
#
#     print(res)
#     return res,txt


def searchfn(key):
    res1=requests.get("https://en.wikipedia.org/wiki/"+key).text
    res=res1.split('<div id="toc"')[0]


    res=res.split("<p>")

    txt=""
    print()
    for i in range(1,len(res)):

        htmlString=res[i].split("</p>")[0]
        s2 = re.sub(r'<.*?>', '', htmlString)
        s2=re.sub(r'&#91;.*?#93;', '', s2)

        txt=txt+s2+" "
    print(txt)


    res=res1.split('class="image"')[0].split("<a href=")
    res=res[len(res)-1].split('"')

    print (res[1],"============")

    res2=requests.get("https://en.wikipedia.org"+res[1]).text

    res=res2.split('<img')[2].split('src="')[1].split('"')[0]


    print(res)
    return res,txt