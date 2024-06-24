package betapi;

import betapi.oddsapiservice.OddsApiService;
import betapi.oddsapiservice.model.Event;
import betapi.oddsapiservice.model.Sport;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Controller
public class BetApiController {
    
    private static final Logger log = LoggerFactory.getLogger(BetApiController.class);

    private final OddsApiService oddsApiService;

    @Autowired
    public BetApiController(OddsApiService oddsApiService) {
        //testing log level
        this.oddsApiService = oddsApiService;
    }

    @GetMapping("/getSports")
    @ResponseBody
    public List<Sport> getSports() {
        log.debug("Getting sports");
        return oddsApiService.getSports();
    }

    @GetMapping("/testHandicap")
    @ResponseBody
    public List<Event> getTestHandicap() {
        log.debug("Getting test handicap");
        return oddsApiService.getOdds(
                "basketball_nba",
                "eu",
                "spreads",
                null,
                null,
                null,
                null
        );
    }



}
