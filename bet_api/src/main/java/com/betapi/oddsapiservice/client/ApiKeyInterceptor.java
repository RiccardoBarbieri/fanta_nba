package com.betapi.oddsapiservice.client;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpRequest;
import org.springframework.http.client.ClientHttpRequestExecution;
import org.springframework.http.client.ClientHttpRequestInterceptor;
import org.springframework.http.client.ClientHttpResponse;
import org.springframework.http.client.support.HttpRequestWrapper;
import org.springframework.web.util.UriBuilder;
import org.springframework.web.util.UriComponentsBuilder;

import java.io.IOException;
import java.net.URI;

public class ApiKeyInterceptor implements ClientHttpRequestInterceptor {

    private static final Logger log = LoggerFactory.getLogger(ApiKeyInterceptor.class);

    private final String apiKey;

    public ApiKeyInterceptor(String apiKey) {
        this.apiKey = apiKey;
    }

    @Override
    public ClientHttpResponse intercept(HttpRequest request, byte[] body, ClientHttpRequestExecution execution) throws IOException {
        log.debug("Request: {} {} - adding api key", request.getMethod(), request.getURI());
        //modify request uri adding parameter
        UriBuilder uriBuilder = UriComponentsBuilder.fromUri(request.getURI());
        uriBuilder.queryParam("apiKey", apiKey);
        HttpRequest modifiedRequest = new HttpRequestWrapper(request) {
            @Override
            public URI getURI() {
                return uriBuilder.build();
            }
        };
        return execution.execute(modifiedRequest, body);
    }
}
