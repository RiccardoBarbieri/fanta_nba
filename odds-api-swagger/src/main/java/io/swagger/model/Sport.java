package io.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;
import org.springframework.validation.annotation.Validated;

import javax.validation.constraints.*;

/**
 * Sport
 */
@Validated
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2024-06-24T10:03:13.459259793Z[GMT]")


public class Sport   {
  @JsonProperty("key")
  private String key = null;

  @JsonProperty("active")
  private Boolean active = null;

  @JsonProperty("group")
  private String group = null;

  @JsonProperty("description")
  private String description = null;

  @JsonProperty("title")
  private String title = null;

  @JsonProperty("has_outrights")
  private Boolean hasOutrights = null;

// --Commented out by Inspection START (28/06/2024 17:27):
//  public Sport key(String key) {
//    this.key = key;
//    return this;
//  }
// --Commented out by Inspection STOP (28/06/2024 17:27)

// --Commented out by Inspection START (28/06/2024 17:27):
//  /**
//   * A unique slug for the sport. Use this as the \"sport\" param in /odds requests.
//   * @return key
//   **/
//  @Schema(exampl// --Commented out by Inspection (28/06/2024 17:27):e = "americanfootball_nfl", description = "A unique slug for the sport. Use this as the \"sport\" param in /odds requests.")
//      @NotNull
//
//    public String getKey() {
//    return key;
//  }
// --Commented out by Inspection STOP (28/06/2024 17:27)

// --Commented out by Inspection START (28/06/2024 17:27):
//  public void setKey(String key) {
//    this.key = key;
// --Commented out by Inspection START (28/06/2024 17:27):
////  }
////
////// --Commented out by Inspection START (28/06/2024 17:27):
// --Commented out by Inspection STOP (28/06/2024 17:27)
////  public Sport active(Boolean active) {
////    this.active = active;
////    return this;
////  }
//// --Commented out by Inspection STOP (28/06/2024 17:27)
// --Commented out by Inspection START (28/06/2024 17:27):
//// --Commented out by Inspection STOP (28/06/2024 17:27)
//
//  /**
//// --Commented out by Inspection START (28/06/2024 17:27):
// --Commented out by Inspection STOP (28/06/2024 17:27)
//   * Indicates if the sport is in season.
//   * @return active
//   **/
//  @Schema(example = "true", description = "Indicates if the sport is in season.")
// --Commented out by Inspection STOP (28/06/2024 17:27)
      @NotNull

    public Boolean isActive() {
    return active;
  }

// --Commented out by Inspection START (28/06/2024 17:27):
//  public void setActive(Boolean active) {
//    this.active = active;
//  }
//
//  public Sport group(String group) {
//// --Commented out by Inspection START (28/06/2024 17:27):
// --Commented out by Inspection STOP (28/06/2024 17:27)
//    this.group = group;
//    return this;
//  }
//
//  /**
//   * A broader grouping.
//   * @return group
//   **/
// --Commented out by Inspection STOP (28/06/2024 17:27)
  @Schema(example = "American Football", description = "A broader grouping.")
      @NotNull

// --Commented out by Inspection START (28/06/2024 17:27):
//    public String getGroup() {
// --Commented out by Inspection START (28/06/2024 17:27):
//// --Commented out by Inspection START (28/06/2024 17:27):
//////    return group;
//////  }
//////
// --Commented out by Inspection STOP (28/06/2024 17:27)
////  public void setGroup(String group) {
////    this.group = group;
//// --Commented out by Inspection STOP (28/06/2024 17:27)
//  }
//
//  public Sport description(String description) {
//    this.description = description;
//    return this;
//  }
//
//  /**
// --Commented out by Inspection START (28/06/2024 17:27):
////   * A brief description of the sport. Subject to change (for example, if sponsors change).
// --Commented out by Inspection START (28/06/2024 17:27):
////// --Commented out by Inspection STOP (28/06/2024 17:27)
////   * @return description
////   **/
////  @Schema(example = "US Football", description = "A brief description of the sport. Subject to change (for example, if sponsors change).")
// --Commented out by Inspection STOP (28/06/2024 17:27)
// --Commented out by Inspection START (28/06/2024 17:27):
////      @NotNull
////
//// --Commented out by Inspection START (28/06/2024 17:27):
//////    public String getDescription() {
//////    return description;
//////  }
//////
//////  public void setDescription(String description) {
//// --Commented out by Inspection STOP (28/06/2024 17:27)
////    this.description = description;
// --Commented out by Inspection STOP (28/06/2024 17:27)
// --Commented out by Inspection STOP (28/06/2024 17:27)
  }

  public Sport title(String title) {
    this.title = title;
    return this;
  }

  /**
   * A presentable title of the sport. Occasionally this value can change, for example if a league undergoes a name change or change in sponsorship.
   * @return title
   **/
  @Schema(example = "NFL", description = "A presentable title of the sport. Occasionally this value can change, for example if a league undergoes a name change or change in sponsorship.")
      @NotNull

    public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }

  public Sport hasOutrights(Boolean hasOutrights) {
    this.hasOutrights = hasOutrights;
    return this;
  }

  /**
   * Indicates if the sport has outrights markets.
   * @return hasOutrights
   **/
  @Schema(example = "false", description = "Indicates if the sport has outrights markets.")
      @NotNull

    public Boolean isHasOutrights() {
    return hasOutrights;
  }

  public void setHasOutrights(Boolean hasOutrights) {
    this.hasOutrights = hasOutrights;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Sport sport = (Sport) o;
    return Objects.equals(this.key, sport.key) &&
        Objects.equals(this.active, sport.active) &&
        Objects.equals(this.group, sport.group) &&
        Objects.equals(this.description, sport.description) &&
        Objects.equals(this.title, sport.title) &&
        Objects.equals(this.hasOutrights, sport.hasOutrights);
  }

  @Override
  public int hashCode() {
    return Objects.hash(key, active, group, description, title, hasOutrights);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Sport {\n");
    
    sb.append("    key: ").append(toIndentedString(key)).append("\n");
    sb.append("    active: ").append(toIndentedString(active)).append("\n");
    sb.append("    group: ").append(toIndentedString(group)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    hasOutrights: ").append(toIndentedString(hasOutrights)).append("\n");
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
