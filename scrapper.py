from Model import Chapter
import requests
import json
from bs4 import BeautifulSoup

data = {}
data["chapters"] = {}
data["verses"] = {}


"""
make a request to each chapter
get all the relevant details of the chapter in a list
store list in the data
go through the list
make a request to each verse
get all the details of the verse
store the verses for the chapter in a list

"""

hindi_numbers = ["०", "१", "२", "३", "४", "५", "६", "७", "८", "९", "१०", "११", "१२", "१३", "१४", "१५", "१६", "१७", "१८", "१९", "२०", "२१", "२२", "२३", "२४", "२५", "२६", "२७", "२८", "२९", "३०", "३१", "३२", "३३", "३४", "३५", "३६", "३७", "३८", "३९", "४०", "४१", "४२", "४३", "४४", "४५", "४६", "४७", "४८",
                 "४९", "५०", "५१", "५२", "५३", "५४", "५५", "५६", "५७", "५८", "५९", "६०", "६१", "६२", "६३", "६४", "६५", "६६", "६७", "६८", "६९", "७०", "७१", "७२", "७३", "७४", "७५", "७६", "७७", "७८", "७९", "८०", "८१", "८२", "८३", "८४", "८५", "८६", "८७", "८८", "८९", "९०", "९१", "९२", "९३", "९४", "९५", "९६", "९७", "९८", "९९", "१००"]

chapter_hindi = "अध्याय"
verse_hindi = "श्लोक"

chapters = data["chapters"]


# Getting details of the chapters
for chapter_number in range(1, 19):
    print("Getting chapter:", chapter_number)

    page = requests.get("https://bhagavadgita.io/chapter/" +
                        str(chapter_number)+"/hi/")
    soup = BeautifulSoup(page.content, "html.parser")

    chapter = Chapter()
    chapter.chapter_number = hindi_numbers[1]
    chapter.chapter_summary = soup.find("p").text
    chapter.name = soup.find("b").text.split(" ")[-1:]
    chapter.name_meaning = soup.find("h3").text
    chapters[chapter_number] = vars(chapter)


# data = []
# mydivs = soup.find_all("h2", {"class": "card-header-title chapter-name"})
# for i in mydivs:
#     obj = {}
#     obj["name"] = i.text
#     data.append(obj)


file1 = open("MyFile2.json", "w", encoding="utf-8")
json.dump(data, file1, ensure_ascii=False)
