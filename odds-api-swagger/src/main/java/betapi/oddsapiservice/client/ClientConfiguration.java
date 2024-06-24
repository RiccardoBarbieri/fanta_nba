package betapi.oddsapiservice.client;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.http.client.HttpComponentsClientHttpRequestFactory;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestClient;

@Component
public class ClientConfiguration {

    private static final Logger log = LoggerFactory.getLogger(ClientConfiguration.class);


    @Value("${odds_api.key}")
    public String apiKey;

    @Value("${odds_api.url}")
    public String baseUrl;

    @Bean
    public RestClient restClient() {
        RestClient customRestClient = RestClient.builder()
                .requestFactory(new HttpComponentsClientHttpRequestFactory()) //http request library apache
                .baseUrl(baseUrl)
                .requestInterceptor(new ApiKeyInterceptor(apiKey))
//                .defaultStatusHandler() //use to add status handling if needed
                .build();

        return customRestClient;
    }
}
