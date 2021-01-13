from Model import Chapter, Verse
import requests
import json
from bs4 import BeautifulSoup

data = {}
data["chapters"] = {}
data["verses"] = {}


"""
make a request to each chapter
get all the details of the chapter in an object
add chapter to corresponding number in the data object
make a request to each verse
get all the details of the verse
store the verses for the chapter number and corresponding verse number in the data object

"""

hindi_numbers = ["०", "१", "२", "३", "४", "५", "६", "७", "८", "९", "१०", "११", "१२", "१३", "१४", "१५", "१६", "१७", "१८", "१९", "२०", "२१", "२२", "२३", "२४", "२५", "२६", "२७", "२८", "२९", "३०", "३१", "३२", "३३", "३४", "३५", "३६", "३७", "३८", "३९", "४०", "४१", "४२", "४३", "४४", "४५", "४६", "४७", "४८",
                 "४९", "५०", "५१", "५२", "५३", "५४", "५५", "५६", "५७", "५८", "५९", "६०", "६१", "६२", "६३", "६४", "६५", "६६", "६७", "६८", "६९", "७०", "७१", "७२", "७३", "७४", "७५", "७६", "७७", "७८", "७९", "८०", "८१", "८२", "८३", "८४", "८५", "८६", "८७", "८८", "८९", "९०", "९१", "९२", "९३", "९४", "९५", "९६", "९७", "९८", "९९", "१००"]

chapter_hindi = "अध्याय"
verse_hindi = "श्लोक"
verse_meaning_hindi = "अनुवाद"
word_meaning_hindi = "शब्दार्थ"

chapters = data["chapters"]
verses = data["verses"]

# Use "/hi/" at the of the URLs for Hindi


def convertNumberToHindi(num):
    hindi = ""
    num = num.split("-")
    hindi_list = map(lambda number: hindi_numbers[int(number)], num)
    return "-".join(hindi_list)


# Getting details of the chapters
for chapter_number in range(1, 19):
    print("Getting chapter:", chapter_number)

    page = requests.get("https://bhagavadgita.io/chapter/" +
                        str(chapter_number))
    soup = BeautifulSoup(page.content, "html.parser")

    chapter = Chapter()
    # chapter.chapter_number = hindi_numbers[chapter_number] # uncomment for hindi
    chapter.chapter_number = chapter_number  # comment for hindi
    chapter.chapter_summary = soup.find("p").text
    chapter.name = strip(soup.find("b").text.split("-")[-1])
    chapter.name_meaning = soup.find("h3").text
    chapter.verse_numbers = []

    no_of_verses = 0
    verses[chapter_number] = {}

    # Getting all verse numbers ( some have two combined )

    page_no = 1
    has_more_pages = True

    while has_more_pages:
        url = "https://bhagavadgita.io/chapter/" + \
            str(chapter_number) + "?page=" + str(page_no)

        page = requests.get(url)

        if(page.status_code == 200):
            print("Getting verse numbers from page", page_no)
            soup = BeautifulSoup(page.content, "html.parser")
            verse_number_element = soup.find_all(
                "h4", {"class": "font-up font-bold white-text mt-2 mb-3"})
            for element in verse_number_element:
                verse_number = element.text.split(" ")[-1]
                chapter.verse_numbers.append(verse_number)
                no_of_verses += 1
                verses[chapter_number][verse_number] = {}
            page_no += 1
        else:
            has_more_pages = False
            chapter.verses_count = no_of_verses

    # Get all verses for the chapters
    has_more_verses = True

    for verse_number in chapter.verse_numbers:
        url = "https://bhagavadgita.io/chapter/" + \
            str(chapter_number) + "/verse/" + str(verse_number)

        page = requests.get(url)

        if(page.status_code == 200):
            print("Getting verse:", verse_number)

            soup = BeautifulSoup(page.content, "html.parser")

            verse = Verse()
            verse.text = soup.find("p", {"class": "verse-sanskrit"}).text
            verse.meaning = soup.find("p", {"class": "verse-meaning"}).text
            verse.word_meanings = soup.find(
                "p", {"class": "verse-word"}).text
            # verse.verse_number = convertNumberToHindi(verse_number) # uncomment for hindi
            verse.verse_number = verse_number                         # comment for hindi
            verses[chapter_number][verse_number] = vars(verse)

        else:
            print("No more verses for chapter", chapter_number)
            has_more_verses = False
            chapter.verses_count = no_of_verses

    # converting to dict before adding to data to serialize it
    chapters[chapter_number] = vars(chapter)


# data = []
# mydivs = soup.find_all("h2", {"class": "card-header-title chapter-name"})
# for i in mydivs:
#     obj = {}
#     obj["name"] = i.text
#     data.append(obj)

# Writing the data to json file
data_file = open("dataset_english.json", "w", encoding="utf-8")
json.dump(data, data_file, ensure_ascii=False)
