package betapi.database;

import betapi.database.documents.Bookmaker;
import betapi.database.repositories.BookmakerRepository;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.event.EventListener;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

@Component
public class ScheduleBookmakers {

    private static final Logger log = LoggerFactory.getLogger(ScheduleBookmakers.class);

    private static final String BOOKMAKERS_URL = "https://the-odds-api.com/sports-odds-data/bookmaker-apis.html";

    private BookmakerRepository bookmakerRepository;

    @Autowired
    private void setBookmakerRepository(BookmakerRepository bookmakerRepository) {
        this.bookmakerRepository = bookmakerRepository;
    }

    @Scheduled(cron = "0 0 0 1 */1 *")
    @EventListener(ApplicationReadyEvent.class)
    public void retrieveBookmakers() {
        log.debug("Retrieving bookmakers");

        List<Bookmaker> bookmakers;

        try {
            bookmakers = getBookmakers();

            log.debug("Writing bookmakers to database");

            // Remove bookmakers that no longer exist
            bookmakerRepository.findAll().forEach(bookmaker -> {
                if (!bookmakers.contains(bookmaker)) {
                    log.debug("Detected missing bookmaker: {}, removing", bookmaker.getKey());
                    bookmakerRepository.delete(bookmaker);
                }
            });
            bookmakers.forEach(bookmaker -> {
                if (!bookmakerRepository.existsByKey(bookmaker.getKey())) {
                    log.debug("Adding bookmaker: {}", bookmaker.getKey());
                    bookmakerRepository.insert(bookmaker);
                }
            });

            log.debug("Bookmakers updated");
        } catch (IOException e) {
            log.error("Failed to retrieve bookmakers", e);
        }

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
