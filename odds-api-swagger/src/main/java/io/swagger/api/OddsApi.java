/**
 * NOTE: This class is auto generated by the swagger code generator program (3.0.57).
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */
package io.swagger.api;

import io.swagger.model.Odds;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.enums.ParameterIn;
import io.swagger.v3.oas.annotations.media.ArraySchema;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import jakarta.validation.Valid;
import jakarta.validation.constraints.NotNull;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@jakarta.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2024-06-24T10:03:13.459259793Z[GMT]")
@Validated
public interface OddsApi {

    @Operation(summary = "Get head-to-head odds", description = "Returns the top 'X' head-to-head odds for a specific event.", security = {
            @SecurityRequirement(name = "ApiKeyAuth")})
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "List of the top 'X' head-to-head odds", content = @Content(mediaType = "application/json", array = @ArraySchema(schema = @Schema(implementation = Odds.class)))),

            @ApiResponse(responseCode = "201", description = "There are no available head-to-head odds."),

            @ApiResponse(responseCode = "400", description = "Bad Request - The request parameters are invalid."),

            @ApiResponse(responseCode = "500", description = "Internal Server Error - An error occurred on the server.")})
    @RequestMapping(value = "/odds/head2head",
            produces = {"application/json"},
            method = RequestMethod.GET)
    ResponseEntity<List<Odds>> oddsHead2headGet(@NotNull @Parameter(in = ParameterIn.QUERY, description = "ID of the event", required = true, schema = @Schema()) @Valid @RequestParam(value = "eventId") String eventId
            , @NotNull @Parameter(in = ParameterIn.QUERY, description = "The sport key of the event", required = true, schema = @Schema()) @Valid @RequestParam(value = "sportKey") String sportKey
            , @Parameter(in = ParameterIn.QUERY, description = "Comma-separated list of regions to get odds for (e.g., \"us,uk,eu\")", schema = @Schema(defaultValue = "eu,uk")) @Valid @RequestParam(value = "regions", required = false, defaultValue = "eu,uk") String regions
    );


    @Operation(summary = "Get head-to-head handicap (spread) odds", description = "Returns the top 'X' head-to-head handicap odds for a specific event.", security = {
            @SecurityRequirement(name = "ApiKeyAuth")})
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "List of the top 'X' head-to-head handicap odds", content = @Content(mediaType = "application/json", array = @ArraySchema(schema = @Schema(implementation = Odds.class)))),

            @ApiResponse(responseCode = "201", description = "There are no available head-to-head handicap (spread) odds."),

            @ApiResponse(responseCode = "400", description = "Bad Request - The request parameters are invalid."),

            @ApiResponse(responseCode = "500", description = "Internal Server Error - An error occurred on the server.")})
    @RequestMapping(value = "/odds/spreads",
            produces = {"application/json"},
            method = RequestMethod.GET)
    ResponseEntity<List<Odds>> oddsSpreadsGet(@NotNull @Parameter(in = ParameterIn.QUERY, description = "ID of the event", required = true, schema = @Schema()) @Valid @RequestParam(value = "eventId") String eventId
            , @NotNull @Parameter(in = ParameterIn.QUERY, description = "The sport key of the event", required = true, schema = @Schema()) @Valid @RequestParam(value = "sportKey") String sportKey
            , @Parameter(in = ParameterIn.QUERY, description = "Comma-separated list of regions to get odds for (e.g., \"us,uk,eu\")", schema = @Schema(defaultValue = "eu,uk")) @Valid @RequestParam(value = "regions", required = false, defaultValue = "eu,uk") String regions
    );

}

