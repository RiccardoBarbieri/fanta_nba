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

@HttpExchange(url = "/v4", accept = "application/json") //header always needed by odds api
public interface OddsApiService {

    // SPORTS - Returns a list of in-season sport objects.
    @GetExchange(value = "/sports")
    @ResponseBody
    List<Sport> getSports(/*@RequestParam String apiKey*/
            @RequestParam(required = false) Boolean all);

// --Commented out by Inspection START (28/06/2024 17:27):
//    // ODDS - Returns a list of upcoming and live games with recent odds for a given sport, region and market
//    @GetExchange(value = "/sports/{sportKey}/odds")
//    @ResponseBody
//    List<Odds> getOdds(/*@RequestParam String apiKey*/
//            @PathVariable String sportKey,
//            @RequestParam String regions,
//            @RequestParam(required = false) String markets,
//            @RequestParam(required = false) String dateFormat,
//            @RequestParam(required = false) String oddsFormat,
//            @RequestParam(required = false) String eventIds,
//            @RequestParam(required = false) String bookmakers,
//            @RequestParam(required = false) String commenceTimeFrom,
//            @RequestParam(required = false) String commenceTimeTo);
// --Commented out by Inspection STOP (28/06/2024 17:27)

    // EVENTS - Returns a list of in-play and pre-match events for a specified sport or league. The response includes event id, home and away teams, and the commence time for each event.
    @GetExchange(value = "/sports/{sportKey}/events")
    @ResponseBody
    List<Event> getEvents(/*@RequestParam String apiKey*/
            @PathVariable String sportKey,
            @RequestParam(required = false) String dateFormat,
            @RequestParam(required = false) String eventIds,
            @RequestParam(required = false) String commenceTimeFrom,
            @RequestParam(required = false) String commenceTimeTo);

    // EVENT ODDS - Returns odds for a single event.
    @GetExchange(value = "/sports/{sportKey}/events/{eventId}/odds")
    @ResponseBody
    Odds getEventOdds(/*@RequestParam String apiKey*/
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
