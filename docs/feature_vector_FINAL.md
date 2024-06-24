# Feature vector

Ognuno dei gruppi si riferisce ad uno storico a lungo termine (e.g. l'intera stagione) da valutare per ogununa delle due squadre che si incontrano; per ogni parametro farei anche una valutazione delle ultime X partite, così da capire l'andamento rispetto alla casistica generale.

## Performance di squadra per valutare i dati storici
- record vittorie/sconfitte
- media punti segnati/subiti

Ora io calcolerei questi stessi parametri ma solo in caso di:
- scontri diretti
- casa/trasferta


Inoltre, si potrebbero calcolare le stesse statistiche inserendo le seguenti variabili:
- giorni di riposo della squadra
- play-off oppure regular-season (si potrebbe dettagliare ancora di più, e.g. vaire fasi dei play-off o periodi della stagione)
- arbitro principale 
- qualità del roster (presenza/assenza dei top-players)


## Dati sull'incontro da predirre
Di seguito sono riportate le informazioni da sapere relative all'incontro che si intende valutare:
- squadre che si incontrano
- luogo (casa/trasferta per una squadra o per l'altra)
- giorni di riposo delle due squadre che giocano
- arbitro principale
- tipo di partita (play-off o stagione normale)
- qualità del roster (presenza/assenza dei top-players)


Alle suddette informazioni, le stesse che hanno composto il DB dei dati storici, si aggiungono ulteriori dati da considerare:
- GIOCATORI
    - qualità del roster (in questo caso si intende il calcolo del "valore" dei singoli giocatori in campo)
    - (in caso di play-off, valutare anche esperienza dei giocatori)
- QUOTE
    - quote pre-partita (3/4 giorni prima della partita)
    - variazione quote (poche ore prima della partita)
- RELAZIONI (sarebbe figo valutare qualche "scoop" in caso ci sia il modo)
    - relazione tra giocatori 
    - relazioni con l'allenatore
    - cambiamenti dello staff
    - dichiarazioni/rinnovi/addi (management)



# NOTE: qualità del roster
Oltre alla casistica della presenza/assenza dei top-players (che bisogna anche capire come identificare), il prof. vuole sapere per ogni match la "forza" del roster.
Per fare ciò secondo me ha senso creare una sorta di punteggio a cui ogni giocatore contribuisce. Di seguito ho riportato le statistiche che andrebbero considerate.

## Parametri statistici individuali
- Punti per partita (PTS)
- Rimbalzi per partita (REB)
  - Rimbalzi offensivi (OREB)
  - Rimbalzi difensivi (DREB)
- Assist per partita (AST)
- Percentuale di tiri dal campo (FG%)
- Percentuale di tiri da tre punti (3P%)
- Percentuale di tiri liberi (FT%)
- Palle perse per partita (TO)
- Palle recuperate per partita (STL)
- Stoppate per partita (BLK)
- Minuti giocati per partita (MIN)

## Parametri specifici per ruolo
Si può anche valutare di dare più o meno peso a certi punteggi in base al ruolo del giocatore (e.g. se un centro tira male da 3 non è sicuramente un problema).

## Parametri avanzati
Questi me li ha detti chatgpt, alcuni non so neanche cosa siano e se siano recuperabili dall'API, ma credo di si
- Player Efficiency Rating (PER)
- True Shooting Percentage (TS%)
- Effective Field Goal Percentage (eFG%)
- Win Shares (WS)
  - Win Shares per 48 minuti (WS/48)
- Box Plus/Minus (BPM)
- Value Over Replacement Player (VORP)
- Usage Rate (USG%)
- Offensive Rating (ORTG)
- Defensive Rating (DRTG)
- Net Rating (NETRTG)
- Real Plus-Minus (RPM)
- Adjusted Plus-Minus (APM)
- Player Impact Estimate (PIE)



Di seguito, ci sono altri dati che mi ha consigliato ChatGpt ma che sinceramente non userei, anche se sicuramente utili. Sono dati abbastanza qualitativi e quindi difficili da calcolare, sopratutto basandosi solo sull'API dell'NBA.
Ho tenuto solo quelli più interessanti a mio parere.

## Parametri contestuali
- Performance nei momenti decisivi: Punti segnati, assist, rimbalzi e altre statistiche nei momenti chiave delle partite (clutch time).
- Consistenza: Variazione delle performance partita per partita.
- Impatto in partite contro avversari forti: Prestazioni contro le migliori squadre della lega.
- Condizione fisica: Stato di salute e storicità degli infortuni.

## Parametri qualitativi
- Leadership e intangibles: Capacità di leadership e altri aspetti non misurabili come l'etica del lavoro, la presenza nello spogliatoio, e l'influenza positiva sui compagni di squadra.
- Esperienza: Numero di anni in NBA e esperienza nei playoff.
- Prestazioni nei playoff: Statistiche e impatto nelle partite di playoff rispetto alla stagione regolare.

## Parametri situazionali
- Ruolo nella squadra: Importanza del ruolo del giocatore all'interno della squadra (starter, sixth man, role player).
- Compatibilità con i compagni di squadra: Chimica e sinergia con gli altri giocatori chiave del roster.
- Efficienza sotto pressione: Capacità di performare sotto pressione in situazioni ad alta intensità.
- Comportamento in trasferta: Differenza di performance tra partite in casa e in trasferta.


## Parametri di confronto
- Comparazione con altri giocatori nella stessa posizione: Classifica del giocatore rispetto ai suoi pari ruolo nella lega.
- Premi e riconoscimenti: Selezioni All-Star, premi MVP, inclusioni in All-NBA teams, ecc.
- Contributo a vittorie: Percentuale di vittorie a cui ha contribuito direttamente (game-winning plays).

## Dati biometrici
- Altezza, peso e wingspan: Misure fisiche del giocatore.
- Atletismo: Velocità, agilità, salto verticale, ecc.




