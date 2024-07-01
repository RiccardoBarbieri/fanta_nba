package betapi.oddsapiservice.client;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.web.client.RestTemplateCustomizer;
import org.springframework.web.client.RestTemplate;


public class ClientConfiguration implements RestTemplateCustomizer {

    @Value("${odds_api.key}")
    public String apiKey;

    @Value("${odds_api.url}")
    public String baseUrl;
    @Override
    public void customize(RestTemplate restTemplate) {
        restTemplate.getInterceptors().add(new ApiKeyInterceptor(apiKey));
    }


/*
    @Bean
    public RestTemplate restTemplate() {
        RestTemplate restTemplate = new RestTemplate();

        List<ClientHttpRequestInterceptor> interceptors
                = restTemplate.getInterceptors();
        if (CollectionUtils.isEmpty(interceptors)) {
            interceptors = new ArrayList<>();
        }
        interceptors.add(new ApiKeyInterceptor(apiKey));
        restTemplate.setInterceptors(interceptors);
        return restTemplate;
    }*/
}