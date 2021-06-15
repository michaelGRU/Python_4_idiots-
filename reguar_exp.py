# # regualar expression
# import re

# sen = "hello, my name is michael. and i 9 was educated at Oxford"
# pattern = re.compile(r"\d")
# matches = pattern.finditer(sen)
# for match in matches:
#     print(match)
import re

f = "Hello. My name is Michael? you're 20 years old. I study at Harvard. I am smart."
sentences = f.split(".")
for s in sentences:
    # Remove punctuation and convert to lowercase
    clean = re.sub("[^\w\n ]+", "", s).lower()
    clean = re.sub("_+", "", clean).strip()
    # Create list of words separated by whitespace
    words = re.split("\s+", clean)
    print(words)
