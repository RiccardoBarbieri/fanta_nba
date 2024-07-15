package betapi.swagger.api;

import betapi.swagger.model.Market;
import betapi.swagger.model.Odds;
import betapi.swagger.model.Bookmaker;
import betapi.swagger.model.Outcome;

import java.math.BigDecimal;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class FakeOddsGenerator {


    private final static String[] bookmakersKeys = {"unibet_eu", "sport888", "betfair_ex_eu", "gtbets", "williamhill", "marathonbet", "betanysports", "pinnacle", "nordicbet", "betsson"};
    private final static String[] bookmakersTitles = {"Unibet", "888 Sport", "Betfair", "GTbets", "William Hill", "Marathon Bet", "BetAnySports", "Pinnacle", "Nordic Bet", "Betsson"};

    public static Odds getFakeOdds(String marketKey, String sportKey, String home_tem, String away_team) {
        Random random = new Random();

        Odds odds = new Odds();
        odds.setSportKey(sportKey);
        odds.setHomeTeam(home_tem);
        odds.setAwayTeam(away_team);
        odds.setId("FAKED_ID_" + random.nextInt(1000, 9999));

        for (int i = 0; i < bookmakersKeys.length; i++) {
            float price1 = 2.45f + random.nextFloat() * (2.65f - 2.45f);
            float price2 = 1.5f + random.nextFloat() * (1.6f - 1.5f);
            price1 = Math.round(price1 * 100.0f) / 100.0f;
            price2 = Math.round(price2 * 100.0f) / 100.0f;

            Bookmaker bk = new Bookmaker();
            bk.setTitle(bookmakersTitles[i]);
            bk.setKey(bookmakersKeys[i]);
            bk.setLastUpdate(OffsetDateTime.now());

            List<Outcome> outcomes = new ArrayList<>();
            Outcome o_home = new Outcome();
            o_home.setName(home_tem);
            o_home.setPrice(price1);
            Outcome o_away = new Outcome();
            o_away.setName(away_team);
            o_away.setPrice(price2);

            if (marketKey.equals("spreads")) {
                float spread = 1.5f + random.nextInt(8);
                o_home.setPoint(BigDecimal.valueOf(spread));
                o_home.setPoint(BigDecimal.valueOf(spread*-1));
            }

            outcomes.add(o_home);
            outcomes.add(o_away);

            List<Market> markets = new ArrayList<>();
            Market m = new Market();
            m.setKey(Market.KeyEnum.fromValue(marketKey));
            m.setLastUpdate(OffsetDateTime.now());
            m.setOutcomes(outcomes);
            markets.add(m);

            bk.setMarkets(markets);

            odds.addBookmakersItem(bk);
        }
        return odds;
    }
}
