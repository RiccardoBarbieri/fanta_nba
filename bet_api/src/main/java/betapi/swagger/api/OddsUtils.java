package betapi.swagger.api;

import betapi.database.ScheduleBookmakers;
import betapi.swagger.model.Bookmaker;
import betapi.swagger.model.Market;
import betapi.swagger.model.Odds;
import betapi.swagger.model.Outcome;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@Component
public class OddsUtils {

    private static ScheduleBookmakers scheduleBookmakers;

    @Autowired
    public OddsUtils(ScheduleBookmakers scheduleBookmakers) {
        OddsUtils.scheduleBookmakers = scheduleBookmakers;
    }

    public static List<Odds> sortBookmakersByOdds(Odds odds) {
        Odds oddsCopyForHomeTeam = deepCopyOdds(odds);
        Odds oddsCopyForAwayTeam = deepCopyOdds(odds);

        // Ordina i bookmakers per la squadra di casa
        List<Bookmaker> sortedByHomeTeam = oddsCopyForHomeTeam.getBookmakers().stream()
                .sorted((b1, b2) -> {
                    Float price1 = getPriceForTeam(b1, odds.getHomeTeam());
                    Float price2 = getPriceForTeam(b2, odds.getHomeTeam());
                    return price2.compareTo(price1); // Ordine decrescente
                })
                .collect(Collectors.toList());

        // Ordina i bookmakers per la squadra in trasferta
        List<Bookmaker> sortedByAwayTeam = oddsCopyForAwayTeam.getBookmakers().stream()
                .sorted((b1, b2) -> {
                    Float price1 = getPriceForTeam(b1, odds.getAwayTeam());
                    Float price2 = getPriceForTeam(b2, odds.getAwayTeam());
                    return price2.compareTo(price1); // Ordine decrescente
                })
                .collect(Collectors.toList());

        // Aggiorna le liste di bookmakers nelle copie delle Odds
        oddsCopyForHomeTeam.setBookmakers(sortedByHomeTeam);
        oddsCopyForAwayTeam.setBookmakers(sortedByAwayTeam);

        // Ritorna entrambe le copie
        return Arrays.asList(oddsCopyForHomeTeam, oddsCopyForAwayTeam);
    }

    private static Float getPriceForTeam(Bookmaker bookmaker, String team) {
        return bookmaker.getMarkets().stream()
                .flatMap(market -> market.getOutcomes().stream())
                .filter(outcome -> outcome.getName().equals(team))
                .map(Outcome::getPrice)
                .findFirst()
                .orElse(Float.MIN_VALUE); // Valore predefinito nel caso in cui non si trovi l'outcome
    }

    private static Odds deepCopyOdds(Odds original) {
        Odds copy = new Odds();
        copy.setId(original.getId());
        copy.setSportKey(original.getSportKey());
        copy.setSportTitle(original.getSportTitle());
        copy.setCommenceTime(original.getCommenceTime());
        copy.setHomeTeam(original.getHomeTeam());
        copy.setAwayTeam(original.getAwayTeam());
        copy.setBookmakers(original.getBookmakers().stream()
                .map(OddsUtils::deepCopyBookmaker)
                .collect(Collectors.toList()));
        return copy;
    }

    private static Bookmaker deepCopyBookmaker(Bookmaker original) {
        Bookmaker copy = new Bookmaker();
        copy.setKey(original.getKey());
        copy.setTitle(original.getTitle());
        copy.setUrl(original.getUrl());
        copy.setLastUpdate(original.getLastUpdate());
        copy.setMarkets(original.getMarkets().stream()
                .map(OddsUtils::deepCopyMarket)
                .collect(Collectors.toList()));
        return copy;
    }

    private static Market deepCopyMarket(Market original) {
        Market copy = new Market();
        copy.setKey(original.getKey());
        copy.setOutcomes(original.getOutcomes().stream()
                .map(OddsUtils::deepCopyOutcome)
                .collect(Collectors.toList()));
        return copy;
    }

    private static Outcome deepCopyOutcome(Outcome original) {
        Outcome copy = new Outcome();
        copy.setName(original.getName());
        copy.setPrice(original.getPrice());
        copy.setPoint(original.getPoint());
        copy.setDescription(original.getDescription());
        return copy;
    }

    public static void addBookmakersUrl(Odds odds, String regions) throws IOException {
        List<betapi.database.documents.Bookmaker> bookmakersList;
        try {
            bookmakersList = scheduleBookmakers.getBookmakers();
            Map<String, String> bookmakerUrlMap = bookmakersList.stream()
                    .collect(Collectors.toMap(b -> (b.getRegion() + b.getKey()), betapi.database.documents.Bookmaker::getUrl));

            for (Bookmaker b : odds.getBookmakers()) {

                String url;
                if (regions.contains(",")) {
                    for (String reg: regions.split(",")) {
                        url = bookmakerUrlMap.get(reg + b.getKey());
                        if (url != null) {
                            b.setUrl(url);
                            break;
                        }
                    }
                }
                else {
                    b.setUrl(bookmakerUrlMap.get(regions.substring(0,2) + b.getKey()));
                }
            }
        } catch (IOException e) {
            throw new IOException(e);
        }
    }
}
