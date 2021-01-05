import json

rawFile = open("lds-scriptures-json.txt", "r")

outFile = open("wog.tsv","a+")

jsonObj = json.load(rawFile)

abbrevs = {
    "1 Nephi":"1Ne",
    "2 Nephi":"2Ne",
    "Jacob":"jac",
    "Enos":"Eno",
    "Jarom":"jar",
    "Omni":"omn",
    "Words of Mormon":"wom",
    "Mosiah":"mosi",
    "Alma":"alm",
    "Helaman":"hel",
    "3 Nephi":"3Ne",
    "4 Nephi":"4Ne",
    "Mormon":"morm",
    "Ether":"Eth",
    "Moroni":"Moro"

}

book = 100
prevBook = ""

for i in jsonObj:
    if i['volume_title']=='Book of Mormon':
        if(prevBook!=i['book_title']):
            prevBook=i['book_title']
            book+=1

        # print(i["book_title"],"\t",abbrevs[i['book_title']],"\t",book,"\t",i['chapter_number'],'\t',i['verse_number'],'\t',i['scripture_text'])
        line =  "%s \t %s \t %d \t %d \t %d \t %s\n" % (i["book_title"],abbrevs[i['book_title']],book,i['chapter_number'],i['verse_number'],i['scripture_text'])
        # print(line,end="")
        outFile.write(line)
        