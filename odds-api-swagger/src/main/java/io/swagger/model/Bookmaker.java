package io.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.model.Market;
import io.swagger.v3.oas.annotations.media.Schema;
import java.util.ArrayList;
import java.util.List;
import org.threeten.bp.OffsetDateTime;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

// --Commented out by Inspection START (28/06/2024 17:27):
///**
// * Bookmaker
// */
//@Validated
//@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2024-06-24T10:03:13.459259793Z[GMT]")
//
//
//public class Bookmaker   {
//  @JsonProperty("url")
//  private String url = null;
//
//  @JsonProperty("key")
//  private String key = null;
//
//  @JsonProperty("title")
//  private String title = null;
//
//  @JsonProperty("last_update")
// --Commented out by Inspection START (28/06/2024 17:27):
////  private OffsetDateTime lastUpdate = null;
////
////  @JsonProperty("markets")
////  @Valid
////  private List<Market> markets = null;
// --Commented out by Inspection STOP (28/06/2024 17:27)
//
//  public Bookmaker url(String url) {
//    this.url = url;
//    return this;
//  }
//
//// --Commented out by Inspection START (28/06/2024 17:27):
////  /**
////   * The URL of the bookmaker's website.
// --Commented out by Inspection START (28/06/2024 17:27):
//////   * @return url
//////   **/
//// --Commented out by Inspection START (28/06/2024 17:27):
// --Commented out by Inspection STOP (28/06/2024 17:27)
//////  @Schema(example = "https://www.draftkings.com", description = "The URL of the bookmaker's website.")
//////      @NotNull
// --Commented out by Inspection STOP (28/06/2024 17:27)
////
// --Commented out by Inspection START (28/06/2024 17:27):
//////    public String getUrl() {
//////    return url;
//////  }
//// --Commented out by Inspection START (28/06/2024 17:27):
// --Commented out by Inspection STOP (28/06/2024 17:27)
////// --Commented out by Inspection STOP (28/06/2024 17:27)
////
////  public void setUrl(String url) {
// --Commented out by Inspection STOP (28/06/2024 17:27)
//    this.url = url;
//  }
//
//  public Bookmaker key(String key) {
//    this.key = key;
//    return this;
//  }
//
//// --Commented out by Inspection START (28/06/2024 17:27):
// --Commented out by Inspection START (28/06/2024 17:27):
//////  /**
//////   * A unique slug (key) of the bookmaker.
//////   * @return key
// --Commented out by Inspection STOP (28/06/2024 17:27)
////   **/
////  @Schema(example = "draftkings", description = "A unique slug (key) of the bookmaker.")
// --Commented out by Inspection START (28/06/2024 17:27):
//////      @NotNull
//////
//////    public String getKey() {
//////    return key;
//////  }
////// --Commented out by Inspection STOP (28/06/2024 17:27)
// --Commented out by Inspection STOP (28/06/2024 17:27)
//
//// --Commented out by Inspection START (28/06/2024 17:27):
////  public void setKey(String key) {
////    this.key = key;
////  }
////
////  public Bookmaker title(String title) {
// --Commented out by Inspection START (28/06/2024 17:27):
//////    this.title = title;
//////    return this;
//////  }
//////
//////  /**
//////   * A formatted title of the bookmaker.
// --Commented out by Inspection STOP (28/06/2024 17:27)
////   * @return title
////   **/
// --Commented out by Inspection START (28/06/2024 17:27):
//////  @Schema(example = "DraftKings", description = "A formatted title of the bookmaker.")
////// --Commented out by Inspection STOP (28/06/2024 17:27)
////      @NotNull
////
////    public String getTitle() {
// --Commented out by Inspection START (28/06/2024 17:27):
//// --Commented out by Inspection STOP (28/06/2024 17:27)
////    return title;
////  }
////
////  public void setTitle(String title) {
// --Commented out by Inspection STOP (28/06/2024 17:27)
//// --Commented out by Inspection START (28/06/2024 17:27):
////    this.title = title;
////  }
////
////  public Bookmaker lastUpdate(OffsetDateTime lastUpdate) {
////    this.lastUpdate = lastUpdate;
////    return this;
////  }
////
////  /**
////   * A timestamp of when the bookmaker's odds were last read. Will be an integer if dateFormat=unix, otherwise it will be a string.
////   * @return lastUpdate
////   **/
////  @Schema(example = "2023-10-10T12:10:29Z", description = "A timestamp of when the bookmaker's odds were last read. Will be an integer if dateFormat=unix, otherwise it will be a string.")
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
////  public Bookmaker markets(List<Market> markets) {
////    this.markets = markets;
////    return this;
////  }
////
////// --Commented out by Inspection START (28/06/2024 17:27):
//////  public Bookmaker addMarketsItem(Market marketsItem) {
//// --Commented out by Inspection STOP (28/06/2024 17:27)
////    if (this.markets == null) {
////      this.markets = new ArrayList<Market>();
////    }
////    this.markets.add(marketsItem);
////    return this;
////  }
//// --Commented out by Inspection STOP (28/06/2024 17:27)
//
//  /**
//   * Get markets
//   * @return markets
//   **/
//  @Schema(description = "")
//      @NotNull
//    @Valid
//    public List<Market> getMarkets() {
//    return markets;
//  }
//
//  public void setMarkets(List<Market> markets) {
//    this.markets = markets;
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
//    Bookmaker bookmaker = (Bookmaker) o;
//    return Objects.equals(this.url, bookmaker.url) &&
//        Objects.equals(this.key, bookmaker.key) &&
//        Objects.equals(this.title, bookmaker.title) &&
//        Objects.equals(this.lastUpdate, bookmaker.lastUpdate) &&
//        Objects.equals(this.markets, bookmaker.markets);
//  }
//
//  @Override
//  public int hashCode() {
//    return Objects.hash(url, key, title, lastUpdate, markets);
//  }
//
//  @Override
//  public String toString() {
// --Commented out by Inspection STOP (28/06/2024 17:27)
    StringBuilder sb = new StringBuilder();
    sb.append("class Bookmaker {\n");
    
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
    sb.append("    key: ").append(toIndentedString(key)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    lastUpdate: ").append(toIndentedString(lastUpdate)).append("\n");
    sb.append("    markets: ").append(toIndentedString(markets)).append("\n");
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
