import re

def solution(new_id):
    not_allowed = '~ ! @ # $ % ^ & * ( ) = + [ { ] } : ? , < > /'.split(' ')
    
    new_id = new_id.lower() # 1
    new_id = ''.join([c for c in new_id if c not in not_allowed]) # 2
    new_id = re.sub('[.]{2,}', '.', new_id) # 3
    if new_id.startswith('.'): new_id = new_id[1:] # 4
    if new_id.endswith('.'): new_id = new_id[:-1] # 4
    if len(new_id) == 0: new_id += 'a' # 5
    if len(new_id) >= 16: new_id = new_id[:15] # 6
    if new_id.endswith('.'): new_id = new_id[:-1] # 6
    # 7
    if len(new_id) <= 2: 
        last_word = new_id[-1]
        while len(new_id) < 3:
            new_id += last_word
    
    return new_id