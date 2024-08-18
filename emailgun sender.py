import os
import random
import requests
import threading
import time
def send_email_via_mailgun(api_key, domain, sender, recipient, subject, html):
    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={
            "from": sender,
            "to": recipient,
            "subject": subject,
            "html": html
        }
    )
# Example usage:
api_key = "f2470bd958dce295a25f2b055ff47591-623e10c8-1b06fa46"
domain = "tonypetkov.eu"
sender = "FTX <ftx-Support-claim@tonypetkov.eu>"
cont=1


def sendMail(recipients):
    try:
        folder_path="./letters"
        files = os.listdir(folder_path)
        random_file = random.choice(files)
        random_file_path = os.path.join(folder_path, random_file)
        html_text = open(random_file_path , 'r', encoding='utf-8').read()
        def random_name_and_subject():
            try:
                        # Read all names from names.txt
                with open('sender_names.txt', 'r',encoding='utf-8') as name_file:
                    names = name_file.readlines()
                        
                        # Read all subjects from subjects.txt
                with open('subjects.txt', 'r' ,encoding='utf-8') as subject_file:
                    subjects = subject_file.readlines()
                        
                        # Choose a random name and subject if lists are not empty
                if names and subjects:
                    random_name = random.choice(names).strip()
                    random_subject = random.choice(subjects).strip()
                    return random_name, random_subject
                else:
                    return None, None
                    
            except FileNotFoundError:
                return None, None
        name, subject = random_name_and_subject()
        try:
            text1=open('./txt/##text1##.txt','r',encoding='utf-8').read().splitlines()
            if len(text1)>=1:
                html_text=html_text.replace("##text1##", random.choice(text1))
        except:
            pass
        try:
            text2=open('./txt/##text2##.txt','r',encoding='utf-8').read().splitlines()
            if len(text2)>=1:
                html_text=html_text.replace("##text2##", random.choice(text2))
        except:
            pass
        try:
            text3=open('./txt/##text3##.txt','r',encoding='utf-8').read().splitlines()
            if len(text3)>=1:
                html_text=html_text.replace("##text3##", random.choice(text3))
        except:
            pass
        
        sent=open("SentSuccess.txt","r",encoding='utf-8').read().splitlines()
        email=str(recipients[0])
        print(email)
        if email not in sent:
            response = send_email_via_mailgun(api_key, domain, sender, recipients[0], subject,  html_text)
            if response.status_code == 200:
                print("Email sent successfully")
                open("SentSuccess.txt","a",encoding='utf-8').write(email+'\n')
                time.sleep(4)
            else:
                print(f"Failed to send email: {response.status_code}")
                print(response.text)
        else:
            print('alread sent')
    except Exception as e:
        print('error!', e)



    






def thread():
    with open('emailList.txt', 'r', errors='ignore') as file:
        lista = file.read().split('\n')
    batch_size = 1
    if len(lista)<batch_size:
        batch_size=len(lista)
    threadnum = 1
    threads = []
    
    for i in range(0, len(lista), batch_size):
        email_batch = lista[i:i + batch_size]
        thread = threading.Thread(target=sendMail, args=(email_batch,))
        threads.append(thread)
        thread.start()
        
        if len(threads) == threadnum:
            for x in threads:
                x.join()
            threads = []
    
    # Ensure all remaining threads are completed
    for x in threads:
        x.join()
while True:
    thread()
