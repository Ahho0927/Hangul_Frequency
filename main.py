from hgtk.checker import has_batchim
from hgtk.letter import decompose
from re import sub as list_replace
from os import system
from tqdm import tqdm


with open('./data.txt','rt',encoding="utf-8") as f:
    text_data: str = f.read()

# setup
HANGUL_CHO_ALL: list[str] = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
HANGUL_JUNG_ALL: list[str] = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
HANGUL_JONG_ALL: list[str] = ['ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

# HANGUL_CHO_ASSEMBLED: list[str] = ['ㄲ','ㄸ','ㅃ','ㅆ','ㅉ']
# HANGUL_JUNG_ASSEMBLED: list[str] = ['ㅘ','ㅙ','ㅚ','ㅝ','ㅞ','ㅟ','ㅢ']
# HANGUL_JONG_ASSEMBLED: list[str] = ['ㄲ','ㄳ','ㄵ','ㄶ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅄ','ㅆ']

HANGUL_CHO_UNASSEMBLED: list[str] = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
HANGUL_JUNG_UNASSEMBLED: list[str] = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ']
HANGUL_JONG_UNASSEMBLED: list[str] = HANGUL_CHO_UNASSEMBLED

HANGUL_DISTRIBUTE_CHO: dict[str] = {'ㄲ':'ㄱㄱ','ㄸ':'ㄷㄷ','ㅃ':'ㅂㅂ','ㅆ':'ㅅㅅ','ㅉ':'ㅈㅈ'}
HANGUL_DISTRIBUTE_JUNG: dict[str] = {'ㅘ':'ㅏㅗ','ㅙ':'ㅐㅗ','ㅚ':'ㅗㅣ','ㅝ':'ㅓㅜ','ㅞ':'ㅔㅜ','ㅟ':'ㅜㅣ','ㅢ':'ㅡㅣ'}
HANGUL_DISTRIBUTE_JONG: dict[str] = {'ㄲ':'ㄱㄱ','ㄳ':'ㄱㅅ','ㄵ':'ㄴㅈ','ㄶ':'ㄴㅎ','ㄺ':'ㄹㄱ','ㄻ':'ㄹㅁ','ㄼ':'ㄹㅂ','ㄽ':'ㄹㅅ','ㄾ':'ㄹㅌ','ㄿ':'ㄹㅍ','ㅀ':'ㄹㅎ','ㅄ':'ㅂㅅ','ㅆ':'ㅅㅅ'}


HANGUL_CONSONANT_ALL: list[str] = ['ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄸ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅃ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
HANGUL_VOWEL_ALL: list[str] = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']

# HANGUL_CONSONANT_ASSEMBLED: list[str] = ['ㄲ','ㄳ','ㄵ','ㄶ','ㄸ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅃ','ㅄ','ㅆ','ㅉ']
# HANGUL_VOWEL_ASSEMBLED: list[str] = ['ㅘ','ㅙ','ㅚ','ㅝ','ㅞ','ㅟ','ㅢ']


HANGUL_CONSONANT_UNASSEMBLED: list[str] = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
HANGUL_VOWEL_UNASSEMBLED: list[str] = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ']

HANGUL_DISTRIBUTE_CONSONANT: dict[str] = {'ㄲ':'ㄱㄱ','ㄳ':'ㄱㅅ','ㄵ':'ㄴㅈ','ㄶ':'ㄴㅎ','ㄸ':'ㄷㄷ','ㄺ':'ㄹㄱ','ㄻ':'ㄹㅁ','ㄼ':'ㄹㅂ','ㄽ':'ㄹㅅ','ㄾ':'ㄹㅌ','ㄿ':'ㄹㅍ','ㅀ':'ㄹㅎ','ㅃ':'ㅂㅂ','ㅄ':'ㅂㅅ','ㅆ':'ㅅㅅ','ㅉ':'ㅈㅈ'}
HANGUL_DISTRIBUTE_VOWEL: dict[str] = {'ㅘ':'ㅏㅗ','ㅙ':'ㅐㅗ','ㅚ':'ㅗㅣ','ㅝ':'ㅓㅜ','ㅞ':'ㅔㅜ','ㅟ':'ㅜㅣ','ㅢ':'ㅡㅣ'}



count_hangul_cho: dict[str, int] = {letter: 0 for letter in HANGUL_CHO_ALL}
count_hangul_jung: dict[str, int] = {letter: 0 for letter in HANGUL_JUNG_ALL}
count_hangul_jong: dict[str, int] = {letter: 0 for letter in HANGUL_JONG_ALL}

# count_hangul_cho_assembled: dict[str, int] = {letter: 0 for letter in HANGUL_CHO_ASSEMBLED}
# count_hangul_jung_assembled: dict[str, int] = {letter: 0 for letter in HANGUL_JUNG_ASSEMBLED}
# count_hangul_jong_assembled: dict[str, int] = {letter: 0 for letter in HANGUL_JONG_ASSEMBLED}

count_hangul_cho_unassembled: dict[str, int] = {letter: 0 for letter in HANGUL_CHO_UNASSEMBLED}
count_hangul_jung_unassembled: dict[str, int] = {letter: 0 for letter in HANGUL_JUNG_UNASSEMBLED}
count_hangul_jong_unassembled: dict[str, int] = {letter: 0 for letter in HANGUL_JONG_UNASSEMBLED}


count_hangul_consonant: dict[str, int] = {letter: 0 for letter in HANGUL_CONSONANT_ALL}
count_hangul_vowel: dict[str, int] = {letter: 0 for letter in HANGUL_VOWEL_ALL}

# count_hangul_consonant_assembled: dict[str, int] = {letter: 0 for letter in HANGUL_CONSONANT_ASSEMBLED}
# count_hangul_vowel_assembled: dict[str, int] = {letter: 0 for letter in HANGUL_VOWEL_ASSEMBLED}

count_hangul_consonant_unassembled: dict[str, int] = {letter: 0 for letter in HANGUL_CONSONANT_UNASSEMBLED}
count_hangul_vowel_unassembled: dict[str, int] = {letter: 0 for letter in HANGUL_VOWEL_UNASSEMBLED}


count_hangul_with_batchim: int = 0
count_hangul_chojong_reversed: int = 0


# count
print("Loading . . .")
text_data = list_replace('[^각-힣]', '', text_data) # Non-Hangul Filtered
for letter in tqdm(text_data):
    cho, jung, jong = decompose(letter)
    
    count_hangul_cho[cho] += 1
    count_hangul_jung[jung] += 1
    if jong != '':
        count_hangul_jong[jong] += 1
    
    for l in HANGUL_DISTRIBUTE_CHO.get(cho, cho):
        count_hangul_cho_unassembled[l] += 1
    for l in HANGUL_DISTRIBUTE_JUNG.get(jung, jung):
        count_hangul_jung_unassembled[l] += 1
    for l in HANGUL_DISTRIBUTE_JONG.get(jong, jong):
        count_hangul_jong_unassembled[l] += 1
    
    count_hangul_consonant[cho] += 1
    count_hangul_vowel[jung] += 1
    if jong != '':
        count_hangul_consonant[jong] += 1
    
    for l in HANGUL_DISTRIBUTE_CONSONANT.get(cho, cho):
        count_hangul_consonant_unassembled[l] += 1
    for l in HANGUL_DISTRIBUTE_VOWEL.get(jung, jung):
        count_hangul_vowel_unassembled[l] += 1
    for l in HANGUL_DISTRIBUTE_CONSONANT.get(jong, jong):
        count_hangul_consonant_unassembled[l] += 1

    if has_batchim(letter):
        count_hangul_with_batchim += 1
        cho_jong = cho+jong
        if cho_jong != ''.join(sorted(cho_jong)):
            count_hangul_chojong_reversed += 1
    

# display output
system('cls')

 # int -> str(fixed width)
for dict in [count_hangul_cho, count_hangul_jung]:
    for key, value in dict.items():
        space_length_max = 20
        space_length = space_length_max - len(str(value))
        dict[key] = str(value) + ' ' * space_length
for dict in [count_hangul_cho_unassembled, count_hangul_jung_unassembled]:
    for key, value in dict.items():
        space_length_max = 20
        space_length = space_length_max - len(str(value))
        dict[key] = str(value) + ' ' * space_length

for key, value in count_hangul_consonant.items():
    space_length_max = 20
    space_length = space_length_max - len(str(value))
    count_hangul_consonant[key] = str(value) + ' ' * space_length
for key, value in count_hangul_consonant_unassembled.items():
    space_length_max = 20
    space_length = space_length_max - len(str(value))
    count_hangul_consonant_unassembled[key] = str(value) + ' ' * space_length

 # print

with open('./result.txt','wt',encoding="utf-8") as f:
    f.write("# CHO, JUNG, JONG")
    f.write("\n\n## ALL\n")
    for i, key in enumerate(HANGUL_JONG_ALL):
        if i < len(HANGUL_CHO_ALL):
            f.write(HANGUL_CHO_ALL[i]+ ' | ' + count_hangul_cho[HANGUL_CHO_ALL[i]])
        else:
            f.write('㊀ | '+" "*20)
        if i < len(HANGUL_JUNG_ALL):
            f.write(HANGUL_JUNG_ALL[i] + ' | ' + count_hangul_jung[HANGUL_JUNG_ALL[i]])
        else:
            f.write('㊀ | '+" "*20)
        f.write(key + ' | ' + str(count_hangul_jong[key]) + "\n")

    f.write("\n## UNASSEMBLED\n")
    for i, key in enumerate(HANGUL_JONG_UNASSEMBLED):
        f.write(HANGUL_CHO_UNASSEMBLED[i] + ' | ' + count_hangul_cho_unassembled[HANGUL_CHO_UNASSEMBLED[i]]+ HANGUL_JUNG_UNASSEMBLED[i] + ' | ' + count_hangul_jung_unassembled[HANGUL_JUNG_UNASSEMBLED[i]] + key + ' | ' + str(count_hangul_jong_unassembled[key]) + "\n")


    f.write("\n\n\n# CONSONANT, VOWEL")
    f.write("\n\n## ALL\n")
    for i, key in enumerate(HANGUL_CONSONANT_ALL):
        f.write(key + ' | ' + count_hangul_consonant[key])
        if i < len(HANGUL_VOWEL_ALL):
            f.write(HANGUL_VOWEL_ALL[i] + ' | ' + str(count_hangul_vowel[HANGUL_VOWEL_ALL[i]]) + "\n")
        else: f.write("\n")

    f.write("\n## UNASSEMBLED\n")
    for i, key in enumerate(HANGUL_CONSONANT_UNASSEMBLED):
        f.write(key + ' | ' + count_hangul_consonant_unassembled[key] + HANGUL_VOWEL_UNASSEMBLED[i] + ' | ' + str(count_hangul_vowel_unassembled[HANGUL_VOWEL_UNASSEMBLED[i]]) + "\n")

    f.write("\n\n")
    f.write("ALL                    | " + str(len(text_data)) + "\n")
    f.write("HANGUL with BATCHIM    | " + str(count_hangul_with_batchim) + "\n")
    f.write("HANGUL without BATCHIM | " + str(len(text_data) - count_hangul_with_batchim) + "\n")
    f.write("CHO-JONG REVERSED      | " + str(count_hangul_chojong_reversed) + "\n")
    f.write("CHO-JONG not REVERSED  | " + str(count_hangul_with_batchim - count_hangul_chojong_reversed) + "\n")

with open('./result.txt','rt',encoding="utf-8") as f:
    print(f.read())