package betapi.oddsapiservice.client;

import org.jetbrains.annotations.NotNull;
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

    public final String apiKey;

    public ApiKeyInterceptor(String apiKey) {
        this.apiKey = apiKey;
    }

    @NotNull
    @Override
    public ClientHttpResponse intercept(HttpRequest request, @NotNull byte[] body, @NotNull ClientHttpRequestExecution execution) throws IOException {
        log.debug("Request: {} {} - adding api key", request.getMethod(), request.getURI());
        //modify request uri adding parameter
        UriBuilder uriBuilder = UriComponentsBuilder.fromUri(request.getURI());
        uriBuilder.queryParam("apiKey", apiKey);

        // Check and modify commenceTimeFrom if present
        String commenceTimeFrom = request.getURI().getQuery(); // Get the original query string
        if (commenceTimeFrom != null && commenceTimeFrom.contains("commenceTimeFrom")) {
            commenceTimeFrom = commenceTimeFrom.split("=")[1].split("Z")[0].replace("%3A", ":")+"Z";
            uriBuilder.replaceQueryParam("commenceTimeFrom", commenceTimeFrom);
        }

        // Check and modify commenceTimeTo if present
        String commenceTimeTo = request.getURI().getQuery(); // Get the original query string
        if (commenceTimeTo != null && commenceTimeTo.contains("commenceTimeTo")) {
            commenceTimeTo = commenceTimeTo.split("commenceTimeTo=")[1].split("Z")[0].replace("%3A", ":")+"Z";
            uriBuilder.replaceQueryParam("commenceTimeTo", commenceTimeTo);
        }

        HttpRequest modifiedRequest = new HttpRequestWrapper(request) {
            @NotNull
            @Override
            public URI getURI() {
                return uriBuilder.build();
            }
        };
        return execution.execute(modifiedRequest, body);
    }
}
