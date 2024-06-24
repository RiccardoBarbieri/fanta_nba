package io.swagger.api;

import io.swagger.model.Event;
import io.swagger.model.Sport;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.enums.ParameterIn;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.media.ArraySchema;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.CookieValue;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import javax.validation.Valid;
import javax.validation.constraints.*;
import javax.servlet.http.HttpServletRequest;
import java.io.IOException;
import java.util.List;
import java.util.Map;

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2024-06-24T10:03:13.459259793Z[GMT]")
@RestController
public class SportsApiController implements SportsApi {

    private static final Logger log = LoggerFactory.getLogger(SportsApiController.class);

    private final ObjectMapper objectMapper;

    private final HttpServletRequest request;

    @org.springframework.beans.factory.annotation.Autowired
    public SportsApiController(ObjectMapper objectMapper, HttpServletRequest request) {
        this.objectMapper = objectMapper;
        this.request = request;
    }

    public ResponseEntity<List<Event>> sportsGetEventsGet(@NotNull @Parameter(in = ParameterIn.QUERY, description = "The sport key of the event" ,required=true,schema=@Schema()) @Valid @RequestParam(value = "sportKey", required = true) String sportKey
,@Parameter(in = ParameterIn.QUERY, description = "Comma-separated list of regions to get odds for (e.g., \"us,uk,eu\")" ,schema=@Schema( defaultValue="eu,uk")) @Valid @RequestParam(value = "regions", required = false, defaultValue="eu,uk") String regions
) {
        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            try {
                return new ResponseEntity<List<Event>>(objectMapper.readValue("[ {\n  \"sport_key\" : \"americanfootball_nfl\",\n  \"id\" : \"e912304de2b2ce35b473ce2ecd3d1502\",\n  \"home_team\" : \"Houston Texans\",\n  \"sport_title\" : \"NFL\",\n  \"commence_time\" : \"2023-10-11T23:10:00Z\",\n  \"away_team\" : \"Kansas City Chiefs\"\n}, {\n  \"sport_key\" : \"americanfootball_nfl\",\n  \"id\" : \"e912304de2b2ce35b473ce2ecd3d1502\",\n  \"home_team\" : \"Houston Texans\",\n  \"sport_title\" : \"NFL\",\n  \"commence_time\" : \"2023-10-11T23:10:00Z\",\n  \"away_team\" : \"Kansas City Chiefs\"\n} ]", List.class), HttpStatus.NOT_IMPLEMENTED);
            } catch (IOException e) {
                log.error("Couldn't serialize response for content type application/json", e);
                return new ResponseEntity<List<Event>>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
        }

        return new ResponseEntity<List<Event>>(HttpStatus.NOT_IMPLEMENTED);
    }

    public ResponseEntity<List<Sport>> sportsGetSportsGet() {
        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            try {
                return new ResponseEntity<List<Sport>>(objectMapper.readValue("[ {\n  \"has_outrights\" : false,\n  \"active\" : true,\n  \"description\" : \"US Football\",\n  \"title\" : \"NFL\",\n  \"key\" : \"americanfootball_nfl\",\n  \"group\" : \"American Football\"\n}, {\n  \"has_outrights\" : false,\n  \"active\" : true,\n  \"description\" : \"US Football\",\n  \"title\" : \"NFL\",\n  \"key\" : \"americanfootball_nfl\",\n  \"group\" : \"American Football\"\n} ]", List.class), HttpStatus.NOT_IMPLEMENTED);
            } catch (IOException e) {
                log.error("Couldn't serialize response for content type application/json", e);
                return new ResponseEntity<List<Sport>>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
        }

        return new ResponseEntity<List<Sport>>(HttpStatus.NOT_IMPLEMENTED);
    }

}
