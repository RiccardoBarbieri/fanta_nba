### Dopo aver letto vari articoli ho appurato che questo sono le statistiche che ci servono:

## Vettore finale
win_percentage_A
fg_percentage_A
fg3_percentage_A
ft_percentage_A
rebounds_A
assists_A
turnovers_A
steals_A
blocks_A
plus_minus_A
offensive_rating_A
defensive_rating_A
true_shooting_percentage_A 
win_percentage_B
fg_percentage_B
fg3_percentage_B
ft_percentage_B
rebounds_B
assists_B
turnovers_B
steals_B
blocks_B
plus_minus_B
offensive_rating_B
defensive_rating_B
true_shooting_percentage_B
Starting_line_up_A
Starting_line_up_B
Bench_A
Bench_B
Bookmark_A
Bookmark_B
win_percentage_A_last5games
win_percentage_B_last5games
Referee_name
Home_Team -> 0 se A in casa, 1 se A fuori casa
Distance_travelled -> distanza tra le città
Data_partita
Season -> anno della stagione (farei un dataset solo con le ultime 3 stagioni)
Topic -> 0 se siamo in regular season, 1 se siamo nei playoff  (altre partite tipo amichevoli o partite di preseason non vanno contate)



## Notes:
Tutte le statistiche si ottengono da nba.com chiaramente senza contare i bookmarks.
Il risultato finale deve quindi essere una tabella dove ogni riga rappresenta una partita!
# Importante questi valori:
Starting_line_up_A
Starting_line_up_B
Bench_A
Bench_B
# i primi due sono obbligatori, i secondi 2 sono necessari per avere un modello più accurato ma non sono necessari. 
# In particolare i primi due dovrebbero essere reperibili qui:
https://www.nba.com/players/todays-lineups

In ogni caso io troverei l'elo di ogni giocatore o su nba.com ma più probabilmente è meglio su dunkest (che sarebbe il fantanba)
a questo punto si sommano gli elo del quintetto iniziale e quelli della panchina per ottenere l'elo. Chiaramente andrebbero poi calcolate per ogni 
partita perchè il roster può cambiare -> bisogna avere il roster di ogni squadra per ogni partita.
Secondo me sono statistiche che esistono già in giro ma non le ho trovate. se non nel link sopra.

Per me possiamo fare che facciamo solo la starting line senza fare la bench che potrebbe avere anche senso...





