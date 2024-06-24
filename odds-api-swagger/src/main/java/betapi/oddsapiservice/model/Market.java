package betapi.oddsapiservice.model;

import com.betapi.oddsapiservice.utils.Utils;

import java.util.Date;
import java.util.List;

public class Market {

    private MarketKey key;
    private String last_update;
    private List<Outcome> outcomes;

    public String getKey() {
        return key.getKey();
    }

    public void setKey(String key) {
        this.key = MarketKey.fromKey(key);
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

    public List<Outcome> getOutcomes() {
        return outcomes;
    }

    public void setOutcomes(List<Outcome> outcomes) {
        this.outcomes = outcomes;
    }
}
