# Image Recognizer

Image Recognizer è una web application semplice che permette il riconoscimento automatico di oggetti all'interno di immagini caricate tramite interfaccia web, utilizzando il modello YOLOv8.

## Caratteristiche

- **Upload immagini**: Carica un'immagine dalla tua macchina per il riconoscimento.
- **Riconoscimento oggetti**: Utilizza YOLOv8 per identificare e contare gli oggetti presenti nell'immagine.
- **Interfaccia web**: Frontend essenziale basato su FastAPI e Jinja2.

## Tecnologie utilizzate

- [FastAPI](https://fastapi.tiangolo.com/) per la gestione delle API e del server web.
- [Jinja2](https://jinja.palletsprojects.com/) per il rendering dei template HTML.
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) per il riconoscimento delle immagini.
- [Python 3.8+](https://www.python.org/)

## Installazione

1. **Clona la repository:**
   ```bash
   git clone https://github.com/lorymasia/image_recognizer.git
   cd image_recognizer
   ```

2. **Crea un ambiente virtuale (opzionale ma consigliato):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Su Windows: venv\Scripts\activate
   ```

3. **Installa le dipendenze:**
   ```bash
   pip install -r requirements.txt
   ```

## Utilizzo

1. **Avvia il server FastAPI:**
   ```bash
   uvicorn main:app --reload
   ```

2. **Accedi all'applicazione:**
   Apri il browser su [http://127.0.0.1:8000](http://127.0.0.1:8000)

3. **Carica un'immagine:**
   - Nella homepage, seleziona una immagine dal tuo dispositivo e clicca su "Carica".
   - Verranno mostrati gli oggetti riconosciuti e il conteggio per ciascuna categoria individuata.

## Struttura del progetto

```
image_recognizer/
│
├── main.py               # Applicazione FastAPI principale
├── requirements.txt      # Dipendenze Python
├── templates/            # Template HTML (index.html, upload.html)
└── .gitignore
```

## Note

- Il modello YOLOv8 (`yolov8s.pt`) viene scaricato automaticamente da Ultralytics se non già presente.
- Tutte le immagini caricate vengono salvate temporaneamente sul server per l'elaborazione.
- Assicurati di avere una GPU compatibile per performance ottimali, anche se il modello può girare su CPU.

## Licenza

Questo progetto è open source e rilasciato sotto licenza MIT. Consulta il file LICENSE per maggiori dettagli.
