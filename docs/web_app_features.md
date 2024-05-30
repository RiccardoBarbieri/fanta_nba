# Info che la web app necessita relative alla NBA

Per ogni giorno devono essere presentate le partite se presenti, poi informazioni generali su classifica (regular-season e play-off) ed informazioni sulle singole squadre e i relativi giocatori. 
Bisogna decidere fino a che livello di dettaglio arrivare (ultimi X match oppure anche dati storici).

Di seguito ho riportato le informazioni che penso siano necessarie da ottenere all'interno della web app. Ovviamente molte sono accessorie, per dare completezza all'interfaccia. 



## Informazioni sulle squadre

### Dettagli squadra
- Nome della squadra
- Logo della squadra
- Città e Arena
- Allenatore
- Record attuale (Vittorie-Sconfitte)
- Posizione in classifica nella Conference
- Posizione in classifica nella Division
- Performance in casa (Record)
- Performance in trasferta (Record)
- Streak corrente (vittorie/sconfitte consecutive)
- Ultime 10 partite (Record)

### Statistiche di squadra
- Punti per partita (PPG)
- Punti subiti per partita (OPPG)
- Differenziale di punti (PD)
- Rimbalzi per partita (RPG)
- Assist per partita (APG)
- Palle rubate per partita (SPG)
- Stoppate per partita (BPG)
- Perdite di palla per partita (TOPG)
- Percentuale di tiri dal campo (FG%)
- Percentuale di tiri da tre punti (3P%)
- Percentuale di tiri liberi (FT%)
- Offensive Rating (ORTG)
- Defensive Rating (DRTG)
- Net Rating (NETRTG)

### Informazioni sui giocatori
- Nome del giocatore
- Ruolo
- Numero di maglia
- Età
- Altezza e peso
- Statistiche stagionali principali (PTS, REB, AST, FG%, 3P%, FT%)
- Ultime 5 partite (statistiche)

### Infortuni e assenze
- Giocatori infortunati: Nome e motivo
- Giocatori assenti (non infortunati): Nome e motivo dell'assenza




## Informazioni sulle partite

### Dettagli partita
- Data e ora della partita
- Luogo della partita (Arena)
- Arbitri designati
- Squadra di casa
- Squadra ospite

### Statistiche storiche
- Ultimi 10 incontri diretti (Record)
- Differenziale di punti negli scontri diretti
- Ultime 5 partite di ciascuna squadra (Record, PTS, OPPG)



## Classifiche

### Classifica della Conference
- Nome della squadra
- Record (Vittorie-Sconfitte)
- Differenziale di punti
- Percentuale di vittorie
- Striscia corrente (W-L streak)
- Ultime 10 partite (Record)

### Classifica della Division
- Nome della squadra
- Record (Vittorie-Sconfitte)
- Differenziale di punti
- Percentuale di vittorie
- Striscia corrente (W-L streak)
- Ultime 10 partite (Record)




# Info che la web app necessita relative alle quote dei bookmakers

Mi immagino uan schermata in cui c'è la partita in questione, la nostra previsione e le varie quote.

Si potrebbe pensare di inserire le 3 quote più alte da 3 bookmakers differenti.

In ogni caso, se dal nostro modello esce solo squadra vincente A o squadra vincente B ha senso inserire come quote solo "vince squadra A" o "vince squadra B".
Se invece dal modello esce anche una sorta di percentuale (e.g. squadra A vince al 75%), si può pensare di inserire altre quote come il margine di punti (e.g. squadra A vince con +7 punti di scarto) oppure uan cosa come "la partita andrà all'overtime".
Il costo per l'inserimento di queste quote sarebbe irrisorio e darebbe un bell effetto nella web app. Soprattutto, in caso si fornisca anche una percentuale di accuratezza dell'output del modello, ha senso fornire queste quote in più (sempre però limitate al risultato della partita).

Di seguito, le principali quote che potrebbero essere di interesse:
- vincitore
- vincitore con differenza punti (over/under)
- vincitore primo/secondo tempo
- vincitore della serie (in caso sia una partita di play-off)

Come si può vedere sono tutte quote relative al vincitore. Se la probabilità di vittoria è molto alta magari conviene scommettere su una differenza punti alta o sulla vittoria di entrambi i tempi.

Non sono presenti quote sui punti totali, sulle prestazioni dei giocatori, ... in quanto non sono informazioni estrapolabili dal modello!


# Funzionalità accessoria (grafico efficacia modello)
Sarebbe interessante far si che al termine di ogni match vi sia un confronto tra l'output fornito dal modello e il risutlato effettivo della partita.
In questo modo si potrbbe fornire un grafico in cui viene mostrata l'efficacia del nostro modello.




# Strutturazione pagine webapp

1. Supponiamo una prima pagina in cui si dia la possibilità all'utente di selezionare lo sport ed il campionato. Attualmente abbiamo infomrazioni solo su NBA (ovvero il nostro modello è allenato solo su questa competizione) ma, per quanto riguarda le scommesse, abbiamo disponibilità per tutti gli sports.
Oltre alle quote e alla previsione, mostriamo poi dati sul campionato (e.g. partite, clasifiche, informazioni della squadra). Attualmente noi pensiamo di opendere queste informazioni dalla NBA_API ma sarebbe interessante trovare una api che le fornisca per ogni sport, così da poter astrarre da una singola implementazione ed essere veramente flessibili.
Arriveremmo al punto che con un minimo sforzo la nostra web app sarebbe in grado si supportare qualsiasi sport (rimanendo comunque il fatto che il modello è allenato solo per NBA).

2. Dopo aver scelto sport e competizione, potremmo passare ad una schermata in cui è presente la classifica della competizione e le partite del giorno o della settimana (comunque filtraili per data). CI concentrerrremo quindi solo su info generali niente dettagli o quote delle scommesse.

3. Cliccando sulle squadre della classifica potremmo avere informazioni su di esse (altra pagina) e sui relativi giovatori (dettagliando anche informazioni su di essi volendo)

4. Cliccando sui match invece entrerremo nella schermata **core** della nostra applicazione con, oltre a info generali sulle due squadre (estensibili cliccando sul dettaglio della squadra), informazioni sulle quote principali (e più vantaggiose dei siti di scommesse) per ognuna delle due squadre. Daremo la possibilità all'utente di filtrare per certi siti di scommesse di suo interesse.

### Note
Per ora le scommesse disponibili sono solo h2h e spread (handicap) in quanto sono le uniche sensate con un modello di previsione che fornisce il vincitore. Con questa strutturazione il tutto sarebbe comunque facilmente estensibile in futuro.

API per ottenere tutte le info su tutti gli sport: https://api-sports.io/ (si potrebbe implementare in maniera parametrizzata così da renderla facilemte estensibile in futuro con altri sport)