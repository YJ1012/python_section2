import re

data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in list(data.split("\n")):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))


test_arr="112233445512345,./aabbccddeeffabcdef"
patt = re.compile("a.b");
print(test_arr);
print(patt.sub("---", test_arr))


test_c ="abcdefgabcdefgaabbccddeeffgg";
test_i ="12345123451122334455";
patt_i = re.compile("[6-9]");
print(patt_i.match(test_c));
print(patt_i.match(test_i));
patt_c = re.compile("[h-x]");
print(patt_c.match(test_c));
print(patt_c.match(test_i));

ttt=[];
pat_test1=re.compile("a[.]{3,}b");

ttt.append("acccb");
ttt.append("a....b");
ttt.append("aaab");
ttt.append("a.cccb");

for i in range(4):
    print(ttt[i],pat_test1.match(ttt[i]));
