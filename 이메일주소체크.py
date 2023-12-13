import re

def check_email(email):
    # 이메일 주소를 검증하는 정규표현식
    #raw string notation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # re.search() 함수를 사용하여 이메일 주소 체크
    match = re.search(pattern, email)
    
    if match:
        print(f"{email}은(는) 유효한 이메일 주소입니다.")
    else:
        print(f"{email}은(는) 유효하지 않은 이메일 주소입니다.")

# 샘플 이메일 주소 10개
sample_emails = [
    "user@example.com",
    "john.doe123@gmail.com",
    "info@company.co.kr",
    "invalid.email@dot@dot.com",
    "missing.at.symbol.com",
    "user@-invalid-domain.com",
    "user@invalid-domain-.com",
    "user@.invalid-domain.com",
    "user@invalid_domain.com",
    "user@valid-domain.com"
]

# 각각의 샘플 이메일 주소에 대해 체크
for email in sample_emails:
    check_email(email)
