import requests
import random
# Для установки этой библиотеки пишем в командной строке
# pip install random_user_agent
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

# Записывает почты и пароли от сгенерированных аккаунтов в файл vvvregaccs.txt в той же папке, где и сама прога
f=open("vvvregaccs.txt", "a")

# Не трогаем
software_names = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)

# Генерирует аккаунты FuckingSlave с порядковыми номерами от 1 до 100
for i in range(1, 100):
    
    # Раздел с данными
    data = {
        # Не меняем
        "cid" : str(random.randint(10**8,10**9-1))+"."+str(random.randint(10**8,10**9-1)),
        
        # Менять можно
        "email" : "FuckingSlave"+str(i)+"@gmail.com",
        
        # Не меняем
        "login" : random.randint(10**19,10**20-1),
        
        # Менять можно
        "password" : "Petya"+str(random.randint(1,100)),
        
        # Сюда реф код из ссылки
        "ref" : "857af97100074748b72e70627485ed38",
        
        # Менять можно
        "username" : "FistingAnal"+str(i)+"@mail.ru",
    }
    
    # Имитация живого человека, не трогаем
    headers = {
        "Origin" : "https://vvvmovies.com",
        "Referer" : "https://vvvmovies.com/",
        "User-Agent" : user_agent_rotator.get_random_user_agent()
    }
    
    # Не трогаем
    r=requests.post("https://api.vvvgamers.com/user/account/register?cid="+data["cid"], data=data, headers=headers)
    print(i, r, headers["User-Agent"])
    if r.status_code==200:
        f.write(data["email"]+" "+data["password"]+"\n")
f.close()