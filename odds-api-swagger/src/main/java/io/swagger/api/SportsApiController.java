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
                ZonedDateTime.parse(dateTime);
                return false;
            } catch (DateTimeParseException ex) {
                return true;
            }
        }
    }

    public ResponseEntity<List<Event>> sportsGetEventsGet(
            @NotNull @Parameter(in = ParameterIn.QUERY, description = "The sport key of the events", required = true, schema = @Schema()) @Valid @RequestParam(value = "sportKey", required = true) String sportKey,
            @Parameter(in = ParameterIn.QUERY, description = "Filter to show games that commence on and after this parameter", schema = @Schema()) @Valid @RequestParam(value = "commenceTimeFrom", required = false) String commenceTimeFrom,
            @Parameter(in = ParameterIn.QUERY, description = "Filter to show games that commence on and before this parameter", schema = @Schema()) @Valid @RequestParam(value = "commenceTimeTo", required = false) String commenceTimeTo
    ) {
        log.info("Received sportsGetEventsGet request with sportKey: {}, commenceTimeFrom: {}, commenceTimeTo: {}", sportKey, commenceTimeFrom, commenceTimeTo);

        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            // Validate sportKey
            if (sportKey == null || sportKey.trim().isEmpty()) {
                log.warn("Bad request received with invalid sportKey");
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }

            // Validate commenceTimeFrom and commenceTimeTo (optional)
            if (commenceTimeFrom != null && isValidDateTime(commenceTimeFrom)) {
                log.warn("Bad request received with invalid commenceTimeFrom: {}", commenceTimeFrom);
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }
            if (commenceTimeTo != null && isValidDateTime(commenceTimeTo)) {
                log.warn("Bad request received with invalid commenceTimeTo: {}", commenceTimeTo);
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }

            try {
                List<Event> events = oddsApiService.getEvents(sportKey, null, null, commenceTimeFrom, commenceTimeTo);
                if (events != null && !events.isEmpty()) {
                    log.debug("Returning {} events", events.size());
                    return new ResponseEntity<>(events, HttpStatus.OK);
                } else {
                    log.info("No events found for sportsGetEventsGet");
                    return new ResponseEntity<>(events, HttpStatus.NO_CONTENT);
                }
            } catch (IllegalArgumentException e) {
                log.error("Bad request received: {}", e.getMessage());
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }/*catch (AuthenticationException e) {
                return new ResponseEntity<>(HttpStatus.UNAUTHORIZED);
            } catch (AccessDeniedException e) {
                return new ResponseEntity<>(HttpStatus.FORBIDDEN);
            }*/ catch (Exception e) {
                log.error("Internal server error: {}", e.getMessage());
                return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
        }

        log.warn("Unsupported Accept header: {}", accept);
        return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
    }

    private List<String> getUniqueGroups(List<Sport> sports) {
        return sports.stream()
                .map(Sport::getGroup)
                .distinct()
                .collect(Collectors.toList());
    }

    public ResponseEntity<List<String>> sportsGetSportGroupsGet(
            @Parameter(in = ParameterIn.QUERY, description = "If set to true, both in and out of season sports will be returned", schema = @Schema()) @Valid @RequestParam(value = "all", required = false) Boolean all
    ) {
        log.info("Received sportsGetSportGroupsGet request with all: {}", all);

        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            try {
                List<Sport> sports = oddsApiService.getSports(all != null ? all.toString() : null);
                if (sports != null && !sports.isEmpty()) {
                    List<String> groups = getUniqueGroups(sports);
                    if (groups != null && !groups.isEmpty()) {
                        log.debug("Returning {} sport groups", groups.size());
                        return new ResponseEntity<>(groups, HttpStatus.OK);
                    } else {
                        log.info("No sport groups found for sportsGetSportGroupsGet");
                        return new ResponseEntity<>(new ArrayList<>(), HttpStatus.NO_CONTENT);
                    }
                } else {
                    log.info("No sports found for sportsGetSportGroupsGet");
                    return new ResponseEntity<>(new ArrayList<>(), HttpStatus.NO_CONTENT);
                }
            } catch (IllegalArgumentException e) {
                log.error("Bad request received: {}", e.getMessage());
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }/*catch (AuthenticationException e) {
                return new ResponseEntity<>(HttpStatus.UNAUTHORIZED);
            } catch (AccessDeniedException e) {
                return new ResponseEntity<>(HttpStatus.FORBIDDEN);
            }*/ catch (Exception e) {
                log.error("Internal server error: {}", e.getMessage());
                return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
        }

        log.warn("Unsupported Accept header: {}", accept);
        return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
    }

    private List<Sport> filterByGroup(List<Sport> sports, String group) {
        if (group == null) return sports;
        return sports.stream()
                .filter(sport -> group.equals(sport.getGroup()))
                .collect(Collectors.toList());
    }

    public ResponseEntity<List<Sport>> sportsGetSportsGet(
            @Parameter(in = ParameterIn.QUERY, description = "The sport group name", schema = @Schema()) @Valid @RequestParam(value = "groupName", required = false) String groupName,
            @Parameter(in = ParameterIn.QUERY, description = "If set to true, both in and out of season sports will be returned", schema = @Schema()) @Valid @RequestParam(value = "all", required = false) Boolean all
    ) {
        log.info("Received sportsGetSportsGet request with groupName: {}, all: {}", groupName, all);

        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            // Validate groupName (optional)
            if (groupName != null && groupName.trim().isEmpty()) {
                log.warn("Bad request received with invalid groupName");
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }

            try {
                List<Sport> sports = oddsApiService.getSports(all != null ? all.toString() : null);
                if (sports != null && !sports.isEmpty()) {
                    List<Sport> sportFiltered = filterByGroup(sports, groupName);
                    if (sportFiltered != null && !sportFiltered.isEmpty()) {
                        log.debug("Returning {} sports", sportFiltered.size());
                        return new ResponseEntity<>(sportFiltered, HttpStatus.OK);
                    } else {
                        log.info("No sports found for sportsGetSportsGet");
                        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
                    }
                } else {
                    log.info("No sports found for sportsGetSportsGet");
                    return new ResponseEntity<>(HttpStatus.NO_CONTENT);
                }
            } catch (IllegalArgumentException e) {
                log.error("Bad request received: {}", e.getMessage());
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }/*catch (AuthenticationException e) {
                return new ResponseEntity<>(HttpStatus.UNAUTHORIZED);
            } catch (AccessDeniedException e) {
                return new ResponseEntity<>(HttpStatus.FORBIDDEN);
            }*/ catch (Exception e) {
                log.error("Internal server error: {}", e.getMessage());
                return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
        }

        log.warn("Unsupported Accept header: {}", accept);
        return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
    }

}
