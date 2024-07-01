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

    private List<Odds> getEventOdds(String sportKey, String eventId, String regions, String market){
        Odds odds = oddsApiService.getEventOdds(null, sportKey, eventId, regions, market, null, null, null, null, null, null);

        try {
            OddsUtils.addBookmakersUrl(odds, regions);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        return OddsUtils.sortBookmakersByOdds(odds);
    }

    private boolean parameterValidation(String sportKey, String eventId, String regions) {
        if (sportKey == null || sportKey.trim().isEmpty() ||
                eventId == null || eventId.trim().isEmpty()) {
            return true;
        }

        if (regions != null && !regions.trim().isEmpty()) {
            List<String> validRegions = Arrays.asList("eu", "uk", "us", "au");
            List<String> inputRegions = Arrays.asList(regions.split(","));
            return !inputRegions.stream().allMatch(validRegions::contains);
        }

        return false;
    }


    public ResponseEntity<List<Odds>> oddsHead2headGet(@NotNull @Parameter(in = ParameterIn.QUERY, description = "ID of the event", required = true, schema = @Schema()) @Valid @RequestParam(value = "eventId", required = true) String eventId
            , @NotNull @Parameter(in = ParameterIn.QUERY, description = "The sport key of the event", required = true, schema = @Schema()) @Valid @RequestParam(value = "sportKey", required = true) String sportKey
            , @Parameter(in = ParameterIn.QUERY, description = "Comma-separated list of regions to get odds for (e.g., \"us,uk,eu\")", schema = @Schema(defaultValue = "eu,uk")) @Valid @RequestParam(value = "regions", required = false, defaultValue = "eu,uk") String regions
    ) {
        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            if (parameterValidation(sportKey, eventId, regions)) {
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }
            try {
                List<Odds> odds = getEventOdds(sportKey, eventId, regions, "h2h");
                if (!odds.isEmpty()) {
                    return new ResponseEntity<>(odds, HttpStatus.OK);
                } else {
                    return new ResponseEntity<>(odds, HttpStatus.NO_CONTENT);
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

    public ResponseEntity<List<Odds>> oddsSpreadsGet(@NotNull @Parameter(in = ParameterIn.QUERY, description = "ID of the event", required = true, schema = @Schema()) @Valid @RequestParam(value = "eventId", required = true) String eventId
            , @NotNull @Parameter(in = ParameterIn.QUERY, description = "The sport key of the event", required = true, schema = @Schema()) @Valid @RequestParam(value = "sportKey", required = true) String sportKey
            , @Parameter(in = ParameterIn.QUERY, description = "Comma-separated list of regions to get odds for (e.g., \"us,uk,eu\")", schema = @Schema(defaultValue = "eu,uk")) @Valid @RequestParam(value = "regions", required = false, defaultValue = "eu,uk") String regions
    ) {
        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            if (parameterValidation(sportKey, eventId, regions)) {
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }
            try {
                List<Odds> odds = getEventOdds(sportKey, eventId, regions, "spreads");
                if (!odds.isEmpty()) {
                    return new ResponseEntity<>(odds, HttpStatus.OK);
                } else {
                    return new ResponseEntity<>(odds, HttpStatus.NO_CONTENT);
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

}
