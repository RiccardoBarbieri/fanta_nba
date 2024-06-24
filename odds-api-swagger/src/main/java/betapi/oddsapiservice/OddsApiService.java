package betapi.oddsapiservice;

import betapi.oddsapiservice.model.Event;
import betapi.oddsapiservice.model.Sport;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.service.annotation.GetExchange;
import org.springframework.web.service.annotation.HttpExchange;

import java.util.List;

@HttpExchange(url = "/v4", accept = "application/json") //header always needed by odds api
public interface OddsApiService {

    @GetExchange(value = "/sports")
    @ResponseBody
    List<Sport> getSports(/*@RequestParam String apiKey*/);

    @GetExchange(value = "/sports/{sportKey}/odds")
    @ResponseBody
    List<Event> getOdds(/*@RequestParam String apiKey*/
            @PathVariable String sportKey,
            @RequestParam String regions,
            @RequestParam(required = false) String markets,
            @RequestParam(required = false) String dateFormat,
            @RequestParam(required = false) String oddsFormat,
            @RequestParam(required = false) String commenceTimeFrom,
            @RequestParam(required = false) String commenceTimeTo);

    @GetExchange(value = "/sports/{sportKey}/events/{eventId}/odds")
    @ResponseBody
    Event getEventOdds(/*@RequestParam String apiKey*/
            @PathVariable String sportKey,
            @PathVariable String eventId,
            @RequestParam String regions,
            @RequestParam(required = false) String markets,
            @RequestParam(required = false) String dateFormat,
            @RequestParam(required = false) String oddsFormat,
            @RequestParam(required = false) String bookmakers);


}
