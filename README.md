# HackMeFast
*Egy szándékosan sérülékeny FastAPI webalkalmazás biztonsági teszteléshez és tanuláshoz.*

##  Leírás  
A **HackMeFast** egy FastAPI alapú webalkalmazás, amelyet **szándékosan** olyan sérülékenységekkel tervez~~tem~~ek, amelyek gyakoriak a való életben is. A cél egy **biztonság tesztelési és oktatási platform** létrehozása, ahol a bárki gyakorolhatja és megértheti az alábbi támadásokat:  

- **Directory Traversal**
- **Cross-Site Request Forgery (CSRF)**
- **Cross-Site Scripting (XSS)**

## Főbb jellemzők  
-  **FastAPI-alapú sérülékeny backend**  
-  Valós **webes és API biztonsági problémák demonstrálása**  
-  Tanulási célokra 
-  **Egyszerű telepítés** Python ~~,Angular és Docker~~ segítségével  

## Telepítés és futtatás  
### Szükséges eszközök (egyelőre)
- **Python 3.x**  
- **pip** (`pip install -U pip`)  
- **FastAPI és a szükséges csomagok** (`pip install -r requirements.txt`)  

### **1. Klónozd a repót**  
```bash
git clone https://github.com/your-username/HackMeFast.git 
cd HackMeFast
```

### **2. Függőségek telepítése**
```bash
pip install -r requirements.txt
```
### **3. Az alkalmazás futtatása**
```bash
chmod +x start.sh
./start.sh
```
Az API elérhető lesz itt: http://127.0.0.1:8000

A Swagger UI elérhetősége: http://127.0.0.1:8000/docs