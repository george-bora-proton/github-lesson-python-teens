OUTPUT_FILE = 'story_final.txt'

def save_story(story):
    with open(OUTPUT_FILE, 'w') as file:
        file.write(story)