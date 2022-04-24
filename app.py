from flask import Flask, render_template, request, redirect
import requests 
import random
from learn import * 
from browser import headers

app = Flask(__name__)  


def uri_exists(url):
    try:
        r = requests.get('http://'+url, stream=True, headers=headers)
        if r.status_code == 200:
            return True
        else:
            return False
    except:
        print("")
        return False



class URLShortener: 
    """ 
        URL Shortener class which shortens the URL and generates the result in a six character hashvalue 
        and insert the value in the database ...  

    """

    #hash = dict()  

    HASHING_STR = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" 
    MOD = 56800235584
    
    def __init__(self):
        pass

    
    def getString(self,number):
        ans = ""  
        while number:  
            ans = str(URLShortener.HASHING_STR[number%62]) + ans
            number //= 62
        return ans 
    

    def shortenURL(self, url_string):  
        num = random.random() * (URLShortener.MOD + 10); 
        hashedString = self.getString(int(num)) 

        while isPresentInDatabase(hashedString,collectionHandle): 
            num = random.random() * (URLShortener.MOD + 10); 
            hashedString = self.getString(int(num))  
        
        if insertDB(hashedString, url_string, collectionHandle):
            print("Inserted in DB")
        
        return hashedString
        

    def urlDecode(self, hash_string): 
        if isPresentInDatabase(hash_string, collectionHandle):
            return fetchURL(hash_string, collectionHandle)
        else:
            return ""



shorteningEngine = URLShortener()

notValid = False

@app.route('/')
def home_page(): 
    return render_template('index.html' ,notValid=notValid)


@app.route('/<url>')
def call_url(url): 
    print(url)
    url = shorteningEngine.urlDecode(url)
    if url != "" and uri_exists(url):
        print("Fetch Success")
        return redirect('http://'+ url)  
    else: 
        return render_template('failure.html')
     


@app.route('/generate' ,methods= ['GET', 'POST'])
def generate_results():  
    if request.method == 'POST':  
        URL = request.form.get('url') 
        if uri_exists(URL): 
            print(URL + ", exits")
            shortenedUrl=shorteningEngine.shortenURL(URL)
            return render_template('display_page.html', shortenedUrl=shortenedUrl, decoded= shorteningEngine.urlDecode(shortenedUrl)) 
        else: 
            print(URL + ", doesn't exists")
            return redirect('/')
    else:
        return redirect('/')

    
if __name__ == "__main__":
    app.run(debug=True)


