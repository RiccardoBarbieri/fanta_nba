package io.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;
import java.math.BigDecimal;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

// --Commented out by Inspection START (28/06/2024 17:27):
///**
// * Outcome
// */
//@Validated
//@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2024-06-24T10:03:13.459259793Z[GMT]")
//
//
//public class Outcome   {
//  @JsonProperty("name")
//  private String name = null;
//
//  @JsonProperty("price")
//  private Float price = null;
//
//  @JsonProperty("point")
// --Commented out by Inspection START (28/06/2024 17:27):
////  private BigDecimal point = null;
////
////  @JsonProperty("description")
////  private String description = null;
// --Commented out by Inspection STOP (28/06/2024 17:27)
//
//  public Outcome name(String name) {
//    this.name = name;
//    return this;
//  }
//
//// --Commented out by Inspection START (28/06/2024 17:27):
////  /**
////   * The outcome label. The value will depend on the market. For totals markets, this will be 'Over' or 'Under'. For team markets, it will be the name of the team or participant, or 'Draw'.
////   * @return name
////   **/
// --Commented out by Inspection (28/06/2024 17:27):////  @Schema(example = "Houston Texans", description = "The out// --Commented out by Inspection (28/06/2024 17:27):come label. The value will depend on the market. For totals markets, this will be 'Over' or 'Under'. For team markets, it will be the name of the team or participant, or 'Draw'.")
////      @NotNull
////
////    public String getName() {
////    return name;
////  }
//// --Commented out by Inspection STOP (28/06/2024 17:27)
//
// --Commented out by Inspection START (28/06/2024 17:27):
////// --Commented out by Inspection START (28/06/2024 17:27):
//////  public void setName(String name) {
// --Commented out by Inspection STOP (28/06/2024 17:27)
////    this.name = name;
////  }
////
////  public Outcome price(Float price) {
// --Commented out by Inspection START (28/06/2024 17:27):
//////    this.price = price;
//////    return this;
//////  }
//////
//////  /**
//////   * The odds of the outcome. The format is determined by the oddsFormat query param. The format is decimal by default.
// --Commented out by Inspection STOP (28/06/2024 17:27)
////   * @return price
////   **/
// --Commented out by Inspection START (28/06/2024 17:27):
//////  @Schema(example = "2.23", description = "The odds of the outcome. The format is determined by the oddsFormat query param. The format is decimal by default.")
////// --Commented out by Inspection STOP (28/06/2024 17:27)
// --Commented out by Inspection STOP (28/06/2024 17:27)
//      @NotNull
//
//    public Float getPrice() {
//    return price;
//  }
//
//// --Commented out by Inspection START (28/06/2024 17:27):
////  public void setPrice(Float price) {
////    this.price = price;
////  }
////
////  public Outcome point(BigDecimal point) {
////    this.point = point;
////    return this;
////  }
////
////  /**
////   * The handicap or points of the outcome, only applicable to spreads and totals markets (this property will be missing for h2h and outrights markets).
////   * @return point
////   **/
////  @Schema(example = "20.5", description// --Commented out by Inspection (28/06/2024 17:27): = "The handicap or points of the outcome, only applicable to spreads and totals markets (this property will be missing for h2h and outrights markets).")
//// --Commented out by Inspection STOP (28/06/2024 17:27)
//
//    @Valid
//    public BigDecimal getPoint() {
//    return point;
//  }
//
//  public void setPoint(BigDecimal point) {
//    this.point = point;
//  }
//
//// --Commented out by Inspection START (28/06/2024 17:27):
//// --Commented out by Inspection START (28/06/2024 17:27):
//////  public Outcome description(String description) {
//////    this.description = description;
//////    return this;
//////  }
////// --Commented out by Inspection STOP (28/06/2024 17:27)
////
////  /**
////   * This field is oly relevant for certain markets. It contains more information about the outcome (for example, for player prop markets, it includes the player's name).
////   * @return description
////   **/
////  @Schema(description = "This field is oly relevant for certain markets. It contains more information about the outcome (for example, for player prop markets, it includes the player's name).")
//// --Commented out by Inspection STOP (28/06/2024 17:27)
//
//    public String getDescription() {
//    return description;
//  }
//
//  public void setDescription(String description) {
//    this.description = description;
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
//    Outcome outcome = (Outcome) o;
//    return Objects.equals(this.name, outcome.name) &&
//        Objects.equals(this.price, outcome.price) &&
//        Objects.equals(this.point, outcome.point) &&
//        Objects.equals(this.description, outcome.description);
//  }
//
//  @Override
//  public int hashCode() {
//    return Objects.hash(name, price, point, description);
//  }
//
//  @Override
//  public String toString() {
//    StringBuilder sb = new StringBuilder();
// --Commented out by Inspection STOP (28/06/2024 17:27)
    sb.append("class Outcome {\n");
    
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    price: ").append(toIndentedString(price)).append("\n");
    sb.append("    point: ").append(toIndentedString(point)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
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
