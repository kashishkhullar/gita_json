# Srimad Bhagwad Gita in JSON
This project aims to provide entire bhagwad gita in json format in hindi.

## JSON Schema
```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "chapter_hindi": {
      "type": "string"
    },
    "verse_hindi": {
      "type": "string"
    },
    "verse_meaning_hindi": {
      "type": "string"
    },
    "word_meaning_hindi": {
      "type": "string"
    },
    "chapters": {
      "type": "object",
      "properties": {
        "chapter_number": {
          "type": "object",
          "properties": {
            "chapter_number": {
              "type": "string"
            },
            "chapter_summary": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "name_meaning": {
              "type": "string"
            },
            "verses_count": {
              "type": "integer"
            },
            "verse_numbers": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                }
              ]
            }
          }
        },
        "verses": {
          "type": "object",
          "properties": {
            "chapter_number": {
              "type": "object",
              "properties": {
                "verse_number": {
                  "type": "object",
                  "properties": {
                    "meaning": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "verse_number": {
                      "type": "string"
                    },
                    "word_meanings": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

## Dataset
Refer to file `dataset.json` in the root folder of the project.

## Source
Entire data has been scrapped from <a>https://bhagavadgita.io/</a> using python packages <a href="https://pypi.org/project/beautifulsoup4/">BeautifulSoup</a> and <a href="https://pypi.org/project/requests/">Requests</a>

## Run

Required: Python 3 and pip

1. Install required packages
    ```cmd
    pip install requests beautifulsoup4
    ```

1. Add name of the output file in `scrapper.py` By default its `dataset.json`
   ```python
   data_file = open("_file_name_.json", "w", encoding="utf-8")
   ```
2. run the python file `scrapper.py`

    ```
    python scrapper.py
    ```
3. A json file with the name you saved will be created in the root directory of the project folder


