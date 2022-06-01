import requests
import re


from dbconnector import *

qry="SELECT * FROM `information` where Info_id > 972"

# where Info_id > 0 and Info_id < 51
result=select(qry)
ii=0
for i in result:
    ii=ii+1

    qry="https://www.google.com/search?q="+i[2]+"+images"



    res=requests.get(qry).text

    ress=res.split('class="BVG0Nb"')

    imgurl=ress[1].split('imgurl=')[1].split('&')[0]
    qry="UPDATE `information` SET `Image`=%s WHERE `Info_id`=%s"
    val=(imgurl,str(i[0]))
    iud(qry,val)
    print(ii,i[0],imgurl)



# print(res)

# ress=res.split('class="idg8be"')
#
# print(ress[1])
# data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAH8AaQMBIgACEQEDEQH/xAAcAAEAAgIDAQAAAAAAAAAAAAAABQYECAEDBwL/xAA7EAABAwIDAwgIBAcBAAAAAAABAAIDBBEFBiESMdEXIkFRVGFxlBMUMkKBkaHBYnKx8BYjM1JzgrIV/8QAGQEBAAMBAQAAAAAAAAAAAAAAAAEDBAIF/8QAIREBAAEEAgIDAQAAAAAAAAAAAAECAxESFDEEIRNBUlH/2gAMAwEAAhEDEQA/APcUREBERAREQEREBERAREQEREBERBBYtJ6SeVjpXNEWzstabXvquunxSdjA10jX23FwUbmKuEGLVEZOtmnd+FRDMWYD7WvivHu35puTiXpW7EVUR6XIV08m6SNo6xZfJkkd7dcB4FVZuLM/dyuwYsO/5LnlTPZx8dLIWDprX/MrkbbBzK06dZVa/wDVG/nfQLg4m3eQD+ZyfPB8ErT6zUs19Ox3iAuuTE6ho9zxAv8AdVp2LtG5zPBdL8VZ/cflZOVV9SmPGj7hPsmkklkqHVLttjSR0fRWSI7UbXdYBXnTMUa1klhpY6r0OlN6aI/gH6LX4VzeZZ/Ko1w7URFvZBERBV8zZUdjFYyqpqv0Dy0Nka5pc1wG42BGv70WTRZTwqmgaySD077c58hOvwGgU+ip49raase1vzXNYpz6QM2UcFl3Uzoz1xyuH0vZR8uQ6HX0FXUs/PZ3BW5FFXjWau6YIv3Y6qeT43g+JYXigpKWldVwehdJ6cRO1cLWbv8AFWKjyLHJDHJVVszXOaHOYxgBaT0XJKy85tBxHBbgH+a8a/6n7K1riPEs/l3ybv8AVbgyXhEf9T1mb/JMR/zZZRyvgxZs+otA6w91/wBVNIrYsWo6phXN65PdUqTUZCY+uDoa1zKNx58RbzrdIB+/6q6MaGtDQLAaABfSJbs0W86x2V3a7mNp6ERFarEREBERAREQVXNd6nGMIp4BtSRyl77e6CQBfx1+RVqVNJqsuV1RVV1MJ6eSVzhWsNy0OOgeDuto3aBOnRvvbaWdlTAyaI3Y8XCgdqIikEREBERAREQEREBERBU8y4pU19PJhWD0raiWra+Jz3+w1u5xPdv+qm8v4e7CsGoqB8plfTwtY6Q+8QLXUFmTA2UFHW4rhtdNRyRtdO6F0l4HuGp5rrhrifeAvc9KnMuVr8QwSiq5AdqaJr+cLGxF9e9QJJERSCIiAiIgIiICIiAhRcFBRschndM85hp5nUMc22JAbwub0B1rltu8W6bi+lzoXwyUkT6cWiLRsjqHUq1j2KVGL4fNh2DUwlNUJad8smjWAc13x13dWqnsDoThmEUdC6QyGCFsZed7rC11AzkRFIIiICIiAiIgIiICIiCvZhwyip6WrxOEtpKmOMvdIH7DZLDQP6D1Am9lL4XM6ow6mmftbUkbXc4WOo6e9dVVhVLW1LZqxnphGQY43nmtPXbrWcBYWCDlERAREQEREFB5YMmdvqPJy8E5YMmdvqPJy8Frzh9bDTNe2ooYqra9nbNtnr6Ndw8Neu4yosWpY5IntwmAuje1wJc3Wzr2tsfD49dlZojL3zlgyZ2+o8nLwTlhyZ2+o8nLwXh38QYZ6wJv4api4WFjPoRa2vM6R07+oi5vATyGWVz7WBOgsNB0DQDo7gmhlshyw5M7fUeTl4Jyw5M7fUeTl4LWxE0gy2T5YcmdvqPJy8E5YcmdvqPJy8FrYiaQZbJ8sGTO31Hk5eCcsGTO31Hk5eC1sWd6zQXF8MdtDfarcAT4bP3TQy2F5YMmdvqPJy8E5YMmduqPJy8Fr0+pw9x5uGPaNq5ArDutu9nvHyX0yrw5uhwgvHfWO4JoZbB8sGTO3VHk5eCcsOTO31Hk5eC14qKmjkhcyHDhBIbbMnrDnW69LWN1hpoZf//Z


# print(len(ress))
