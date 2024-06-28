package io.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;
import io.swagger.model.Outcome;
import io.swagger.v3.oas.annotations.media.Schema;
import java.util.ArrayList;
import java.util.List;
import org.threeten.bp.OffsetDateTime;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

// --Commented out by Inspection START (28/06/2024 17:27):
///**
// * Market
// */
//@Validated
//@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2024-06-24T10:03:13.459259793Z[GMT]")
//
//
//public class Market   {
//  /**
//   * The name of the odds market.
//   */
//  public enum KeyEnum {
//    H2H("h2h"),
//
//    SPREADS("spreads"),
//
//    TOTALS("totals"),
//
//    OUTRIGHTS("outrights");
//
//    private final String value;
//
//    KeyEnum(String value) {
//      this.value = value;
//    }
//
//    @Override
//    @JsonValue
//    public String toString() {
//      return String.valueOf(value);
//    }
//
//    @JsonCreator
//    public static KeyEnum fromValue(String text) {
//      for (KeyEnum b : KeyEnum.values()) {
//        if (String.valueOf(b.value).equals(text)) {
//          return b;
//        }
//      }
//      return null;
//    }
//  }
//  @JsonProperty("key")
//  private KeyEnum key = null;
//
// --Commented out by Inspection START (28/06/2024 17:27):
////  @JsonProperty("last_update")
////  private OffsetDateTime lastUpdate = null;
////
// --Commented out by Inspection STOP (28/06/2024 17:27)
//  @JsonProperty("outcomes")
//  @Valid
//  private List<Outcome> outcomes = null;
// --Commented out by Inspection START (28/06/2024 17:27):
////
////  public Market key(KeyEnum key) {
////    this.key = key;
// --Commented out by Inspection STOP (28/06/2024 17:27)
// --Commented out by Inspection START (28/06/2024 17:27):
////    return this;
////  }
////
////// --Commented out by Inspection START (28/06/2024 17:27):
//////  /**
//////   * The name of the odds market.
// --Commented out by Inspection STOP (28/06/2024 17:27)
////   * @return key
////   **/
////  @Schema(example = "h2h", description = "The name of the odds market.")
////      @NotNull
////
////    public KeyEnum getKey() {
////    return key;
////  }
//// --Commented out by Inspection STOP (28/06/2024 17:27)
//
//  public void setKey(KeyEnum key) {
//// --Commented out by Inspection START (28/06/2024 17:27):
////    this.key = key;
////  }
////
// --Commented out by Inspection START (28/06/2024 17:27):
//////  public Market lastUpdate(OffsetDateTime lastUpdate) {
//////    this.lastUpdate = lastUpdate;
//////    return this;
// --Commented out by Inspection STOP (28/06/2024 17:27)
////  }
////
////  /**
////   * A timestamp of when the market's odds were last read. Will be an integer if dateFormat=unix// --Commented out by Inspection (28/06/2024 17:27):, otherwise it will be a string. To check the recency of odds, we recommend using this field instead of the \"last_update\" field at the bookmaker level.
////   * @return lastUpdate
// --Commented out by Inspection START (28/06/2024 17:27):
//////   **/
//////  @Schema(example = "2023-10-10T12:10:29Z", description = "A timestamp of when the market's odds were last read. Will be an integer if dateFormat=unix, otherwise it will be a string. To check the recency of odds, we recommend using this field instead of the \"last_update\" field at the bookmaker level.")
// --Commented out by Inspection STOP (28/06/2024 17:27)
//// --Commented out by Inspection STOP (28/06/2024 17:27)
//      @NotNull
//
//    @Valid
//    public OffsetDateTime getLastUpdate() {
//    return lastUpdate;
//  }
//
//  public void setLastUpdate(OffsetDateTime lastUpdate) {
//    this.lastUpdate = lastUpdate;
//  }
//
//// --Commented out by Inspection START (28/06/2024 17:27):
////  public Market outcomes(List<Outcome> outcomes) {
////    this.outcomes = outcomes;
////    return this;
////  }
////
////// --Commented out by Inspection START (28/06/2024 17:27):
//////  public Market addOutcomesItem(Outcome outcomesItem) {
//// --Commented out by Inspection STOP (28/06/2024 17:27)
////    if (this.outcomes == null) {
////      this.outcomes = new ArrayList<Outcome>();
////    }
////    this.outcomes.add(outcomesItem);
////    return this;
////  }
//// --Commented out by Inspection STOP (28/06/2024 17:27)
//
//  /**
//   * Get outcomes
//   * @return outcomes
//   **/
//  @Schema(description = "")
//      @NotNull
//    @Valid
//    public List<Outcome> getOutcomes() {
//    return outcomes;
//  }
//
//  public void setOutcomes(List<Outcome> outcomes) {
//    this.outcomes = outcomes;
//  }
//
//
//  @Override
//  public boolean equals(java.lang.Object o) {
//    if (this == o) {
//      return true;
//    }
//    if (o == null || getClass() != o.getClass()) {
//      return false;
//    }
//    Market market = (Market) o;
//    return Objects.equals(this.key, market.key) &&
//        Objects.equals(this.lastUpdate, market.lastUpdate) &&
//        Objects.equals(this.outcomes, market.outcomes);
//  }
//
//  @Override
//  public int hashCode() {
//    return Objects.hash(key, lastUpdate, outcomes);
//  }
//
//  @Override
//  public String toString() {
//    StringBuilder sb = new StringBuilder();
//    sb.append("class Market {\n");
//
//    sb.append("    key: ").append(toIndentedString(key)).append("\n");
// --Commented out by Inspection STOP (28/06/2024 17:27)
    sb.append("    lastUpdate: ").append(toIndentedString(lastUpdate)).append("\n");
    sb.append("    outcomes: ").append(toIndentedString(outcomes)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}
