/**
 * NOTE: This class is auto generated by the swagger code generator program (3.0.57).
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */
package betapi.swagger.api;

import betapi.swagger.model.Event;
import betapi.swagger.model.Sport;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.enums.ParameterIn;
import io.swagger.v3.oas.annotations.media.ArraySchema;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import jakarta.validation.Valid;
import jakarta.validation.constraints.NotNull;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;


@jakarta.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2024-06-28T13:02:24.955337310Z[GMT]")
@Validated
public interface SportsApi {

    @Operation(summary = "Get events list", description = "Returns all available events.", tags = {})
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "List of all available events", content = @Content(mediaType = "application/json", array = @ArraySchema(schema = @Schema(implementation = Event.class)))),

            @ApiResponse(responseCode = "201", description = "There are no available events."),

            @ApiResponse(responseCode = "400", description = "Bad Request - The request parameters are invalid."),

            @ApiResponse(responseCode = "500", description = "Internal Server Error - An error occurred on the server.")})
    @RequestMapping(value = "/sports/getEvents",
            produces = {"application/json"},
            method = RequestMethod.GET)
    ResponseEntity<List<Event>> sportsGetEventsGet(@NotNull @Parameter(in = ParameterIn.QUERY, description = "The sport key of the events", required = true, schema = @Schema()) @Valid @RequestParam(value = "sportKey", required = true) String sportKey
            , @Parameter(in = ParameterIn.QUERY, description = "Filter to show games that commence on and after this parameter", schema = @Schema()) @Valid @RequestParam(value = "commenceTimeFrom", required = false) String commenceTimeFrom
            , @Parameter(in = ParameterIn.QUERY, description = "Filter to show games that commence on and before this parameter", schema = @Schema()) @Valid @RequestParam(value = "commenceTimeTo", required = false) String commenceTimeTo
    );


    @Operation(summary = "Get sport groups", description = "Returns all available sport groups.", tags = {})
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "List of all available sport groups", content = @Content(mediaType = "application/json", array = @ArraySchema(schema = @Schema(implementation = String.class)))),

            @ApiResponse(responseCode = "201", description = "There are no available groups."),

            @ApiResponse(responseCode = "400", description = "Bad Request - The request parameters are invalid."),

            @ApiResponse(responseCode = "500", description = "Internal Server Error - An error occurred on the server.")})
    @RequestMapping(value = "/sports/getSportGroups",
            produces = {"application/json"},
            method = RequestMethod.GET)
    ResponseEntity<List<String>> sportsGetSportGroupsGet(@Parameter(in = ParameterIn.QUERY, description = "If set to true, both in and out of season sports will be returned", schema = @Schema()) @Valid @RequestParam(value = "all", required = false) Boolean all
    );


    @Operation(summary = "Get sports list", description = "Returns all available sports.", tags = {})
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "List of all available sports", content = @Content(mediaType = "application/json", array = @ArraySchema(schema = @Schema(implementation = Sport.class)))),

            @ApiResponse(responseCode = "201", description = "There are no available sports."),

            @ApiResponse(responseCode = "400", description = "Bad Request - The request parameters are invalid."),

            @ApiResponse(responseCode = "500", description = "Internal Server Error - An error occurred on the server.")})
    @RequestMapping(value = "/sports/getSports",
            produces = {"application/json"},
            method = RequestMethod.GET)
    ResponseEntity<List<Sport>> sportsGetSportsGet(@Parameter(in = ParameterIn.QUERY, description = "The sport group name", schema = @Schema()) @Valid @RequestParam(value = "groupName", required = false) String groupName
            , @Parameter(in = ParameterIn.QUERY, description = "If set to true, both in and out of season sports will be returned", schema = @Schema()) @Valid @RequestParam(value = "all", required = false) Boolean all
    );

}

