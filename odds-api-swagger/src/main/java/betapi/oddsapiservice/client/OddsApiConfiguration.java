package betapi.oddsapiservice.client;

import betapi.oddsapiservice.OddsApiService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.DependsOn;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.reactive.function.client.support.WebClientAdapter;
import org.springframework.web.service.invoker.HttpServiceProxyFactory;

@Configuration
@EnableAutoConfiguration
@ComponentScan("betapi.oddsapiservice.client")
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

    @Bean
    @Qualifier("clientConfiguration")
    public ClientConfiguration clientConfiguration() {
        return new ClientConfiguration();
    }

    @Bean
    @DependsOn(value = {"clientConfiguration"})
    public RestTemplateBuilder restTemplateBuilder() {
        return new RestTemplateBuilder(clientConfiguration());
    }

}
