import re

def tokenize_gujarati(text):
    pattern = r"[.,!?;:()\[\]{}]" \
              r"|\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b" \
              r"|\b\d+([.,]\d+)*\b" \
              r"|\b\w+@\w+\.\w+\b" \
              r"|\b@\w+\b" \
              r"|\bhttps?://\S+\b" \
              r"|[\u0A80-\u0AFF]+" 
              
    return re.findall(pattern, text)

text = input("Enter Gujarati text: ")
print("Tokens:", tokenize_gujarati(text))
