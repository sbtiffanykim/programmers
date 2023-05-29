def solution(id_pw, db):
    accounts = {info[0]: info[1] for info in db}
    
    if id_pw[0] in accounts.keys():
        if accounts[id_pw[0]] == id_pw[1]:
            return 'login'
        else: 
            return 'wrong pw'
    else:
        return 'fail'