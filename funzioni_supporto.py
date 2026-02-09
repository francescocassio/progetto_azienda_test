import os
from funzioni_services import inserisci_fattura, mostra_fatture


def pulisci_schermo():
    # Pulisce la console (funziona su Mac, Windows e Linux)
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    print("\n" + "=" * 40)
    print("      📂 GESTIONALE FATTURE v1.0")
    print("=" * 40)
    print("  [1] 📥 Salva nuova fattura")
    print("  [2] 📋 Mostra tutte le fatture")
    print("  [0] 🚪 Termina programma")
    print("=" * 40)


def scelta():
    while True:
        menu()
        try:
            opzione = int(input("\n👉 Scelta: "))

            if opzione == 1:
                pulisci_schermo()
                print("--- INSERIMENTO FATTURA ---")
                inserisci_fattura()
                input("\nPremi Invio per tornare al menu...")

            elif opzione == 2:
                pulisci_schermo()
                print("--- ARCHIVIO FATTURE ---")
                mostra_fatture()
                input("\nPremi Invio per tornare al menu...")

            elif opzione == 0:
                print("\n👋 Chiusura in corso... Arrivederci!")
                break

            else:
                print("\n⚠️  Opzione non valida! Scegli tra 0, 1 o 2.")

        except ValueError:
            print("\n❌ Campo non accettato: inserisci un NUMERO.")
        except EOFError:
            print("\n\nWTF? CTRL + D? Ma cosa combini! Uscita forzata...")
            break
        except Exception as e:
            print(f"\n☢️  Errore critico: {e}")
            break


if __name__ == '__main__':
    scelta()