package betapi.oddsapiservice.model;

import betapi.oddsapiservice.utils.Utils;

import java.util.Date;
import java.util.List;

public class Bookmaker {

    private String key;
    private String title;
    private String last_update;
    private List<Market> markets;

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getLast_update() {
        return last_update;
    }

    public void setLast_update(String last_update) {
        this.last_update = last_update;
    }

    //Additional getter for last_update in Date format
    //checks if the format is unix or iso8601 and returns a Date object
    public Date getLast_update_date() {
        return Utils.getDate(last_update);
    }

    public List<Market> getMarkets() {
        return markets;
    }

    public void setMarkets(List<Market> markets) {
        this.markets = markets;
    }
}
