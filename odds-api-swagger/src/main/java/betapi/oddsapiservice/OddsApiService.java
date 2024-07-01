package betapi.oddsapiservice;

import io.swagger.model.Event;
import io.swagger.model.Odds;
import io.swagger.model.Sport;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.service.annotation.GetExchange;
import org.springframework.web.service.annotation.HttpExchange;

import java.util.List;

@HttpExchange(url = "https://api.the-odds-api.com/v4", accept = "application/json") //header always needed by odds api
public interface OddsApiService {

    // SPORTS - Returns a list of in-season sport objects.
    @GetExchange(value = "/sports")
    @ResponseBody
    List<Sport> getSports(@RequestParam(required = false, defaultValue = "26637b945257ea4ca4743c2644092541") String apiKey,
            @RequestParam(required = false) String all);

    // ODDS - Returns a list of upcoming and live games with recent odds for a given sport, region and market
    @GetExchange(value = "/sports/{sportKey}/odds")
    @ResponseBody
    List<Odds> getOdds(@RequestParam(required = false, defaultValue = "26637b945257ea4ca4743c2644092541") String apiKey,
            @PathVariable String sportKey,
            @RequestParam String regions,
            @RequestParam(required = false) String markets,
            @RequestParam(required = false) String dateFormat,
            @RequestParam(required = false) String oddsFormat,
            @RequestParam(required = false) String eventIds,
            @RequestParam(required = false) String bookmakers,
            @RequestParam(required = false) String commenceTimeFrom,
            @RequestParam(required = false) String commenceTimeTo);

    // EVENTS - Returns a list of in-play and pre-match events for a specified sport or league. The response includes event id, home and away teams, and the commence time for each event.
    @GetExchange(value = "/sports/{sportKey}/events")
    @ResponseBody
    List<Event> getEvents(@RequestParam(required = false, defaultValue = "26637b945257ea4ca4743c2644092541") String apiKey,
            @PathVariable String sportKey,
            @RequestParam(required = false) String dateFormat,
            @RequestParam(required = false) String eventIds,
            @RequestParam(required = false) String commenceTimeFrom,
            @RequestParam(required = false) String commenceTimeTo);

    // EVENT ODDS - Returns odds for a single event.
    @GetExchange(value = "/sports/{sportKey}/events/{eventId}/odds")
    @ResponseBody
    Odds getEventOdds(@RequestParam(required = false, defaultValue = "26637b945257ea4ca4743c2644092541") String apiKey,
            @PathVariable String sportKey,
            @PathVariable String eventId,
            @RequestParam String regions,
            @RequestParam(required = false) String markets,
            @RequestParam(required = false) String dateFormat,
            @RequestParam(required = false) String oddsFormat,
            @RequestParam(required = false) String eventIds,
            @RequestParam(required = false) String bookmakers,
            @RequestParam(required = false) String commenceTimeFrom,
            @RequestParam(required = false) String commenceTimeTo);
}
