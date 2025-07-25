# a program which prints the longest communication unit each interviewee said
import os

# enter the path to the folder with your data here:
path = r"ENTER YOUR PATH HERE"

def number_of_words(text):
    return len(text.strip().split())

with open('results.txt', 'w', encoding='utf-8') as results:
    for filename in os.listdir(path):
        if filename.endswith(".cha"):
            file_path = os.path.join(path, filename)
            with open(file_path, 'r', encoding='utf-8') as text:
                comm_units = []
                longest = ""
                max_words = 0
                for line in text:
                    # feel free to replace *CHI: with any tag you need for your own research
                    if line.startswith("*CHI:"):
                        unit = line[5:].strip()
                        comm_units.append(unit)
                        num_words = number_of_words(unit)
                        if num_words > max_words:
                            max_words = num_words
                            longest = unit
                results.write(f"{filename}, {longest}\n")
