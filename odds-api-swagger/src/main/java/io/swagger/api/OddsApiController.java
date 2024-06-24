package io.swagger.api;

import java.math.BigDecimal;
import io.swagger.model.Odds;
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
public class OddsApiController implements OddsApi {

    private static final Logger log = LoggerFactory.getLogger(OddsApiController.class);

    private final ObjectMapper objectMapper;

    private final HttpServletRequest request;

    @org.springframework.beans.factory.annotation.Autowired
    public OddsApiController(ObjectMapper objectMapper, HttpServletRequest request) {
        this.objectMapper = objectMapper;
        this.request = request;
    }

    public ResponseEntity<List<Odds>> oddsHead2headGet(@NotNull @Parameter(in = ParameterIn.QUERY, description = "ID of the event" ,required=true,schema=@Schema()) @Valid @RequestParam(value = "eventId", required = true) String eventId
,@NotNull @Parameter(in = ParameterIn.QUERY, description = "The sport key of the event" ,required=true,schema=@Schema()) @Valid @RequestParam(value = "sportKey", required = true) String sportKey
,@Parameter(in = ParameterIn.QUERY, description = "Comma-separated list of regions to get odds for (e.g., \"us,uk,eu\")" ,schema=@Schema( defaultValue="eu,uk")) @Valid @RequestParam(value = "regions", required = false, defaultValue="eu,uk") String regions
,@Parameter(in = ParameterIn.QUERY, description = "Number of records to retrieve" ,schema=@Schema( defaultValue="1")) @Valid @RequestParam(value = "records", required = false, defaultValue="1") BigDecimal records
) {
        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            try {
                return new ResponseEntity<List<Odds>>(objectMapper.readValue("[ {\n  \"bookmakers\" : [ {\n    \"markets\" : [ {\n      \"outcomes\" : [ {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      }, {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      } ],\n      \"last_update\" : \"2023-10-10T12:10:29Z\",\n      \"key\" : \"h2h\"\n    }, {\n      \"outcomes\" : [ {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      }, {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      } ],\n      \"last_update\" : \"2023-10-10T12:10:29Z\",\n      \"key\" : \"h2h\"\n    } ],\n    \"last_update\" : \"2023-10-10T12:10:29Z\",\n    \"title\" : \"DraftKings\",\n    \"url\" : \"https://www.draftkings.com\",\n    \"key\" : \"draftkings\"\n  }, {\n    \"markets\" : [ {\n      \"outcomes\" : [ {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      }, {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      } ],\n      \"last_update\" : \"2023-10-10T12:10:29Z\",\n      \"key\" : \"h2h\"\n    }, {\n      \"outcomes\" : [ {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      }, {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      } ],\n      \"last_update\" : \"2023-10-10T12:10:29Z\",\n      \"key\" : \"h2h\"\n    } ],\n    \"last_update\" : \"2023-10-10T12:10:29Z\",\n    \"title\" : \"DraftKings\",\n    \"url\" : \"https://www.draftkings.com\",\n    \"key\" : \"draftkings\"\n  } ],\n  \"event\" : {\n    \"sport_key\" : \"americanfootball_nfl\",\n    \"id\" : \"e912304de2b2ce35b473ce2ecd3d1502\",\n    \"home_team\" : \"Houston Texans\",\n    \"sport_title\" : \"NFL\",\n    \"commence_time\" : \"2023-10-11T23:10:00Z\",\n    \"away_team\" : \"Kansas City Chiefs\"\n  }\n}, {\n  \"bookmakers\" : [ {\n    \"markets\" : [ {\n      \"outcomes\" : [ {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      }, {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      } ],\n      \"last_update\" : \"2023-10-10T12:10:29Z\",\n      \"key\" : \"h2h\"\n    }, {\n      \"outcomes\" : [ {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      }, {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      } ],\n      \"last_update\" : \"2023-10-10T12:10:29Z\",\n      \"key\" : \"h2h\"\n    } ],\n    \"last_update\" : \"2023-10-10T12:10:29Z\",\n    \"title\" : \"DraftKings\",\n    \"url\" : \"https://www.draftkings.com\",\n    \"key\" : \"draftkings\"\n  }, {\n    \"markets\" : [ {\n      \"outcomes\" : [ {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      }, {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      } ],\n      \"last_update\" : \"2023-10-10T12:10:29Z\",\n      \"key\" : \"h2h\"\n    }, {\n      \"outcomes\" : [ {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      }, {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      } ],\n      \"last_update\" : \"2023-10-10T12:10:29Z\",\n      \"key\" : \"h2h\"\n    } ],\n    \"last_update\" : \"2023-10-10T12:10:29Z\",\n    \"title\" : \"DraftKings\",\n    \"url\" : \"https://www.draftkings.com\",\n    \"key\" : \"draftkings\"\n  } ],\n  \"event\" : {\n    \"sport_key\" : \"americanfootball_nfl\",\n    \"id\" : \"e912304de2b2ce35b473ce2ecd3d1502\",\n    \"home_team\" : \"Houston Texans\",\n    \"sport_title\" : \"NFL\",\n    \"commence_time\" : \"2023-10-11T23:10:00Z\",\n    \"away_team\" : \"Kansas City Chiefs\"\n  }\n} ]", List.class), HttpStatus.NOT_IMPLEMENTED);
            } catch (IOException e) {
                log.error("Couldn't serialize response for content type application/json", e);
                return new ResponseEntity<List<Odds>>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
        }

        return new ResponseEntity<List<Odds>>(HttpStatus.NOT_IMPLEMENTED);
    }

