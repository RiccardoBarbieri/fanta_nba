package io.swagger.api;

import betapi.oddsapiservice.OddsApiService;
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

import jakarta.servlet.http.HttpServletRequest;
import jakarta.validation.Valid;
import jakarta.validation.constraints.NotNull;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@jakarta.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2024-06-28T09:35:20.064601790Z[GMT]")
@RestController
public class SportsApiController implements SportsApi {

    private static final Logger log = LoggerFactory.getLogger(SportsApiController.class);
    private static final String IS08601_DATEFORMAT = "yyyy-MM-dd'T'HH:mm:ssX";

    private final HttpServletRequest request;

    private final OddsApiService oddsApiService;

    @org.springframework.beans.factory.annotation.Autowired
    public SportsApiController(HttpServletRequest request, OddsApiService oddsApiService) {
        this.request = request;
        this.oddsApiService = oddsApiService;
    }

    private boolean isValidDateTime(String dateTime) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern(IS08601_DATEFORMAT);
        try {
            ZonedDateTime.parse(dateTime, formatter);
            return false;
        } catch (DateTimeParseException e) {
            try {
                ZonedDateTime parsedDate = ZonedDateTime.parse(dateTime);
                return false;
            } catch (DateTimeParseException ex) {
                return true;
            }
        }
    }

    public ResponseEntity<List<Event>> sportsGetEventsGet(@NotNull @Parameter(in = ParameterIn.QUERY, description = "The sport key of the events", required = true, schema = @Schema()) @Valid @RequestParam(value = "sportKey", required = true) String sportKey
            , @Parameter(in = ParameterIn.QUERY, description = "Filter to show games that commence on and after this parameter", schema = @Schema()) @Valid @RequestParam(value = "commenceTimeFrom", required = false) String commenceTimeFrom
            , @Parameter(in = ParameterIn.QUERY, description = "Filter to show games that commence on and before this parameter", schema = @Schema()) @Valid @RequestParam(value = "commenceTimeTo", required = false) String commenceTimeTo
    ) {
        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            // Validate sportKey
            if (sportKey == null || sportKey.trim().isEmpty()) {
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }

            // Validate commenceTimeFrom and commenceTimeTo (optional)
            if (commenceTimeFrom != null && isValidDateTime(commenceTimeFrom)) {
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }
            if (commenceTimeTo != null && isValidDateTime(commenceTimeTo)) {
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }

            try {
                List<Event> events = oddsApiService.getEvents(null, sportKey, null, null, commenceTimeFrom, commenceTimeTo);
                if (events != null && !events.isEmpty()) {
                    return new ResponseEntity<>(events, HttpStatus.OK);
                } else {
                    return new ResponseEntity<>(events, HttpStatus.NO_CONTENT);
                }
            } catch (IllegalArgumentException e) {
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }
            /*catch (AuthenticationException e) {
                return new ResponseEntity<>(HttpStatus.UNAUTHORIZED);
            } catch (AccessDeniedException e) {
                return new ResponseEntity<>(HttpStatus.FORBIDDEN);
            }*/ catch (Exception e) {
                return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
        }
        return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
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
            try {
                List<Sport> sports = oddsApiService.getSports(null, all.toString());
                if (sports != null && !sports.isEmpty()) {
                    List<String> groups = getUniqueGroups(sports);
                    if (groups != null && !groups.isEmpty()) {
                        return new ResponseEntity<List<String>>(groups, HttpStatus.OK);
                    } else {
                        return new ResponseEntity<>(new ArrayList<>(), HttpStatus.NO_CONTENT);
                    }
                } else {
                    return new ResponseEntity<>(new ArrayList<>(), HttpStatus.NO_CONTENT);
                }
            } catch (IllegalArgumentException e) {
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }
            /*catch (AuthenticationException e) {
                return new ResponseEntity<>(HttpStatus.UNAUTHORIZED);
            } catch (AccessDeniedException e) {
                return new ResponseEntity<>(HttpStatus.FORBIDDEN);
            }*/ catch (Exception e) {
                return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
        }
        return new ResponseEntity<List<String>>(HttpStatus.BAD_REQUEST);
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
            // Validate groupName (optional)
            if (groupName != null && groupName.trim().isEmpty()) {
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }

            try {
                List<Sport> sports = oddsApiService.getSports(null, all.toString());
                if (sports != null && !sports.isEmpty()) {
                    List<Sport> sportFiltered = filterByGroup(sports, groupName);
                    if (sportFiltered != null && !sportFiltered.isEmpty()) {
                        return new ResponseEntity<>(sportFiltered, HttpStatus.OK);
                    } else {
                        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
                    }
                } else {
                    return new ResponseEntity<>(HttpStatus.NO_CONTENT);
                }
            } catch (IllegalArgumentException e) {
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }
            /*catch (AuthenticationException e) {
                return new ResponseEntity<>(HttpStatus.UNAUTHORIZED);
            } catch (AccessDeniedException e) {
                return new ResponseEntity<>(HttpStatus.FORBIDDEN);
            }*/ catch (Exception e) {
                return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
        }
        return new ResponseEntity<List<Sport>>(HttpStatus.BAD_REQUEST);
    }

}
