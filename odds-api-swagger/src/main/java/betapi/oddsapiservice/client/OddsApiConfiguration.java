package betapi.oddsapiservice.client;

import betapi.oddsapiservice.OddsApiService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.reactive.function.client.support.WebClientAdapter;
import org.springframework.web.service.invoker.HttpServiceProxyFactory;

@Configuration
public class OddsApiConfiguration {

    @Bean
    @Autowired
    public OddsApiService oddsApiService(WebClient.Builder webClientBuilder) {
        WebClient webClient = webClientBuilder.build();
        HttpServiceProxyFactory factory = HttpServiceProxyFactory
                .builder(WebClientAdapter.forClient(webClient))
                .build();

        return factory.createClient(OddsApiService.class);
    }
}
