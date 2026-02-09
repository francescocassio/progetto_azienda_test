import datetime
import mysql.connector
import time
from funzioni_database import create_connection, esegui_query, esegui_query_param, esegui_query_select


def inserisci_fattura():

    risultato = esegui_query_select("SELECT MAX(id_fattura) FROM fattura")
    id_massimo = risultato[0][0]

    id_fattura = (id_massimo if id_massimo is not None else 0) + 1 #AIUTO GEMINI (calcolo se id è nullo perchè 0 fatture, lo trasforma in 0)
    destinatario = input("Inserisci il destinatario: ").strip()
    bsvenduto = input("Inserisci il bene servizio venduto: ").strip()

    try:
        importo = float(input("Inserisci l'importo: "))
    except:
        print("Errore: L'importo deve essere un numero valido. Operazione annullata.")
        return

    if destinatario == "" or bsvenduto == "":
        print("Errore: Destinatario o Servizio mancanti. Operazione annullata.")
        return

    iva = importo / 1.22

    imponibile = importo - iva

    #impostiamo come data di fattura direttamente la data odierna in cui la stiamo registrando
    data_fattura = datetime.date.today()

    # impacchettiamo tutti i dati in una tupla, per passarla in allegato alla execute
    dati = (id_fattura, destinatario, bsvenduto, importo, iva, imponibile, data_fattura)

    q_inserisci_fattura = f"""
    INSERT INTO fattura (id_fattura,destinatario, bene_servizio_venduto, importo, iva, imponibile, data_fattura)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    esegui_query_param(q_inserisci_fattura, dati)

    print("Complimenti, fattura inserita!")


def mostra_fatture():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM fattura")

    print("--- ELENCO FATTURE ---")

    #qui non usiamo fetchall cosi leggiamo i dati al volo e li visualizziamo
    print(f"{'id_fattura':<12}{'emittente':<20}{'destinatario':<15}{'bene/servizio':<15}{'importo':<10}{'IVA':<10}{'imp':<10}{'data':<15}")
    for f in cursor:
        print(f"{f[0]:<12}{f[1]:<20}{f[2]:<15}{f[3]:<15}{f[4]:<10}{f[5]:<10}{f[6]:<10}{str(f[7]):<15}")


    # print(cursor.description)
    cursor.close()
    conn.close()