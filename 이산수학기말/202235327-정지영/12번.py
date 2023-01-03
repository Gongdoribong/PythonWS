original = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
original = list(original)
cypher = 'EIJFUAXVHWP CSRKOBTQYDMLZNG'
cypher = list(cypher)

def encryption(words):  # 암호화
    words = words.upper()
    words = list(words)
    result = []
    for i in range(len(words)):
        for j in range(len(original)):
            if words[i] == original[j]:
                result.append(cypher[j])
                
            
    return ''.join(result)

def decryption(words): #복호화
    words = list(words)
    result=[]
    for i in range(len(words)):
        for j in range(len(cypher)):
            if words[i] == cypher[j]:
                result.append(original[j])
            
    return ''.join(result).lower()

    
    
word1 = 'have to study'
word2 = 'UWQFTAYAESIYHASIYWFQ'
print(f'암호할 메시지:{word1} 암호화:{encryption(word1)}')    
print(f'암호된 메시지:{word2} 복호화:{decryption(word2)}') 