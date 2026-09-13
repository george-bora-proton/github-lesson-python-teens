from read_file_contents import read_files
from save_story import save_story

def main():
    story_text = read_files()
    save_story(story_text)

if __name__ == "__main__":
    main()