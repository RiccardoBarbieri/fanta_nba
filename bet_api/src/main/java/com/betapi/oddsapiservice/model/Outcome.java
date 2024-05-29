package com.betapi.oddsapiservice.model;

public class Outcome {

    private String name;
    private Float price;
    private Float point;
    private String description;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Float getPrice() {
        return price;
    }

    public void setPrice(Float price) {
        this.price = price;
    }

    public Float getPoint() {
        return point;
    }

    public void setPoint(Float point) {
        this.point = point;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
}
