def main():
    path_to_file = 'books/frankenstein.txt'
    with open('books/frankenstein.txt') as f:
        file_contents = ""
        wc = 0
        file_contents = f.read()
        wc = file_contents.split()
        # print(file_contents)
        # print(len(wc))
    char_freq = count_characters(file_contents)
    # for char, freq in char_freq.items():
        # print(f"{char}: {freq}")
    print_report(wc, char_freq, path_to_file) 
    return file_contents, wc

def count_characters(file_contents):
    lowered_string = file_contents.lower()
    character_count = {}
    for char in lowered_string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    print(character_count)
    return character_count

def print_report(wc, char_freq, path_to_file): 
	print(f"--- Begin report of {path_to_file} ---") 
	# print(f"{wc} words found in the document\n") 
	
	sorted_chars = sorted(char_freq.items(), key=lambda item: item[1], reverse=True) 
	
	for char, freq in sorted_chars: 
		print(f"The '{char}' character was found {freq} times") 
		
	print("--- End report ---") 

if __name__ == "__main__":
    main()