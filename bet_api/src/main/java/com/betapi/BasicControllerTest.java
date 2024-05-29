package com.betapi;

import com.betapi.oddsapiservice.OddsApiService;
import com.betapi.oddsapiservice.model.Event;
import com.betapi.oddsapiservice.model.Sport;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Controller
public class BasicControllerTest {
    
    private static final Logger log = LoggerFactory.getLogger(BasicControllerTest.class);
    

    private OddsApiService oddsApiService;

    @Autowired
    public BasicControllerTest(OddsApiService oddsApiService) {
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
