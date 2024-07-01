package io.swagger.api;

import betapi.database.ScheduleBookmakers;
import betapi.oddsapiservice.OddsApiService;
import io.swagger.model.Bookmaker;
import io.swagger.model.Market;
import io.swagger.model.Odds;
import io.swagger.model.Outcome;
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
import java.io.IOException;
import java.math.BigDecimal;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@jakarta.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2024-06-24T10:03:13.459259793Z[GMT]")
@RestController
public class OddsApiController implements OddsApi {

    private static final Logger log = LoggerFactory.getLogger(OddsApiController.class);

    private final HttpServletRequest request;

    private final OddsApiService oddsApiService;

    private final ScheduleBookmakers scheduleBookmakers;

    @org.springframework.beans.factory.annotation.Autowired
    public OddsApiController(HttpServletRequest request, OddsApiService oddsApiService, ScheduleBookmakers scheduleBookmakers) {
        this.request = request;
        this.oddsApiService = oddsApiService;
        this.scheduleBookmakers = scheduleBookmakers;
    }


    private static List<Odds> sortBookmakersByOdds(Odds odds) {
        // Copia profonda dell'oggetto Odds originale
        Odds oddsCopyForHomeTeam = deepCopyOdds(odds);
        Odds oddsCopyForAwayTeam = deepCopyOdds(odds);

        // Ordina i bookmakers per la squadra di casa
        List<Bookmaker> sortedByHomeTeam = oddsCopyForHomeTeam.getBookmakers().stream()
                .sorted((b1, b2) -> {
                    Float price1 = getPriceForTeam(b1, odds.getHomeTeam());
                    Float price2 = getPriceForTeam(b2, odds.getHomeTeam());
                    return price2.compareTo(price1); // Ordine decrescente
                })
                .collect(Collectors.toList());

        // Ordina i bookmakers per la squadra in trasferta
        List<Bookmaker> sortedByAwayTeam = oddsCopyForAwayTeam.getBookmakers().stream()
                .sorted((b1, b2) -> {
                    Float price1 = getPriceForTeam(b1, odds.getAwayTeam());
                    Float price2 = getPriceForTeam(b2, odds.getAwayTeam());
                    return price2.compareTo(price1); // Ordine decrescente
                })
                .collect(Collectors.toList());

        // Aggiorna le liste di bookmakers nelle copie delle Odds
        oddsCopyForHomeTeam.setBookmakers(sortedByHomeTeam);
        oddsCopyForAwayTeam.setBookmakers(sortedByAwayTeam);

        // Ritorna entrambe le copie
        return Arrays.asList(oddsCopyForHomeTeam, oddsCopyForAwayTeam);
    }

    private static Float getPriceForTeam(Bookmaker bookmaker, String team) {
        return bookmaker.getMarkets().stream()
                //.filter(market -> market.getKey().equals("h2h"))
                .flatMap(market -> market.getOutcomes().stream())
                .filter(outcome -> outcome.getName().equals(team))
                .map(Outcome::getPrice)
                .findFirst()
                .orElse(Float.MIN_VALUE); // Valore predefinito nel caso in cui non si trovi l'outcome
    }

    private static Odds deepCopyOdds(Odds original) {
        // Implementazione della copia profonda
        Odds copy = new Odds();
        copy.setId(original.getId());
        copy.setSportKey(original.getSportKey());
        copy.setSportTitle(original.getSportTitle());
        copy.setCommenceTime(original.getCommenceTime());
        copy.setHomeTeam(original.getHomeTeam());
        copy.setAwayTeam(original.getAwayTeam());
        copy.setBookmakers(original.getBookmakers().stream()
                .map(OddsApiController::deepCopyBookmaker)
                .collect(Collectors.toList()));
        return copy;
    }

    private static Bookmaker deepCopyBookmaker(Bookmaker original) {
        Bookmaker copy = new Bookmaker();
        copy.setKey(original.getKey());
        copy.setTitle(original.getTitle());
        copy.setUrl(original.getUrl());
        copy.setLastUpdate(original.getLastUpdate());
        copy.setMarkets(original.getMarkets().stream()
                .map(OddsApiController::deepCopyMarket)
                .collect(Collectors.toList()));
        return copy;
    }

    private static Market deepCopyMarket(Market original) {
        Market copy = new Market();
        copy.setKey(original.getKey());
        copy.setOutcomes(original.getOutcomes().stream()
                .map(OddsApiController::deepCopyOutcome)
                .collect(Collectors.toList()));
        return copy;
    }

    private static Outcome deepCopyOutcome(Outcome original) {
        Outcome copy = new Outcome();
        copy.setName(original.getName());
        copy.setPrice(original.getPrice());
        copy.setPoint(original.getPoint());
        copy.setDescription(original.getDescription());
        return copy;
    }

    private List<Odds> getEventOdds(String sportKey, String eventId, String regions, String market){
        Odds odds = oddsApiService.getEventOdds(sportKey, eventId, regions, market, null, null, null, null, null, null);

        List<betapi.database.documents.Bookmaker> bookmakersList;
        try {
            bookmakersList = scheduleBookmakers.getBookmakers();
            Map<String, String> bookmakerUrlMap = bookmakersList.stream()
                    .collect(Collectors.toMap(b -> b.getKey(), b -> b.getUrl()));

            for (Bookmaker b : odds.getBookmakers()) {
                String url = bookmakerUrlMap.get(b.getKey());
                if (url != null) {
                    b.setUrl(url);
                }
            }
        } catch (IOException e) {
            log.error("Failed to fetch bookmakers", e);
        }

        return sortBookmakersByOdds(odds);
    }

    private boolean parameterValidation(String sportKey, String eventId, String regions) {
        // Validazione dei parametri non nulli o vuoti
        if (sportKey == null || sportKey.trim().isEmpty() ||
                eventId == null || eventId.trim().isEmpty()) {
            return true;
        }

        // Validazione delle regioni
        if (regions != null && !regions.trim().isEmpty()) {
            List<String> validRegions = Arrays.asList("eu", "uk", "us", "au");
            List<String> inputRegions = Arrays.asList(regions.split(","));
            if (!inputRegions.stream().allMatch(validRegions::contains)) {
                return true;
            }
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
                List<Odds> odds = getEventOdds(sportKey, eventId, regions, "spreads");
                if (odds != null && !odds.isEmpty()) {
                    return new ResponseEntity<List<Odds>>(odds, HttpStatus.OK);
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
                if (odds != null && !odds.isEmpty()) {
                    return new ResponseEntity<List<Odds>>(odds, HttpStatus.OK);
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
