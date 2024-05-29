package com.betapi.oddsapiservice.utils;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Utils {

    public static Date getDate(String lastUpdate) {
        if (lastUpdate.matches("\\d{10}")) {
            return new Date(Long.parseLong(lastUpdate) * 1000);
        } else {
            try {
                return new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss'Z'").parse(lastUpdate);
            } catch (ParseException e) {
                e.printStackTrace();
                return null;
            }
        }
    }

}
