package betapi.database.documents;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "bookmakers")
public class Bookmaker {

    private String region;
    @Id
    private String key;
    private String url;

// --Commented out by Inspection START (28/06/2024 17:27):
//    public Bookmaker() {
//    }
// --Commented out by Inspection STOP (28/06/2024 17:27)

// --Commented out by Inspection START (28/06/2024 17:27):
// --Commented out by Inspection START (28/06/2024 17:27):
////    public Bookmaker(String region, String key, String url) {
////        this.region = region;
//// --Commented out by Inspection STOP (28/06/2024 17:27)
// --Commented out by Inspection STOP (28/06/2024 17:27)
// --Commented out by Inspection START (28/06/2024 17:27):
//// --Commented out by Inspection START (28/06/2024 17:27):
////        this.key = key;
// --Commented out by Inspection STOP (28/06/2024 17:27)
//        this.url = url;
//    }
//
//// --Commented out by Inspection START (28/06/2024 17:27):
// --Commented out by Inspection STOP (28/06/2024 17:27)
//    public String getRegion() {
//        return region;
//    }
//
//    public void setRegion(String region) {
// --Commented out by Inspection STOP (28/06/2024 17:27)
        this.region = region;
    }

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    @Override
    public String toString() {
        return "Bookmaker{" +
                "region='" + region + '\'' +
                ", key='" + key + '\'' +
                ", url='" + url + '\'' +
                '}';
    }
}
