package com.betapi.oddsapiservice.bookmakers;

import com.betapi.oddsapiservice.bookmakers.model.Bookmaker;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.event.EventListener;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

@Component
public class ScheduleBookmakers {

    private static final Logger log = LoggerFactory.getLogger(ScheduleBookmakers.class);

    private static final String BOOKMAKERS_URL = "https://the-odds-api.com/sports-odds-data/bookmaker-apis.html";

    public static void main(String[] args) {
        ScheduleBookmakers scheduleBookmakers = new ScheduleBookmakers();
        try {
            scheduleBookmakers.getBookmakers();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Scheduled(cron = "0 0 0 1 */1 *")
    @EventListener(ApplicationReadyEvent.class)
    public void retrieveBookmakers() {
        log.debug("Retrieving bookmakers");

        List<Bookmaker> bookmakers = new ArrayList<>();

        try {
            bookmakers = getBookmakers();
        } catch (IOException e) {
            log.error("Failed to retrieve bookmakers", e);
        }

        File bookmakersFile = null;

        log.debug("Writing bookmakers to database");
//        ObjectMapper objectMapper = new ObjectMapper();
//        objectMapper.writeValue(bookmakersFile, bookmakers);
    }

    private List<Bookmaker> getBookmakers() throws IOException {
        Document bookmakersPage = Jsoup.connect(BOOKMAKERS_URL).get();

        Elements tables = bookmakersPage.select("table");

        List<Bookmaker> bookmakers = new ArrayList<>();

        for (Element table : tables) {
            Elements rowsNoHead = table.select("tr").stream().filter(row -> row.siblingIndex() > 1).collect(Elements::new, Elements::add, Elements::addAll);

            for (Element row : rowsNoHead) {
                Elements columns = row.select("td");
                String regionKey = columns.get(0).text();
                String bookmakerKey = columns.get(1).text();
                String bookmakerUrl = Objects.requireNonNull(columns.get(2).selectFirst("a")).attribute("href").getValue();

                log.trace("Bookmaker: {}, URL: {}, Region: {}", bookmakerKey, bookmakerUrl, regionKey);
                bookmakers.add(new Bookmaker(regionKey, bookmakerKey, bookmakerUrl));
            }
        }

        bookmakers.forEach(bookmaker -> log.debug(bookmaker.toString()));

        return bookmakers;
    }

}
