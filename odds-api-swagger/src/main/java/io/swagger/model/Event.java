package io.swagger.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;
import org.springframework.validation.annotation.Validated;
import org.threeten.bp.OffsetDateTime;

import javax.validation.Valid;
import javax.validation.constraints.NotNull;
import java.util.Objects;

/**
 * Event
 */
@Validated
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2024-06-24T10:03:13.459259793Z[GMT]")


public class Event   {
  @JsonProperty("id")
  private String id = null;

  @JsonProperty("sport_key")
  private String sportKey = null;

  @JsonProperty("sport_title")
  private String sportTitle = null;

  @JsonProperty("commence_time")
  private OffsetDateTime commenceTime = null;

  @JsonProperty("home_team")
  private String homeTeam = null;

  @JsonProperty("away_team")
  private String awayTeam = null;

  public Event id(String id) {
    this.id = id;
    return this;
  }

  /**
   * A unique 32 character identifier for the event.
   * @return id
   **/
  @Schema(example = "e912304de2b2ce35b473ce2ecd3d1502", description = "A unique 32 character identifier for the event.")
      @NotNull

    public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }

  public Event sportKey(String sportKey) {
    this.sportKey = sportKey;
    return this;
  }

  /**
   * A unique slug for the sport. Use this as the \"sport\" param in /odds requests.
   * @return sportKey
   **/
  @Schema(example = "americanfootball_nfl", description = "A unique slug for the sport. Use this as the \"sport\" param in /odds requests.")
      @NotNull

    public String getSportKey() {
    return sportKey;
  }

  public void setSportKey(String sportKey) {
    this.sportKey = sportKey;
  }

  public Event sportTitle(String sportTitle) {
    this.sportTitle = sportTitle;
    return this;
  }

  /**
   * A presentable title of the sport. Occasionally this value can change, for example if a league undergoes a name change or change in sponsorship.
   * @return sportTitle
   **/
  @Schema(example = "NFL", description = "A presentable title of the sport. Occasionally this value can change, for example if a league undergoes a name change or change in sponsorship.")
      @NotNull

    public String getSportTitle() {
    return sportTitle;
  }

  public void setSportTitle(String sportTitle) {
    this.sportTitle = sportTitle;
  }

  public Event commenceTime(OffsetDateTime commenceTime) {
    this.commenceTime = commenceTime;
    return this;
  }

  /**
   * The match start time (ISO 8601 formatted). This will be a Unix timestamp integer if the dateFormat query param is set to dateFormat=unix.
   * @return commenceTime
   **/
  @Schema(example = "2023-10-11T23:10Z", description = "The match start time (ISO 8601 formatted). This will be a Unix timestamp integer if the dateFormat query param is set to dateFormat=unix.")
      @NotNull

    @Valid
    public OffsetDateTime getCommenceTime() {
    return commenceTime;
  }

  public void setCommenceTime(OffsetDateTime commenceTime) {
    this.commenceTime = commenceTime;
  }

  public Event homeTeam(String homeTeam) {
    this.homeTeam = homeTeam;
    return this;
  }

  /**
   * The home team. If home/away is not applicable for the sport (such as MMA and Tennis), it will be one of the participants. Null for outrights (futures) events.
   * @return homeTeam
   **/
  @Schema(example = "Houston Texans", description = "The home team. If home/away is not applicable for the sport (such as MMA and Tennis), it will be one of the participants. Null for outrights (futures) events.")
  
    public String getHomeTeam() {
    return homeTeam;
  }

  public void setHomeTeam(String homeTeam) {
    this.homeTeam = homeTeam;
  }

  public Event awayTeam(String awayTeam) {
    this.awayTeam = awayTeam;
    return this;
  }

  /**
   * The away team. If home/away is not applicable for the sport (such as MMA and Tennis), it will be one of the participants. Null for outrights (futures) events.
   * @return awayTeam
   **/
  @Schema(example = "Kansas City Chiefs", description = "The away team. If home/away is not applicable for the sport (such as MMA and Tennis), it will be one of the participants. Null for outrights (futures) events.")
  
    public String getAwayTeam() {
    return awayTeam;
  }

  public void setAwayTeam(String awayTeam) {
    this.awayTeam = awayTeam;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Event event = (Event) o;
    return Objects.equals(this.id, event.id) &&
        Objects.equals(this.sportKey, event.sportKey) &&
        Objects.equals(this.sportTitle, event.sportTitle) &&
        Objects.equals(this.commenceTime, event.commenceTime) &&
        Objects.equals(this.homeTeam, event.homeTeam) &&
        Objects.equals(this.awayTeam, event.awayTeam);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, sportKey, sportTitle, commenceTime, homeTeam, awayTeam);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Event {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    sportKey: ").append(toIndentedString(sportKey)).append("\n");
    sb.append("    sportTitle: ").append(toIndentedString(sportTitle)).append("\n");
    sb.append("    commenceTime: ").append(toIndentedString(commenceTime)).append("\n");
    sb.append("    homeTeam: ").append(toIndentedString(homeTeam)).append("\n");
    sb.append("    awayTeam: ").append(toIndentedString(awayTeam)).append("\n");
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
