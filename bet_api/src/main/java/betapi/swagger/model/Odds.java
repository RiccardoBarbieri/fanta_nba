package betapi.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;
import java.util.ArrayList;
import java.util.List;
import org.springframework.validation.annotation.Validated;
import jakarta.validation.Valid;
import jakarta.validation.constraints.*;

/**
 * Odds
 */
@Validated
@jakarta.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2024-06-24T10:03:13.459259793Z[GMT]")


public class Odds extends Event {

  @JsonProperty("bookmakers")
  @Valid
  private List<Bookmaker> bookmakers = null;

  public Odds bookmakers(List<Bookmaker> bookmakers) {
    this.bookmakers = bookmakers;
    return this;
  }

  public Odds addBookmakersItem(Bookmaker bookmakersItem) {
    if (this.bookmakers == null) {
      this.bookmakers = new ArrayList<Bookmaker>();
    }
    this.bookmakers.add(bookmakersItem);
    return this;
  }

  /**
   * Get bookmakers
   * @return bookmakers
   **/
  @Schema(description = "")
  @NotNull
  @Valid
  public List<Bookmaker> getBookmakers() {
    return bookmakers;
  }

  public void setBookmakers(List<Bookmaker> bookmakers) {
    this.bookmakers = bookmakers;
  }

  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    if (!super.equals(o)) {
      return false;
    }
    Odds odds = (Odds) o;
    return Objects.equals(this.bookmakers, odds.bookmakers);
  }

  @Override
  public int hashCode() {
    return Objects.hash(super.hashCode(), bookmakers);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Odds {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    bookmakers: ").append(toIndentedString(bookmakers)).append("\n");
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
