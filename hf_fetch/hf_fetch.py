import argparse
import requests
from bs4 import BeautifulSoup
import os

def get_files(repo,base='https://hf-mirror.com'):
    # 请求头部信息，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3'
    }
    files=[]
    if repo:
        url = f"{base}/{repo}/tree/main"
        response = requests.get(url, headers=headers)
        # print(response)
        if response.status_code == 200:
            # 获取 HTML 源代码
            html = response.text
            
            # 使用 BeautifulSoup 解析 HTML
            soup = BeautifulSoup(html, 'lxml')
            dfiles=soup.find_all('a',attrs={'title':"Download file"}) 
            # print(len(dfiles))
            for file in dfiles:
                # print(file['href'])
                files.append('%s%s'%(base,file['href']))
        else:
            print("fail")
    return files

def main():
    parser = argparse.ArgumentParser(description='huggingface model downoader')
    parser.add_argument('-repo', help='huggingface model,like xxx/yyyy')
    parser.add_argument('-base',default='https://hf-mirror.com', help='proxy')
    parser.add_argument('-o',default='~/.cache/huggingface/hub', help='output path')
    args = parser.parse_args()
    files=get_files(args.repo,args.base)
    durls=[]
    for durl in files:
        durl=durl.replace('?download=true','')
        durls.append(durl)
    os.system('wget -c --progress=bar -P %s/%s  %s'%(args.o,'models--%s'%args.repo.replace('/','--'),' '.join(durls)))

if __name__ == "__main__":
    main()