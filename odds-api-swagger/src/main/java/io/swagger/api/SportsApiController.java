package io.swagger.api;

import betapi.oddsapiservice.OddsApiService;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.swagger.model.Event;
import io.swagger.model.Sport;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.enums.ParameterIn;
import io.swagger.v3.oas.annotations.media.Schema;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;
import javax.validation.Valid;
import javax.validation.constraints.NotNull;
import java.util.List;
import java.util.stream.Collectors;

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2024-06-28T09:35:20.064601790Z[GMT]")
@RestController
public class SportsApiController implements SportsApi {

    private static final Logger log = LoggerFactory.getLogger(SportsApiController.class);

    private final HttpServletRequest request;

    private final OddsApiService oddsApiService;

    @org.springframework.beans.factory.annotation.Autowired
    public SportsApiController(HttpServletRequest request, OddsApiService oddsApiService) {
        this.request = request;
        this.oddsApiService = oddsApiService;
    }

    public ResponseEntity<List<Event>> sportsGetEventsGet(@NotNull @Parameter(in = ParameterIn.QUERY, description = "The sport key of the events" ,required=true,schema=@Schema()) @Valid @RequestParam(value = "sportKey", required = true) String sportKey
            ,@Parameter(in = ParameterIn.QUERY, description = "Filter to show games that commence on and after this parameter" ,schema=@Schema()) @Valid @RequestParam(value = "commenceTimeFrom", required = false) String commenceTimeFrom
            ,@Parameter(in = ParameterIn.QUERY, description = "Filter to show games that commence on and before this parameter" ,schema=@Schema()) @Valid @RequestParam(value = "commenceTimeTo", required = false) String commenceTimeTo
    ) {
        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            List<Event> events = oddsApiService.getEvents(sportKey, null, null, commenceTimeFrom, commenceTimeTo);
        }

        return new ResponseEntity<List<Event>>(HttpStatus.NOT_IMPLEMENTED);
    }


    private List<String> getUniqueGroups(List<Sport> sports) {
        return sports.stream()
                .map(Sport::getGroup)
                .distinct()
                .collect(Collectors.toList());
    }

    public ResponseEntity<List<String>> sportsGetSportGroupsGet(@Parameter(in = ParameterIn.QUERY, description = "If set to true, both in and out of season sports will be returned", schema = @Schema()) @Valid @RequestParam(value = "all", required = false) Boolean all) {
        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            List<Sport> sports = oddsApiService.getSports(all);
            if (sports != null && !sports.isEmpty()) {
                return new ResponseEntity<List<String>>(getUniqueGroups(sports), HttpStatus.OK);
            } else {
                return new ResponseEntity<List<String>>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
        }

        return new ResponseEntity<List<String>>(HttpStatus.NOT_IMPLEMENTED);
    }

    private List<Sport> filterByGroup(List<Sport> sports, String group) {
        return sports.stream()
                .filter(sport -> group.equals(sport.getGroup()))
                .collect(Collectors.toList());
    }

    public ResponseEntity<List<Sport>> sportsGetSportsGet(@Parameter(in = ParameterIn.QUERY, description = "The sport group name", schema = @Schema()) @Valid @RequestParam(value = "groupName", required = false) String groupName
            , @Parameter(in = ParameterIn.QUERY, description = "If set to true, both in and out of season sports will be returned", schema = @Schema()) @Valid @RequestParam(value = "all", required = false) Boolean all
    ) {
        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            List<Sport> sports = oddsApiService.getSports(all);
            if (sports != null && !sports.isEmpty()) {
                List<Sport> sportFiltered = filterByGroup(sports, groupName);
                if (sportFiltered != null && !sportFiltered.isEmpty()) {
                    return new ResponseEntity<List<Sport>>(sportFiltered, HttpStatus.OK);
                }
                return new ResponseEntity<List<Sport>>(HttpStatus.INTERNAL_SERVER_ERROR);
            } else {
                return new ResponseEntity<List<Sport>>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
        }

        return new ResponseEntity<List<Sport>>(HttpStatus.NOT_IMPLEMENTED);
    }

}
