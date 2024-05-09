# length / function
# len()
# method
# str.lower()
text = "my name is ashish"
print(text.upper())
new_text = text.upper()
print(new_text)

text1 = "My Name Is Tiwari"
text_newwala = text1.lower()
print(text_newwala)

text1 = "My Name Is Tiwari"
text_newwala = text1.title()
print(text_newwala)

text1 = "        My Name Is Tiwari   "
text_newwala = text1.lstrip()
print(text_newwala)

text1 = "My Name Is Tiwari"
text_newwala = text1.find("war")
print(text_newwala)

text1 = "My Name Is Tiwari"
text_newwala = text1.replace("a", "@")
print(text_newwala)

text1 = "My Name Is Tiwari"
text_newwala = "name" in text
print(text_newwala)

text1 = "My Name Is Tiwari"
text_newwala = "name" not in text
print(text_newwala)