    public ResponseEntity<List<Odds>> oddsSpreadsGet(@NotNull @Parameter(in = ParameterIn.QUERY, description = "ID of the event" ,required=true,schema=@Schema()) @Valid @RequestParam(value = "eventId", required = true) String eventId
,@NotNull @Parameter(in = ParameterIn.QUERY, description = "The sport key of the event" ,required=true,schema=@Schema()) @Valid @RequestParam(value = "sportKey", required = true) String sportKey
,@Parameter(in = ParameterIn.QUERY, description = "Comma-separated list of regions to get odds for (e.g., \"us,uk,eu\")" ,schema=@Schema( defaultValue="eu,uk")) @Valid @RequestParam(value = "regions", required = false, defaultValue="eu,uk") String regions
,@Parameter(in = ParameterIn.QUERY, description = "Number of records to retrieve" ,schema=@Schema( defaultValue="1")) @Valid @RequestParam(value = "records", required = false, defaultValue="1") BigDecimal records
) {
        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            try {
                return new ResponseEntity<List<Odds>>(objectMapper.readValue("[ {\n  \"bookmakers\" : [ {\n    \"markets\" : [ {\n      \"outcomes\" : [ {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      }, {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      } ],\n      \"last_update\" : \"2023-10-10T12:10:29Z\",\n      \"key\" : \"h2h\"\n    }, {\n      \"outcomes\" : [ {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      }, {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      } ],\n      \"last_update\" : \"2023-10-10T12:10:29Z\",\n      \"key\" : \"h2h\"\n    } ],\n    \"last_update\" : \"2023-10-10T12:10:29Z\",\n    \"title\" : \"DraftKings\",\n    \"url\" : \"https://www.draftkings.com\",\n    \"key\" : \"draftkings\"\n  }, {\n    \"markets\" : [ {\n      \"outcomes\" : [ {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      }, {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      } ],\n      \"last_update\" : \"2023-10-10T12:10:29Z\",\n      \"key\" : \"h2h\"\n    }, {\n      \"outcomes\" : [ {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      }, {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      } ],\n      \"last_update\" : \"2023-10-10T12:10:29Z\",\n      \"key\" : \"h2h\"\n    } ],\n    \"last_update\" : \"2023-10-10T12:10:29Z\",\n    \"title\" : \"DraftKings\",\n    \"url\" : \"https://www.draftkings.com\",\n    \"key\" : \"draftkings\"\n  } ],\n  \"event\" : {\n    \"sport_key\" : \"americanfootball_nfl\",\n    \"id\" : \"e912304de2b2ce35b473ce2ecd3d1502\",\n    \"home_team\" : \"Houston Texans\",\n    \"sport_title\" : \"NFL\",\n    \"commence_time\" : \"2023-10-11T23:10:00Z\",\n    \"away_team\" : \"Kansas City Chiefs\"\n  }\n}, {\n  \"bookmakers\" : [ {\n    \"markets\" : [ {\n      \"outcomes\" : [ {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      }, {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      } ],\n      \"last_update\" : \"2023-10-10T12:10:29Z\",\n      \"key\" : \"h2h\"\n    }, {\n      \"outcomes\" : [ {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      }, {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      } ],\n      \"last_update\" : \"2023-10-10T12:10:29Z\",\n      \"key\" : \"h2h\"\n    } ],\n    \"last_update\" : \"2023-10-10T12:10:29Z\",\n    \"title\" : \"DraftKings\",\n    \"url\" : \"https://www.draftkings.com\",\n    \"key\" : \"draftkings\"\n  }, {\n    \"markets\" : [ {\n      \"outcomes\" : [ {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      }, {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      } ],\n      \"last_update\" : \"2023-10-10T12:10:29Z\",\n      \"key\" : \"h2h\"\n    }, {\n      \"outcomes\" : [ {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      }, {\n        \"price\" : 2.23,\n        \"name\" : \"Houston Texans\",\n        \"description\" : \"description\",\n        \"point\" : 20.5\n      } ],\n      \"last_update\" : \"2023-10-10T12:10:29Z\",\n      \"key\" : \"h2h\"\n    } ],\n    \"last_update\" : \"2023-10-10T12:10:29Z\",\n    \"title\" : \"DraftKings\",\n    \"url\" : \"https://www.draftkings.com\",\n    \"key\" : \"draftkings\"\n  } ],\n  \"event\" : {\n    \"sport_key\" : \"americanfootball_nfl\",\n    \"id\" : \"e912304de2b2ce35b473ce2ecd3d1502\",\n    \"home_team\" : \"Houston Texans\",\n    \"sport_title\" : \"NFL\",\n    \"commence_time\" : \"2023-10-11T23:10:00Z\",\n    \"away_team\" : \"Kansas City Chiefs\"\n  }\n} ]", List.class), HttpStatus.NOT_IMPLEMENTED);
            } catch (IOException e) {
                log.error("Couldn't serialize response for content type application/json", e);
                return new ResponseEntity<List<Odds>>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
        }

        return new ResponseEntity<List<Odds>>(HttpStatus.NOT_IMPLEMENTED);
    }

}
