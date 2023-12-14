import requests
from bs4 import BeautifulSoup

def naver_blog_crawler(search_keyword):
    # 검색어를 이용하여 Naver 블로그 검색 결과 페이지의 URL을 생성
    search_url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}'

    # HTTP GET 요청을 보내서 HTML 페이지를 받아옴
    response = requests.get(search_url)

    # 응답이 성공적인지 확인
    if response.status_code == 200:
        # BeautifulSoup을 사용하여 HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 블로그 검색 결과가 들어있는 부분을 선택
        blog_results = soup.select('.sh_blog_top')

        # 각 블로그 결과에 대해 정보 추출
        for result in blog_results:
            # 블로그명 추출
            blog_name = result.select_one('.sh_blog_title').text

            # 블로그 주소 추출
            blog_url = result.select_one('.sh_blog_title')['href']

            # 포스팅 제목 추출
            post_title = result.select_one('.sh_blog_title').attrs['title']

            # 포스팅 날짜 추출
            post_date = result.select_one('.txt_inline').text

            # 결과 출력
            print(f'블로그명: {blog_name}')
            print(f'블로그주소: {blog_url}')
            print(f'제목: {post_title}')
            print(f'포스팅날짜: {post_date}')
            print('-' * 50)

    else:
        print('HTTP 요청이 실패하였습니다.')

# 검색어 입력
search_keyword = input('검색어를 입력하세요: ')

# 크롤링 실행
naver_blog_crawler(search_keyword)
