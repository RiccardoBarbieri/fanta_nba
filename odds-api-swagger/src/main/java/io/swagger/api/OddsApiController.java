package io.swagger.api;

import betapi.oddsapiservice.OddsApiService;
import io.swagger.model.Odds;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.enums.ParameterIn;
import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.validation.Valid;
import jakarta.validation.constraints.NotNull;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;

@jakarta.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2024-06-24T10:03:13.459259793Z[GMT]")
@RestController
public class OddsApiController implements OddsApi {

    private static final Logger log = LoggerFactory.getLogger(OddsApiController.class);

    private final HttpServletRequest request;

    private final OddsApiService oddsApiService;

    @org.springframework.beans.factory.annotation.Autowired
    public OddsApiController(HttpServletRequest request, OddsApiService oddsApiService) {
        this.request = request;
        this.oddsApiService = oddsApiService;
    }

    private List<Odds> getEventOdds(String sportKey, String eventId, String regions, String market) {
        log.debug("Fetching odds for sportKey: {}, eventId: {}, regions: {}, market: {}", sportKey, eventId, regions, market);

        Odds odds = oddsApiService.getEventOdds(sportKey, eventId, regions, market, null, null, null, null, null, null);

        try {
            OddsUtils.addBookmakersUrl(odds, regions);
        } catch (IOException e) {
            log.error("Failed to add bookmakers URL to odds: {}", e.getMessage());
            throw new RuntimeException(e);
        }

        List<Odds> sortedOdds = OddsUtils.sortBookmakersByOdds(odds);
        log.debug("Fetched and sorted odds successfully");

        return sortedOdds;
    }

    private boolean parameterValidation(String sportKey, String eventId, String regions) {
        if (sportKey == null || sportKey.trim().isEmpty() ||
                eventId == null || eventId.trim().isEmpty()) {
            log.warn("Invalid parameters provided: sportkey {} & eventId {}", sportKey, eventId);
            return false;
        }

        if (regions != null && !regions.trim().isEmpty()) {
            List<String> validRegions = Arrays.asList("eu", "uk", "us", "au");
            List<String> inputRegions = Arrays.asList(regions.split(","));
            boolean invalidRegions = !inputRegions.stream().allMatch(validRegions::contains);
            if (invalidRegions) {
                log.warn("Invalid regions provided: {}", regions);
            }
            return invalidRegions;
        }

        return false;
    }

    public ResponseEntity<List<Odds>> oddsHead2headGet(
            @NotNull @Parameter(in = ParameterIn.QUERY, description = "ID of the event", required = true, schema = @Schema()) @Valid @RequestParam(value = "eventId", required = true) String eventId,
            @NotNull @Parameter(in = ParameterIn.QUERY, description = "The sport key of the event", required = true, schema = @Schema()) @Valid @RequestParam(value = "sportKey", required = true) String sportKey,
            @Parameter(in = ParameterIn.QUERY, description = "Comma-separated list of regions to get odds for (e.g., \"us,uk,eu\")", schema = @Schema(defaultValue = "eu,uk")) @Valid @RequestParam(value = "regions", required = false, defaultValue = "eu,uk") String regions
    ) {
        log.info("Received oddsHead2headGet request with eventId: {}, sportKey: {}, regions: {}", eventId, sportKey, regions);

        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            if (parameterValidation(sportKey, eventId, regions)) {
                log.warn("Bad request received with invalid parameters");
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }
            try {
                List<Odds> odds = getEventOdds(sportKey, eventId, regions, "h2h");
                if (!odds.isEmpty()) {
                    log.debug("Returning {} odds records", odds.size());
                    return new ResponseEntity<>(odds, HttpStatus.OK);
                } else {
                    log.info("No content found for oddsHead2headGet");
                    return new ResponseEntity<>(odds, HttpStatus.NO_CONTENT);
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

    public ResponseEntity<List<Odds>> oddsSpreadsGet(
            @NotNull @Parameter(in = ParameterIn.QUERY, description = "ID of the event", required = true, schema = @Schema()) @Valid @RequestParam(value = "eventId", required = true) String eventId,
            @NotNull @Parameter(in = ParameterIn.QUERY, description = "The sport key of the event", required = true, schema = @Schema()) @Valid @RequestParam(value = "sportKey", required = true) String sportKey,
            @Parameter(in = ParameterIn.QUERY, description = "Comma-separated list of regions to get odds for (e.g., \"us,uk,eu\")", schema = @Schema(defaultValue = "eu,uk")) @Valid @RequestParam(value = "regions", required = false, defaultValue = "eu,uk") String regions
    ) {
        log.info("Received oddsSpreadsGet request with eventId: {}, sportKey: {}, regions: {}", eventId, sportKey, regions);

        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            if (parameterValidation(sportKey, eventId, regions)) {
                log.warn("Bad request received with invalid parameters");
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }
            try {
                List<Odds> odds = getEventOdds(sportKey, eventId, regions, "spreads");
                if (!odds.isEmpty()) {
                    log.debug("Returning {} odds records", odds.size());
                    return new ResponseEntity<>(odds, HttpStatus.OK);
                } else {
                    log.info("No content found for oddsSpreadsGet");
                    return new ResponseEntity<>(odds, HttpStatus.NO_CONTENT);
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
