package betapi.oddsapiservice.client;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.client.ClientHttpRequestInterceptor;
import org.springframework.http.client.HttpComponentsClientHttpRequestFactory;
import org.springframework.util.CollectionUtils;
import org.springframework.web.client.RestClient;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;
import java.util.List;

@Configuration
public class ClientConfiguration {

    @Value("${odds_api.url}")
    public String baseUrl;

    @Value("${odds_api.key}")
    public String apiKey;

    @Bean
    public RestClient restClient() {

        return RestClient.builder()
                .requestFactory(new HttpComponentsClientHttpRequestFactory()) //http request library apache
                .baseUrl(baseUrl)
                .requestInterceptor(new ApiKeyInterceptor(apiKey))
//                .defaultStatusHandler() //use to add status handling if needed
                .build();
    }
}