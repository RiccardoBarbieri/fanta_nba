package com.betapi.oddsapiservice.bookmakers.model;

public class Bookmaker {

    private String region;
    private String key;
    private String url;

    public Bookmaker() {
    }

    public Bookmaker(String region, String key, String url) {
        this.region = region;
        this.key = key;
        this.url = url;
    }

    public String getRegion() {
        return region;
    }

    public void setRegion(String region) {
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
