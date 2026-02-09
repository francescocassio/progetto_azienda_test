# Gestionale CRUD Fatture di Vendita 📄

Un'applicazione Python per la gestione completa delle fatture di vendita.

## 🚀 Come avviare il progetto (Quick Start)
Segui questi tre comandi rapidi per preparare l'ambiente:

1. **Crea la venv:** `python3 -m venv venv` (su Windows usa `python`)
2. **Attivala:** - Mac/Linux: `source venv/bin/activate`
   - Win: `.\venv\Scripts\activate`
3. **Installa librerie:** `pip install -r requirements.txt`

---

## 🛠️ Configurazione IDE

### Se usi PyCharm (Consigliato)
PyCharm è molto intelligente e può gestire tutto per te:
1. **Apri la cartella** del progetto in PyCharm.
2. Se appare un avviso in alto con scritto **"No Python interpreter configured"**, clicca su **"Configure Python Interpreter"**.
3. Scegli **"Add Interpreter"** -> **"Local Interpreter"**.
4. Seleziona **"Existing"** e punta al file python dentro la cartella `venv` che hai creato (es: `venv/bin/python` o `venv/Scripts/python.exe`).
5. Se PyCharm rileva il file `requirements.txt`, clicca su **"Install requirements"** nell'avviso giallo che apparirà in alto.

### Se usi VS Code
1. Apri la cartella.
2. Premi `Cmd+Shift+P` (Mac) o `Ctrl+Shift+P` (Win).
3. Cerca **"Python: Select Interpreter"** e seleziona quello della tua `venv`.

---

## 📂 Struttura del Progetto
- `main.py`: File principale.
- `requirements.txt`: Elenco librerie necessarie.
- `.gitignore`: Esclude `venv/`, `.idea/` e file temporanei.
- `README.md`: Istruzioni d'uso.

---

## 📝 Note per lo sviluppo
Se aggiungi nuove librerie, ricordati di aggiornare il file dei requisiti:
`pip freeze > requirements.txt`