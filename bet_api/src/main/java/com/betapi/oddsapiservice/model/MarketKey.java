package com.betapi.oddsapiservice.model;

public enum MarketKey {

    H2H("h2h"),
    SPREADS("spreads"),
    TOTALS("totals"),
    OUTRIGHTS("outrights");

    private String key;

    MarketKey(String key) {
        this.key = key;
    }

    public String getKey() {
        return key;
    }

    public static MarketKey fromKey(String key) {
        for (MarketKey marketKey : MarketKey.values()) {
            if (marketKey.getKey().equals(key)) {
                return marketKey;
            }
        }
        return null;
    }
}
