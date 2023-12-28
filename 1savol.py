# 1.(httpx, asyncio, io, context manager)
# (url=64.227.101.77)
# decriptions nomli papkadagi hamma fayllardan fruit larning kerakli name, price va descriptionlarini o'qib oling.
# httpx async client bilan yuqoridagi urlga post request yuboring. Requestdan qaytgan status codelar "Response 001.txt 200" korinishida faylga yozib boring.
# fayllar bilan ishlash uchun FileManager nomli custom context manager yarating.
from pprint import pprint
import asyncio
from time import time
import aiohttp
import httpx
import os
class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path
    def __iter__(self):
        self.file = open(file=self.file_path)
        return self
    def __next__(self):
        line  = self.file.read()
        if not line:
            self.file.close()
            raise StopIteration
        return line.strip()

def Dictdata(put):
    slov = {}
    lst = list()
    for file in os.listdir(put):
        for line in FileManager(f"{put}/{file}"):
            ls=line.split("\n")
            slov['name'] = ls[0]
            slov['price'] = ls[1].split(' ')[0]
            slov['text'] = ls[2]
        print(slov)
   # dict(sorted(slov.items()))
    print(lst)



async def send_request(url, client: aiohttp.ClientSession,slovar):
    response = await client.post(url, slovar)
    # data = response.json()
    # print(data)
    # writejson(data)

async def get_comments(ls):
    url = "http://164.92.64.76/desc/"
    async with httpx.AsyncClient() as client:
        tasks = [asyncio.create_task(send_request(url, client,)) for i in ls]
        print(tasks)
        await asyncio.gather(*tasks)



if __name__ == '__main__':
    # sync_get_comments()
    # asyncio.run(get_comments())
    Dictdata('descriptions')