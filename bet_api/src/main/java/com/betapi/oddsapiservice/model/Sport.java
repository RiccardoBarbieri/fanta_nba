package com.betapi.oddsapiservice.model;

public class Sport {

    private String key;
    private String group;
    private String title;
    private String description;
    private Boolean active;
    private Boolean has_outrights;

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Boolean getActive() {
        return active;
    }

    public void setActive(Boolean active) {
        this.active = active;
    }

    public Boolean getHas_outrights() {
        return has_outrights;
    }

    public void setHas_outrights(Boolean has_outrights) {
        this.has_outrights = has_outrights;
    }
}
