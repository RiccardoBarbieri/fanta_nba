package betapi.oddsapiservice.model;

import java.util.List;

public class EventOdds extends Event{

    private List<Bookmaker> bookmakers;

    public List<Bookmaker> getBookmakers() {
        return bookmakers;
    }

    public void setBookmakers(List<Bookmaker> bookmakers) {
        this.bookmakers = bookmakers;
    }
}
