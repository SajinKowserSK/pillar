import requests
API_KEY = "810cac55-0ba9-4ecc-bf32-fb25d6f342dc"

def summarize(text):
    r = requests.post("https://api.deepai.org/api/summarization",data={'text': text},
        headers={'api-key': API_KEY}

    ).json()

    return r['output']


if __name__ == "__main__":
    print(summarize("Mrs. Smith also notes that for the past "
                    "two to three weeks, she has been having "
                    "intermittent pounding bifrontal headaches "
                    "that worsen with straining, such as when "
                    "coughing or having a bowel movement. "
                    "The headaches are not positional "
                    "and are not worse at any particular "
                    "time of day. She rates the pain as 7 or 8 on a scale of 1 to 10, "
                    "with 10 being the worst possible headache. "
                    "The pain lessened somewhat when she took Vicodin "
                    "that she had lying around. She denies associated nausea, "
                    "vomiting, photophobia, loss of vision, seeing flashing "
                    "lights or zigzag lines, numbness, weakness, "
                    "language difficulties, and gait abnormalities. "
                    "Her recent headaches differ from her “typical migraines,” "
                    "which have occurred about 4-6 times per year since she was a"
                    " teenager and consist of seeing shimmering white stars move "
                    "horizontally across her vision for a couple minutes followed "
                    "by a pounding headache behind one or the other eye, "
                    "photophobia, phonophobia, and nausea and "
                    "vomiting lasting several hours to two days. "
                    "She has never taken anything for these headaches "
                    "other than ibuprofen or Vicodin, both of which are "
                    "partially effective. The last headache of that type was two months ago."))