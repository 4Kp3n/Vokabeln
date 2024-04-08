import os
import shutil
import re

REPO_PATH = "./Dateien"  
# Pfad anpassen!
OBSIDIAN_PATH = "C:/Users/User/Kioku/Anki" # Change this to the path of your folder

# summary: Takes a path to a .md file and parses all contained vocabulary cards (Anki format required!)
# filepath: Path to the .md file to parse
# return: A nested list with all contained vocabulary cards in the following format:
# [['Type', 'Vorderseite', 'Rueckseite', '[Tags]', '[ID]'], ...]
def parse_md_file(filepath):
    # Elements will be captured in the following format (Tags and ID might be empty):
    # ['Type', 'Vorderseite', 'Rueckseite', 'Tags', 'ID']
    elements = [ ] 

    # Regular expression pattern to match everything between 'START' and 'END', across multiple lines
    # (Get the unsorted card content first to break down later)
    card_pattern = re.compile(r"START\n(.*?)END", re.DOTALL)
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    # Contains a list of all raw strings between START and END
    list_of_card_strings = card_pattern.findall(text)

    # Loop through list and get Type, Vorderseite, Rueckseite, Tags and ID 
    for card_string in list_of_card_strings:
        # Regex patterns to find the correct strings
        front_pattern = re.compile(r"(Vorderseite:.*?)\nR.ckseite", re.DOTALL)
        back_pattern = re.compile(r"(R.ckseite:.*?)(?:\nTags:|\nEND|\n<!--ID|$)", re.DOTALL) 
        tags_pattern = re.compile(r"(Tags:.*)")
        id_pattern = re.compile(r"<!--ID:.*")
        # Card type is ALWAYS the first line
        card_type = card_string.split('\n', 1)[0]
        # Search for the regex patterns in card_string
        try:
            card_front = front_pattern.search(card_string).group(1)+'\n'
            card_back = back_pattern.search(card_string).group(1)+'\n'
        except:
            print("Following card does not fulfill format requirements: {}".format(card_string))
            continue
        card_tags = tags_pattern.search(card_string)
        card_id = id_pattern.search(card_string)

        # Add everything to the elements list that will be returned
        tmp = [card_type, card_front, card_back]

        # (card_tags might be empty)
        if card_tags: 
            card_tags = card_tags.group(1) + '\n'
            tmp.append(card_tags)

        # (card_id might be empty)
        if card_id:
            tmp.append(card_id)

        elements.append(tmp)

    return elements


# summary: Get all .md files in a given folder path
# path: The path to the folder to check for .md files
# return: A list with filenames of all .md files in folder
def get_all_md_files_in_folder(path):
    ret = []
    for filename in os.listdir(path):
        if (filename.endswith(".md") and filename != "README.md"):
            ret.append(filename)
    return ret

# Get all .md files in both folders
def main():
    repo_md_filenames = get_all_md_files_in_folder(REPO_PATH)
    obsidian_md_filenames = get_all_md_files_in_folder(OBSIDIAN_PATH)

    # For every .md file in the repository check if a file with the same name is already contained in the Obsidian folder
    for md_file in repo_md_filenames:
        print("Current file: ", md_file)
        # Not contained -> just copy file
        if md_file not in obsidian_md_filenames:
            print("Copy {} to {}".format(md_file, OBSIDIAN_PATH))
            shutil.copy(os.path.join(REPO_PATH, md_file), os.path.join(OBSIDIAN_PATH, md_file))
        # File already exists -> compare each entry for missing ones
        else:
            repo_fp = os.path.join(REPO_PATH, md_file)
            obsidian_fp = os.path.join(OBSIDIAN_PATH, md_file)
            repo_cards = parse_md_file(repo_fp)
            obsidian_cards = parse_md_file(obsidian_fp)

            for rcard in repo_cards:
                found = False

                for ocard in obsidian_cards:
                    # Front and back are the same - do nothing 
                    if (rcard[1] == ocard[1]) and (rcard[2] == ocard[2]):
                        # TODO check for changes to Tag parameter
                        found = True
                        break

                    # Only front is equal - update the back
                    # 1. Find index of first line of front
                    # 2. Calculate start and end ob back based on index
                    # 3. Exchange section and write to file
                    if (rcard[1] == ocard[1]):
                        print("The back is different - overwrite it")
                        # Read in the file
                        with open(obsidian_fp, 'r', encoding='utf-8') as fp:
                            data = fp.readlines()

                        # Find the front to know where the back starts
                        front_lines = ocard[1].strip().split('\n')
                        back_lines = ocard[2].strip().split('\n')
                        for index, line in enumerate(data):
                            line = line.strip()
                            if (line == front_lines[0].strip()):
                                data[index+len(front_lines):index+len(front_lines)+len(back_lines)] = [rcard[2]]
                        with open(obsidian_fp, 'w', encoding='utf-8') as fp:
                            fp.write(''.join(data))
                        found = True
                        break

                    # Only back is equal - update the front
                    if (rcard[2] == ocard[2]):
                        print("The front is different - overwrite it")
                        # Read in the file
                        with open(obsidian_fp, 'r', encoding='utf-8') as fp:
                            data = fp.readlines()
                        front_lines = ocard[1].strip().split('\n')
                        back_lines = ocard[2].strip().split('\n')
                        for index, line in enumerate(data):
                            line = line.strip()
                            if (line == back_lines[0].strip()):
                                data[index-len(front_lines):index] = [rcard[1]]
                        with open(obsidian_fp, 'w', encoding='utf-8') as fp:
                            fp.write(''.join(data))

                        found = True
                        break

                if not found:
                    print('New card "{}" will be added'.format(rcard[1]))
                    # TODO add new card to end of file

# Run main function
if __name__ == '__main__':
    main()